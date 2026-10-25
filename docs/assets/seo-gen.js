/* SmartToolsy: Meta Tag Generator, SERP Preview, Robots.txt Generator, Keyword Density Checker. */
(function () {
  'use strict';
  var tool = document.body.getAttribute('data-tool');
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var attr = function (s) { return String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); };
  var val = function (id) { var el = $(id); return el ? el.value.trim() : ''; };
  var chars = function (s) { return [...s].length; };
  function copyBtn(btnId, srcId) {
    var b = $(btnId); if (!b) return;
    b.addEventListener('click', function () {
      var t = $(srcId).value;
      (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).catch(function () { $(srcId).select(); document.execCommand('copy'); })
        .finally(function () { var o = b.textContent; b.textContent = 'Copied'; setTimeout(function () { b.textContent = o; }, 1500); });
    });
  }
  function download(name, text) {
    var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([text], { type: 'text/plain' })); a.download = name;
    document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(a.href); }, 3000);
  }
  // pixel width the way Google renders snippets (Arial)
  var ctx = document.createElement('canvas').getContext('2d');
  function px(text, font) { ctx.font = font; return ctx.measureText(text).width; }
  function cut(text, font, max) {
    if (px(text, font) <= max) return text;
    var a = [...text], lo = 0, hi = a.length;
    while (lo < hi) { var mid = (lo + hi + 1) >> 1; if (px(a.slice(0, mid).join('') + '…', font) <= max) lo = mid; else hi = mid - 1; }
    return a.slice(0, lo).join('').replace(/[\s,.;:–-]+$/, '') + '…';
  }
  function meter(el, used, max, unit, okMin) {
    if (!el) return;
    var pct = Math.min(100, used / max * 100), st = used === 0 ? 'none' : used > max ? 'bad' : okMin && used < okMin ? 'mid' : 'good';
    el.className = 'meter m-' + st;
    el.innerHTML = '<i style="width:' + pct.toFixed(1) + '%"></i><span>' + Math.round(used) + ' / ' + max + ' ' + unit + '</span>';
  }
  function crumbs(url) {
    try { var u = new URL(/^https?:\/\//i.test(url) ? url : 'https://' + url); return u.hostname.replace(/^www\./, '') + u.pathname.split('/').filter(Boolean).slice(0, 3).map(function (p) { return ' › ' + decodeURIComponent(p); }).join(''); }
    catch (e) { return url || 'example.com'; }
  }
  async function fetchPage(url, withText) {
    var r = await fetch('/api/seo-check?url=' + encodeURIComponent(url) + (withText ? '&text=1' : ''));
    var d = await r.json().catch(function () { return { error: 'Unexpected response. Please try again.' }; });
    if (!r.ok || d.error) throw new Error(d.error || 'Could not fetch that page.');
    if (!d.html) throw new Error('That address isn’t a web page.');
    return d;
  }

  /* ============================================================ Meta tag generator */
  if (tool === 'meta-tag-generator') {
    var F = ['mt-title', 'mt-desc', 'mt-url', 'mt-site', 'mt-img', 'mt-tw', 'mt-type', 'mt-index', 'mt-follow', 'mt-lang', 'mt-basic'];
    var run = function () {
      var t = val('mt-title'), d = val('mt-desc'), u = val('mt-url'), site = val('mt-site'), img = val('mt-img'), tw = val('mt-tw').replace(/^@?/, ''),
        type = val('mt-type'), robots = [$('mt-index').value, $('mt-follow').value].join(', '), lang = val('mt-lang'), basic = $('mt-basic').checked;
      var L = [];
      if (basic) { L.push('<meta charset="utf-8">'); L.push('<meta name="viewport" content="width=device-width, initial-scale=1">'); }
      if (t) L.push('<title>' + esc(t) + '</title>');
      if (d) L.push('<meta name="description" content="' + attr(d) + '">');
      if (robots !== 'index, follow') L.push('<meta name="robots" content="' + robots + '">');
      if (u) L.push('<link rel="canonical" href="' + attr(u) + '">');
      if (t || d || img) {
        L.push('', '<!-- Open Graph (Facebook, LinkedIn, WhatsApp, Slack) -->');
        L.push('<meta property="og:type" content="' + type + '">');
        if (site) L.push('<meta property="og:site_name" content="' + attr(site) + '">');
        if (t) L.push('<meta property="og:title" content="' + attr(t) + '">');
        if (d) L.push('<meta property="og:description" content="' + attr(d) + '">');
        if (u) L.push('<meta property="og:url" content="' + attr(u) + '">');
        if (img) L.push('<meta property="og:image" content="' + attr(img) + '">');
        if (lang) L.push('<meta property="og:locale" content="' + attr(lang.replace('-', '_')) + '">');
        L.push('', '<!-- X (Twitter) -->');
        L.push('<meta name="twitter:card" content="' + (img ? 'summary_large_image' : 'summary') + '">');
        if (tw) L.push('<meta name="twitter:site" content="@' + attr(tw) + '">');
        if (t) L.push('<meta name="twitter:title" content="' + attr(t) + '">');
        if (d) L.push('<meta name="twitter:description" content="' + attr(d) + '">');
        if (img) L.push('<meta name="twitter:image" content="' + attr(img) + '">');
      }
      $('mt-out').value = L.join('\n');
      meter($('mt-tm'), px(t, '20px Arial'), 600, 'px', 200);
      meter($('mt-dm'), chars(d), 160, 'characters', 70);
      $('mt-prev').innerHTML = '<div class="serp"><div class="serp-url">' + esc(crumbs(u)) + '</div><div class="serp-title">' + esc(cut(t || 'Your page title', '20px Arial', 600)) + '</div><div class="serp-desc">' + esc(cut(d || 'Your meta description will appear here.', '14px Arial', 920)) + '</div></div>' +
        '<div class="social"><div class="social-img">' + (img ? '<img src="' + attr(img) + '" alt="" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()">' : '<span>1200 × 630 image</span>') + '</div><div class="social-txt"><span>' + esc((crumbs(u).split(' ')[0] || '').toUpperCase()) + '</span><b>' + esc(t || 'Your page title') + '</b><p>' + esc(d) + '</p></div></div>';
      var warn = [];
      if (t && px(t, '20px Arial') > 600) warn.push('The title is wider than Google usually shows, so the end may be cut off.');
      if (d && chars(d) > 160) warn.push('The description is over 160 characters and may be shortened in results.');
      if (u && !/^https?:\/\//i.test(u)) warn.push('The canonical URL should be a full address starting with https://.');
      if (img && !/^https?:\/\//i.test(img)) warn.push('The image should be a full address starting with https:// so social sites can load it.');
      if ($('mt-index').value === 'noindex') warn.push('noindex keeps this page out of Google search results.');
      $('mt-warn').innerHTML = warn.map(function (w) { return '<li>' + esc(w) + '</li>'; }).join('');
    };
    F.forEach(function (id) { var el = $(id); if (el) { el.addEventListener('input', run); el.addEventListener('change', run); } });
    copyBtn('mt-copy', 'mt-out');
    run();
  }

  /* ============================================================ SERP preview */
  if (tool === 'serp-preview-tool') {
    var mode = 'desktop';
    var run2 = function () {
      var t = val('sp-title'), d = val('sp-desc'), u = val('sp-url');
      var tw = px(t, '20px Arial'), dw = px(d, '14px Arial');
      var dMax = mode === 'desktop' ? 920 : 680;
      meter($('sp-tm'), tw, 600, 'px', 285);
      meter($('sp-dm'), dw, dMax, 'px', 400);
      $('sp-tc').textContent = chars(t) + ' characters';
      $('sp-dc').textContent = chars(d) + ' characters';
      var dateTxt = $('sp-date').checked ? new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }) + ' — ' : '';
      var dShown = cut(d || 'Add a meta description to control the text under your title. If you leave it empty, Google picks text from the page.', '14px Arial', dMax - (dateTxt ? px(dateTxt, '14px Arial') : 0));
      $('sp-out').className = 'serp-wrap ' + mode;
      $('sp-out').innerHTML = '<div class="serp big"><div class="serp-site"><span class="serp-fav">' + esc((crumbs(u)[0] || 'e').toUpperCase()) + '</span><div><b>' + esc(val('sp-name') || crumbs(u).split(' ')[0]) + '</b><span class="serp-url">' + esc(crumbs(u)) + '</span></div></div>' +
        '<div class="serp-title">' + esc(cut(t || 'Your page title goes here', '20px Arial', mode === 'desktop' ? 600 : 560)) + '</div><div class="serp-desc">' + (dateTxt ? '<span class="serp-date">' + esc(dateTxt) + '</span>' : '') + esc(dShown) + '</div></div>';
      var tips = [];
      if (!t) tips.push('Add a title. It’s the clickable headline in search results.');
      else if (tw > 600) tips.push('Your title is ' + Math.round(tw - 600) + ' px too wide and will likely be cut off. Shorten it or move the key words to the front.');
      else if (tw < 285) tips.push('Your title is quite short. You have room to add a benefit or your brand name.');
      if (d && dw > dMax) tips.push('Your description is longer than Google shows on ' + mode + '. The end will be replaced with “…”.');
      if (d && chars(d) < 70) tips.push('A short description may be replaced by text Google picks from the page. Aim for 120–160 characters.');
      $('sp-tips').innerHTML = tips.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') || '<li class="ok">Looks good: the title and description fit.</li>';
    };
    ['sp-title', 'sp-desc', 'sp-url', 'sp-name', 'sp-date'].forEach(function (id) { $(id).addEventListener('input', run2); $(id).addEventListener('change', run2); });
    document.querySelectorAll('[data-mode]').forEach(function (b) {
      b.addEventListener('click', function () { mode = b.getAttribute('data-mode'); document.querySelectorAll('[data-mode]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); run2(); });
    });
    $('sp-fetch').addEventListener('click', async function () {
      var u = val('sp-url'), m = $('sp-msg'), b = $('sp-fetch');
      if (!u) { m.textContent = 'Enter the page URL first.'; return; }
      b.disabled = true; m.textContent = 'Fetching the current title and description…';
      try { var d = await fetchPage(u); $('sp-title').value = d.html.title || ''; $('sp-desc').value = d.html.description || ''; $('sp-url').value = d.finalUrl; m.textContent = 'Loaded from the live page. Edit the text to try new versions.'; run2(); }
      catch (e) { m.textContent = e.message; } finally { b.disabled = false; }
    });
    run2();
  }

  /* ============================================================ robots.txt generator */
  if (tool === 'robots-txt-generator') {
    var AI_TRAIN = ['GPTBot', 'ClaudeBot', 'Google-Extended', 'CCBot', 'Applebot-Extended', 'meta-externalagent', 'Bytespider', 'Amazonbot'];
    var AI_SEARCH = ['OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot'];
    var run3 = function () {
      var def = $('rb-default').value, delay = val('rb-delay'), sm = val('rb-sitemap').split(/\s+/).filter(Boolean);
      var dis = val('rb-disallow').split(/\n+/).map(function (s) { return s.trim(); }).filter(Boolean).map(function (s) { return s[0] === '/' || s[0] === '*' ? s : '/' + s; });
      var alw = val('rb-allow').split(/\n+/).map(function (s) { return s.trim(); }).filter(Boolean).map(function (s) { return s[0] === '/' || s[0] === '*' ? s : '/' + s; });
      var L = ['User-agent: *'];
      if (def === 'block') L.push('Disallow: /');
      else { if (!dis.length && !alw.length) L.push('Disallow:'); dis.forEach(function (p) { L.push('Disallow: ' + p); }); alw.forEach(function (p) { L.push('Allow: ' + p); }); }
      if (delay) L.push('Crawl-delay: ' + delay);
      var block = [];
      if ($('rb-ai').checked) block = block.concat(AI_TRAIN);
      if ($('rb-ais').checked) block = block.concat(AI_SEARCH);
      block.forEach(function (bot) { L.push('', 'User-agent: ' + bot, 'Disallow: /'); });
      if (sm.length) { L.push(''); sm.forEach(function (s) { L.push('Sitemap: ' + s); }); }
      $('rb-out').value = L.join('\n') + '\n';
      var w = [];
      if (def === 'block') w.push('“Block all” stops every search engine from crawling the site. Use it only for private or staging sites.');
      if (delay) w.push('Google ignores Crawl-delay. Bing and some other crawlers respect it.');
      sm.forEach(function (s) { if (!/^https?:\/\//i.test(s)) w.push('Sitemap addresses must be full URLs, e.g. https://example.com/sitemap.xml.'); });
      if (dis.some(function (p) { return p === '/'; })) w.push('Disallow: / in the list blocks the whole site.');
      if ($('rb-ais').checked) w.push('Blocking AI search crawlers can keep your pages out of ChatGPT search and Perplexity answers, which can cost you visitors.');
      $('rb-warn').innerHTML = w.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('');
    };
    ['rb-default', 'rb-delay', 'rb-sitemap', 'rb-disallow', 'rb-allow', 'rb-ai', 'rb-ais'].forEach(function (id) { $(id).addEventListener('input', run3); $(id).addEventListener('change', run3); });
    copyBtn('rb-copy', 'rb-out');
    $('rb-dl').addEventListener('click', function () { download('robots.txt', $('rb-out').value); });
    run3();
  }

  /* ============================================================ keyword density */
  if (tool === 'keyword-density-checker') {
    var STOP = new Set(('a about above after again against all am an and any are as at be because been before being below between both but by can could did do does doing down during each few for from further had has have having he her here hers him his how i if in into is it its just me more most my no nor not now of off on once only or other our out over own same she should so some such than that the their them then there these they this those through to too under until up very was we were what when where which while who whom why will with would you your also may might must one get got us via ' +
      'can’t don’t it’s you’re we’re they’re i’m that’s cant dont youre theyre im thats').split(/\s+/));
    var run4 = function () {
      var text = $('kd-text').value, skip = $('kd-stop').checked, target = val('kd-target').toLowerCase();
      var words = (text.toLowerCase().match(/[\p{L}\p{N}][\p{L}\p{N}'’-]*/gu) || []);
      var n = words.length;
      $('kd-words').textContent = n.toLocaleString('en-US');
      $('kd-unique').textContent = new Set(words).size.toLocaleString('en-US');
      if (!n) { $('kd-out').innerHTML = ''; $('kd-tgt').innerHTML = ''; return; }
      function grams(k) {
        var f = new Map();
        for (var i = 0; i + k <= n; i++) {
          var g = words.slice(i, i + k);
          if (skip && (STOP.has(g[0]) || STOP.has(g[k - 1]))) continue;
          if (g.some(function (w) { return /^\d+$/.test(w); }) && k === 1) continue;
          if (k === 1 && g[0].length < 2) continue;
          var key = g.join(' '); f.set(key, (f.get(key) || 0) + 1);
        }
        return [...f.entries()].filter(function (e) { return k === 1 || e[1] > 1; }).sort(function (a, b) { return b[1] - a[1]; }).slice(0, 15);
      }
      var html = [[1, 'Single words'], [2, 'Two-word phrases'], [3, 'Three-word phrases']].map(function (g) {
        var rows = grams(g[0]);
        return '<div class="kd-col"><h3>' + g[1] + '</h3>' + (rows.length ? '<table class="kd-tbl"><thead><tr><th>Keyword</th><th>Count</th><th>Density</th></tr></thead><tbody>' + rows.map(function (r) {
          var dens = r[1] * g[0] / n * 100;
          return '<tr' + (dens > 4 && g[0] === 1 ? ' class="kd-hi"' : '') + '><td>' + esc(r[0]) + '</td><td>' + r[1] + '</td><td>' + dens.toFixed(2) + '%</td></tr>';
        }).join('') + '</tbody></table>' : '<p class="count-note">Not enough repeated phrases yet.</p>') + '</div>';
      }).join('');
      $('kd-out').innerHTML = html;
      if (target) {
        var tw = target.split(/\s+/), cnt = 0;
        for (var i = 0; i + tw.length <= n; i++) { var ok = true; for (var j = 0; j < tw.length; j++) if (words[i + j] !== tw[j]) { ok = false; break; } if (ok) cnt++; }
        var dens = cnt * tw.length / n * 100, first = words.slice(0, 100).join(' ').indexOf(target) >= 0;
        var note = cnt === 0 ? 'The keyword doesn’t appear in the text.' : dens > 3 ? 'That’s high. Repeating a keyword this often can read as stuffing; use synonyms and related terms instead.' : dens < 0.5 ? 'Fairly light. Make sure the topic is clear, especially in the title, first paragraph and headings.' : 'A natural level for most pages.';
        $('kd-tgt').innerHTML = '<p><b>“' + esc(target) + '”</b> appears <b>' + cnt + '</b> time' + (cnt === 1 ? '' : 's') + ' (' + dens.toFixed(2) + '% density). ' + (first ? 'It’s in the first 100 words. ' : cnt ? 'It isn’t in the first 100 words. ' : '') + esc(note) + '</p>';
      } else $('kd-tgt').innerHTML = '';
    };
    ['kd-text', 'kd-stop', 'kd-target'].forEach(function (id) { $(id).addEventListener('input', run4); $(id).addEventListener('change', run4); });
    $('kd-fetch').addEventListener('click', async function () {
      var u = val('kd-url'), m = $('kd-msg'), b = $('kd-fetch');
      if (!u) { m.textContent = 'Enter a page URL, or paste text below.'; return; }
      b.disabled = true; m.textContent = 'Fetching the page text…';
      try { var d = await fetchPage(u, true); $('kd-text').value = d.html.fullText || ''; m.textContent = 'Loaded the visible text of ' + d.finalUrl + ' (menus and footers included).'; run4(); }
      catch (e) { m.textContent = e.message; } finally { b.disabled = false; }
    });
    run4();
  }
})();
