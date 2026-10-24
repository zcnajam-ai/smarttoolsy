/* SmartToolsy tool logic. Each block runs only on its own page. */
(function () {
  'use strict';
  var $ = ST.$, fmt = ST.fmt, esc = ST.esc;
  var tool = document.body.getAttribute('data-tool');
  var T = {};
  function on(id, ev, fn) { var el = $(id); if (el) el.addEventListener(ev, fn); }
  function todayISO() { var d = new Date(); d.setMinutes(d.getMinutes() - d.getTimezoneOffset()); return d.toISOString().slice(0, 10); }
  function parseDate(s) { if (!s) return null; var p = s.split('-'); return new Date(Date.UTC(+p[0], +p[1] - 1, +p[2])); }
  function addMonths(a, n) { // same day n months later, clamped to the end of a short month
    var y = a.getUTCFullYear(), m = a.getUTCMonth() + n, last = new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
    return new Date(Date.UTC(y, m, Math.min(a.getUTCDate(), last)));
  }
  function ymd(a, b) { // complete years, months, days from a to b (a <= b), UTC dates
    var months = (b.getUTCFullYear() - a.getUTCFullYear()) * 12 + b.getUTCMonth() - a.getUTCMonth();
    var anchor = addMonths(a, months);
    if (anchor > b) { months--; anchor = addMonths(a, months); }
    return { y: Math.floor(months / 12), m: months % 12, d: Math.round((b - anchor) / 864e5) };
  }
  function plural(n, w) { return fmt(n, 0) + ' ' + w + (n === 1 ? '' : 's'); }
  function rand(n) { // unbiased integer in [0, n)
    var max = 4294967296, lim = max - (max % n), buf = new Uint32Array(1);
    do { crypto.getRandomValues(buf); } while (buf[0] >= lim);
    return buf[0] % n;
  }

  /* ---------- Word counter ---------- */
  T['word-counter'] = function () {
    var inp = $('wc-in');
    var STOP = 'the a an and or but of to in on at for with is are was were be been it this that as by from i you he she we they not your our my'.split(' ');
    function run() {
      var t = inp.value, words = t.match(/[\p{L}\p{N}]+(?:[-'’][\p{L}\p{N}]+)*/gu) || [];
      $('wc-words').textContent = fmt(words.length, 0);
      $('wc-chars').textContent = fmt(t.length, 0);
      $('wc-nospace').textContent = fmt(t.replace(/\s/g, '').length, 0);
      $('wc-sent').textContent = fmt(t.trim() ? (t.match(/[^.!?]+[.!?]+(\s|$)|[^.!?]+$/g) || []).filter(function (s) { return s.trim(); }).length : 0, 0);
      $('wc-para').textContent = fmt(t.split(/\n+/).filter(function (p) { return p.trim(); }).length, 0);
      function mins(wpm) { var s = Math.round(words.length / wpm * 60); return s < 60 ? s + ' sec' : Math.floor(s / 60) + ' min ' + (s % 60 ? s % 60 + ' sec' : ''); }
      $('wc-read').textContent = mins(238); $('wc-speak').textContent = mins(140);
      var freq = {};
      words.forEach(function (w) { w = w.toLowerCase(); if (w.length > 2 && STOP.indexOf(w) === -1) freq[w] = (freq[w] || 0) + 1; });
      var top = Object.keys(freq).sort(function (a, b) { return freq[b] - freq[a]; }).slice(0, 10);
      $('wc-top').innerHTML = top.length ? top.map(function (w) { return esc(w) + ' — ' + freq[w] + ' (' + fmt(freq[w] / words.length * 100, 1) + '%)'; }).join('<br>') : 'Start typing to see keyword frequency.';
    }
    inp.addEventListener('input', run);
    on('wc-copy', 'click', function () { ST.copy(inp.value); });
    on('wc-clear', 'click', function () { inp.value = ''; run(); inp.focus(); });
    run();
  };

  /* ---------- Case converter ---------- */
  T['case-converter'] = function () {
    var inp = $('cc-in');
    var SMALL = /^(a|an|and|as|at|but|by|for|in|nor|of|on|or|per|so|the|to|up|via|vs?\.?|yet)$/i;
    function words(line) { return line.replace(/([a-z0-9])([A-Z])/g, '$1 $2').split(/[^\p{L}\p{N}]+/u).filter(Boolean); }
    var F = {
      upper: function (t) { return t.toUpperCase(); },
      lower: function (t) { return t.toLowerCase(); },
      title: function (t) {
        return t.split('\n').map(function (line) {
          var parts = line.toLowerCase().split(/(\s+)/), first = true, n = parts.filter(function (p) { return p.trim(); }).length, i = 0;
          return parts.map(function (w) {
            if (!w.trim()) return w; i++;
            var keep = !first && i !== n && SMALL.test(w); first = false;
            return keep ? w : w.replace(/\p{L}/u, function (c) { return c.toUpperCase(); });
          }).join('');
        }).join('\n');
      },
      sentence: function (t) { return t.toLowerCase().replace(/(^\s*|[.!?]\s+|\n\s*)(\p{L})/gu, function (m, a, b) { return a + b.toUpperCase(); }); },
      camel: function (t) { return t.split('\n').map(function (l) { return words(l).map(function (w, i) { w = w.toLowerCase(); return i ? w.charAt(0).toUpperCase() + w.slice(1) : w; }).join(''); }).join('\n'); },
      pascal: function (t) { return t.split('\n').map(function (l) { return words(l).map(function (w) { w = w.toLowerCase(); return w.charAt(0).toUpperCase() + w.slice(1); }).join(''); }).join('\n'); },
      snake: function (t) { return t.split('\n').map(function (l) { return words(l).join('_').toLowerCase(); }).join('\n'); },
      kebab: function (t) { return t.split('\n').map(function (l) { return words(l).join('-').toLowerCase(); }).join('\n'); },
      alt: function (t) { var i = 0; return t.replace(/\p{L}/gu, function (c) { return i++ % 2 ? c.toUpperCase() : c.toLowerCase(); }); }
    };
    $('cc-btns').addEventListener('click', function (e) { var b = e.target.closest('[data-case]'); if (b) inp.value = F[b.dataset.case](inp.value); });
    on('cc-copy', 'click', function () { ST.copy(inp.value); });
  };

  /* ---------- Lorem ipsum ---------- */
  T['lorem-ipsum-generator'] = function () {
    var W = 'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo consequat duis aute irure in reprehenderit voluptate velit esse cillum fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt culpa qui officia deserunt mollit anim id est laborum porta nibh venenatis cras pulvinar mattis nunc blandit turpis cursus faucibus scelerisque viverra mauris pellentesque habitant morbi tristique senectus netus malesuada fames ac egestas'.split(' ');
    var OPEN = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.';
    function word() { return W[rand(W.length)]; }
    function sentence() { var n = 6 + rand(10), s = []; for (var i = 0; i < n; i++) s.push(word()); if (n > 9) s[3 + rand(3)] += ','; var t = s.join(' '); return t.charAt(0).toUpperCase() + t.slice(1) + '.'; }
    function para() { var n = 4 + rand(4), s = []; for (var i = 0; i < n; i++) s.push(sentence()); return s.join(' '); }
    function gen() {
      var n = Math.min(100, Math.max(1, parseInt($('li-n').value, 10) || 1)), u = $('li-unit').value, start = $('li-start').checked, out;
      if (u === 'w') { var ws = []; for (var i = 0; i < n; i++) ws.push(word()); if (start) { var o = OPEN.replace(/[.,]/g, '').toLowerCase().split(' '); for (i = 0; i < Math.min(n, o.length); i++) ws[i] = o[i]; } out = ws.join(' '); out = out.charAt(0).toUpperCase() + out.slice(1); }
      else if (u === 's') { var ss = []; for (i = 0; i < n; i++) ss.push(sentence()); if (start) ss[0] = OPEN; out = ss.join(' '); }
      else { var ps = []; for (i = 0; i < n; i++) ps.push(para()); if (start) ps[0] = OPEN + ' ' + ps[0]; out = $('li-html').checked ? ps.map(function (p) { return '<p>' + p + '</p>'; }).join('\n\n') : ps.join('\n\n'); }
      $('li-out').value = out;
    }
    on('li-go', 'click', gen); on('li-copy', 'click', function () { ST.copy($('li-out').value); }); gen();
  };

  /* ---------- Text cleaner ---------- */
  T['text-cleaner'] = function () {
    on('tc-go', 'click', function () {
      var t = $('tc-in').value.replace(/\r\n?/g, '\n'), before = t ? t.split('\n').length : 0;
      if ($('tc-breaks').checked) t = t.split(/\n\s*\n/).map(function (p) { return p.replace(/\s*\n\s*/g, ' '); }).join('\n\n');
      var lines = t.split('\n');
      if ($('tc-spaces').checked) lines = lines.map(function (l) { return l.replace(/[ \t ]+/g, ' '); });
      if ($('tc-trim').checked) lines = lines.map(function (l) { return l.trim(); });
      if ($('tc-empty').checked) lines = lines.filter(function (l) { return l.trim(); });
      if ($('tc-dupes').checked) { var seen = {}; lines = lines.filter(function (l) { if (seen['_' + l]) return false; seen['_' + l] = 1; return true; }); }
      if ($('tc-sort').checked) lines.sort(function (a, b) { return a.localeCompare(b); });
      $('tc-out').value = lines.join('\n');
      $('tc-note').textContent = 'Lines: ' + fmt(before, 0) + ' before, ' + fmt(lines.length, 0) + ' after.';
    });
    on('tc-copy', 'click', function () { ST.copy($('tc-out').value); });
  };

  /* ---------- Slug ---------- */
  T['slug-generator'] = function () {
    var STOP = /^(a|an|and|are|as|at|be|by|for|from|in|is|it|of|on|or|the|to|with|your|you|how|what|why)$/;
    function run() {
      var sep = $('sg-sep').value, max = parseInt($('sg-max').value, 10) || 60;
      var s = $('sg-in').value.normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/ß/g, 'ss').replace(/[æ]/g, 'ae').replace(/[ø]/g, 'o')
        .toLowerCase().replace(/&/g, ' and ').replace(/['’]/g, '');
      var w = s.split(/[^a-z0-9]+/).filter(Boolean);
      if ($('sg-stop').checked && w.length > 2) { var f = w.filter(function (x) { return !STOP.test(x); }); if (f.length) w = f; }
      var out = '';
      for (var i = 0; i < w.length; i++) { var next = out ? out + sep + w[i] : w[i]; if (next.length > max && out) break; out = next.slice(0, max); }
      $('sg-out').textContent = out || '—';
    }
    ['sg-in', 'sg-max'].forEach(function (id) { on(id, 'input', run); });
    ['sg-sep', 'sg-stop'].forEach(function (id) { on(id, 'change', run); });
    on('sg-copy', 'click', function () { var v = $('sg-out').textContent; if (v !== '—') ST.copy(v); });
    run();
  };

  /* ---------- Age ---------- */
  T['age-calculator'] = function () {
    $('ag-on').value = todayISO();
    on('ag-go', 'click', function () {
      var a = parseDate($('ag-dob').value), b = parseDate($('ag-on').value), out = $('ag-out');
      if (!a || !b) { out.innerHTML = '<span class="err">Enter a date of birth.</span>'; return; }
      if (a > b) { out.innerHTML = '<span class="err">The date of birth is after the second date.</span>'; return; }
      var r = ymd(a, b), days = Math.round((b - a) / 864e5);
      var ny = b.getUTCFullYear(), bm = a.getUTCMonth(), bd = a.getUTCDate();
      function bday(y) { var d = new Date(Date.UTC(y, bm, bd)); if (d.getUTCMonth() !== bm) d = new Date(Date.UTC(y, 2, 1)); return d; }
      var next = bday(ny); if (next <= b) next = bday(ny + 1);
      var toNext = Math.round((next - b) / 864e5);
      out.innerHTML = '<div class="big">' + plural(r.y, 'year') + ', ' + plural(r.m, 'month') + ', ' + plural(r.d, 'day') + '</div>' +
        '<div class="stats"><div class="stat"><b>' + fmt(r.y * 12 + r.m, 0) + '</b><span>Total months</span></div>' +
        '<div class="stat"><b>' + fmt(Math.floor(days / 7), 0) + '</b><span>Total weeks</span></div>' +
        '<div class="stat"><b>' + fmt(days, 0) + '</b><span>Total days</span></div>' +
        '<div class="stat"><b>' + fmt(toNext, 0) + '</b><span>Days to next birthday</span></div></div>';
    });
  };

  /* ---------- BMI ---------- */
  T['bmi-calculator'] = function () {
    document.querySelectorAll('input[name="bm-u"]').forEach(function (r) {
      r.addEventListener('change', function () { var m = document.querySelector('input[name="bm-u"]:checked').value === 'm'; $('bm-metric').hidden = !m; $('bm-imp').hidden = m; $('bm-out').innerHTML = ''; });
    });
    on('bm-go', 'click', function () {
      var metric = !$('bm-metric').hidden, kg, m, out = $('bm-out');
      if (metric) { kg = parseFloat($('bm-kg').value); m = parseFloat($('bm-cm').value) / 100; }
      else { kg = parseFloat($('bm-lb').value) * 0.45359237; m = ((parseFloat($('bm-ft').value) || 0) * 12 + (parseFloat($('bm-in').value) || 0)) * 0.0254; }
      if (!(kg > 0) || !(m > 0.3)) { out.innerHTML = '<span class="err">Enter a weight and height greater than zero.</span>'; return; }
      var bmi = kg / (m * m), cat = bmi < 18.5 ? 'Underweight' : bmi < 25 ? 'Healthy weight' : bmi < 30 ? 'Overweight' : 'Obesity';
      var lo = 18.5 * m * m, hi = 24.9 * m * m;
      var range = metric ? fmt(lo, 1) + ' – ' + fmt(hi, 1) + ' kg' : fmt(lo / 0.45359237, 1) + ' – ' + fmt(hi / 0.45359237, 1) + ' lb';
      out.innerHTML = '<div class="big">BMI ' + fmt(bmi, 1) + '</div><p style="margin:4px 0 0"><strong>' + cat + '</strong>. A healthy weight for your height is about ' + range + '.</p>';
    });
  };

  /* ---------- Percentage ---------- */
  T['percentage-calculator'] = function () {
    function v(id) { var x = $(id).value; return x === '' ? NaN : parseFloat(x); }
    function run() {
      var a1 = v('pc-a1'), a2 = v('pc-a2'), b1 = v('pc-b1'), b2 = v('pc-b2'), c1 = v('pc-c1'), c2 = v('pc-c2');
      $('pc-a').textContent = isFinite(a1) && isFinite(a2) ? fmt(a1 / 100 * a2, 4) : '—';
      $('pc-b').textContent = isFinite(b1) && isFinite(b2) && b2 !== 0 ? fmt(b1 / b2 * 100, 4) + '%' : '—';
      if (isFinite(c1) && isFinite(c2) && c1 !== 0) { var ch = (c2 - c1) / Math.abs(c1) * 100; $('pc-c').textContent = (ch >= 0 ? '+' : '') + fmt(ch, 4) + '% (' + (ch >= 0 ? 'increase' : 'decrease') + ')'; }
      else $('pc-c').textContent = '—';
    }
    ['pc-a1', 'pc-a2', 'pc-b1', 'pc-b2', 'pc-c1', 'pc-c2'].forEach(function (id) { on(id, 'input', run); });
  };

  /* ---------- Loan ---------- */
  T['loan-calculator'] = function () {
    on('ln-go', 'click', function () {
      var P = parseFloat($('ln-p').value), R = parseFloat($('ln-r').value), Y = parseFloat($('ln-y').value), out = $('ln-out');
      if (!(P > 0) || !(Y > 0) || !(R >= 0)) { out.innerHTML = '<span class="err">Enter a loan amount, a rate of 0 or more, and a term.</span>'; $('ln-sched-wrap').hidden = true; return; }
      var n = Math.round(Y * 12), r = R / 1200, M = r === 0 ? P / n : P * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
      var total = M * n;
      out.innerHTML = '<span class="lbl">Monthly payment</span><div class="big">' + fmt(M, 2) + '</div>' +
        '<div class="stats"><div class="stat"><b>' + fmt(total - P, 2) + '</b><span>Total interest</span></div>' +
        '<div class="stat"><b>' + fmt(total, 2) + '</b><span>Total of ' + n + ' payments</span></div></div>';
      var bal = P, rows = '', yi = 0, yp = 0;
      for (var k = 1; k <= n; k++) {
        var int = bal * r, prin = M - int; bal -= prin; yi += int; yp += prin;
        if (k % 12 === 0 || k === n) { rows += '<tr><td>' + Math.ceil(k / 12) + '</td><td>' + fmt(yp, 2) + '</td><td>' + fmt(yi, 2) + '</td><td>' + fmt(Math.max(0, bal), 2) + '</td></tr>'; yi = yp = 0; }
      }
      $('ln-sched').innerHTML = '<table style="width:100%;border-collapse:collapse;margin-top:8px" class="sched"><thead><tr><th>Year</th><th>Principal</th><th>Interest</th><th>Balance</th></tr></thead><tbody>' + rows + '</tbody></table>';
      $('ln-sched-wrap').hidden = false;
    });
  };

  /* ---------- Discount ---------- */
  T['discount-calculator'] = function () {
    function run() {
      var p = parseFloat($('ds-p').value) || 0, d1 = parseFloat($('ds-d').value) || 0, d2 = parseFloat($('ds-d2').value) || 0, t = parseFloat($('ds-t').value) || 0;
      var after = p * (1 - d1 / 100) * (1 - d2 / 100), final = after * (1 + t / 100);
      $('ds-final').textContent = fmt(final, 2); $('ds-save').textContent = fmt(p - after, 2);
      $('ds-eff').textContent = p ? fmt((1 - after / p) * 100, 2) + '%' : '—';
    }
    ['ds-p', 'ds-d', 'ds-d2', 'ds-t'].forEach(function (id) { on(id, 'input', run); }); run();
  };

  /* ---------- Date difference ---------- */
  T['date-difference-calculator'] = function () {
    $('dd-a').value = todayISO();
    on('dd-go', 'click', function () {
      var a = parseDate($('dd-a').value), b = parseDate($('dd-b').value), out = $('dd-out');
      if (!a || !b) { out.innerHTML = '<span class="err">Choose both dates.</span>'; return; }
      if (a > b) { var t = a; a = b; b = t; }
      var inc = $('dd-inc').checked, days = Math.round((b - a) / 864e5) + (inc ? 1 : 0);
      var end = inc ? new Date(b.getTime() + 864e5) : b, r = ymd(a, end);
      var biz = 0; for (var d = new Date(a); d < end; d = new Date(d.getTime() + 864e5)) { var w = d.getUTCDay(); if (w && w !== 6) biz++; }
      out.innerHTML = '<div class="big">' + plural(days, 'day') + '</div><p style="margin:4px 0 0">' +
        (r.y ? plural(r.y, 'year') + ', ' : '') + plural(r.m, 'month') + ', ' + plural(r.d, 'day') + '</p>' +
        '<div class="stats"><div class="stat"><b>' + fmt(Math.floor(days / 7), 0) + ' w ' + days % 7 + ' d</b><span>Weeks and days</span></div>' +
        '<div class="stat"><b>' + fmt(biz, 0) + '</b><span>Business days</span></div>' +
        '<div class="stat"><b>' + fmt(days * 24, 0) + '</b><span>Hours</span></div></div>';
    });
  };

  /* ---------- Unit converter ---------- */
  T['unit-converter'] = function () {
    var U = {
      length: { 'Millimetre (mm)': 0.001, 'Centimetre (cm)': 0.01, 'Metre (m)': 1, 'Kilometre (km)': 1000, 'Inch (in)': 0.0254, 'Foot (ft)': 0.3048, 'Yard (yd)': 0.9144, 'Mile (mi)': 1609.344, 'Nautical mile': 1852 },
      mass: { 'Milligram (mg)': 1e-6, 'Gram (g)': 0.001, 'Kilogram (kg)': 1, 'Tonne (t)': 1000, 'Ounce (oz)': 0.028349523125, 'Pound (lb)': 0.45359237, 'Stone (st)': 6.35029318, 'US ton': 907.18474 },
      temp: { 'Celsius (°C)': 'c', 'Fahrenheit (°F)': 'f', 'Kelvin (K)': 'k' },
      area: { 'Square centimetre': 1e-4, 'Square metre': 1, 'Hectare': 1e4, 'Square kilometre': 1e6, 'Square inch': 0.00064516, 'Square foot': 0.09290304, 'Square yard': 0.83612736, 'Acre': 4046.8564224, 'Square mile': 2589988.110336 },
      volume: { 'Millilitre (ml)': 0.001, 'Litre (l)': 1, 'Cubic metre': 1000, 'Teaspoon (US)': 0.00492892159375, 'Tablespoon (US)': 0.01478676478125, 'Cup (US)': 0.2365882365, 'Fluid ounce (US)': 0.0295735295625, 'Pint (US)': 0.473176473, 'Quart (US)': 0.946352946, 'US gallon': 3.785411784, 'UK gallon': 4.54609 },
      speed: { 'Metres per second': 1, 'Kilometres per hour': 1 / 3.6, 'Miles per hour': 0.44704, 'Knots': 1852 / 3600, 'Feet per second': 0.3048 }
    };
    var DEF = { length: [1, 4], mass: [2, 5], temp: [0, 1], area: [1, 6], volume: [1, 9], speed: [1, 2] };
    function toBase(t, u, v) { var f = U[t][u]; if (t !== 'temp') return v * f; return f === 'c' ? v : f === 'f' ? (v - 32) * 5 / 9 : v - 273.15; }
    function fromBase(t, u, v) { var f = U[t][u]; if (t !== 'temp') return v / f; return f === 'c' ? v : f === 'f' ? v * 9 / 5 + 32 : v + 273.15; }
    function nice(x) { if (!isFinite(x)) return '—'; var a = Math.abs(x); return a !== 0 && (a < 1e-4 || a >= 1e12) ? x.toPrecision(6) : fmt(x, 6); }
    function fill() {
      var t = $('uc-type').value, keys = Object.keys(U[t]), html = keys.map(function (k) { return '<option>' + k + '</option>'; }).join('');
      $('uc-from').innerHTML = html; $('uc-to').innerHTML = html;
      $('uc-from').selectedIndex = DEF[t][0]; $('uc-to').selectedIndex = DEF[t][1]; run();
    }
    function run() {
      var t = $('uc-type').value, v = parseFloat($('uc-val').value), from = $('uc-from').value, to = $('uc-to').value;
      if (!isFinite(v)) { $('uc-out').textContent = '—'; $('uc-all').innerHTML = ''; return; }
      var base = toBase(t, from, v);
      $('uc-out').textContent = nice(v) + ' ' + from.replace(/ \(.*\)/, '') + ' = ' + nice(fromBase(t, to, base)) + ' ' + to.replace(/ \(.*\)/, '');
      $('uc-all').innerHTML = Object.keys(U[t]).filter(function (k) { return k !== from; }).map(function (k) { return nice(fromBase(t, k, base)) + ' ' + esc(k); }).join('<br>');
    }
    on('uc-type', 'change', fill); on('uc-val', 'input', run); on('uc-from', 'change', run); on('uc-to', 'change', run);
    on('uc-swap', 'click', function () { var a = $('uc-from').selectedIndex; $('uc-from').selectedIndex = $('uc-to').selectedIndex; $('uc-to').selectedIndex = a; run(); });
    fill();
  };

  /* ---------- Color converter ---------- */
  T['color-converter'] = function () {
    function hexToRgb(h) { h = h.trim().replace(/^#/, ''); if (/^[0-9a-f]{3}$/i.test(h)) h = h.replace(/./g, '$&$&'); if (!/^[0-9a-f]{6}$/i.test(h)) return null; return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4), 16)]; }
    function rgbToHex(c) { return '#' + c.map(function (x) { return ('0' + x.toString(16)).slice(-2); }).join('').toUpperCase(); }
    function rgbToHsl(c) {
      var r = c[0] / 255, g = c[1] / 255, b = c[2] / 255, mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2, h = 0, s = 0, d = mx - mn;
      if (d) { s = d / (1 - Math.abs(2 * l - 1)); h = mx === r ? ((g - b) / d) % 6 : mx === g ? (b - r) / d + 2 : (r - g) / d + 4; h *= 60; if (h < 0) h += 360; }
      return [Math.round(h), Math.round(s * 100), Math.round(l * 100)];
    }
    function hslToRgb(h, s, l) { s /= 100; l /= 100; var k = function (n) { return (n + h / 30) % 12; }, a = s * Math.min(l, 1 - l); var f = function (n) { return Math.round(255 * (l - a * Math.max(-1, Math.min(k(n) - 3, 9 - k(n), 1)))); }; return [f(0), f(8), f(4)]; }
    function lum(c) { var v = c.map(function (x) { x /= 255; return x <= 0.04045 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); }); return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]; }
    function show(rgb, src) {
      $('co-err').textContent = '';
      var hex = rgbToHex(rgb), hsl = rgbToHsl(rgb);
      if (src !== 'hex') $('co-hex').value = hex;
      if (src !== 'rgb') $('co-rgb').value = 'rgb(' + rgb.join(', ') + ')';
      if (src !== 'hsl') $('co-hsl').value = 'hsl(' + hsl[0] + ', ' + hsl[1] + '%, ' + hsl[2] + '%)';
      if (src !== 'pick') $('co-pick').value = hex.toLowerCase();
      var L = lum(rgb), cw = 1.05 / (L + 0.05), cb = (L + 0.05) / 0.05, white = cw >= cb;
      var sw = $('co-swatch'); sw.style.background = hex; sw.style.color = white ? '#fff' : '#000';
      var best = Math.max(cw, cb);
      $('co-contrast').textContent = (white ? 'White' : 'Black') + ' text contrast ' + best.toFixed(2) + ':1 — ' + (best >= 7 ? 'passes AAA' : best >= 4.5 ? 'passes AA' : best >= 3 ? 'large text only (AA)' : 'fails WCAG');
    }
    on('co-pick', 'input', function () { show(hexToRgb($('co-pick').value), 'pick'); });
    on('co-hex', 'input', function () { var c = hexToRgb($('co-hex').value); c ? show(c, 'hex') : ($('co-err').textContent = 'Enter a HEX code like #2F5BEA or #F80.'); });
    on('co-rgb', 'input', function () { var m = $('co-rgb').value.match(/\d+(\.\d+)?/g); if (m && m.length >= 3 && m.slice(0, 3).every(function (x) { return +x <= 255; })) show(m.slice(0, 3).map(function (x) { return Math.round(+x); }), 'rgb'); else $('co-err').textContent = 'Enter RGB like rgb(47, 91, 234), each value 0–255.'; });
    on('co-hsl', 'input', function () { var m = $('co-hsl').value.match(/\d+(\.\d+)?/g); if (m && m.length >= 3 && +m[0] <= 360 && +m[1] <= 100 && +m[2] <= 100) show(hslToRgb(+m[0], +m[1], +m[2]), 'hsl'); else $('co-err').textContent = 'Enter HSL like hsl(226, 81%, 55%).'; });
    show(hexToRgb('#2F5BEA'), 'hex');
  };

  /* ---------- Base64 ---------- */
  T['base64-encoder-decoder'] = function () {
    function enc(s) { var b = new TextEncoder().encode(s), bin = ''; for (var i = 0; i < b.length; i += 0x8000) bin += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000)); var o = btoa(bin); return $('b6-url').checked ? o.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '') : o; }
    function dec(s) { s = s.replace(/\s/g, '').replace(/-/g, '+').replace(/_/g, '/'); while (s.length % 4) s += '='; var bin = atob(s), b = new Uint8Array(bin.length); for (var i = 0; i < bin.length; i++) b[i] = bin.charCodeAt(i); return new TextDecoder('utf-8', { fatal: true }).decode(b); }
    on('b6-enc', 'click', function () { $('b6-err').textContent = ''; $('b6-out').value = enc($('b6-in').value); });
    on('b6-dec', 'click', function () { $('b6-err').textContent = ''; try { $('b6-out').value = dec($('b6-in').value); } catch (e) { $('b6-out').value = ''; $('b6-err').textContent = 'That is not valid Base64, or it decodes to binary data rather than text.'; } });
    on('b6-copy', 'click', function () { ST.copy($('b6-out').value); });
  };

  /* ---------- Timestamp ---------- */
  T['unix-timestamp-converter'] = function () {
    function tick() { $('ts-now').textContent = Math.floor(Date.now() / 1000); }
    tick(); setInterval(tick, 1000);
    var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || 'local time';
    function full(d, utc) { return d.toLocaleString('en-US', { timeZone: utc ? 'UTC' : undefined, weekday: 'short', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false }); }
    on('ts-in', 'input', function () {
      var s = $('ts-in').value.trim(), out = $('ts-out');
      if (!s) { out.innerHTML = ''; return; }
      if (!/^-?\d+(\.\d+)?$/.test(s)) { out.innerHTML = '<span class="err">Enter digits only, like 1767225600.</span>'; return; }
      var n = parseFloat(s), ms = Math.abs(n) >= 1e11 ? n : n * 1000, d = new Date(ms);
      if (isNaN(d)) { out.innerHTML = '<span class="err">That timestamp is out of range.</span>'; return; }
      out.innerHTML = '<p style="margin:0">Read as <strong>' + (Math.abs(n) >= 1e11 ? 'milliseconds' : 'seconds') + '</strong></p>' +
        '<p style="margin:6px 0 0"><strong>UTC:</strong> ' + full(d, true) + '</p><p style="margin:4px 0 0"><strong>' + esc(tz) + ':</strong> ' + full(d) + '</p>' +
        '<p style="margin:4px 0 0"><strong>ISO 8601:</strong> <span class="code">' + d.toISOString() + '</span></p>';
    });
    on('ts-date', 'input', function () {
      var v = $('ts-date').value, out = $('ts-out2'); if (!v) { out.innerHTML = ''; return; }
      var d = new Date(v);
      out.innerHTML = '<p style="margin:0"><strong>Seconds:</strong> <span class="code">' + Math.floor(d.getTime() / 1000) + '</span></p><p style="margin:4px 0 0"><strong>Milliseconds:</strong> <span class="code">' + d.getTime() + '</span></p>';
    });
  };

  /* ---------- Password ---------- */
  T['password-generator'] = function () {
    var SETS = { up: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', low: 'abcdefghijklmnopqrstuvwxyz', num: '0123456789', sym: '!@#$%^&*()-_=+[]{};:,.<>/?~|' };
    function gen() {
      var len = +$('pw-len').value, avoid = $('pw-amb').checked, pools = [];
      $('pw-len-v').textContent = len;
      ['up', 'low', 'num', 'sym'].forEach(function (k) { if ($('pw-' + k).checked) { var s = SETS[k]; if (avoid) s = s.replace(/[Il1O0o|]/g, ''); pools.push(s); } });
      if (!pools.length) { $('pw-out').textContent = 'Choose at least one character type'; $('pw-strength').textContent = ''; return; }
      var all = pools.join(''), chars = pools.map(function (p) { return p[rand(p.length)]; });
      while (chars.length < len) chars.push(all[rand(all.length)]);
      chars = chars.slice(0, len);
      for (var i = chars.length - 1; i > 0; i--) { var j = rand(i + 1), t = chars[i]; chars[i] = chars[j]; chars[j] = t; }
      $('pw-out').textContent = chars.join('');
      var bits = Math.round(len * Math.log2(all.length));
      $('pw-strength').textContent = 'About ' + bits + ' bits of entropy — ' + (bits >= 100 ? 'excellent' : bits >= 80 ? 'very strong' : bits >= 60 ? 'strong' : bits >= 40 ? 'fair' : 'weak');
    }
    on('pw-go', 'click', gen); on('pw-len', 'input', gen);
    ['pw-up', 'pw-low', 'pw-num', 'pw-sym', 'pw-amb'].forEach(function (id) { on(id, 'change', gen); });
    on('pw-copy', 'click', function () { ST.copy($('pw-out').textContent); });
    gen();
  };

  /* ---------- QR code ---------- */
  T['qr-code-generator'] = function () {
    var LBL = { url: 'Website link', text: 'Text', tel: 'Phone number', email: 'Email address' };
    var PH = { url: 'https://example.com', text: 'Any message', tel: '+1 555 0100', email: 'name@example.com' };
    function payload() {
      var t = $('qr-type').value, v = $('qr-in').value.trim();
      if (t === 'wifi') { var e = function (s) { return s.replace(/([\\;,:"])/g, '\\$1'); }; return 'WIFI:T:' + $('qr-enc').value + ';S:' + e($('qr-ssid').value) + ';P:' + ($('qr-enc').value === 'nopass' ? '' : e($('qr-pass').value)) + ';;'; }
      if (t === 'tel') return 'tel:' + v.replace(/[^\d+]/g, '');
      if (t === 'email') return 'mailto:' + v;
      if (t === 'url' && v && !/^[a-z]+:/i.test(v)) return 'https://' + v;
      return v;
    }
    function draw() {
      var c = $('qr-canvas'), size = +$('qr-size').value, ctx = c.getContext('2d'), data = payload();
      c.width = c.height = size; $('qr-err').textContent = '';
      ctx.fillStyle = $('qr-bg').value; ctx.fillRect(0, 0, size, size);
      if (!data || data === 'tel:' || data === 'mailto:') return;
      var q; try { q = QR.make(data); } catch (e) { $('qr-err').textContent = e.message; return; }
      var n = q.size + 8, cell = size / n; ctx.fillStyle = $('qr-fg').value;
      for (var y = 0; y < q.size; y++) for (var x = 0; x < q.size; x++) if (q.get(x, y)) ctx.fillRect(Math.floor((x + 4) * cell), Math.floor((y + 4) * cell), Math.ceil(cell), Math.ceil(cell));
    }
    on('qr-type', 'change', function () {
      var t = $('qr-type').value, w = t === 'wifi'; $('qr-f-wifi').hidden = !w; $('qr-f-main').hidden = w;
      if (!w) { $('qr-in-lbl').textContent = LBL[t]; $('qr-in').placeholder = PH[t]; $('qr-in').value = ''; }
      draw();
    });
    ['qr-in', 'qr-ssid', 'qr-pass', 'qr-fg', 'qr-bg'].forEach(function (id) { on(id, 'input', draw); });
    ['qr-enc', 'qr-size'].forEach(function (id) { on(id, 'change', draw); });
    on('qr-dl', 'click', function () { var a = document.createElement('a'); a.download = 'qr-code.png'; a.href = $('qr-canvas').toDataURL('image/png'); a.click(); });
    draw();
  };

  /* ---------- Random numbers ---------- */
  T['random-number-generator'] = function () {
    on('rn-go', 'click', function () {
      var lo = Math.ceil(+$('rn-min').value), hi = Math.floor(+$('rn-max').value), n = Math.floor(+$('rn-n').value), uniq = $('rn-uniq').checked;
      $('rn-err').textContent = '';
      if (!isFinite(lo) || !isFinite(hi) || hi < lo) { $('rn-err').textContent = 'The maximum must be greater than or equal to the minimum.'; return; }
      if (!(n >= 1 && n <= 1000)) { $('rn-err').textContent = 'Choose between 1 and 1000 numbers.'; return; }
      var span = hi - lo + 1;
      if (span > 4294967296) { $('rn-err').textContent = 'The range is too large. Keep it under about 4 billion.'; return; }
      if (uniq && n > span) { $('rn-err').textContent = 'There are only ' + fmt(span, 0) + ' numbers in that range, so you cannot draw ' + n + ' without repeats.'; return; }
      var out = [], seen = new Set();
      while (out.length < n) { var x = lo + rand(span); if (uniq) { if (seen.has(x)) continue; seen.add(x); } out.push(x); }
      if ($('rn-sort').checked) out.sort(function (a, b) { return a - b; });
      $('rn-out').textContent = out.join(', ');
    });
    on('rn-copy', 'click', function () { ST.copy($('rn-out').textContent); });
  };

  /* ---------- JSON ---------- */
  T['json-formatter'] = function () {
    function sortKeys(v) { if (Array.isArray(v)) return v.map(sortKeys); if (v && typeof v === 'object') { var o = {}; Object.keys(v).sort().forEach(function (k) { o[k] = sortKeys(v[k]); }); return o; } return v; }
    function locate(src, msg) {
      var m = msg.match(/position (\d+)/), pos = m ? +m[1] : -1;
      var lc = msg.match(/line (\d+) column (\d+)/); if (lc) return ' (line ' + lc[1] + ', column ' + lc[2] + ')';
      if (pos < 0) return '';
      var before = src.slice(0, pos).split('\n'); return ' (line ' + before.length + ', column ' + (before[before.length - 1].length + 1) + ')';
    }
    function go(min) {
      var src = $('js-in').value, msg = $('js-msg');
      if (!src.trim()) { msg.innerHTML = '<span class="err">Paste some JSON first.</span>'; return; }
      try {
        var v = JSON.parse(src); if ($('js-sort').checked) v = sortKeys(v);
        var ind = $('js-ind').value; $('js-out').value = min ? JSON.stringify(v) : JSON.stringify(v, null, ind === 'tab' ? '\t' : +ind);
        msg.innerHTML = '<strong style="color:var(--ok)">Valid JSON.</strong> ' + fmt($('js-out').value.length, 0) + ' characters.';
      } catch (e) { $('js-out').value = ''; msg.innerHTML = '<span class="err">Invalid JSON' + locate(src, e.message) + ':</span> ' + esc(e.message); }
    }
    on('js-fmt', 'click', function () { go(false); }); on('js-min', 'click', function () { go(true); });
    on('js-copy', 'click', function () { ST.copy($('js-out').value); });
  };

  /* ---------- Image compressor ---------- */
  T['image-compressor'] = function () {
    var file = null, url = null;
    function kb(b) { return b >= 1048576 ? fmt(b / 1048576, 2) + ' MB' : fmt(b / 1024, 1) + ' KB'; }
    function run() {
      if (!file) return;
      $('im-q-v').textContent = $('im-q').value;
      var img = new Image(), src = URL.createObjectURL(file);
      img.onload = function () {
        var w = img.naturalWidth, h = img.naturalHeight, mw = parseInt($('im-w').value, 10);
        if (mw > 0 && mw < w) { h = Math.round(h * mw / w); w = mw; }
        var c = document.createElement('canvas'); c.width = w; c.height = h;
        var ctx = c.getContext('2d'), type = $('im-fmt').value;
        if (type === 'image/jpeg') { ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, w, h); }
        ctx.drawImage(img, 0, 0, w, h); URL.revokeObjectURL(src);
        c.toBlob(function (blob) {
          if (!blob) { $('im-msg').textContent = 'Your browser could not create that format. Try JPG.'; return; }
          if (url) URL.revokeObjectURL(url); url = URL.createObjectURL(blob);
          $('im-img').src = url; $('im-dl').href = url;
          $('im-dl').download = file.name.replace(/\.[^.]+$/, '') + '-compressed.' + (type === 'image/jpeg' ? 'jpg' : type.split('/')[1]);
          $('im-o').textContent = kb(file.size); $('im-n').textContent = kb(blob.size);
          var s = (1 - blob.size / file.size) * 100; $('im-s').textContent = s >= 0 ? fmt(s, 0) + '%' : '+' + fmt(-s, 0) + '% larger';
          $('im-msg').textContent = w + ' × ' + h + ' px'; $('im-prev').hidden = false;
        }, type, +$('im-q').value / 100);
      };
      img.onerror = function () { $('im-msg').textContent = 'That file could not be opened as an image.'; };
      img.src = src;
    }
    on('im-file', 'change', function () { file = $('im-file').files[0] || null; run(); });
    ['im-q', 'im-w'].forEach(function (id) { on(id, 'input', function () { $('im-q-v').textContent = $('im-q').value; clearTimeout(run._t); run._t = setTimeout(run, 150); }); });
    on('im-fmt', 'change', run);
  };

  /* ================= PDF helpers ================= */
  function kb(b) { return b >= 1048576 ? fmt(b / 1048576, 2) + ' MB' : fmt(b / 1024, 1) + ' KB'; }
  function readBytes(f) { return f.arrayBuffer().then(function (b) { return new Uint8Array(b); }); }
  function pdfUrl(bytes) { return URL.createObjectURL(new Blob([bytes], { type: 'application/pdf' })); }
  function baseName(n) { return n.replace(/\.[^.]+$/, ''); }
  function setupDrop(input) { // highlight the label while dragging files over it
    var lab = input.closest('.drop'); if (!lab) return;
    ['dragenter', 'dragover'].forEach(function (ev) { lab.addEventListener(ev, function () { lab.classList.add('over'); }); });
    ['dragleave', 'drop'].forEach(function (ev) { lab.addEventListener(ev, function () { lab.classList.remove('over'); }); });
  }
  // Parse "1-3, 5, 8-" into [[0,1,2],[4],[7..n-1]] (0-based). Empty = all pages.
  function parseRanges(s, n) {
    s = (s || '').trim(); if (!s) { var all = []; for (var i = 0; i < n; i++) all.push(i); return [all]; }
    return s.split(/[,;]+/).map(function (part) {
      part = part.trim(); if (!part) return null;
      var m = part.match(/^(\d*)\s*[-–]\s*(\d*)$/), a, b;
      if (m) { a = m[1] ? +m[1] : 1; b = m[2] ? +m[2] : n; }
      else if (/^\d+$/.test(part)) { a = b = +part; }
      else throw new Error('“' + part + '” is not a page or range. Use numbers like 2 or 4-7.');
      if (a < 1 || b < 1 || a > n || b > n) throw new Error('Page ' + (a > n || a < 1 ? a : b) + ' does not exist. This PDF has ' + n + ' page' + (n === 1 ? '' : 's') + '.');
      var r = []; if (a <= b) for (i = a; i <= b; i++) r.push(i - 1); else for (i = a; i >= b; i--) r.push(i - 1);
      return r;
    }).filter(Boolean);
  }
  function renderFileList(listEl, items, onChange, meta) {
    listEl.innerHTML = '';
    items.forEach(function (it, i) {
      var li = document.createElement('li');
      li.innerHTML = '<span class="fname"></span><span class="fmeta"></span>' +
        '<button class="icon-btn" type="button" data-a="up" aria-label="Move up">↑</button>' +
        '<button class="icon-btn" type="button" data-a="down" aria-label="Move down">↓</button>' +
        '<button class="icon-btn" type="button" data-a="rm" aria-label="Remove">✕</button>';
      li.querySelector('.fname').textContent = (i + 1) + '. ' + it.file.name;
      li.querySelector('.fmeta').textContent = meta(it);
      li.querySelector('[data-a=up]').disabled = i === 0;
      li.querySelector('[data-a=down]').disabled = i === items.length - 1;
      li.addEventListener('click', function (e) {
        var a = e.target.getAttribute('data-a'); if (!a) return;
        if (a === 'rm') items.splice(i, 1);
        else { var j = a === 'up' ? i - 1 : i + 1, t = items[i]; items[i] = items[j]; items[j] = t; }
        onChange();
      });
      listEl.appendChild(li);
    });
  }
  function pdfLoadError(name, e) {
    var msg = String(e && e.message || e);
    if (/encrypt/i.test(msg)) return name + ' is password-protected. Unlock it in your PDF reader first.';
    return name + ' could not be read as a PDF. It may be damaged.';
  }

  /* ---------- Merge PDF ---------- */
  T['merge-pdf'] = function () {
    var items = [], url = null, inp = $('mp-file'); setupDrop(inp);
    function refresh() {
      renderFileList($('mp-list'), items, refresh, function (it) { return kb(it.file.size); });
      $('mp-go').disabled = items.length < 2;
      $('mp-msg').textContent = items.length === 1 ? 'Add at least one more PDF to merge.' : '';
      $('mp-dl-wrap').hidden = true;
    }
    inp.addEventListener('change', function () {
      Array.prototype.forEach.call(inp.files, function (f) { items.push({ file: f }); });
      inp.value = ''; refresh();
    });
    on('mp-clear', 'click', function () { items = []; refresh(); });
    on('mp-go', 'click', function () {
      var btn = $('mp-go'); btn.disabled = true; $('mp-dl-wrap').hidden = true; $('mp-msg').textContent = 'Merging…';
      PDFLib.PDFDocument.create().then(function (out) {
        var chain = Promise.resolve(), pages = 0;
        items.forEach(function (it) {
          chain = chain.then(function () { return readBytes(it.file); })
            .then(function (b) { return PDFLib.PDFDocument.load(b).catch(function (e) { throw new Error(pdfLoadError(it.file.name, e)); }); })
            .then(function (src) { return out.copyPages(src, src.getPageIndices()); })
            .then(function (ps) { ps.forEach(function (p) { out.addPage(p); }); pages += ps.length; });
        });
        return chain.then(function () { return out.save(); }).then(function (bytes) {
          if (url) URL.revokeObjectURL(url); url = pdfUrl(bytes);
          $('mp-dl').href = url; $('mp-dl-wrap').hidden = false;
          $('mp-msg').textContent = 'Done: ' + pages + ' pages, ' + kb(bytes.length) + '.';
        });
      }).catch(function (e) { $('mp-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; })
        .then(function () { btn.disabled = items.length < 2; });
    });
  };

  /* ---------- Split PDF ---------- */
  T['split-pdf'] = function () {
    var src = null, name = 'document', inp = $('sp-file'), urls = []; setupDrop(inp);
    inp.addEventListener('change', function () {
      var f = inp.files[0]; if (!f) return;
      $('sp-out').innerHTML = ''; $('sp-msg').textContent = ''; $('sp-opts').hidden = true; name = baseName(f.name);
      readBytes(f).then(function (b) { return PDFLib.PDFDocument.load(b); }).then(function (d) {
        src = d; $('sp-info').textContent = f.name + ' — ' + d.getPageCount() + ' page' + (d.getPageCount() === 1 ? '' : 's') + '.';
        $('sp-opts').hidden = false;
      }).catch(function (e) { src = null; $('sp-info').innerHTML = '<span class="err">' + esc(pdfLoadError(f.name, e)) + '</span>'; });
    });
    on('sp-go', 'click', function () {
      if (!src) return;
      var n = src.getPageCount(), mode = document.querySelector('input[name="sp-mode"]:checked').value, groups, list = $('sp-out');
      try { groups = parseRanges($('sp-ranges').value, n); } catch (e) { $('sp-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; return; }
      if (mode === 'one') groups = [[].concat.apply([], groups)];
      else if (mode === 'pages') groups = [].concat.apply([], groups).map(function (p) { return [p]; });
      urls.forEach(URL.revokeObjectURL); urls = []; list.innerHTML = ''; $('sp-msg').textContent = 'Working…';
      var chain = Promise.resolve();
      groups.forEach(function (g) {
        chain = chain.then(function () { return PDFLib.PDFDocument.create(); }).then(function (out) {
          return out.copyPages(src, g).then(function (ps) { ps.forEach(function (p) { out.addPage(p); }); return out.save(); });
        }).then(function (bytes) {
          var u = pdfUrl(bytes); urls.push(u);
          var label = g.length === 1 ? 'page-' + (g[0] + 1) : 'pages-' + (g[0] + 1) + '-' + (g[g.length - 1] + 1);
          var li = document.createElement('li'), a = document.createElement('a');
          a.href = u; a.download = name + '-' + label + '.pdf'; a.textContent = 'Download ' + a.download;
          li.appendChild(a); li.appendChild(document.createTextNode(' — ' + g.length + ' page' + (g.length === 1 ? '' : 's') + ', ' + kb(bytes.length)));
          list.appendChild(li);
        });
      });
      chain.then(function () { $('sp-msg').textContent = groups.length === 1 ? 'Your PDF is ready.' : groups.length + ' PDFs are ready.'; })
        .catch(function (e) { $('sp-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; });
    });
  };

  /* ---------- JPG to PDF ---------- */
  /* Shared: embed an image file into a pdf-lib document, honouring EXIF rotation */
  function jpegOrientation(b) { // EXIF orientation tag, 1 if absent
      if (b[0] !== 0xFF || b[1] !== 0xD8) return 1;
      var i = 2;
      while (i + 4 < b.length) {
        if (b[i] !== 0xFF) return 1;
        var mk = b[i + 1], len = (b[i + 2] << 8) | b[i + 3];
        if (mk === 0xE1 && b[i + 4] === 0x45 && b[i + 5] === 0x78 && b[i + 6] === 0x69 && b[i + 7] === 0x66) {
          var t = i + 10, le = b[t] === 0x49, r16 = function (o) { return le ? b[o] | (b[o + 1] << 8) : (b[o] << 8) | b[o + 1]; };
          var r32 = function (o) { return le ? (b[o] | (b[o + 1] << 8) | (b[o + 2] << 16) | (b[o + 3] << 24)) >>> 0 : ((b[o] << 24) | (b[o + 1] << 16) | (b[o + 2] << 8) | b[o + 3]) >>> 0; };
          var ifd = t + r32(t + 4), cnt = r16(ifd);
          for (var k = 0; k < cnt; k++) { var e = ifd + 2 + k * 12; if (r16(e) === 0x0112) return r16(e + 8); }
          return 1;
        }
        if (mk === 0xDA) return 1;
        i += 2 + len;
      }
      return 1;
    }
    function viaCanvas(file) { // decode with the browser (applies EXIF rotation), re-encode as JPEG
      return new Promise(function (res, rej) {
        var img = new Image(), u = URL.createObjectURL(file);
        img.onload = function () {
          var c = document.createElement('canvas'); c.width = img.naturalWidth; c.height = img.naturalHeight;
          var ctx = c.getContext('2d'); ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, c.width, c.height); ctx.drawImage(img, 0, 0);
          URL.revokeObjectURL(u);
          c.toBlob(function (bl) { bl ? bl.arrayBuffer().then(function (ab) { res(new Uint8Array(ab)); }) : rej(new Error('Could not convert ' + file.name)); }, 'image/jpeg', 0.92);
        };
        img.onerror = function () { rej(new Error(file.name + ' could not be opened as an image.')); };
        img.src = u;
      });
    }
  function embedImageFile(doc, file) {
    return readBytes(file).then(function (b) {
      var isJpg = b[0] === 0xFF && b[1] === 0xD8, isPng = b[0] === 0x89 && b[1] === 0x50;
      if (isJpg && jpegOrientation(b) === 1) return doc.embedJpg(b);
      if (isPng) return doc.embedPng(b);
      return viaCanvas(file).then(function (j) { return doc.embedJpg(j); });
    });
  }
  // Place an embedded image centred on a new page. size: 'fit' | [w,h]; orient: auto|portrait|landscape
  function addImagePage(doc, img, size, orient, margin, index) {
    var iw = img.width * 0.75, ih = img.height * 0.75, pw, ph; // 96 px = 72 pt
    if (size === 'fit') { pw = iw + 2 * margin; ph = ih + 2 * margin; }
    else {
      pw = size[0]; ph = size[1];
      var land = orient === 'landscape' || (orient === 'auto' && iw > ih);
      if (land !== pw > ph) { var t = pw; pw = ph; ph = t; }
    }
    var s = Math.min((pw - 2 * margin) / iw, (ph - 2 * margin) / ih, size === 'fit' ? 1 : Infinity);
    var w = iw * s, h = ih * s, page = index === undefined ? doc.addPage([pw, ph]) : doc.insertPage(index, [pw, ph]);
    page.drawImage(img, { x: (pw - w) / 2, y: (ph - h) / 2, width: w, height: h });
    return page;
  }

  T['jpg-to-pdf'] = function () {
    var items = [], url = null, inp = $('jp-file'); setupDrop(inp);
    var SIZES = { a4: [595.28, 841.89], letter: [612, 792] };
    function refresh() {
      renderFileList($('jp-list'), items, refresh, function (it) { return kb(it.file.size); });
      $('jp-go').disabled = !items.length; $('jp-dl-wrap').hidden = true; $('jp-msg').textContent = '';
    }
    inp.addEventListener('change', function () {
      Array.prototype.forEach.call(inp.files, function (f) { items.push({ file: f }); }); inp.value = ''; refresh();
    });
    on('jp-clear', 'click', function () { items = []; refresh(); });
    on('jp-go', 'click', function () {
      var btn = $('jp-go'), size = $('jp-size').value, orient = $('jp-orient').value, margin = +$('jp-margin').value;
      btn.disabled = true; $('jp-dl-wrap').hidden = true; $('jp-msg').textContent = 'Creating PDF…';
      PDFLib.PDFDocument.create().then(function (doc) {
        var chain = Promise.resolve();
        items.forEach(function (it) {
          chain = chain.then(function () { return embedImageFile(doc, it.file); }).then(function (img) {
            addImagePage(doc, img, size === 'fit' ? 'fit' : SIZES[size], orient, margin);
          }).catch(function (e) { throw new Error(/could not/i.test(e.message) ? e.message : it.file.name + ' could not be added: ' + e.message); });
        });
        return chain.then(function () { return doc.save(); }).then(function (bytes) {
          if (url) URL.revokeObjectURL(url); url = pdfUrl(bytes);
          $('jp-dl').href = url; $('jp-dl-wrap').hidden = false;
          $('jp-msg').textContent = 'Done: ' + items.length + ' page' + (items.length === 1 ? '' : 's') + ', ' + kb(bytes.length) + '.';
        });
      }).catch(function (e) { $('jp-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; })
        .then(function () { btn.disabled = !items.length; });
    });
  };

  /* ---------- PDF to JPG ---------- */
  T['pdf-to-jpg'] = function () {
    var BASE = '/assets/vendor/pdfjs/', lib = null, doc = null, name = 'page', inp = $('pj-file'), urls = []; setupDrop(inp);
    function getLib() {
      if (lib) return Promise.resolve(lib);
      return import(BASE + 'pdf.min.mjs').then(function (m) { m.GlobalWorkerOptions.workerSrc = BASE + 'pdf.worker.min.mjs'; lib = m; return m; });
    }
    inp.addEventListener('change', function () {
      var f = inp.files[0]; if (!f) return;
      $('pj-go').disabled = true; $('pj-out').innerHTML = ''; $('pj-msg').textContent = 'Opening ' + f.name + '…'; name = baseName(f.name);
      Promise.all([getLib(), readBytes(f)]).then(function (r) {
        return r[0].getDocument({ data: r[1], cMapUrl: BASE + 'cmaps/', cMapPacked: true, standardFontDataUrl: BASE + 'standard_fonts/', wasmUrl: BASE + 'wasm/' }).promise;
      }).then(function (d) {
        if (doc) doc.destroy(); doc = d; $('pj-go').disabled = false;
        $('pj-msg').textContent = f.name + ' — ' + d.numPages + ' page' + (d.numPages === 1 ? '' : 's') + '. Choose options and convert.';
      }).catch(function (e) {
        doc = null; $('pj-msg').innerHTML = '<span class="err">' + esc(/password/i.test(e && e.name + e.message) ? f.name + ' is password-protected. Unlock it in your PDF reader first.' : f.name + ' could not be opened as a PDF.') + '</span>';
      });
    });
    on('pj-go', 'click', function () {
      if (!doc) return;
      var pages; try { pages = [].concat.apply([], parseRanges($('pj-pages').value, doc.numPages)); } catch (e) { $('pj-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; return; }
      var type = $('pj-fmt').value, dpi = +$('pj-dpi').value, ext = type === 'image/png' ? 'png' : 'jpg', out = $('pj-out'), btn = $('pj-go');
      urls.forEach(URL.revokeObjectURL); urls = []; out.innerHTML = ''; btn.disabled = true;
      var chain = Promise.resolve(), done = 0;
      pages.forEach(function (p) {
        chain = chain.then(function () { $('pj-msg').textContent = 'Converting page ' + (p + 1) + ' (' + (done + 1) + ' of ' + pages.length + ')…'; return doc.getPage(p + 1); })
          .then(function (page) {
            var vp1 = page.getViewport({ scale: 1 }), scale = dpi / 72;
            var maxPx = 16e6; if (vp1.width * vp1.height * scale * scale > maxPx) scale = Math.sqrt(maxPx / (vp1.width * vp1.height));
            var vp = page.getViewport({ scale: scale }), c = document.createElement('canvas');
            c.width = Math.floor(vp.width); c.height = Math.floor(vp.height);
            return page.render({ canvas: c, viewport: vp, background: '#ffffff' }).promise.then(function () {
              return new Promise(function (res) { c.toBlob(res, type, 0.9); });
            }).then(function (blob) {
              var u = URL.createObjectURL(blob); urls.push(u); done++;
              var fig = document.createElement('figure');
              fig.innerHTML = '<img alt=""><figcaption><a></a><br><span class="fmeta"></span></figcaption>';
              fig.querySelector('img').src = u; fig.querySelector('img').alt = 'Page ' + (p + 1);
              var a = fig.querySelector('a'); a.href = u; a.download = name + '-page-' + (p + 1) + '.' + ext; a.textContent = 'Download page ' + (p + 1);
              fig.querySelector('.fmeta').textContent = c.width + ' × ' + c.height + ' px, ' + kb(blob.size);
              out.appendChild(fig); page.cleanup();
            });
          });
      });
      chain.then(function () { $('pj-msg').textContent = done + ' image' + (done === 1 ? '' : 's') + ' ready. Use each “Download” link to save.'; })
        .catch(function (e) { $('pj-msg').innerHTML = '<span class="err">Conversion failed: ' + esc(e.message) + '</span>'; })
        .then(function () { btn.disabled = false; });
    });
  };

  /* ---------- Mortgage ---------- */
  T['mortgage-calculator'] = function () {
    var IDS = ['mg-price', 'mg-down', 'mg-down-u', 'mg-rate', 'mg-term', 'mg-tax', 'mg-ins', 'mg-pmi', 'mg-hoa', 'mg-start', 'mg-extra'];
    var d = new Date(); d.setMonth(d.getMonth() + 1);
    $('mg-start').value = d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2);
    var lastUnit = 'pct';
    on('mg-down-u', 'change', function () { // convert the value so the down payment stays the same
      var price = +$('mg-price').value || 0, v = +$('mg-down').value || 0, u = $('mg-down-u').value;
      if (u !== lastUnit && price) $('mg-down').value = u === 'usd' ? Math.round(price * v / 100) : +(v / price * 100).toFixed(2);
      lastUnit = u; run();
    });
    function money(x, d) { return '$' + fmt(x, d === undefined ? 0 : d); }
    function amort(P, r, M, extra, limit) { // returns schedule summary
      var bal = P, months = 0, interest = 0, yearly = [], y = { p: 0, i: 0 }, pmiEnd = null;
      while (bal > 0.005 && months < 1200) {
        var int = bal * r, prin = Math.min(bal, M - int + extra); bal -= prin; months++; interest += int; y.p += prin; y.i += int;
        if (pmiEnd === null && limit !== null && bal <= limit) pmiEnd = months;
        if (months % 12 === 0 || bal <= 0.005) { yearly.push({ p: y.p, i: y.i, b: Math.max(0, bal) }); y = { p: 0, i: 0 }; }
      }
      return { months: months, interest: interest, yearly: yearly, pmiEnd: pmiEnd };
    }
    function monthName(start, add) { var p = start.split('-'), dt = new Date(+p[0], +p[1] - 1 + add, 1); return dt.toLocaleString('en-US', { month: 'short', year: 'numeric' }); }
    function run() {
      var price = +$('mg-price').value, dv = +$('mg-down').value || 0, down = $('mg-down-u').value === 'pct' ? price * dv / 100 : dv;
      var rate = +$('mg-rate').value, years = +$('mg-term').value, out = $('mg-out');
      var tax = (+$('mg-tax').value || 0) / 100 * price / 12, ins = (+$('mg-ins').value || 0) / 12, hoa = +$('mg-hoa').value || 0, extra = +$('mg-extra').value || 0;
      if (!(price > 0) || !(rate >= 0) || down < 0) { out.innerHTML = '<span class="err">Enter a home price, down payment and interest rate.</span>'; $('mg-sched-wrap').hidden = true; return; }
      if (down >= price) { out.innerHTML = '<span class="err">The down payment covers the whole price, so no mortgage is needed.</span>'; $('mg-sched-wrap').hidden = true; return; }
      var P = price - down, n = years * 12, r = rate / 1200, M = r === 0 ? P / n : P * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
      var needPmi = down / price < 0.2, pmi = needPmi ? (+$('mg-pmi').value || 0) / 100 * P / 12 : 0;
      var base = amort(P, r, M, 0, needPmi ? 0.78 * price : null), plan = extra > 0 ? amort(P, r, M, extra, needPmi ? 0.78 * price : null) : base;
      var total = M + tax + ins + pmi + hoa, start = $('mg-start').value || $('mg-start').min;
      var parts = [['Principal & interest', M, '#2F5BEA'], ['Property tax', tax, '#F2B33D'], ['Home insurance', ins, '#1F8A5B'], ['PMI', pmi, '#C0392B'], ['HOA', hoa, '#8E7CC3']].filter(function (x) { return x[1] > 0; });
      var html = '<span class="lbl">Estimated monthly payment</span><div class="big">' + money(total) + '</div>';
      html += '<div class="bar" aria-hidden="true">' + parts.map(function (x) { return '<span style="width:' + (x[1] / total * 100) + '%;background:' + x[2] + '"></span>'; }).join('') + '</div>';
      html += '<table class="breakdown"><tbody>' + parts.map(function (x) { return '<tr><td><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:' + x[2] + ';margin-right:8px"></span>' + x[0] + '</td><td>' + money(x[1]) + '</td></tr>'; }).join('') + '</tbody></table>';
      html += '<div class="stats"><div class="stat"><b>' + money(P) + '</b><span>Loan amount (' + fmt(down / price * 100, 1) + '% down)</span></div>' +
        '<div class="stat"><b>' + money(plan.interest) + '</b><span>Total interest</span></div>' +
        '<div class="stat"><b>' + monthName(start, plan.months - 1) + '</b><span>Payoff date</span></div></div>';
      var notes = [];
      if (needPmi && pmi > 0) notes.push(base.pmiEnd ? 'PMI should end automatically around <strong>' + monthName(start, plan.pmiEnd - 1) + '</strong>, when the balance reaches 78% of the home’s price.' : 'PMI applies because the down payment is under 20%.');
      if (!needPmi) notes.push('No PMI: your down payment is at least 20%.');
      if (extra > 0) {
        var saved = base.interest - plan.interest, mo = base.months - plan.months;
        notes.push('Paying ' + money(extra) + ' extra each month saves about <strong>' + money(saved) + '</strong> in interest and pays the loan off <strong>' + Math.floor(mo / 12) + ' years ' + (mo % 12) + ' months</strong> sooner.');
      }
      html += notes.map(function (t) { return '<p style="margin:10px 0 0">' + t + '</p>'; }).join('');
      out.innerHTML = html;
      $('mg-sched').innerHTML = '<table class="sched" style="width:100%;border-collapse:collapse;margin-top:8px"><thead><tr><th>Year</th><th>Principal</th><th>Interest</th><th>Balance</th></tr></thead><tbody>' +
        plan.yearly.map(function (y, i) { return '<tr><td>' + (i + 1) + '</td><td>' + money(y.p) + '</td><td>' + money(y.i) + '</td><td>' + money(y.b) + '</td></tr>'; }).join('') + '</tbody></table>';
      $('mg-sched-wrap').hidden = false;
    }
    IDS.forEach(function (id) { if (id !== 'mg-down-u') { on(id, 'input', run); on(id, 'change', run); } });
    run();
  };

  /* ---------- shared pdf.js loader ---------- */
  var PDFJS_BASE = '/assets/vendor/pdfjs/', pdfjsLib = null;
  function loadPdfjs() {
    if (pdfjsLib) return Promise.resolve(pdfjsLib);
    return import(PDFJS_BASE + 'pdf.min.mjs').then(function (m) { m.GlobalWorkerOptions.workerSrc = PDFJS_BASE + 'pdf.worker.min.mjs'; pdfjsLib = m; return m; });
  }
  function openPdfjs(bytes) {
    return loadPdfjs().then(function (lib) {
      return lib.getDocument({ data: bytes.slice(0), cMapUrl: PDFJS_BASE + 'cmaps/', cMapPacked: true, standardFontDataUrl: PDFJS_BASE + 'standard_fonts/', wasmUrl: PDFJS_BASE + 'wasm/' }).promise;
    });
  }
  function rangesToSet(s, n) { var set = {}; parseRanges(s, n).forEach(function (g) { g.forEach(function (p) { set[p] = true; }); }); return set; }
  function setToRanges(set) {
    var ps = Object.keys(set).map(Number).sort(function (a, b) { return a - b; }), out = [], i = 0;
    while (i < ps.length) { var j = i; while (j + 1 < ps.length && ps[j + 1] === ps[j] + 1) j++; out.push(i === j ? '' + (ps[i] + 1) : (ps[i] + 1) + '-' + (ps[j] + 1)); i = j + 1; }
    return out.join(', ');
  }

  /* ---------- Delete PDF pages ---------- */
  T['delete-pdf-pages'] = function () {
    var inp = $('dp-file'), bytes = null, n = 0, del = {}, name = 'document', url = null, token = 0; setupDrop(inp);
    function paint() {
      document.querySelectorAll('#dp-thumbs button').forEach(function (b) { var p = +b.dataset.p; b.setAttribute('aria-pressed', del[p] ? 'true' : 'false'); });
      var k = Object.keys(del).length; $('dp-msg').textContent = k ? k + ' page' + (k === 1 ? '' : 's') + ' marked for deletion. ' + (n - k) + ' will remain.' : '';
    }
    inp.addEventListener('change', function () {
      var f = inp.files[0]; if (!f) return; var my = ++token;
      name = baseName(f.name); del = {}; $('dp-pages').value = ''; $('dp-thumbs').innerHTML = ''; $('dp-opts').hidden = true; $('dp-dl-wrap').hidden = true; $('dp-msg').textContent = '';
      readBytes(f).then(function (b) { bytes = b; return PDFLib.PDFDocument.load(b); }).then(function (d) {
        n = d.getPageCount(); $('dp-info').textContent = f.name + ' — ' + n + ' page' + (n === 1 ? '' : 's') + '.'; $('dp-opts').hidden = false;
        var grid = $('dp-thumbs');
        for (var i = 0; i < n; i++) {
          var b = document.createElement('button'); b.type = 'button'; b.dataset.p = i; b.setAttribute('aria-pressed', 'false');
          b.setAttribute('aria-label', 'Page ' + (i + 1)); b.innerHTML = '<span class="ph"></span><span class="pn">' + (i + 1) + '</span>';
          grid.appendChild(b);
        }
        return openPdfjs(bytes).then(function (doc) { // thumbnails, one at a time
          var chain = Promise.resolve();
          for (var p = 1; p <= Math.min(n, 400); p++) (function (p) {
            chain = chain.then(function () { if (my !== token) return; return doc.getPage(p).then(function (pg) {
              var vp = pg.getViewport({ scale: 1 }), s = 140 / vp.width, v = pg.getViewport({ scale: s }), c = document.createElement('canvas');
              c.width = Math.ceil(v.width); c.height = Math.ceil(v.height);
              return pg.render({ canvas: c, viewport: v, background: '#ffffff' }).promise.then(function () {
                var slot = grid.querySelector('button[data-p="' + (p - 1) + '"] .ph'); if (slot) slot.replaceWith(c); pg.cleanup();
              });
            }); });
          })(p);
          return chain;
        }).catch(function () { /* previews are optional */ });
      }).catch(function (e) { bytes = null; $('dp-info').innerHTML = '<span class="err">' + esc(pdfLoadError(f.name, e)) + '</span>'; });
    });
    $('dp-thumbs').addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return; var p = +b.dataset.p;
      if (del[p]) delete del[p]; else del[p] = true;
      $('dp-pages').value = setToRanges(del); paint();
    });
    on('dp-pages', 'input', function () { try { del = rangesToSet($('dp-pages').value, n); if (!$('dp-pages').value.trim()) del = {}; paint(); } catch (e) { $('dp-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; } });
    on('dp-go', 'click', function () {
      if (!bytes) return;
      $('dp-dl-wrap').hidden = true;
      try { del = $('dp-pages').value.trim() ? rangesToSet($('dp-pages').value, n) : {}; } catch (e) { $('dp-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; return; }
      var idx = Object.keys(del).map(Number).sort(function (a, b) { return b - a; });
      if (!idx.length) { $('dp-msg').innerHTML = '<span class="err">Choose at least one page to delete.</span>'; return; }
      if (idx.length >= n) { $('dp-msg').innerHTML = '<span class="err">A PDF needs at least one page. Keep one or more pages.</span>'; return; }
      $('dp-dl-wrap').hidden = true;
      PDFLib.PDFDocument.load(bytes).then(function (d) { idx.forEach(function (i) { d.removePage(i); }); return d.save(); }).then(function (out) {
        if (url) URL.revokeObjectURL(url); url = pdfUrl(out);
        $('dp-dl').href = url; $('dp-dl').download = name + '-edited.pdf'; $('dp-dl-wrap').hidden = false;
        $('dp-msg').textContent = 'Removed ' + idx.length + ' page' + (idx.length === 1 ? '' : 's') + '. New PDF: ' + (n - idx.length) + ' pages, ' + kb(out.length) + '.';
      }).catch(function (e) { $('dp-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; });
    });
  };

  /* ---------- Add pages to PDF ---------- */
  T['add-pages-to-pdf'] = function () {
    var main = null, mainName = 'document', items = [], url = null, inMain = $('ap-main'), inAdd = $('ap-add'); setupDrop(inMain); setupDrop(inAdd);
    function ready() { $('ap-go').disabled = !(main && items.length); $('ap-dl-wrap').hidden = true; }
    function refresh() { renderFileList($('ap-list'), items, refresh, function (it) { return kb(it.file.size); }); ready(); }
    inMain.addEventListener('change', function () {
      var f = inMain.files[0]; if (!f) return; mainName = baseName(f.name);
      readBytes(f).then(function (b) { return PDFLib.PDFDocument.load(b).then(function (d) {
        main = b; $('ap-info').textContent = f.name + ' — ' + d.getPageCount() + ' pages.'; $('ap-after').max = d.getPageCount(); ready();
      }); }).catch(function (e) { main = null; $('ap-info').innerHTML = '<span class="err">' + esc(pdfLoadError(f.name, e)) + '</span>'; ready(); });
    });
    inAdd.addEventListener('change', function () { Array.prototype.forEach.call(inAdd.files, function (f) { items.push({ file: f }); }); inAdd.value = ''; refresh(); });
    on('ap-pos', 'change', function () { $('ap-after-f').hidden = $('ap-pos').value !== 'after'; });
    on('ap-go', 'click', function () {
      var btn = $('ap-go'); btn.disabled = true; $('ap-dl-wrap').hidden = true; $('ap-msg').textContent = 'Adding pages…';
      PDFLib.PDFDocument.load(main).then(function (doc) {
        var n = doc.getPageCount(), pos = $('ap-pos').value, at = pos === 'start' ? 0 : pos === 'end' ? n : Math.max(0, Math.min(n, parseInt($('ap-after').value, 10) || 0));
        var first = doc.getPage(0).getSize(), size = [first.width, first.height], added = 0, chain = Promise.resolve();
        items.forEach(function (it) {
          chain = chain.then(function () {
            var isPdf = /\.pdf$/i.test(it.file.name) || it.file.type === 'application/pdf';
            if (isPdf) return readBytes(it.file).then(function (b) { return PDFLib.PDFDocument.load(b).catch(function (e) { throw new Error(pdfLoadError(it.file.name, e)); }); })
              .then(function (src) { return doc.copyPages(src, src.getPageIndices()); })
              .then(function (ps) { ps.forEach(function (p) { doc.insertPage(at + added, p); added++; }); });
            return embedImageFile(doc, it.file).then(function (img) { addImagePage(doc, img, size, 'auto', 36, at + added); added++; });
          });
        });
        return chain.then(function () { return doc.save(); }).then(function (out) {
          if (url) URL.revokeObjectURL(url); url = pdfUrl(out);
          $('ap-dl').href = url; $('ap-dl').download = mainName + '-updated.pdf'; $('ap-dl-wrap').hidden = false;
          $('ap-msg').textContent = 'Added ' + added + ' page' + (added === 1 ? '' : 's') + '. New PDF: ' + (n + added) + ' pages, ' + kb(out.length) + '.';
        });
      }).catch(function (e) { $('ap-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; }).then(function () { btn.disabled = !(main && items.length); });
    });
  };

  /* ---------- TXT to PDF ---------- */
  T['txt-to-pdf'] = function () {
    var inp = $('tp-file'), url = null, fname = 'text'; setupDrop(inp);
    var WINANSI_EXTRA = '€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ';
    function clean(s) { var bad = 0; var out = s.replace(/\r\n?/g, '\n').replace(/\t/g, '    ').replace(/[^\n\x20-\x7e\xa0-\xff]/gu, function (c) { if (WINANSI_EXTRA.indexOf(c) !== -1) return c; bad++; return '?'; }); return { text: out, bad: bad }; }
    inp.addEventListener('change', function () { var f = inp.files[0]; if (!f) return; fname = baseName(f.name); f.text().then(function (t) { $('tp-text').value = t; }); });
    on('tp-go', 'click', function () {
      var raw = $('tp-text').value; if (!raw.trim()) { $('tp-msg').innerHTML = '<span class="err">Add some text first.</span>'; return; }
      var c = clean(raw), size = +$('tp-size').value, margin = +$('tp-margin').value, dims = $('tp-page').value === 'a4' ? [595.28, 841.89] : [612, 792];
      $('tp-dl-wrap').hidden = true;
      PDFLib.PDFDocument.create().then(function (doc) {
        return doc.embedFont(PDFLib.StandardFonts[$('tp-font').value]).then(function (font) {
          var maxW = dims[0] - 2 * margin, lh = size * 1.4, page = null, y = 0, pages = 0;
          function newPage() { page = doc.addPage(dims); y = dims[1] - margin - size; pages++; }
          function wrap(line) { // break a paragraph into lines that fit maxW
            if (!line) return [''];
            var words = line.split(/( +)/), out = [], cur = '';
            words.forEach(function (w) {
              var test = cur + w;
              if (font.widthOfTextAtSize(test, size) <= maxW) { cur = test; return; }
              if (cur.trim()) out.push(cur.replace(/ +$/, ''));
              cur = w.replace(/^ +/, '');
              while (font.widthOfTextAtSize(cur, size) > maxW) { // very long word: hard break
                var k = cur.length; while (k > 1 && font.widthOfTextAtSize(cur.slice(0, k), size) > maxW) k--;
                out.push(cur.slice(0, k)); cur = cur.slice(k);
              }
            });
            out.push(cur); return out;
          }
          newPage();
          c.text.split('\n').forEach(function (para) {
            wrap(para).forEach(function (ln) {
              if (y < margin) newPage();
              if (ln) page.drawText(ln, { x: margin, y: y, size: size, font: font });
              y -= lh;
            });
          });
          doc.setTitle(fname);
          return doc.save().then(function (out) {
            if (url) URL.revokeObjectURL(url); url = pdfUrl(out);
            $('tp-dl').href = url; $('tp-dl').download = fname + '.pdf'; $('tp-dl-wrap').hidden = false;
            $('tp-msg').textContent = 'Done: ' + pages + ' page' + (pages === 1 ? '' : 's') + ', ' + kb(out.length) + '.' + (c.bad ? ' ' + c.bad + ' unsupported character' + (c.bad === 1 ? ' was' : 's were') + ' replaced with “?”.' : '');
          });
        });
      }).catch(function (e) { $('tp-msg').innerHTML = '<span class="err">' + esc(e.message) + '</span>'; });
    });
  };

  /* ---------- Amortization schedule ---------- */
  T['amortization-calculator'] = function () {
    var d = new Date(); d.setMonth(d.getMonth() + 1);
    $('am-start').value = d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2);
    var rows = [];
    function money(x) { return '$' + Number(x).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
    function run() {
      var P = +$('am-p').value, R = +$('am-r').value, Y = +$('am-y').value, extra = +$('am-extra').value || 0, out = $('am-out');
      if (!(P > 0) || !(Y > 0) || !(R >= 0)) { out.innerHTML = '<span class="err">Enter a loan amount, an interest rate of 0 or more, and a term.</span>'; $('am-table').innerHTML = ''; rows = []; return; }
      var n = Math.round(Y * 12), r = R / 1200, M = r === 0 ? P / n : P * r * Math.pow(1 + r, n) / (Math.pow(1 + r, n) - 1);
      var sp = ($('am-start').value || '2026-01').split('-'), sy = +sp[0], sm = +sp[1] - 1, bal = P, ti = 0, tp = 0, k = 0;
      rows = [];
      while (bal > 0.005 && k < 1200) {
        var int = bal * r, prin = Math.min(bal, M - int + extra), pay = prin + int; bal -= prin; ti += int; tp += pay;
        var dt = new Date(sy, sm + k, 1); k++;
        rows.push({ n: k, date: dt.toLocaleString('en-US', { month: 'short', year: 'numeric' }), y: dt.getFullYear(), pay: pay, int: int, prin: prin, bal: Math.max(0, bal) });
      }
      var last = rows[rows.length - 1];
      out.innerHTML = '<span class="lbl">Monthly payment</span><div class="big">' + money(M + extra) + '</div>' + (extra ? '<p style="margin:4px 0 0">' + money(M) + ' required + ' + money(extra) + ' extra</p>' : '') +
        '<div class="stats"><div class="stat"><b>' + money(ti) + '</b><span>Total interest</span></div><div class="stat"><b>' + money(tp) + '</b><span>Total of payments</span></div>' +
        '<div class="stat"><b>' + last.date + '</b><span>Payoff (' + rows.length + ' payments)</span></div></div>';
      var byYear = {}; rows.forEach(function (x) { (byYear[x.y] = byYear[x.y] || []).push(x); });
      $('am-table').innerHTML = Object.keys(byYear).map(function (yr, i) {
        var g = byYear[yr], sI = 0, sP = 0; g.forEach(function (x) { sI += x.int; sP += x.prin; });
        return '<details class="yr"' + (i === 0 ? ' open' : '') + '><summary><strong>' + yr + '</strong> — principal ' + money(sP) + ', interest ' + money(sI) + ', ending balance ' + money(g[g.length - 1].bal) + '</summary>' +
          '<div style="overflow-x:auto"><table class="sched" style="width:100%;border-collapse:collapse"><thead><tr><th>#</th><th>Date</th><th>Payment</th><th>Principal</th><th>Interest</th><th>Balance</th></tr></thead><tbody>' +
          g.map(function (x) { return '<tr><td>' + x.n + '</td><td>' + x.date + '</td><td>' + money(x.pay) + '</td><td>' + money(x.prin) + '</td><td>' + money(x.int) + '</td><td>' + money(x.bal) + '</td></tr>'; }).join('') + '</tbody></table></div></details>';
      }).join('');
    }
    ['am-p', 'am-r', 'am-y', 'am-start', 'am-extra'].forEach(function (id) { on(id, 'input', run); on(id, 'change', run); });
    on('am-csv', 'click', function () {
      if (!rows.length) return;
      var csv = 'Payment,Date,Payment amount,Principal,Interest,Balance\n' + rows.map(function (x) { return [x.n, '"' + x.date + '"', x.pay.toFixed(2), x.prin.toFixed(2), x.int.toFixed(2), x.bal.toFixed(2)].join(','); }).join('\n');
      var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv' })); a.download = 'amortization-schedule.csv'; a.click();
    });
    run();
  };

  /* ---------- Home & construction ---------- */
  var TO_FT = { ft: 1, in: 1 / 12, yd: 3, m: 3.28083989501 };
  function ft(id) { var v = parseFloat($(id).value); return isFinite(v) && v >= 0 ? v * TO_FT[$(id + '-u').value] : NaN; }
  function watch(ids, fn) { ids.forEach(function (id) { on(id, 'input', fn); on(id, 'change', fn); if ($(id + '-u')) on(id + '-u', 'change', fn); }); fn(); }
  function shapeToggle(name, map, fn) {
    document.querySelectorAll('input[name="' + name + '"]').forEach(function (r) {
      r.addEventListener('change', function () { var v = document.querySelector('input[name="' + name + '"]:checked').value; Object.keys(map).forEach(function (k) { $(map[k]).hidden = k !== v; }); fn(); });
    });
  }
  T['gravel-calculator'] = function () {
    function run() {
      var cf = ft('gv-l') * ft('gv-w') * ft('gv-d'), ex = 1 + (+$('gv-extra').value || 0) / 100, yd = cf / 27 * ex, t = yd * (+$('gv-den').value || 0), price = parseFloat($('gv-price').value);
      $('gv-yd').textContent = fmt(yd, 2); $('gv-t').textContent = fmt(t, 2); $('gv-ft').textContent = fmt(cf * ex, 1);
      $('gv-cost').textContent = price > 0 && isFinite(t) ? '$' + (t * price).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) : '—';
    }
    watch(['gv-l', 'gv-w', 'gv-d', 'gv-den', 'gv-extra', 'gv-price'], run);
  };
  T['cubic-yard-calculator'] = function () {
    function run() {
      var circ = document.querySelector('input[name="cy-shape"]:checked').value === 'circle', q = Math.max(1, +$('cy-q').value || 1);
      var area = circ ? Math.PI * Math.pow(ft('cy-dia') / 2, 2) : ft('cy-l') * ft('cy-w'), cf = area * ft('cy-d') * q;
      $('cy-yd').textContent = fmt(cf / 27, 2); $('cy-ft').textContent = fmt(cf, 1); $('cy-m').textContent = fmt(cf * 0.0283168466, 2);
      $('cy-bags').textContent = isFinite(cf) ? fmt(Math.ceil(cf / 2 - 1e-9), 0) : '—';
    }
    shapeToggle('cy-shape', { rect: 'cy-rect', circle: 'cy-circ' }, run);
    watch(['cy-l', 'cy-w', 'cy-dia', 'cy-d', 'cy-q'], run);
  };
  T['concrete-calculator'] = function () {
    function run() {
      var col = document.querySelector('input[name="cc-shape"]:checked').value === 'col', q = Math.max(1, +$('cc-q').value || 1), ex = 1 + (+$('cc-waste').value || 0) / 100;
      var cf = (col ? Math.PI * Math.pow(ft('cc-dia') / 2, 2) * ft('cc-h') : ft('cc-l') * ft('cc-w') * ft('cc-t')) * q * ex;
      $('cc-yd').textContent = fmt(cf / 27, 2); $('cc-ft').textContent = fmt(cf, 1);
      [['cc-80', 0.6], ['cc-60', 0.45], ['cc-40', 0.3]].forEach(function (b) { $(b[0]).textContent = isFinite(cf) ? fmt(Math.ceil(cf / b[1] - 1e-9), 0) : '—'; });
    }
    shapeToggle('cc-shape', { slab: 'cc-slab', col: 'cc-col' }, run);
    watch(['cc-l', 'cc-w', 'cc-t', 'cc-dia', 'cc-h', 'cc-q', 'cc-waste'], run);
  };
  T['roofing-calculator'] = function () {
    function run() {
      var o = (+$('rf-o').value || 0) / 12, L = +$('rf-l').value + 2 * o, W = +$('rf-w').value + 2 * o, p = +$('rf-p').value, f = Math.sqrt(1 + Math.pow(p / 12, 2));
      var area = L * W * f, sq = area / 100 * (1 + +$('rf-waste').value / 100);
      $('rf-area').textContent = fmt(area, 0); $('rf-sq').textContent = fmt(sq, 1); $('rf-bun').textContent = isFinite(sq) ? fmt(Math.ceil(sq * (+$('rf-b').value || 3) - 1e-9), 0) : '—'; $('rf-f').textContent = f.toFixed(3);
    }
    watch(['rf-l', 'rf-w', 'rf-o', 'rf-p', 'rf-waste', 'rf-b'], run);
  };

  /* ---------- Time & date lookup pages ---------- */
  var DAYN = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  function shiftDate(base, unit, k) {
    var d = new Date(base.getTime());
    if (unit === 'minute') d.setMinutes(d.getMinutes() + k);
    else if (unit === 'hour') d = new Date(base.getTime() + k * 3600000); // real elapsed hours
    else if (unit === 'day') d.setDate(d.getDate() + k);
    else if (unit === 'week') d.setDate(d.getDate() + 7 * k);
    else { // month / year: keep day of month, clamp to month end
      var months = unit === 'month' ? k : 12 * k, day = d.getDate();
      d.setDate(1); d.setMonth(d.getMonth() + months);
      var last = new Date(d.getFullYear(), d.getMonth() + 1, 0).getDate(); d.setDate(Math.min(day, last));
    }
    return d;
  }
  function longDate(d) { return d.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }); }
  function clock(d, sec) { return d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', second: sec ? '2-digit' : undefined }); }
  function isoWeek(d) { var t = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate())), day = t.getUTCDay() || 7; t.setUTCDate(t.getUTCDate() + 4 - day); var y0 = new Date(Date.UTC(t.getUTCFullYear(), 0, 1)); return Math.ceil(((t - y0) / 864e5 + 1) / 7); }
  function dayOfYear(d) { return Math.round((new Date(d.getFullYear(), d.getMonth(), d.getDate()) - new Date(d.getFullYear(), 0, 1)) / 864e5) + 1; }
  function bizDays(a, b) { // weekdays strictly after a, up to and including b (a < b)
    var n = 0, d = new Date(a.getFullYear(), a.getMonth(), a.getDate()), end = new Date(b.getFullYear(), b.getMonth(), b.getDate());
    while (d < end) { d.setDate(d.getDate() + 1); var w = d.getDay(); if (w && w !== 6) n++; }
    return n;
  }
  function calDays(a, b) { return Math.round((new Date(b.getFullYear(), b.getMonth(), b.getDate()) - new Date(a.getFullYear(), a.getMonth(), a.getDate())) / 864e5); }
  function relAnswer(unit, k, now) { // returns {main, sub, rows}
    var t = shiftDate(now, unit, k), sameDay = t.toDateString() === now.toDateString(), rows = [];
    if (unit === 'minute' || unit === 'hour') {
      var main = clock(t, false), sub = sameDay ? (k < 0 ? 'Earlier today, ' : 'Later today, ') + longDate(t) + '.' : (k < 0 ? 'On ' : 'On ') + longDate(t) + '.';
      rows.push(['Time', clock(t, true)], ['24-hour time', ('0' + t.getHours()).slice(-2) + ':' + ('0' + t.getMinutes()).slice(-2)], ['Date', longDate(t)], ['Current time', clock(now, true)]);
      return { main: main, sub: sub, rows: rows };
    }
    var days = calDays(now, t), lo = days < 0 ? t : now, hi = days < 0 ? now : t;
    rows.push(['Date', longDate(t)], ['Day of the week', DAYN[t.getDay()]], ['Days ' + (days < 0 ? 'ago' : 'from today'), Math.abs(days).toLocaleString('en-US')],
      ['Business days (Mon–Fri)', bizDays(lo, hi).toLocaleString('en-US')], ['Day of the year', dayOfYear(t) + ' of ' + (dayOfYear(new Date(t.getFullYear(), 11, 31)))], ['ISO week number', isoWeek(t)]);
    if (unit === 'year') return { main: String(t.getFullYear()), sub: Math.abs(k) + ' year' + (Math.abs(k) === 1 ? '' : 's') + ' ago today was ' + longDate(t) + '.', rows: rows };
    return { main: longDate(t), sub: (days < 0 ? 'That was ' : 'That is ') + Math.abs(days).toLocaleString('en-US') + ' day' + (Math.abs(days) === 1 ? '' : 's') + (days < 0 ? ' ago.' : ' from today.'), rows: rows };
  }
  function relCalc() {
    function run() {
      var n = Math.max(0, +$('rc-n').value || 0), u = $('rc-u').value, d = +$('rc-d').value, a = relAnswer(u, d * n, new Date());
      $('rc-out').textContent = (u === 'year' ? a.main + ' (' + a.sub.replace(/^.*was /, '').replace(/\.$/, '') + ')' : a.main) ;
    }
    ['rc-n', 'rc-u', 'rc-d'].forEach(function (id) { on(id, 'input', run); on(id, 'change', run); }); run();
    return run;
  }
  T['rel-time'] = function () {
    var box = document.querySelector('[data-rel-unit]'), unit = box.getAttribute('data-rel-unit'), k = +box.getAttribute('data-rel-n') * +box.getAttribute('data-rel-dir');
    var rc = relCalc();
    function tick() {
      var a = relAnswer(unit, k, new Date());
      $('rt-ans').textContent = a.main; $('rt-sub').textContent = a.sub;
      $('rt-details').innerHTML = a.rows.map(function (r) { return '<tr><td>' + r[0] + '</td><td>' + esc(r[1]) + '</td></tr>'; }).join('');
    }
    tick(); if (unit === 'minute' || unit === 'hour') setInterval(function () { tick(); rc(); }, 1000);
  };
  T['rel-hub'] = function () { relCalc(); };
  function untilInfo(h, m, now) {
    var t = new Date(now.getFullYear(), now.getMonth(), now.getDate(), h, m, 0), tomorrow = false;
    if (t <= now) { t.setDate(t.getDate() + 1); tomorrow = true; }
    var s = Math.round((t - now) / 1000);
    return { s: s, t: t, tomorrow: tomorrow, hh: Math.floor(s / 3600), mm: Math.floor(s % 3600 / 60), ss: s % 60 };
  }
  function hms(i) { return (i.hh ? i.hh + ' h ' : '') + i.mm + ' min ' + i.ss + ' s'; }
  T['until'] = function () {
    var box = document.querySelector('[data-until-h]'), h = +box.getAttribute('data-until-h'), m = +box.getAttribute('data-until-m');
    function tick() {
      var now = new Date(), i = untilInfo(h, m, now);
      $('ut-ans').textContent = hms(i);
      $('ut-sub').textContent = (i.tomorrow ? 'Counting down to tomorrow, ' : 'Today, ') + longDate(i.t) + '. Current time: ' + clock(now, true) + '.';
      $('ut-details').innerHTML = [['Total minutes', Math.floor(i.s / 60).toLocaleString('en-US')], ['Total seconds', i.s.toLocaleString('en-US')], ['Hours (decimal)', (i.s / 3600).toFixed(2)]]
        .map(function (r) { return '<tr><td>' + r[0] + '</td><td>' + r[1] + '</td></tr>'; }).join('');
      var v = ($('uc-t').value || '').split(':');
      if (v.length >= 2) { var j = untilInfo(+v[0], +v[1], now); $('uc-out').textContent = hms(j) + (j.tomorrow ? ' (tomorrow)' : ''); }
    }
    tick(); setInterval(tick, 1000); on('uc-t', 'input', tick);
  };

  /* ---------- Age lookup pages (live values, so pages stay right after New Year) ---------- */
  function setAll(sel, v) { document.querySelectorAll(sel).forEach(function (el) { el.textContent = v; }); }
  T['age-year'] = function () {
    var y = +document.querySelector('[data-age-year]').getAttribute('data-age-year'), now = new Date(), cy = now.getFullYear();
    setAll('.yr-now', cy); setAll('.age-a', cy - y); setAll('.age-b', cy - y - 1);
    function run() {
      var m = +$('ya-m').value, d = +$('ya-d').value, last = new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
      if (d > last) { $('ya-out').textContent = MONTHS_SHORT[m] + ' ' + y + ' has only ' + last + ' days.'; return; }
      var a = new Date(Date.UTC(y, m, d)), b = new Date(Date.UTC(cy, now.getMonth(), now.getDate()));
      var r = ymd(a, b);
      $('ya-out').textContent = 'You are ' + plural(r.y, 'year') + ', ' + plural(r.m, 'month') + ' and ' + plural(r.d, 'day') + ' old.';
    }
    $('ya-m').value = '0'; $('ya-d').value = '1';
    on('ya-m', 'change', run); on('ya-d', 'change', run); run();
  };
  var MONTHS_SHORT = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  T['age-n'] = function () {
    var n = +document.querySelector('[data-age-n]').getAttribute('data-age-n'), cy = new Date().getFullYear();
    setAll('.yr-now', cy); setAll('.yb-a', cy - n); setAll('.yb-b', cy - n - 1);
    function run() {
      var had = document.querySelector('input[name="yn-had"]:checked').value === '1';
      $('yn-out').textContent = 'You were born in ' + (had ? cy - n : cy - n - 1) + '.';
    }
    document.querySelectorAll('input[name="yn-had"]').forEach(function (r) { r.addEventListener('change', run); }); run();
  };

  if (T[tool]) T[tool]();
})();
