/* SmartToolsy batch 4: paycheck calculator (2026 federal tax + FICA), sleep calculator, time zone converter. */
(function () {
  'use strict';
  var tool = document.body.getAttribute('data-tool');
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var money = function (n) { return '$' + (isFinite(n) ? n : 0).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var on = function (ids, fn) { ids.forEach(function (id) { var el = $(id); if (el) { el.addEventListener('input', fn); el.addEventListener('change', fn); } }); };
  var seg = function (attr, fn) {
    var btns = document.querySelectorAll('[' + attr + ']');
    btns.forEach(function (b) { b.addEventListener('click', function () { btns.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); fn(b.getAttribute(attr)); }); });
  };
  var store = {
    get: function (k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { window.localStorage.setItem(k, v); } catch (e) { /* storage unavailable */ } }
  };

  /* ============================================================ Paycheck (tax year 2026) */
  // 2026 brackets (IRS Rev. Proc. 2025-32): upper limit of each bracket's taxable income.
  var TAX2026 = {
    rates: [0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
    single: { std: 16100, top: [12400, 50400, 105700, 201775, 256225, 640600, Infinity], ctc: 200000 },
    mfj: { std: 32200, top: [24800, 100800, 211400, 403550, 512450, 768700, Infinity], ctc: 400000 },
    mfs: { std: 16100, top: [12400, 50400, 105700, 201775, 256225, 384350, Infinity], ctc: 200000 },
    hoh: { std: 24150, top: [17700, 67450, 105700, 201750, 256200, 640600, Infinity], ctc: 200000 },
    ssRate: 0.062, ssBase: 184500, medRate: 0.0145, addMedRate: 0.009, addMedOver: 200000,
    childCredit: 2200, otherCredit: 500
  };
  function bracketTax(taxable, st) {
    var tax = 0, low = 0, marg = TAX2026.rates[0];
    for (var i = 0; i < st.top.length; i++) {
      if (taxable > low) { tax += (Math.min(taxable, st.top[i]) - low) * TAX2026.rates[i]; marg = TAX2026.rates[i]; }
      low = st.top[i];
    }
    return { tax: tax, marg: marg };
  }
  // Exposed for testing: annual figures for given inputs.
  function paycheck(o) {
    var st = TAX2026[o.status] || TAX2026.single, n = o.periods;
    var gross = o.type === 'hourly' ? (o.rate * o.hours + o.rate * 1.5 * o.ot) * 52 : o.amount;
    var k401 = gross * Math.min(100, Math.max(0, o.k401)) / 100;
    var benefits = Math.min(o.pretax * n, Math.max(0, gross - k401));
    var fica = Math.max(0, gross - benefits);
    var agi = Math.max(0, gross - k401 - benefits);
    var taxable = Math.max(0, agi - st.std);
    var bt = bracketTax(taxable, st);
    var credit = o.kids * TAX2026.childCredit + o.deps * TAX2026.otherCredit;
    if (agi > st.ctc) credit = Math.max(0, credit - Math.ceil((agi - st.ctc) / 1000) * 50);
    var fed = Math.max(0, bt.tax - credit);
    var ss = Math.min(fica, TAX2026.ssBase) * TAX2026.ssRate;
    var med = fica * TAX2026.medRate + Math.max(0, fica - TAX2026.addMedOver) * TAX2026.addMedRate;
    var state = agi * Math.max(0, o.stateRate) / 100;
    var post = o.post * n;
    var net = gross - k401 - benefits - fed - ss - med - state - post;
    return { gross: gross, k401: k401, benefits: benefits, taxable: taxable, fed: fed, ss: ss, med: med, state: state, post: post, net: net, marg: bt.marg, credit: credit };
  }
  window.SmartToolsyPaycheck = paycheck;

  if (tool === 'paycheck-calculator') {
    var pcType = 'salary';
    var calcP = function () {
      var hourly = pcType === 'hourly';
      document.querySelectorAll('.pc-hourly').forEach(function (el) { el.hidden = !hourly; });
      $('pc-amt-lbl').textContent = hourly ? 'Hourly wage ($)' : 'Annual salary ($)';
      var amt = +$('pc-amt').value || 0, n = +$('pc-freq').value || 26;
      var r = paycheck({ type: pcType, amount: amt, rate: amt, hours: +$('pc-hours').value || 0, ot: +$('pc-ot').value || 0, periods: n,
        status: $('pc-status').value, kids: Math.max(0, Math.round(+$('pc-kids').value || 0)), deps: Math.max(0, Math.round(+$('pc-deps').value || 0)),
        stateRate: +$('pc-state').value || 0, k401: +$('pc-401k').value || 0, pretax: +$('pc-pretax').value || 0, post: +$('pc-post').value || 0 });
      var rows = [['Gross pay', r.gross], ['Federal income tax', -r.fed], ['Social Security (6.2%)', -r.ss], ['Medicare', -r.med]];
      if (r.state) rows.push(['State &amp; local tax', -r.state]);
      if (r.k401) rows.push(['401(k) / 403(b)', -r.k401]);
      if (r.benefits) rows.push(['Pre-tax benefits', -r.benefits]);
      if (r.post) rows.push(['After-tax deductions', -r.post]);
      rows.push(['Take-home pay', r.net]);
      $('pc-out').innerHTML = rows.map(function (x, i) {
        var neg = x[1] < 0, v = Math.abs(x[1]), last = i === rows.length - 1;
        return '<tr' + (last ? ' class="pc-net"' : '') + '><th scope="row">' + x[0] + '</th><td>' + (neg ? '−' : '') + money(v / n) + '</td><td>' + (neg ? '−' : '') + money(v) + '</td></tr>';
      }).join('');
      var taxes = r.fed + r.ss + r.med + r.state;
      $('pc-net').textContent = money(r.net / n); $('pc-net-yr').textContent = money(r.net);
      $('pc-eff').textContent = r.gross ? (taxes / r.gross * 100).toFixed(1) + '%' : '—';
      $('pc-marg').textContent = Math.round(r.marg * 100) + '%';
      $('pc-net').classList.toggle('neg', r.net < 0);
      $('pc-sum').textContent = r.gross ? 'On ' + money(r.gross) + ' a year you take home about ' + money(r.net / n) + ' per paycheck (' + n + ' paychecks a year). Taxes take ' + money(taxes) + ' a year, ' + (taxes / r.gross * 100).toFixed(1) + '% of your pay.' : '';
    };
    seg('data-pc-type', function (v) {
      var a = $('pc-amt');
      if (v !== pcType) a.value = v === 'hourly' ? 25 : 60000;
      a.step = v === 'hourly' ? '0.25' : '100';
      pcType = v; calcP();
    });
    on(['pc-amt', 'pc-hours', 'pc-ot', 'pc-freq', 'pc-status', 'pc-kids', 'pc-deps', 'pc-state', 'pc-401k', 'pc-pretax', 'pc-post'], calcP);
    calcP();
  }

  /* ============================================================ Sleep calculator */
  var SLEEP_REC = { '3-5': [10, 13, '10 to 13 hours, including naps'], '6-12': [9, 12, '9 to 12 hours'], '13-17': [8, 10, '8 to 10 hours'],
    '18-60': [7, 9, '7 or more hours'], '61-64': [7, 9, '7 to 9 hours'], '65': [7, 8, '7 to 8 hours'] };
  function clock(mins) {
    mins = ((Math.round(mins) % 1440) + 1440) % 1440;
    var h = Math.floor(mins / 60), m = mins % 60, ap = h < 12 ? 'AM' : 'PM', h12 = h % 12 || 12;
    return h12 + ':' + (m < 10 ? '0' : '') + m + ' ' + ap;
  }
  function hrs(mins) { var h = Math.floor(mins / 60), m = Math.round(mins % 60); return h + ' h' + (m ? ' ' + m + ' min' : ''); }
  if (tool === 'sleep-calculator') {
    var slMode = 'wake';
    var calcS = function () {
      var v = $('sl-time').value, fall = Math.max(0, +$('sl-fall').value || 0), cyc = Math.min(150, Math.max(30, +$('sl-cycle').value || 90));
      var rec = SLEEP_REC[$('sl-age').value] || SLEEP_REC['18-60'];
      $('sl-time-lbl').textContent = slMode === 'wake' ? 'Wake-up time' : 'Bedtime';
      $('sl-rec').textContent = 'Recommended for your age: ' + rec[2] + ' of sleep a night (CDC). Highlighted times fall in that range.';
      if (!/^\d{2}:\d{2}$/.test(v)) { $('sl-out').innerHTML = ''; $('sl-sum').textContent = ''; return; }
      var t = +v.slice(0, 2) * 60 + +v.slice(3, 5), list = [];
      for (var c = 6; c >= 3; c--) {
        var sleep = c * cyc, when = slMode === 'wake' ? t - sleep - fall : t + fall + sleep, h = sleep / 60;
        list.push({ c: c, sleep: sleep, when: when, best: h >= rec[0] && h <= rec[1] + 0.01 });
      }
      if (slMode === 'bed') list.reverse();
      $('sl-out').innerHTML = list.map(function (x) {
        return '<div class="stat' + (x.best ? ' best' : '') + '"><b>' + clock(x.when) + '</b><span>' + x.c + ' cycles · ' + hrs(x.sleep) + ' sleep</span></div>';
      }).join('');
      var best = list.filter(function (x) { return x.best; }).map(function (x) { return clock(x.when); });
      $('sl-sum').textContent = slMode === 'wake'
        ? 'To wake up at ' + clock(t) + ', try going to bed at ' + (best.length ? best.join(' or ') : clock(list[1].when)) + '. These times include ' + fall + ' minutes to fall asleep.'
        : 'If you go to bed at ' + clock(t) + ', set your alarm for ' + (best.length ? best.join(' or ') : clock(list[2].when)) + '. That allows ' + fall + ' minutes to fall asleep.';
    };
    seg('data-sl-mode', function (m) { slMode = m; calcS(); });
    $('sl-now').addEventListener('click', function () {
      var d = new Date();
      $('sl-time').value = (d.getHours() < 10 ? '0' : '') + d.getHours() + ':' + (d.getMinutes() < 10 ? '0' : '') + d.getMinutes();
      slMode = 'bed';
      document.querySelectorAll('[data-sl-mode]').forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-sl-mode') === 'bed')); });
      calcS();
    });
    on(['sl-time', 'sl-fall', 'sl-cycle', 'sl-age'], calcS);
    calcS();
  }

  /* ============================================================ Time zone converter */
  var ZONES = [
    ['United States', [['America/New_York', 'Eastern Time – New York'], ['America/Chicago', 'Central Time – Chicago'], ['America/Denver', 'Mountain Time – Denver'],
      ['America/Phoenix', 'Arizona – Phoenix'], ['America/Los_Angeles', 'Pacific Time – Los Angeles'], ['America/Anchorage', 'Alaska – Anchorage'],
      ['Pacific/Honolulu', 'Hawaii – Honolulu'], ['America/Puerto_Rico', 'Atlantic – Puerto Rico']]],
    ['Canada & Latin America', [['America/Toronto', 'Toronto'], ['America/Vancouver', 'Vancouver'], ['America/Halifax', 'Halifax'], ['America/St_Johns', 'St. John’s'],
      ['America/Mexico_City', 'Mexico City'], ['America/Bogota', 'Bogotá'], ['America/Lima', 'Lima'], ['America/Sao_Paulo', 'São Paulo'], ['America/Argentina/Buenos_Aires', 'Buenos Aires']]],
    ['Europe', [['Europe/London', 'London'], ['Europe/Dublin', 'Dublin'], ['Europe/Lisbon', 'Lisbon'], ['Europe/Paris', 'Paris'], ['Europe/Berlin', 'Berlin'],
      ['Europe/Madrid', 'Madrid'], ['Europe/Rome', 'Rome'], ['Europe/Amsterdam', 'Amsterdam'], ['Europe/Stockholm', 'Stockholm'], ['Europe/Warsaw', 'Warsaw'],
      ['Europe/Athens', 'Athens'], ['Europe/Istanbul', 'Istanbul'], ['Europe/Moscow', 'Moscow']]],
    ['Africa & Middle East', [['Africa/Lagos', 'Lagos'], ['Africa/Cairo', 'Cairo'], ['Africa/Johannesburg', 'Johannesburg'], ['Africa/Nairobi', 'Nairobi'],
      ['Asia/Riyadh', 'Riyadh'], ['Asia/Dubai', 'Dubai']]],
    ['Asia & Pacific', [['Asia/Karachi', 'Karachi'], ['Asia/Kolkata', 'India – Mumbai, Delhi'], ['Asia/Kathmandu', 'Kathmandu'], ['Asia/Dhaka', 'Dhaka'],
      ['Asia/Bangkok', 'Bangkok'], ['Asia/Jakarta', 'Jakarta'], ['Asia/Singapore', 'Singapore'], ['Asia/Manila', 'Manila'], ['Asia/Hong_Kong', 'Hong Kong'],
      ['Asia/Shanghai', 'China – Beijing, Shanghai'], ['Asia/Seoul', 'Seoul'], ['Asia/Tokyo', 'Tokyo'], ['Australia/Perth', 'Perth'], ['Australia/Adelaide', 'Adelaide'],
      ['Australia/Brisbane', 'Brisbane'], ['Australia/Sydney', 'Sydney, Melbourne'], ['Pacific/Auckland', 'Auckland']]],
    ['Other', [['UTC', 'UTC (Coordinated Universal Time)']]]
  ];
  var LABEL = {};
  ZONES.forEach(function (g) { g[1].forEach(function (z) { LABEL[z[0]] = z[1]; }); });
  var nameOf = function (z) { return LABEL[z] || z.replace(/_/g, ' ').replace(/\//g, ' / '); };
  var partsCache = {};
  function partsIn(ms, zone) {
    var f = partsCache[zone] || (partsCache[zone] = new Intl.DateTimeFormat('en-US', { timeZone: zone, hourCycle: 'h23', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' }));
    var o = {}; f.formatToParts(new Date(ms)).forEach(function (p) { o[p.type] = +p.value; });
    if (o.hour === 24) o.hour = 0;
    return o;
  }
  // Offset of zone from UTC at instant ms, in minutes.
  function offsetMin(ms, zone) {
    var p = partsIn(ms, zone);
    return Math.round((Date.UTC(p.year, p.month - 1, p.day, p.hour, p.minute, p.second) - Math.floor(ms / 1000) * 1000) / 60000);
  }
  // Convert a wall-clock time in a zone to a UTC instant (handles DST gaps by moving forward).
  function zonedToUtc(y, mo, d, h, mi, zone) {
    var guess = Date.UTC(y, mo - 1, d, h, mi);
    var t = guess - offsetMin(guess, zone) * 60000;
    var o2 = offsetMin(t, zone);
    t = guess - o2 * 60000;
    if (offsetMin(t, zone) !== o2) t = guess - offsetMin(t, zone) * 60000;
    return t;
  }
  function fmtOffset(m) { var s = m < 0 ? '−' : '+', a = Math.abs(m); return 'UTC' + (m === 0 ? '' : s + Math.floor(a / 60) + (a % 60 ? ':' + (a % 60 < 10 ? '0' : '') + a % 60 : '')); }
  window.SmartToolsyTZ = { zonedToUtc: zonedToUtc, offsetMin: offsetMin };

  if (tool === 'time-zone-converter') {
    var local = (Intl.DateTimeFormat().resolvedOptions().timeZone) || 'UTC';
    var all = [];
    try { all = Intl.supportedValuesOf('timeZone'); } catch (e) { all = []; }
    var optionsHtml = function () {
      var h = '<optgroup label="Your time zone"><option value="' + esc(local) + '">' + esc(nameOf(local)) + ' (your time)</option></optgroup>';
      ZONES.forEach(function (g) { h += '<optgroup label="' + esc(g[0]) + '">' + g[1].map(function (z) { return '<option value="' + z[0] + '">' + esc(z[1]) + '</option>'; }).join('') + '</optgroup>'; });
      if (all.length) h += '<optgroup label="All time zones">' + all.filter(function (z) { return !LABEL[z]; }).map(function (z) { return '<option value="' + esc(z) + '">' + esc(nameOf(z)) + '</option>'; }).join('') + '</optgroup>';
      return h;
    };
    $('tz-from').innerHTML = optionsHtml();
    $('tz-add').innerHTML = '<option value="">Choose a city or time zone…</option>' + optionsHtml();
    $('tz-from').value = local;
    var saved = null;
    try { saved = JSON.parse(store.get('tz-list') || 'null'); } catch (e) { saved = null; }
    var valid = function (z) { try { new Intl.DateTimeFormat('en-US', { timeZone: z }); return true; } catch (e) { return false; } };
    var list = (Array.isArray(saved) && saved.length ? saved : ['America/New_York', 'America/Chicago', 'America/Denver', 'America/Los_Angeles', 'Europe/London', 'Asia/Kolkata', 'Asia/Tokyo', 'Australia/Sydney']).filter(valid);
    var setNow = function () {
      var p = partsIn(Date.now(), $('tz-from').value || local);
      $('tz-date').value = p.year + '-' + (p.month < 10 ? '0' : '') + p.month + '-' + (p.day < 10 ? '0' : '') + p.day;
      $('tz-time').value = (p.hour < 10 ? '0' : '') + p.hour + ':' + (p.minute < 10 ? '0' : '') + p.minute;
    };
    var dayNum = function (p) { return Date.UTC(p.year, p.month - 1, p.day) / 86400000; };
    var calcZ = function () {
      var from = $('tz-from').value || local, dv = $('tz-date').value, tv = $('tz-time').value, h24 = $('tz-24').checked;
      if (!/^\d{4}-\d{2}-\d{2}$/.test(dv) || !/^\d{2}:\d{2}$/.test(tv)) { $('tz-out').innerHTML = ''; $('tz-sum').textContent = ''; return; }
      var t = zonedToUtc(+dv.slice(0, 4), +dv.slice(5, 7), +dv.slice(8, 10), +tv.slice(0, 2), +tv.slice(3, 5), from);
      var src = partsIn(t, from);
      var fmt = function (zone) {
        return new Intl.DateTimeFormat('en-US', { timeZone: zone, weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit', hour12: !h24 }).format(new Date(t));
      };
      var abbr = function (zone) {
        var p = new Intl.DateTimeFormat('en-US', { timeZone: zone, timeZoneName: 'short' }).formatToParts(new Date(t)).filter(function (x) { return x.type === 'timeZoneName'; })[0];
        return p && !/^GMT|^UTC/.test(p.value) ? p.value : '';
      };
      var row = function (zone, removable) {
        var p = partsIn(t, zone), dd = dayNum(p) - dayNum(src), a = abbr(zone);
        var tag = dd ? ' <span class="tz-day">' + (dd > 0 ? '+' : '−') + Math.abs(dd) + ' day</span>' : '';
        return '<tr' + (removable ? '' : ' class="tz-src"') + '><th scope="row">' + esc(nameOf(zone)) + (zone === local ? ' <span class="tz-you">you</span>' : '') + '</th><td><b>' + esc(fmt(zone)) + '</b>' + tag + '</td><td>' + fmtOffset(offsetMin(t, zone)) + (a ? ' · ' + esc(a) : '') + '</td><td>' +
          (removable ? '<button class="tz-x" type="button" data-rm="' + esc(zone) + '" aria-label="Remove ' + esc(nameOf(zone)) + '">×</button>' : '') + '</td></tr>';
      };
      $('tz-out').innerHTML = row(from, false) + list.filter(function (z) { return z !== from; }).map(function (z) { return row(z, true); }).join('');
      var first = list.filter(function (z) { return z !== from; })[0];
      $('tz-sum').textContent = first ? fmt(from) + ' in ' + nameOf(from) + ' is ' + fmt(first) + ' in ' + nameOf(first) + '.' : '';
    };
    $('tz-out').addEventListener('click', function (e) {
      var b = e.target.closest('[data-rm]'); if (!b) return;
      var z = b.getAttribute('data-rm');
      list = list.filter(function (x) { return x !== z; }); store.set('tz-list', JSON.stringify(list)); calcZ();
    });
    $('tz-add').addEventListener('change', function () {
      var z = this.value; this.value = '';
      if (z && list.indexOf(z) < 0) { list.push(z); store.set('tz-list', JSON.stringify(list)); }
      calcZ();
    });
    $('tz-now').addEventListener('click', function () { setNow(); calcZ(); });
    on(['tz-date', 'tz-time', 'tz-from', 'tz-24'], calcZ);
    setNow(); $('tz-time').value = '09:00';
    calcZ();
  }
})();
