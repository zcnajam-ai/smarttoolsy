/*
 * SmartToolsy SEO checker: fetches one public web page (plus its robots.txt,
 * sitemap and a few related URLs) and returns the raw facts as JSON.
 * Scoring and advice happen in the browser (static/assets/seo-tools.js).
 *
 * Safety: only http/https on ports 80/443, no credentials in the URL, and every
 * hostname is resolved first so private, loopback and link-local addresses are
 * refused. Redirects are followed by hand so each hop is checked the same way.
 */
const dns = require('node:dns').promises;
const net = require('node:net');

const UA = 'Mozilla/5.0 (compatible; SmartToolsyBot/1.0; +https://www.smarttoolsy.tech/seo-checker/)';
const MAX_BYTES = 3 * 1024 * 1024;
const ALLOW_LOCAL = process.env.SEO_CHECK_ALLOW_LOCAL === '1'; // local tests only

const STOP = new Set(('a about above after again against all am an and any are as at be because been before being below between both but by can could did do does doing down during each few for from further had has have having he her here hers herself him himself his how i if in into is it its itself just me more most my myself no nor not now of off on once only or other our ours ourselves out over own same she should so some such than that the their theirs them themselves then there these they this those through to too under until up very was we were what when where which while who whom why will with would you your yours yourself yourselves also get got may might must one two use used using us via etc per new like make way well many much every within without upon yes yet ' +
  'can’t don’t isn’t it’s you’re we’re they’re i’m let’s that’s here’s there’s what’s cant dont isnt its youre were theyre im lets thats heres theres whats').split(/\s+/));

/* ---------------------------------------------------------------- address safety */
function isPrivateIp(ip) {
  if (net.isIPv4(ip)) {
    const p = ip.split('.').map(Number);
    return p[0] === 10 || p[0] === 127 || p[0] === 0 ||
      (p[0] === 169 && p[1] === 254) ||
      (p[0] === 172 && p[1] >= 16 && p[1] <= 31) ||
      (p[0] === 192 && p[1] === 168) ||
      (p[0] === 100 && p[1] >= 64 && p[1] <= 127) ||
      (p[0] === 192 && p[1] === 0 && p[2] === 0) ||
      (p[0] === 198 && (p[1] === 18 || p[1] === 19)) ||
      p[0] >= 224;
  }
  const v = ip.toLowerCase();
  if (v === '::' || v === '::1') return true;
  if (v.startsWith('fc') || v.startsWith('fd') || v.startsWith('fe8') || v.startsWith('fe9') || v.startsWith('fea') || v.startsWith('feb')) return true;
  const mapped = v.match(/^::ffff:(\d+\.\d+\.\d+\.\d+)$/);
  if (mapped) return isPrivateIp(mapped[1]);
  return false;
}

async function assertPublic(u) {
  if (!/^https?:$/.test(u.protocol)) throw new Error('Only http and https addresses can be checked.');
  if (u.username || u.password) throw new Error('Addresses with a username or password are not allowed.');
  if (u.port && !['80', '443'].includes(u.port) && !ALLOW_LOCAL) throw new Error('Only the standard web ports (80 and 443) can be checked.');
  if (ALLOW_LOCAL) return;
  const host = u.hostname.replace(/^\[|\]$/g, '');
  if (host === 'localhost' || host.endsWith('.localhost') || host.endsWith('.internal') || host.endsWith('.local')) throw new Error('That address is not on the public internet.');
  const addrs = net.isIP(host) ? [{ address: host }] : await dns.lookup(host, { all: true });
  if (!addrs.length || addrs.some((a) => isPrivateIp(a.address))) throw new Error('That address is not on the public internet.');
}

/* ---------------------------------------------------------------- fetching */
async function readLimited(res, limit) {
  if (!res.body) return { text: '', bytes: 0, truncated: false };
  const reader = res.body.getReader();
  const chunks = []; let bytes = 0; let truncated = false;
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    bytes += value.length;
    if (bytes > limit) { truncated = true; try { await reader.cancel(); } catch (e) { /* ignore */ } break; }
    chunks.push(value);
  }
  return { text: Buffer.concat(chunks.map((c) => Buffer.from(c))).toString('utf8'), bytes, truncated };
}

async function fetchFollow(start, { timeout = 9000, limit = MAX_BYTES, maxHops = 6, body = true } = {}) {
  const hops = [];
  let url = new URL(start);
  const t0 = Date.now();
  for (let i = 0; i <= maxHops; i++) {
    await assertPublic(url);
    const res = await fetch(url, {
      redirect: 'manual',
      signal: AbortSignal.timeout(timeout),
      headers: { 'user-agent': UA, accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9' },
    });
    const loc = res.headers.get('location');
    if (res.status >= 300 && res.status < 400 && loc) {
      hops.push({ url: url.href, status: res.status });
      try { await res.body?.cancel(); } catch (e) { /* ignore */ }
      url = new URL(loc, url);
      continue;
    }
    const ttfb = Date.now() - t0;
    const r = body ? await readLimited(res, limit) : { text: '', bytes: 0, truncated: false };
    if (!body) { try { await res.body?.cancel(); } catch (e) { /* ignore */ } }
    return { url: url.href, status: res.status, headers: res.headers, hops, ttfb, timeMs: Date.now() - t0, ...r };
  }
  throw new Error('Too many redirects.');
}

async function tryFetch(u, opts) {
  try { return await fetchFollow(u, opts); } catch (e) { return { error: e.message || String(e) }; }
}

/* ---------------------------------------------------------------- HTML helpers */
const ENT = { amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ', mdash: '—', ndash: '–', hellip: '…', rsquo: '’', lsquo: '‘', ldquo: '“', rdquo: '”', copy: '©', reg: '®', trade: '™' };
function decode(s) {
  return String(s || '').replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (m, g) => {
    if (g[0] === '#') { const n = g[1].toLowerCase() === 'x' ? parseInt(g.slice(2), 16) : parseInt(g.slice(1), 10); return Number.isFinite(n) && n > 0 && n < 0x110000 ? String.fromCodePoint(n) : m; }
    return ENT[g.toLowerCase()] ?? m;
  });
}
const clean = (s) => decode(String(s || '').replace(/<[^>]*>/g, ' ')).replace(/\s+/g, ' ').trim();
function tags(html, name) { return html.match(new RegExp('<' + name + '\\b[^>]*>', 'gi')) || []; }
function attr(tag, name) {
  const m = tag.match(new RegExp('\\s' + name + '\\s*=\\s*(?:"([^"]*)"|\'([^\']*)\'|([^\\s"\'>]+))', 'i'));
  return m ? decode(m[1] ?? m[2] ?? m[3] ?? '') : null;
}
function meta(html, key, value) {
  for (const t of tags(html, 'meta')) { const v = attr(t, key); if (v && v.toLowerCase() === value) return attr(t, 'content'); }
  return null;
}
function topCounts(list, n) {
  const f = new Map();
  for (const w of list) f.set(w, (f.get(w) || 0) + 1);
  return [...f.entries()].filter((e) => e[1] > 1).sort((a, b) => b[1] - a[1]).slice(0, n);
}

function analyzeHtml(html, pageUrl, withText) {
  const base = new URL(pageUrl);
  const headEnd = html.search(/<\/head>/i);
  const headHtml = headEnd > 0 ? html.slice(0, headEnd) : html.slice(0, 20000);
  const noComments = html.replace(/<!--[\s\S]*?-->/g, '');

  const titleM = noComments.match(/<title\b[^>]*>([\s\S]*?)<\/title>/i);
  const htmlTag = tags(noComments, 'html')[0] || '';
  const links = tags(headHtml, 'link');
  const relOf = (t) => (attr(t, 'rel') || '').toLowerCase().split(/\s+/);
  const canonicalTag = links.find((t) => relOf(t).includes('canonical'));

  const headings = {};
  for (let i = 1; i <= 6; i++) {
    headings['h' + i] = (noComments.match(new RegExp('<h' + i + '\\b[^>]*>([\\s\\S]*?)<\\/h' + i + '>', 'gi')) || []).map(clean).filter(Boolean);
  }

  const imgs = tags(noComments, 'img');
  const missingAlt = imgs.filter((t) => attr(t, 'alt') === null);
  const anchors = tags(noComments, 'a');
  let internal = 0, external = 0, nofollow = 0;
  for (const a of anchors) {
    const href = attr(a, 'href');
    if (!href || /^(#|javascript:|mailto:|tel:)/i.test(href)) continue;
    let u; try { u = new URL(href, base); } catch (e) { continue; }
    if (!/^https?:$/.test(u.protocol)) continue;
    if (u.hostname.replace(/^www\./, '') === base.hostname.replace(/^www\./, '')) internal++; else external++;
    if ((attr(a, 'rel') || '').toLowerCase().includes('nofollow')) nofollow++;
  }
  const emptyAnchors = (noComments.match(/<a\b[^>]*>([\s\S]*?)<\/a>/gi) || [])
    .filter((m) => !clean(m) && !/<img\b[^>]*\balt\s*=\s*["'][^"']+/i.test(m) && !/aria-label\s*=/i.test(m)).length;

  const scripts = tags(noComments, 'script');
  const headScripts = tags(headHtml.replace(/<!--[\s\S]*?-->/g, ''), 'script');
  const blocking = headScripts.filter((t) => attr(t, 'src') && !/\s(async|defer)\b/i.test(t) && (attr(t, 'type') || '').toLowerCase() !== 'module');
  const styles = links.filter((t) => relOf(t).includes('stylesheet'));

  const jsonLd = [];
  for (const m of noComments.matchAll(/<script\b[^>]*type\s*=\s*["']?application\/ld\+json["']?[^>]*>([\s\S]*?)<\/script>/gi)) {
    try {
      const walk = (o) => {
        if (Array.isArray(o)) return o.forEach(walk);
        if (o && typeof o === 'object') { if (o['@type']) [].concat(o['@type']).forEach((t) => jsonLd.push(String(t))); if (o['@graph']) walk(o['@graph']); }
      };
      walk(JSON.parse(m[1].trim()));
    } catch (e) { jsonLd.push('(invalid JSON-LD)'); }
  }

  const mixed = [];
  if (base.protocol === 'https:') {
    for (const name of ['img', 'script', 'iframe', 'source', 'video', 'audio', 'embed']) {
      for (const t of tags(noComments, name)) { const s = attr(t, 'src'); if (s && /^http:\/\//i.test(s)) mixed.push(s); }
    }
    for (const t of styles) { const s = attr(t, 'href'); if (s && /^http:\/\//i.test(s)) mixed.push(s); }
  }

  const bodyHtml = noComments.replace(/<head\b[\s\S]*?<\/head>/i, ' ')
    .replace(/<(script|style|noscript|svg|template)\b[\s\S]*?<\/\1>/gi, ' ');
  const text = clean(bodyHtml);
  const words = (text.toLowerCase().match(/[\p{L}\p{N}][\p{L}\p{N}'’-]*/gu) || []);
  const content = words.filter((w) => w.length > 2 && !STOP.has(w) && !/^\d+$/.test(w));
  const bigrams = [];
  for (let i = 0; i < words.length - 1; i++) {
    const a = words[i], b = words[i + 1];
    if (a.length > 2 && b.length > 2 && !STOP.has(a) && !STOP.has(b) && !/^\d+$/.test(a) && !/^\d+$/.test(b)) bigrams.push(a + ' ' + b);
  }

  const deprecated = ['font', 'center', 'marquee', 'blink', 'big', 'strike', 'tt', 'frame', 'applet', 'acronym', 'basefont', 'dir']
    .filter((n) => new RegExp('<' + n + '\\b', 'i').test(noComments));
  const og = {}; for (const k of ['title', 'description', 'image', 'type', 'url', 'site_name']) og[k] = meta(noComments, 'property', 'og:' + k) || meta(noComments, 'name', 'og:' + k);
  const tw = {}; for (const k of ['card', 'title', 'description', 'image']) tw[k] = meta(noComments, 'name', 'twitter:' + k) || meta(noComments, 'property', 'twitter:' + k);
  const charsetTag = tags(headHtml, 'meta').find((t) => attr(t, 'charset') !== null || /content-type/i.test(attr(t, 'http-equiv') || ''));

  return {
    title: titleM ? clean(titleM[1]) : null,
    titleCount: (noComments.match(/<title\b/gi) || []).length,
    description: meta(noComments, 'name', 'description'),
    descriptionCount: tags(noComments, 'meta').filter((t) => (attr(t, 'name') || '').toLowerCase() === 'description').length,
    robots: meta(noComments, 'name', 'robots'),
    googlebot: meta(noComments, 'name', 'googlebot'),
    viewport: meta(noComments, 'name', 'viewport'),
    charset: charsetTag ? (attr(charsetTag, 'charset') || attr(charsetTag, 'content')) : null,
    lang: attr(htmlTag, 'lang'),
    doctype: /^\s*(<\?xml[^>]*>\s*)?<!doctype\s+html/i.test(html),
    canonical: canonicalTag ? attr(canonicalTag, 'href') : null,
    canonicalAbs: canonicalTag && attr(canonicalTag, 'href') ? (() => { try { return new URL(attr(canonicalTag, 'href'), base).href; } catch (e) { return null; } })() : null,
    favicon: links.some((t) => relOf(t).includes('icon')),
    hreflang: links.filter((t) => relOf(t).includes('alternate') && attr(t, 'hreflang')).map((t) => attr(t, 'hreflang')),
    metaRefresh: tags(headHtml, 'meta').some((t) => (attr(t, 'http-equiv') || '').toLowerCase() === 'refresh'),
    og, twitter: tw,
    headings,
    images: { total: imgs.length, missingAlt: missingAlt.length, missingAltExamples: missingAlt.slice(0, 5).map((t) => attr(t, 'src') || '(no src)') },
    links: { internal, external, nofollow, empty: emptyAnchors },
    wordCount: words.length,
    textSample: text.slice(0, 300),
    fullText: withText ? text.slice(0, 200000) : undefined,
    keywords: topCounts(content, 12),
    phrases: topCounts(bigrams, 6),
    jsonLd: [...new Set(jsonLd)],
    microdata: /\sitemscope\b/i.test(noComments),
    scripts: { total: scripts.length, external: scripts.filter((t) => attr(t, 'src')).length, blocking: blocking.length },
    stylesheets: styles.length,
    inlineStyleAttrs: (noComments.match(/\sstyle\s*=\s*["']/gi) || []).length,
    styleBlocks: (noComments.match(/<style\b/gi) || []).length,
    deprecated,
    iframes: tags(noComments, 'iframe').length,
    nestedTables: /<table\b(?:(?!<\/table>)[\s\S])*<table\b/i.test(noComments),
    frameset: /<frameset\b/i.test(noComments),
    mixed: mixed.slice(0, 10), mixedCount: mixed.length,
    emails: [...new Set((text.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi) || []))].length,
    analytics: /googletagmanager\.com|google-analytics\.com|gtag\(|plausible\.io|clarity\.ms|matomo/i.test(noComments),
    domElements: (noComments.match(/<[a-z][a-z0-9-]*\b/gi) || []).length,
  };
}

function parseRobots(txt) {
  const sitemaps = []; let group = []; let star = false; let disallowAll = false; let lastWasUA = false;
  for (const raw of txt.split(/\r?\n/)) {
    const line = raw.replace(/#.*/, '').trim(); if (!line) continue;
    const i = line.indexOf(':'); if (i < 0) continue;
    const k = line.slice(0, i).trim().toLowerCase(), v = line.slice(i + 1).trim();
    if (k === 'sitemap') { sitemaps.push(v); continue; }
    if (k === 'user-agent') { if (!lastWasUA) group = []; group.push(v); star = group.includes('*'); lastWasUA = true; continue; }
    lastWasUA = false;
    if (k === 'disallow' && star && v === '/') disallowAll = true;
  }
  return { sitemaps, disallowAll };
}

const pick = (h, names) => Object.fromEntries(names.map((n) => [n, h.get(n)]).filter((e) => e[1] !== null));

/* ---------------------------------------------------------------- handler */
module.exports = async function handler(req, res) {
  res.setHeader('content-type', 'application/json; charset=utf-8');
  res.setHeader('x-robots-tag', 'noindex');
  let raw = String((req.query && req.query.url) || '').trim();
  if (!raw) { res.statusCode = 400; return res.end(JSON.stringify({ error: 'Enter a web address to check.' })); }
  if (/^[a-z][a-z0-9+.-]*:\/\//i.test(raw) && !/^https?:\/\//i.test(raw)) { res.statusCode = 400; return res.end(JSON.stringify({ error: 'Only http and https addresses can be checked.' })); }
  if (!/^https?:\/\//i.test(raw)) raw = 'https://' + raw;
  let start;
  try { start = new URL(raw); } catch (e) { res.statusCode = 400; return res.end(JSON.stringify({ error: 'That doesn’t look like a valid web address.' })); }

  let page;
  try { page = await fetchFollow(start.href); } catch (e) {
    const msg = e.name === 'TimeoutError' ? 'The page took too long to respond (over 9 seconds).' :
      /ENOTFOUND|EAI_AGAIN/.test(String(e.cause && e.cause.code) + e.message) ? 'That domain could not be found. Check the spelling.' :
        e.message && !/fetch failed/i.test(e.message) ? e.message : 'The page could not be reached. It may be down or blocking automated checks.';
    res.statusCode = 422; return res.end(JSON.stringify({ error: msg }));
  }

  const final = new URL(page.url);
  const origin = final.origin;
  const ctype = page.headers.get('content-type') || '';
  const isHtml = /html|xml/i.test(ctype) || /<html|<!doctype/i.test(page.text.slice(0, 2000));

  const altHost = final.hostname.startsWith('www.') ? final.hostname.slice(4) : 'www.' + final.hostname;
  const rand = Math.random().toString(36).slice(2, 10);
  const [robotsR, notFoundR, httpR, altR, spf] = await Promise.all([
    tryFetch(origin + '/robots.txt', { timeout: 5000, limit: 200000 }),
    tryFetch(origin + '/smarttoolsy-check-' + rand, { timeout: 5000, limit: 50000, body: false }),
    final.protocol === 'https:' ? tryFetch('http://' + final.host + final.pathname, { timeout: 5000, body: false }) : Promise.resolve(null),
    tryFetch(final.protocol + '//' + altHost + final.pathname, { timeout: 5000, body: false }),
    dns.resolveTxt(final.hostname.replace(/^www\./, '')).then((r) => r.some((x) => x.join('').toLowerCase().startsWith('v=spf1'))).catch(() => null),
  ]);

  const robots = robotsR.error ? { error: robotsR.error } : {
    status: robotsR.status,
    found: robotsR.status === 200 && !/<html/i.test(robotsR.text.slice(0, 500)),
    ...(robotsR.status === 200 ? parseRobots(robotsR.text) : { sitemaps: [], disallowAll: false }),
  };
  const sitemapUrl = (robots.sitemaps && robots.sitemaps[0]) || origin + '/sitemap.xml';
  const smR = await tryFetch(sitemapUrl, { timeout: 5000, limit: 2000000 });
  const sitemap = smR.error ? { url: sitemapUrl, error: smR.error } : {
    url: sitemapUrl, status: smR.status,
    found: smR.status === 200 && /<(urlset|sitemapindex)\b/i.test(smR.text),
    urls: (smR.text.match(/<loc>/gi) || []).length, index: /<sitemapindex\b/i.test(smR.text),
  };

  const sameDest = (r) => (r && !r.error ? new URL(r.url).href.replace(/\/$/, '') === final.href.replace(/\/$/, '') : null);

  const out = {
    input: start.href,
    finalUrl: final.href,
    status: page.status,
    redirects: page.hops,
    ttfbMs: page.ttfb,
    timeMs: page.timeMs,
    bytes: page.bytes,
    truncated: page.truncated,
    contentType: ctype,
    headers: pick(page.headers, ['server', 'x-powered-by', 'strict-transport-security', 'cache-control', 'x-robots-tag', 'content-encoding', 'x-frame-options', 'content-security-policy', 'x-content-type-options', 'referrer-policy']),
    https: final.protocol === 'https:',
    isHtml,
    html: isHtml ? analyzeHtml(page.text, final.href, req.query && req.query.text === '1') : null,
    robots,
    sitemap,
    notFoundStatus: notFoundR.error ? null : notFoundR.status,
    httpToHttps: httpR ? (httpR.error ? null : new URL(httpR.url).protocol === 'https:') : null,
    altHost: { host: altHost, sameDestination: sameDest(altR), reachable: !altR.error },
    spf,
    checkedAt: new Date().toISOString(),
  };
  res.setHeader('cache-control', 'public, s-maxage=60');
  res.statusCode = 200;
  res.end(JSON.stringify(out));
};

module.exports.analyzeHtml = analyzeHtml;
module.exports.isPrivateIp = isPrivateIp;
module.exports.parseRobots = parseRobots;
