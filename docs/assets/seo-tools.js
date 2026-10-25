/* SmartToolsy: SEO Checker and Page Speed Test. Runs only on those two pages. */
(function () {
  'use strict';
  var tool = document.body.getAttribute('data-tool');
  if (tool !== 'seo-checker' && tool !== 'page-speed-test') return;
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var num = function (n, d) { return Number(n).toLocaleString('en-US', { maximumFractionDigits: d == null ? 0 : d, minimumFractionDigits: d || 0 }); };

  function normalize(v) {
    v = String(v || '').trim();
    if (!v) return '';
    if (!/^https?:\/\//i.test(v)) v = 'https://' + v;
    try { var u = new URL(v); return u.href; } catch (e) { return ''; }
  }
  function setParam(url) {
    try { var u = new URL(location.href); u.searchParams.set('url', url); history.replaceState(null, '', u); } catch (e) { /* ignore */ }
  }
  function startParam() { try { return new URL(location.href).searchParams.get('url') || ''; } catch (e) { return ''; } }
  function ring(score, label, size) {
    var r = 42, c = 2 * Math.PI * r, s = Math.max(0, Math.min(100, Math.round(score)));
    var cls = s >= 90 ? 'good' : s >= 50 ? 'mid' : 'bad';
    return '<div class="ring ring-' + cls + (size ? ' ring-' + size : '') + '" role="img" aria-label="' + esc(label) + ': ' + s + ' out of 100">' +
      '<svg viewBox="0 0 100 100" aria-hidden="true"><circle class="ring-bg" cx="50" cy="50" r="' + r + '"/>' +
      '<circle class="ring-fg" cx="50" cy="50" r="' + r + '" stroke-dasharray="' + (c * s / 100).toFixed(1) + ' ' + c.toFixed(1) + '"/></svg>' +
      '<b>' + s + '</b>' + (label ? '<span>' + esc(label) + '</span>' : '') + '</div>';
  }
  function busy(btn, on, text) { btn.disabled = on; if (text) btn.textContent = text; }

  /* =============================================================== SEO checker */
  if (tool === 'seo-checker') {
    var STATUS = { pass: ['Passed', '✓'], warn: ['Warning', '!'], fail: ['Failed', '✕'], info: ['Info', 'i'] };
    var CATS = [['meta', 'Title, description and keywords'], ['content', 'Headings and content'], ['links', 'Links and images'],
      ['social', 'Social sharing and structured data'], ['crawl', 'Crawling and indexing'], ['security', 'Security'],
      ['mobile', 'Mobile and HTML code'], ['speed', 'Speed']];

    var build = function (d) {
      var h = d.html || {}, out = [];
      function add(cat, title, status, weight, found, fix) { out.push({ cat: cat, title: title, status: status, weight: weight, found: found, fix: fix || '' }); }
      var len = function (s) { return s ? [...s].length : 0; };

      // ---- meta
      var tl = len(h.title);
      if (!h.title) add('meta', 'Title tag', 'fail', 3, 'No &lt;title&gt; tag found.', 'Add a unique title of about 30–60 characters that describes the page and includes its main keyword.');
      else if (h.titleCount > 1) add('meta', 'Title tag', 'warn', 3, 'The page has ' + h.titleCount + ' title tags. First: “' + esc(h.title) + '”', 'Keep exactly one <title> tag in the <head>.');
      else if (tl < 30) add('meta', 'Title tag', 'warn', 3, '“' + esc(h.title) + '” (' + tl + ' characters)', 'This title is short. Aim for 30–60 characters so it describes the page fully in search results.');
      else if (tl > 60) add('meta', 'Title tag', 'warn', 3, '“' + esc(h.title) + '” (' + tl + ' characters)', 'Google usually shows about 50–60 characters. Put the most important words first so nothing important is cut off.');
      else add('meta', 'Title tag', 'pass', 3, '“' + esc(h.title) + '” (' + tl + ' characters)');

      var dl = len(h.description);
      if (!h.description) add('meta', 'Meta description', 'fail', 3, 'No meta description found.', 'Add a meta description of about 70–160 characters that summarises the page and gives searchers a reason to click.');
      else if (h.descriptionCount > 1) add('meta', 'Meta description', 'warn', 3, h.descriptionCount + ' meta descriptions found.', 'Keep one meta description per page.');
      else if (dl < 70) add('meta', 'Meta description', 'warn', 3, '“' + esc(h.description) + '” (' + dl + ' characters)', 'Fairly short. Expand it to around 120–160 characters with a clear summary of the page.');
      else if (dl > 160) add('meta', 'Meta description', 'warn', 3, '“' + esc(h.description) + '” (' + dl + ' characters)', 'Google may cut descriptions longer than about 160 characters. Move the key message to the start.');
      else add('meta', 'Meta description', 'pass', 3, '“' + esc(h.description) + '” (' + dl + ' characters)');

      var kw = (h.keywords || []).slice(0, 5).map(function (k) { return k[0]; });
      if (kw.length) {
        var t = (h.title || '').toLowerCase(), ds = (h.description || '').toLowerCase();
        var inT = kw.filter(function (k) { return t.indexOf(k) >= 0; }), inD = kw.filter(function (k) { return ds.indexOf(k) >= 0; });
        if (inT.length) add('meta', 'Keywords in title and description', 'pass', 2, 'Most-used words on the page that also appear in the title: ' + inT.map(esc).join(', ') + (inD.length ? '. In the description: ' + inD.map(esc).join(', ') + '.' : '.'));
        else add('meta', 'Keywords in title and description', 'warn', 2, 'None of the page’s most-used words (' + kw.map(esc).join(', ') + ') appear in the title.', 'Make sure the topic you want to rank for appears in the title, the description and the main heading.');
      }

      // ---- content
      var h1 = (h.headings && h.headings.h1) || [];
      if (!h1.length) add('content', 'H1 heading', 'fail', 3, 'No H1 heading found.', 'Add one H1 that states the main topic of the page, usually close to the title.');
      else if (h1.length > 1) add('content', 'H1 heading', 'warn', 2, h1.length + ' H1 headings: ' + h1.slice(0, 3).map(function (x) { return '“' + esc(x) + '”'; }).join(', '), 'Use one H1 for the main topic and H2–H3 for sections.');
      else add('content', 'H1 heading', 'pass', 3, '“' + esc(h1[0]) + '”');
      var hc = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'].map(function (k) { return k.toUpperCase() + ': ' + ((h.headings && h.headings[k]) || []).length; }).join(' · ');
      var h2n = ((h.headings && h.headings.h2) || []).length;
      if (!h2n && h.wordCount > 300) add('content', 'Subheadings', 'warn', 1, hc, 'Break longer content into sections with H2 subheadings. It helps readers scan and helps search engines understand the structure.');
      else add('content', 'Subheadings', 'pass', 1, hc);
      if (h.wordCount < 100) add('content', 'Amount of text', 'fail', 2, num(h.wordCount) + ' words of visible text.', 'Very little text. Pages with more useful, original text on the topic tend to rank better. If the content is loaded by JavaScript, search engines may see less of it.');
      else if (h.wordCount < 300) add('content', 'Amount of text', 'warn', 2, num(h.wordCount) + ' words of visible text.', 'Consider adding more helpful detail: answers to common questions, examples or steps.');
      else add('content', 'Amount of text', 'pass', 2, num(h.wordCount) + ' words of visible text.');

      // ---- links and images
      var im = h.images || {};
      if (!im.total) add('links', 'Image alt text', 'pass', 2, 'No images found on the page.');
      else if (im.missingAlt) add('links', 'Image alt text', im.missingAlt / im.total > 0.5 ? 'fail' : 'warn', 2, im.missingAlt + ' of ' + im.total + ' images have no alt attribute' + (im.missingAltExamples && im.missingAltExamples.length ? ', for example: ' + im.missingAltExamples.slice(0, 3).map(function (s) { return '<code>' + esc(s.slice(0, 80)) + '</code>'; }).join(', ') : '') + '.', 'Add a short alt text describing each meaningful image. Decorative images can use an empty alt="".');
      else add('links', 'Image alt text', 'pass', 2, 'All ' + im.total + ' images have an alt attribute.');
      var ln = h.links || {};
      if (!ln.internal) add('links', 'Internal links', 'warn', 1, 'No links to other pages on the same site.', 'Link to related pages on your site so visitors and crawlers can find them.');
      else add('links', 'Internal links', 'pass', 1, num(ln.internal) + ' internal and ' + num(ln.external) + ' external links' + (ln.nofollow ? ' (' + ln.nofollow + ' nofollow)' : '') + '.');
      if (ln.empty) add('links', 'Links without text', 'warn', 1, ln.empty + ' links have no text, alt text or label.', 'Give every link descriptive text (or an aria-label for icon links) so users and search engines know where it goes.');
      else add('links', 'Links without text', 'pass', 1, 'Every link has text or a label.');

      // ---- social and structured data
      var og = h.og || {}, ogHave = ['title', 'description', 'image'].filter(function (k) { return og[k]; });
      if (ogHave.length === 3) add('social', 'Open Graph tags', 'pass', 2, 'og:title, og:description and og:image are set.');
      else if (ogHave.length) add('social', 'Open Graph tags', 'warn', 2, 'Found ' + ogHave.map(function (k) { return 'og:' + k; }).join(', ') + '. Missing ' + ['title', 'description', 'image'].filter(function (k) { return !og[k]; }).map(function (k) { return 'og:' + k; }).join(', ') + '.', 'Add the missing tags so links shared on Facebook, LinkedIn, WhatsApp and Slack show a proper title, summary and image.');
      else add('social', 'Open Graph tags', 'warn', 2, 'No Open Graph tags found.', 'Add og:title, og:description and og:image (1200 × 630 px works well) to control how the page looks when shared.');
      var tw = h.twitter || {};
      if (tw.card) add('social', 'X (Twitter) card', 'pass', 1, 'twitter:card is “' + esc(tw.card) + '”.');
      else add('social', 'X (Twitter) card', 'warn', 1, 'No twitter:card tag.', 'Add <meta name="twitter:card" content="summary_large_image"> so links on X show a large preview. X falls back to Open Graph tags for the rest.');
      if ((h.jsonLd || []).length || h.microdata) add('social', 'Structured data', 'pass', 2, (h.jsonLd || []).length ? 'Schema.org types found: ' + h.jsonLd.map(esc).join(', ') + '.' : 'Microdata found.');
      else add('social', 'Structured data', 'warn', 2, 'No structured data (JSON-LD or microdata) found.', 'Add schema.org markup, such as Article, Product, LocalBusiness, FAQPage or BreadcrumbList, to become eligible for rich results.');
      add('social', 'Favicon', h.favicon ? 'pass' : 'warn', 1, h.favicon ? 'A favicon is linked.' : 'No favicon link found in the &lt;head&gt;.', h.favicon ? '' : 'Add <link rel="icon" href="/favicon.svg">. Google shows favicons next to mobile search results.');

      // ---- crawling and indexing
      if (d.status >= 200 && d.status < 300) add('crawl', 'HTTP status', 'pass', 3, 'The page returned ' + d.status + '.');
      else add('crawl', 'HTTP status', 'fail', 3, 'The page returned ' + d.status + '.', 'Search engines only index pages that return 200 OK.');
      var hops = d.redirects || [];
      if (hops.length > 1) add('crawl', 'Redirects', 'warn', 1, hops.length + ' redirects before the final page: ' + hops.map(function (x) { return x.status; }).join(' → ') + '.', 'Point links and old URLs straight at the final address to avoid redirect chains.');
      else add('crawl', 'Redirects', 'pass', 1, hops.length ? 'One redirect (' + hops[0].status + ') to the final address.' : 'No redirects.');
      var rob = ((h.robots || '') + ',' + (h.googlebot || '') + ',' + ((d.headers || {})['x-robots-tag'] || '')).toLowerCase();
      if (/noindex|none/.test(rob)) add('crawl', 'Indexing allowed', 'fail', 3, 'The page tells search engines not to index it (noindex).', 'Remove noindex from the robots meta tag or X-Robots-Tag header if you want this page in Google.');
      else if (/nofollow/.test(rob)) add('crawl', 'Indexing allowed', 'warn', 2, 'The page can be indexed, but links are set to nofollow.', 'Remove nofollow from the robots meta tag unless you deliberately don’t want links followed.');
      else add('crawl', 'Indexing allowed', 'pass', 3, 'No noindex directive found.');
      if (!h.canonical) add('crawl', 'Canonical tag', 'warn', 2, 'No canonical tag found.', 'Add <link rel="canonical" href="…"> with the preferred URL so duplicates (with tracking parameters, for example) are combined.');
      else if (h.canonicalAbs && h.canonicalAbs.replace(/\/$/, '') !== d.finalUrl.replace(/\/$/, '')) add('crawl', 'Canonical tag', 'warn', 2, 'Canonical points to a different URL: <code>' + esc(h.canonicalAbs) + '</code>', 'That’s right for duplicate pages, but if this is the main version, the canonical should point to itself.');
      else add('crawl', 'Canonical tag', 'pass', 2, '<code>' + esc(h.canonicalAbs || h.canonical) + '</code>');
      var r = d.robots || {};
      if (r.disallowAll) add('crawl', 'robots.txt', 'fail', 3, 'robots.txt blocks all crawlers from the whole site (Disallow: /).', 'Remove “Disallow: /” for User-agent: * unless the site is meant to be private.');
      else if (r.found) add('crawl', 'robots.txt', 'pass', 1, 'robots.txt found' + (r.sitemaps && r.sitemaps.length ? ' and lists ' + r.sitemaps.length + ' sitemap' + (r.sitemaps.length > 1 ? 's' : '') : '') + '.');
      else add('crawl', 'robots.txt', 'warn', 1, 'No robots.txt file found.', 'Add a robots.txt at the site root with a Sitemap: line pointing to your XML sitemap.');
      var sm = d.sitemap || {};
      if (sm.found) add('crawl', 'XML sitemap', 'pass', 2, 'Sitemap found at <code>' + esc(sm.url) + '</code> with ' + num(sm.urls) + (sm.index ? ' sitemap files.' : ' URLs.'));
      else add('crawl', 'XML sitemap', 'warn', 2, 'No XML sitemap found at <code>' + esc(sm.url) + '</code>.', 'Create an XML sitemap, list it in robots.txt and submit it in Google Search Console.');
      if (d.notFoundStatus === 404 || d.notFoundStatus === 410) add('crawl', 'Missing pages return 404', 'pass', 1, 'A made-up URL on this site correctly returned ' + d.notFoundStatus + '.');
      else if (d.notFoundStatus) add('crawl', 'Missing pages return 404', 'warn', 1, 'A made-up URL returned ' + d.notFoundStatus + ' instead of 404.', 'Pages that don’t exist should return a 404 status. Returning 200 creates “soft 404s” that waste crawl budget.');
      var fu; try { fu = new URL(d.finalUrl); } catch (e) { fu = null; }
      if (fu) {
        var path = fu.pathname + fu.search, issues = [];
        if (d.finalUrl.length > 100) issues.push('long (' + d.finalUrl.length + ' characters)');
        if (/_/.test(fu.pathname)) issues.push('uses underscores');
        if (/[A-Z]/.test(fu.pathname)) issues.push('has capital letters');
        if ((fu.search.match(/[&?]/g) || []).length > 2) issues.push('has several parameters');
        add('crawl', 'SEO-friendly URL', issues.length ? 'warn' : 'pass', 1, '<code>' + esc(path.length > 90 ? path.slice(0, 90) + '…' : path) + '</code>' + (issues.length ? ' is ' + issues.join(', ') + '.' : ''), issues.length ? 'Short, lowercase URLs with words separated by hyphens are easiest to read and share.' : '');
      }
      add('crawl', 'Language declared', h.lang ? 'pass' : 'warn', 1, h.lang ? 'lang="' + esc(h.lang) + '"' + ((h.hreflang || []).length ? ', plus ' + h.hreflang.length + ' hreflang alternates.' : '.') : 'No lang attribute on the &lt;html&gt; tag.', h.lang ? '' : 'Add the page language, for example <html lang="en">.');
      if (d.altHost && d.altHost.reachable && d.altHost.sameDestination === false) add('crawl', 'www and non-www', 'warn', 1, '<code>' + esc(d.altHost.host) + '</code> loads separately instead of redirecting to this address.', 'Redirect one version to the other with a 301 so search engines see a single site.');
      else if (d.altHost && d.altHost.sameDestination) add('crawl', 'www and non-www', 'pass', 1, '<code>' + esc(d.altHost.host) + '</code> redirects to the same address.');

      // ---- security
      add('security', 'HTTPS', d.https ? 'pass' : 'fail', 3, d.https ? 'The page is served over HTTPS.' : 'The page is served over plain HTTP.', d.https ? '' : 'Install a TLS certificate (free from Let’s Encrypt or your host) and redirect HTTP to HTTPS. Browsers mark HTTP pages as “Not secure”.');
      if (d.httpToHttps === true) add('security', 'HTTP redirects to HTTPS', 'pass', 2, 'The http:// version redirects to HTTPS.');
      else if (d.httpToHttps === false) add('security', 'HTTP redirects to HTTPS', 'warn', 2, 'The http:// version does not redirect to HTTPS.', 'Add a permanent (301) redirect from HTTP to HTTPS.');
      if (d.https) {
        if (h.mixedCount) add('security', 'Mixed content', 'fail', 2, h.mixedCount + ' resources load over plain HTTP, for example <code>' + esc((h.mixed || [])[0]) + '</code>.', 'Change these addresses to https:// so browsers don’t block them or show warnings.');
        else add('security', 'Mixed content', 'pass', 2, 'No insecure (http://) resources found.');
        var hsts = (d.headers || {})['strict-transport-security'];
        add('security', 'HSTS header', hsts ? 'pass' : 'warn', 1, hsts ? 'Strict-Transport-Security is set.' : 'No Strict-Transport-Security header.', hsts ? '' : 'Add an HSTS header so browsers always use HTTPS for your site.');
      }
      var sv = ((d.headers || {}).server || '') + ' ' + ((d.headers || {})['x-powered-by'] || '');
      if (/\d/.test(sv) || (d.headers || {})['x-powered-by']) add('security', 'Server signature', 'warn', 1, 'The server reveals software details: <code>' + esc(sv.trim()) + '</code>', 'Hide version numbers in the Server and X-Powered-By headers so attackers can’t easily match known vulnerabilities.');
      else add('security', 'Server signature', 'pass', 1, 'No software version is revealed in the headers.');
      if (h.emails) add('security', 'Plain-text email addresses', 'warn', 1, h.emails + ' email address' + (h.emails > 1 ? 'es are' : ' is') + ' visible in the page text.', 'Spam bots harvest plain-text addresses. A contact form or an obfuscated address reduces spam.');
      else add('security', 'Plain-text email addresses', 'pass', 1, 'No plain-text email addresses found.');
      if (d.spf === true) add('security', 'SPF record', 'pass', 1, 'The domain has an SPF record, which helps stop spammers sending email as you.');
      else if (d.spf === false) add('security', 'SPF record', 'warn', 1, 'No SPF record found for the domain.', 'Add an SPF TXT record listing the services allowed to send your email.');

      // ---- mobile and code
      add('mobile', 'Mobile viewport', h.viewport ? 'pass' : 'fail', 3, h.viewport ? '<code>' + esc(h.viewport) + '</code>' : 'No viewport meta tag.', h.viewport ? '' : 'Add <meta name="viewport" content="width=device-width, initial-scale=1"> so the page scales properly on phones. Google indexes the mobile version of pages.');
      add('mobile', 'Doctype', h.doctype ? 'pass' : 'warn', 1, h.doctype ? '&lt;!DOCTYPE html&gt; declared.' : 'No HTML5 doctype at the top of the page.', h.doctype ? '' : 'Start the page with <!DOCTYPE html> so browsers use standards mode.');
      add('mobile', 'Character encoding', h.charset ? 'pass' : 'warn', 1, h.charset ? 'Declared as ' + esc(h.charset) + '.' : 'No character encoding declared.', h.charset ? '' : 'Add <meta charset="utf-8"> near the top of the <head>.');
      if ((h.deprecated || []).length || h.frameset || h.nestedTables) add('mobile', 'Outdated HTML', 'warn', 1, [(h.deprecated || []).length ? 'Deprecated tags: ' + h.deprecated.map(function (t) { return '&lt;' + t + '&gt;'; }).join(', ') : '', h.frameset ? 'uses frames' : '', h.nestedTables ? 'nested tables used for layout' : ''].filter(Boolean).join('; ') + '.', 'Replace these with modern HTML and CSS.');
      else add('mobile', 'Outdated HTML', 'pass', 1, 'No deprecated tags, frames or nested tables.');
      if (h.inlineStyleAttrs > 20) add('mobile', 'Inline styles', 'warn', 1, h.inlineStyleAttrs + ' elements use inline style attributes.', 'Move repeated styling into a stylesheet. It keeps the HTML smaller and easier to maintain.');
      else add('mobile', 'Inline styles', 'pass', 1, (h.inlineStyleAttrs || 0) + ' inline style attributes.');
      if (h.metaRefresh) add('mobile', 'Meta refresh', 'warn', 1, 'The page uses a meta refresh.', 'Use a server-side 301 redirect instead of a meta refresh.');
      if (h.iframes) add('mobile', 'Iframes', 'info', 0, h.iframes + ' iframe' + (h.iframes > 1 ? 's' : '') + ' embedded. Content inside iframes is generally credited to the other site, not yours.');

      // ---- speed
      var tt = d.ttfbMs;
      add('speed', 'Server response time', tt < 600 ? 'pass' : tt < 1500 ? 'warn' : 'fail', 2, num(tt) + ' ms to the first byte, measured from our server in the US.', tt < 600 ? '' : 'Slow responses delay everything else. Caching, a CDN or a faster host usually help.');
      var kb = d.bytes / 1024;
      add('speed', 'HTML size', kb < 100 ? 'pass' : kb < 300 ? 'warn' : 'fail', 1, num(kb, 1) + ' KB of HTML' + (d.truncated ? ' (only the first 3 MB were analysed)' : '') + '.', kb < 100 ? '' : 'Large HTML takes longer to download and parse. Remove inline data, unused markup and large inline scripts.');
      var enc = (d.headers || {})['content-encoding'];
      if (enc) add('speed', 'Compression', 'pass', 2, 'The HTML is compressed with ' + esc(enc) + '.');
      else add('speed', 'Compression', kb < 4 ? 'pass' : 'warn', 2, kb < 4 ? 'The page is small enough that compression makes little difference.' : 'The HTML is sent without gzip or Brotli compression.', 'Turn on gzip or Brotli on your server or CDN. It typically shrinks HTML by 70% or more.');
      var sc = h.scripts || {};
      if (sc.blocking) add('speed', 'Render-blocking scripts', 'warn', 2, sc.blocking + ' script' + (sc.blocking > 1 ? 's' : '') + ' in the &lt;head&gt; load without async or defer.', 'Add defer (or async) to scripts in the <head>, or move them to the end of the body, so the page can render first.');
      else add('speed', 'Render-blocking scripts', 'pass', 2, 'No render-blocking scripts in the &lt;head&gt;.');
      var reqs = (sc.external || 0) + (h.stylesheets || 0) + (im.total || 0);
      add('speed', 'Page requests', reqs > 60 ? 'warn' : 'pass', 1, (sc.external || 0) + ' scripts, ' + (h.stylesheets || 0) + ' stylesheets and ' + (im.total || 0) + ' images in the HTML.', reqs > 60 ? 'Many separate files slow the page down. Combine, remove or lazy-load what isn’t needed.' : '');
      add('speed', 'DOM size', h.domElements > 1500 ? 'warn' : 'pass', 1, num(h.domElements) + ' HTML elements.', h.domElements > 1500 ? 'A very large DOM makes pages slower to render and update. Simplify the markup where you can.' : '');
      add('speed', 'Analytics', 'info', 0, h.analytics ? 'An analytics script was detected.' : 'No common analytics script was detected.');
      return out;
    };

    var score = function (checks) {
      var tot = 0, got = 0;
      checks.forEach(function (c) { if (c.status === 'info' || !c.weight) return; tot += c.weight; got += c.weight * (c.status === 'pass' ? 1 : c.status === 'warn' ? 0.5 : 0); });
      return tot ? Math.round(got / tot * 100) : 0;
    };

    var serp = function (d) {
      var h = d.html || {}, u; try { u = new URL(d.finalUrl); } catch (e) { return ''; }
      var crumbs = u.hostname.replace(/^www\./, '') + u.pathname.split('/').filter(Boolean).slice(0, 3).map(function (p) { return ' › ' + decodeURIComponent(p); }).join('');
      var t = h.title || u.hostname, ds = h.description || (h.textSample || '').slice(0, 160);
      if ([...t].length > 60) t = [...t].slice(0, 58).join('') + '…';
      if ([...ds].length > 160) ds = [...ds].slice(0, 157).join('') + '…';
      return '<div class="serp"><div class="serp-url">' + esc(crumbs) + '</div><div class="serp-title">' + esc(t) + '</div><div class="serp-desc">' + esc(ds) + '</div></div>';
    };

    var render = function (d) {
      var checks = build(d), s = score(checks);
      var n = { pass: 0, warn: 0, fail: 0 };
      checks.forEach(function (c) { if (n[c.status] != null) n[c.status]++; });
      var h = d.html || {};
      var html = '<div class="seo-summary">' + ring(s, 'SEO score', 'lg') +
        '<div class="seo-sum-text"><p class="seo-url">Report for <a href="' + esc(d.finalUrl) + '" rel="nofollow noopener" target="_blank">' + esc(d.finalUrl) + '</a></p>' +
        '<div class="seo-counts"><button type="button" class="seo-f is-on" data-f="all">All <b>' + checks.length + '</b></button>' +
        '<button type="button" class="seo-f st-fail" data-f="fail">Failed <b>' + n.fail + '</b></button>' +
        '<button type="button" class="seo-f st-warn" data-f="warn">Warnings <b>' + n.warn + '</b></button>' +
        '<button type="button" class="seo-f st-pass" data-f="pass">Passed <b>' + n.pass + '</b></button></div>' +
        '<p class="seo-next"><a class="btn ghost" href="/page-speed-test/?url=' + encodeURIComponent(d.finalUrl) + '">Test this page’s speed →</a></p></div></div>';
      if (d.html) html += '<h3 class="seo-h">Google search preview</h3>' + serp(d);
      if ((h.keywords || []).length) {
        html += '<h3 class="seo-h">Most common keywords</h3><p class="kw">' + h.keywords.map(function (k) { return '<span>' + esc(k[0]) + ' <b>' + k[1] + '</b></span>'; }).join('') + '</p>';
        if ((h.phrases || []).length) html += '<p class="kw kw-ph">' + h.phrases.map(function (k) { return '<span>' + esc(k[0]) + ' <b>' + k[1] + '</b></span>'; }).join('') + '</p>';
      }
      var order = { fail: 0, warn: 1, pass: 2, info: 3 };
      CATS.forEach(function (c) {
        var list = checks.filter(function (x) { return x.cat === c[0]; }).sort(function (a, b) { return order[a.status] - order[b.status] || b.weight - a.weight; });
        if (!list.length) return;
        html += '<section class="seo-cat"><h3 class="seo-h">' + esc(c[1]) + '</h3><ul class="checks">' + list.map(function (x) {
          return '<li class="chk st-' + x.status + '" data-s="' + x.status + '"><span class="chk-ico" aria-hidden="true">' + STATUS[x.status][1] + '</span>' +
            '<div><p class="chk-t"><b>' + esc(x.title) + '</b> <span class="sr">' + STATUS[x.status][0] + '</span></p><p class="chk-f">' + x.found + '</p>' +
            (x.fix && x.status !== 'pass' ? '<p class="chk-fix">' + esc(x.fix) + '</p>' : '') + '</div></li>';
        }).join('') + '</ul></section>';
      });
      html += '<p class="count-note">Checked ' + esc(new Date(d.checkedAt).toLocaleString()) + '. Results reflect the HTML our server received; content added later by JavaScript isn’t included.</p>';
      var out = $('seo-out'); out.innerHTML = html; out.hidden = false;
      out.querySelectorAll('.seo-f').forEach(function (b) {
        b.addEventListener('click', function () {
          var f = b.getAttribute('data-f');
          out.querySelectorAll('.seo-f').forEach(function (x) { x.classList.toggle('is-on', x === b); });
          out.querySelectorAll('.chk').forEach(function (li) { li.hidden = f !== 'all' && li.getAttribute('data-s') !== f; });
          out.querySelectorAll('.seo-cat').forEach(function (sec) { sec.hidden = !sec.querySelector('.chk:not([hidden])'); });
        });
      });
    };

    var run = async function (e) {
      if (e) e.preventDefault();
      var url = normalize($('seo-url').value), msg = $('seo-msg'), btn = $('seo-go');
      if (!url) { msg.textContent = 'Enter a web address, for example example.com.'; return; }
      $('seo-url').value = url; setParam(url);
      busy(btn, true, 'Checking…'); msg.textContent = 'Fetching the page and running the checks. This usually takes a few seconds.'; $('seo-out').hidden = true;
      try {
        var r = await fetch('/api/seo-check?url=' + encodeURIComponent(url), { headers: { accept: 'application/json' } });
        var d = await r.json().catch(function () { return { error: 'The checker returned an unexpected response. Please try again.' }; });
        if (!r.ok || d.error) throw new Error(d.error || 'The check failed (' + r.status + ').');
        if (!d.isHtml) throw new Error('That address returned ' + (d.contentType || 'a file') + ', not a web page.');
        msg.textContent = ''; render(d);
        $('seo-out').scrollIntoView({ behavior: 'smooth', block: 'start' });
      } catch (err) {
        msg.textContent = err.message || 'Something went wrong. Please try again.';
      } finally { busy(btn, false, 'Check SEO'); }
    };
    $('seo-form').addEventListener('submit', run);
    var sp = startParam(); if (sp) { $('seo-url').value = sp; run(); }
  }

  /* =============================================================== Page speed */
  if (tool === 'page-speed-test') {
    var panel = document.querySelector('[data-psi-key]');
    var KEY = panel ? panel.getAttribute('data-psi-key') : '';
    var strategy = 'mobile', last = null, timer = null;
    var FIELD = [['LARGEST_CONTENTFUL_PAINT_MS', 'Largest Contentful Paint', 'LCP', 'ms'], ['INTERACTION_TO_NEXT_PAINT', 'Interaction to Next Paint', 'INP', 'ms'],
      ['CUMULATIVE_LAYOUT_SHIFT_SCORE', 'Cumulative Layout Shift', 'CLS', 'cls'], ['FIRST_CONTENTFUL_PAINT_MS', 'First Contentful Paint', 'FCP', 'ms'], ['EXPERIMENTAL_TIME_TO_FIRST_BYTE', 'Time to First Byte', 'TTFB', 'ms']];
    var LAB = [['first-contentful-paint', 'First Contentful Paint'], ['largest-contentful-paint', 'Largest Contentful Paint'], ['total-blocking-time', 'Total Blocking Time'], ['cumulative-layout-shift', 'Cumulative Layout Shift'], ['speed-index', 'Speed Index']];
    var CATL = { FAST: ['Good', 'good'], AVERAGE: ['Needs improvement', 'mid'], SLOW: ['Poor', 'bad'] };
    var md = function (s) { return esc(String(s || '').replace(/\[([^\]]+)\]\([^)]+\)/g, '$1').replace(/`([^`]+)`/g, '$1')).replace(/\s*Learn more about[^.]*\.?$/i, ''); };
    var fv = function (m, unit) { var p = m.percentile; return unit === 'cls' ? (p / 100).toFixed(2) : p >= 1000 ? (p / 1000).toFixed(1) + ' s' : num(p) + ' ms'; };

    var renderField = function (le, title) {
      if (!le || !le.metrics || !Object.keys(le.metrics).length) return '';
      var rows = FIELD.filter(function (f) { return le.metrics[f[0]]; }).map(function (f) {
        var m = le.metrics[f[0]], c = CATL[m.category] || ['—', 'mid'], dist = m.distributions || [];
        var bar = dist.length === 3 ? '<div class="dist" aria-hidden="true">' + dist.map(function (x, i) { return '<i class="d' + i + '" style="width:' + (x.proportion * 100).toFixed(1) + '%"></i>'; }).join('') + '</div>' : '';
        return '<div class="fm fm-' + c[1] + '"><span class="fm-n">' + esc(f[1]) + ' <abbr>' + f[2] + '</abbr></span><b>' + fv(m, f[3]) + '</b><span class="fm-c">' + c[0] + '</span>' + bar + '</div>';
      }).join('');
      var ov = CATL[le.overall_category];
      return '<h3 class="seo-h">' + title + '</h3><p class="count-note">Core Web Vitals assessment: <b class="cwv-' + (le.overall_category === 'FAST' ? 'good' : ov ? 'bad' : 'mid') + '">' + (le.overall_category === 'FAST' ? 'Passed' : le.overall_category ? 'Failed' : 'Not available') + '</b>. 75th percentile of real Chrome users over the last 28 days.</p><div class="fms">' + rows + '</div>';
    };

    var render = function (d) {
      var lh = d.lighthouseResult || {}, cats = lh.categories || {}, au = lh.audits || {};
      var gauges = [['performance', 'Performance'], ['accessibility', 'Accessibility'], ['best-practices', 'Best Practices'], ['seo', 'SEO']]
        .filter(function (c) { return cats[c[0]] && cats[c[0]].score != null; })
        .map(function (c) { return ring(cats[c[0]].score * 100, c[1]); }).join('');
      var shot = au['final-screenshot'] && au['final-screenshot'].details && au['final-screenshot'].details.data;
      var html = '<div class="psi-top"><div class="rings">' + gauges + '</div>' + (shot ? '<img class="psi-shot" src="' + esc(shot) + '" alt="Screenshot of the page as tested">' : '') + '</div>';
      html += '<p class="count-note">' + (strategy === 'mobile' ? 'Mobile' : 'Desktop') + ' test of <a href="' + esc(lh.finalDisplayedUrl || lh.finalUrl || d.id) + '" rel="nofollow noopener" target="_blank">' + esc(lh.finalDisplayedUrl || lh.finalUrl || d.id) + '</a>. Scores: 90–100 good, 50–89 needs improvement, 0–49 poor.</p>';
      var fieldHtml = renderField(d.loadingExperience, 'What real users experience');
      if (!fieldHtml && d.originLoadingExperience) fieldHtml = renderField(d.originLoadingExperience, 'What real users experience (whole site)');
      html += fieldHtml || '<h3 class="seo-h">What real users experience</h3><p class="count-note">Chrome doesn’t have enough real-user data for this page or site yet. That’s normal for new or low-traffic sites; the lab test below still applies.</p>';
      html += '<h3 class="seo-h">Lab test results</h3><div class="fms">' + LAB.filter(function (l) { return au[l[0]]; }).map(function (l) {
        var a = au[l[0]], c = a.score >= 0.9 ? 'good' : a.score >= 0.5 ? 'mid' : 'bad';
        return '<div class="fm fm-' + c + '"><span class="fm-n">' + esc(l[1]) + '</span><b>' + esc(a.displayValue || '—') + '</b></div>';
      }).join('') + '</div>';
      var perf = cats.performance || {}, seen = {};
      var opps = (perf.auditRefs || []).filter(function (r) {
        var a = au[r.id];
        if (!a || seen[r.id] || r.group === 'metrics' || a.score == null || a.score >= 0.9) return false;
        if (/^(notApplicable|informative|manual|error)$/.test(a.scoreDisplayMode)) return false;
        seen[r.id] = 1; return true;
      }).map(function (r) {
        var a = au[r.id], ms = (a.details && a.details.overallSavingsMs) || 0, sav = a.metricSavings || {};
        Object.keys(sav).forEach(function (k) { if (k !== 'CLS') ms = Math.max(ms, sav[k] || 0); });
        return { a: a, ms: ms };
      }).sort(function (x, y) { return y.ms - x.ms || x.a.score - y.a.score; }).slice(0, 12);
      html += '<h3 class="seo-h">What to fix first</h3>';
      html += opps.length ? '<ul class="checks">' + opps.map(function (o) {
        var st = o.a.score < 0.5 ? 'fail' : 'warn';
        return '<li class="chk st-' + st + '"><span class="chk-ico" aria-hidden="true">' + (st === 'fail' ? '✕' : '!') + '</span><div><p class="chk-t"><b>' + esc(o.a.title) + '</b>' +
          (o.a.displayValue ? ' <span class="chk-v">' + esc(o.a.displayValue) + '</span>' : (o.ms >= 100 ? ' <span class="chk-v">Est. savings ' + (o.ms / 1000).toFixed(1) + ' s</span>' : '')) +
          '</p><p class="chk-fix">' + md(o.a.description) + '</p></div></li>';
      }).join('') + '</ul>' : '<p class="count-note">No significant performance issues found. Nice work.</p>';
      var lhV = lh.lighthouseVersion ? 'Lighthouse ' + esc(lh.lighthouseVersion) + ', ' : '';
      html += '<p class="count-note">' + lhV + 'run by Google PageSpeed Insights on ' + esc(new Date(lh.fetchTime || Date.now()).toLocaleString()) + '. Lab scores vary a little between runs. <a href="/seo-checker/?url=' + encodeURIComponent(lh.finalDisplayedUrl || d.id || '') + '">Check this page’s SEO →</a></p>';
      var out = $('ps-out'); out.innerHTML = html; out.hidden = false;
    };

    var run = async function (e) {
      if (e) e.preventDefault();
      var url = normalize($('ps-url').value), msg = $('ps-msg'), btn = $('ps-go');
      if (!url) { msg.textContent = 'Enter a web address, for example example.com.'; return; }
      $('ps-url').value = url; setParam(url);
      busy(btn, true, 'Testing…'); $('ps-out').hidden = true;
      var t0 = Date.now();
      msg.textContent = 'Loading the page in Google’s test browser… This usually takes 15–40 seconds.';
      clearInterval(timer);
      timer = setInterval(function () { msg.textContent = 'Testing the ' + strategy + ' version… ' + Math.round((Date.now() - t0) / 1000) + ' s (usually 15–40 seconds).'; }, 1000);
      var q = 'url=' + encodeURIComponent(url) + '&strategy=' + strategy + '&category=performance&category=accessibility&category=best-practices&category=seo' + (KEY ? '&key=' + encodeURIComponent(KEY) : '');
      try {
        var r = await fetch('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?' + q);
        var d = await r.json().catch(function () { return {}; });
        if (!r.ok || d.error) {
          var m = (d.error && d.error.message) || '';
          if (r.status === 429 || /quota/i.test(m)) throw new Error('Google’s free testing limit is busy right now. Please wait a minute and try again.');
          if (/FAILED_DOCUMENT_REQUEST|ERRORED_DOCUMENT_REQUEST|DNS_FAILURE|NO_FCP|NOT_HTML/i.test(m)) throw new Error('Google couldn’t load that page. Check the address, and make sure the page is public and not blocking bots.');
          throw new Error(m ? 'The test failed: ' + m.replace(/^Lighthouse returned error:\s*/, '') : 'The test failed. Please try again.');
        }
        last = d; msg.textContent = ''; render(d);
        $('ps-out').scrollIntoView({ behavior: 'smooth', block: 'start' });
      } catch (err) {
        msg.textContent = err.message && !/Failed to fetch/i.test(err.message) ? err.message : 'Couldn’t reach Google PageSpeed Insights. Check your connection and try again.';
      } finally { clearInterval(timer); busy(btn, false, 'Test speed'); }
    };
    document.querySelectorAll('[data-strategy]').forEach(function (b) {
      b.addEventListener('click', function () {
        strategy = b.getAttribute('data-strategy');
        document.querySelectorAll('[data-strategy]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        if (last && $('ps-url').value) run();
      });
    });
    $('ps-form').addEventListener('submit', run);
    var sp2 = startParam(); if (sp2) { $('ps-url').value = sp2; run(); }
  }
})();
