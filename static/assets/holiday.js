/* SmartToolsy holiday tools: turkey calculator, Christmas budget calculator. */
(function () {
  'use strict';
  var tool = document.body.getAttribute('data-tool');
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var money = function (n) { return (n < 0 ? '−$' : '$') + Math.abs(isFinite(n) ? n : 0).toLocaleString('en-US', { maximumFractionDigits: 0 }); };
  var on = function (ids, fn) { ids.forEach(function (id) { var el = $(id); if (el) { el.addEventListener('input', fn); el.addEventListener('change', fn); } }); };
  function ymd(d) { return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function hm(min) { var h = Math.floor(min / 60), m = Math.round(min % 60); return (h ? h + ' h' : '') + (m ? (h ? ' ' : '') + m + ' min' : (h ? '' : '0 min')); }
  function when(d) { return d.toLocaleString('en-US', { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' }); }
  function day(d) { return d.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' }); }

  /* ============================================================ Turkey */
  if (tool === 'turkey-calculator') {
    // USDA roasting chart, 325°F, minutes: [min lb, max lb, low, high]
    var UNSTUFFED = [[4, 8, 90, 195], [8, 12, 165, 180], [12, 14, 180, 225], [14, 18, 225, 255], [18, 20, 255, 270], [20, 24, 270, 300]];
    var STUFFED = [[6, 8, 150, 210], [8, 12, 180, 210], [12, 14, 210, 240], [14, 18, 240, 255], [18, 20, 255, 285], [20, 24, 285, 315]];
    var weightTouched = false;
    var thanksgiving = function (now) {
      function tg(y) { var d = new Date(y, 10, 1); while (d.getDay() !== 4) d.setDate(d.getDate() + 1); d.setDate(d.getDate() + 21); return d; }
      var today = new Date(now.getFullYear(), now.getMonth(), now.getDate()), t = tg(now.getFullYear());
      return t < today ? tg(now.getFullYear() + 1) : t;
    };
    $('tk-date').value = ymd(thanksgiving(new Date()));
    var size = function () {
      var rate = +$('tk-left').value, eq = Math.max(0, +$('tk-adults').value || 0) + Math.max(0, +$('tk-kids').value || 0) / 2;
      var lb = Math.max(4, Math.ceil(eq * rate));
      if (!eq) { $('tk-size').textContent = '—'; $('tk-breast').textContent = '—'; return; }
      if (lb > 24) {
        var each = Math.ceil(lb / 2);
        $('tk-size').textContent = lb + ' lb total';
        $('tk-breast').textContent = '2 × ' + each + ' lb';
        $('tk-breast').nextElementSibling.textContent = 'Easier: two turkeys';
      } else {
        $('tk-size').textContent = lb + '–' + (lb + 2) + ' lb';
        $('tk-breast').textContent = eq <= 6 ? Math.max(3, Math.ceil(eq * rate * 0.75)) + ' lb breast' : '—';
        $('tk-breast').nextElementSibling.textContent = eq <= 6 ? 'Or a bone-in breast' : 'Too many guests for a breast';
      }
      if (!weightTouched) $('tk-lb').value = Math.min(24, lb > 24 ? Math.ceil(lb / 2) : lb);
    };
    var roast = function () {
      var w = +$('tk-lb').value || 0, stuffed = $('tk-stuffed').value === '1', frozen = $('tk-frozen').value === '1';
      if (w < 4) { $('tk-sum').textContent = 'Enter a turkey weight of at least 4 lb.'; $('tk-plan').innerHTML = ''; return; }
      var tbl = stuffed ? STUFFED : UNSTUFFED, row = tbl[tbl.length - 1], over = w > 24;
      for (var i = 0; i < tbl.length; i++) if (w <= tbl[i][1]) { row = tbl[i]; break; }
      if (stuffed && w < 6) row = STUFFED[0];
      var lo = row[2], hi = row[3];
      if (frozen) { lo *= 1.5; hi *= 1.5; }
      var dp = ($('tk-date').value || '').split('-'), tp = ($('tk-time').value || '16:00').split(':');
      var dinner = dp.length === 3 ? new Date(+dp[0], +dp[1] - 1, +dp[2], +tp[0] || 0, +tp[1] || 0) : null;
      var msg = 'Roast at 325°F for about ' + hm(lo) + ' to ' + hm(hi) + (frozen ? ' (50% longer because it starts frozen)' : '') + ', until it reaches 165°F.';
      if (over) msg += ' Turkeys over 24 lb are beyond the USDA chart, so allow extra time and rely on the thermometer.';
      $('tk-sum').textContent = msg;
      if (!dinner) { $('tk-plan').innerHTML = ''; return; }
      var M = 60000, out = new Date(dinner - 20 * M), start = new Date(out - hi * M), rows = [];
      if (!frozen) {
        var thawDays = Math.ceil(w / 4.5), fridge = new Date(start.getFullYear(), start.getMonth(), start.getDate() - thawDays);
        rows.push(['Move it to the fridge to thaw (' + thawDays + ' day' + (thawDays === 1 ? '' : 's') + ')', day(fridge)]);
        rows.push(['Or start a cold-water thaw (' + hm(w * 30) + ')', when(new Date(start - (w * 30 + 60) * M))]);
      }
      rows.push(['Preheat the oven to 325°F', when(new Date(start - 30 * M))]);
      rows.push(['Turkey goes in the oven', when(start)]);
      rows.push(['Start checking the temperature', when(new Date(start.getTime() + (lo - 30) * M))]);
      rows.push(['Out of the oven at 165°F, then rest', when(out)]);
      rows.push(['Carve and eat', when(dinner)]);
      $('tk-plan').innerHTML = rows.map(function (r) { return '<tr><th scope="row">' + esc(r[0]) + '</th><td>' + esc(r[1]) + '</td></tr>'; }).join('');
    };
    $('tk-lb').addEventListener('input', function () { weightTouched = true; });
    on(['tk-adults', 'tk-kids', 'tk-left'], function () { size(); roast(); });
    on(['tk-lb', 'tk-stuffed', 'tk-frozen', 'tk-date', 'tk-time'], roast);
    size(); roast();
  }

  /* ============================================================ Christmas budget */
  if (tool === 'christmas-budget-calculator') {
    var KEY = 'st-xmas-budget', FIELDS = ['cb-budget', 'cb-saved', 'cb-pay', 'cb-food', 'cb-travel', 'cb-decor', 'cb-wrap'];
    var DEFAULT = [['Partner', 150], ['Mom', 60], ['Dad', 60], ['Sister', 40], ['Coworkers', 50]];
    var store = function () {
      var data = { f: {}, r: [] };
      FIELDS.forEach(function (id) { data.f[id] = $(id).value; });
      [].slice.call($('cb-rows').children).forEach(function (tr) { var i = tr.querySelectorAll('input'); data.r.push([i[0].value, i[1].value]); });
      try { localStorage.setItem(KEY, JSON.stringify(data)); } catch (e) { /* storage unavailable */ }
    };
    var row = function (name, amt) {
      var tr = document.createElement('tr');
      tr.innerHTML = '<td><input type="text" aria-label="Person" placeholder="Name" value="' + esc(name) + '"></td>' +
        '<td><input type="number" min="0" step="5" aria-label="Gift budget" value="' + esc(amt) + '"></td>' +
        '<td><button type="button" class="icon-btn" aria-label="Remove person">×</button></td>';
      tr.querySelector('button').addEventListener('click', function () { tr.remove(); calc(); });
      tr.querySelectorAll('input').forEach(function (el) { el.addEventListener('input', calc); });
      $('cb-rows').appendChild(tr);
    };
    var calc = function () {
      var gifts = 0, people = 0;
      [].slice.call($('cb-rows').children).forEach(function (tr) { var v = +tr.querySelectorAll('input')[1].value || 0; gifts += v; if (v) people++; });
      var other = ['cb-food', 'cb-travel', 'cb-decor', 'cb-wrap'].reduce(function (s, id) { return s + (+$(id).value || 0); }, 0);
      var total = gifts + other, budget = +$('cb-budget').value || 0, saved = +$('cb-saved').value || 0;
      var left = budget - total, need = Math.max(0, total - saved);
      var now = new Date(), today = new Date(now.getFullYear(), now.getMonth(), now.getDate()), xmas = new Date(now.getFullYear(), 11, 25);
      if (xmas < today) xmas = new Date(now.getFullYear() + 1, 11, 25);
      var days = Math.round((xmas - today) / 864e5), every = +$('cb-pay').value, pays = Math.max(1, Math.floor(days / every));
      $('cb-total').textContent = money(total);
      $('cb-left').textContent = money(left); $('cb-left').classList.toggle('neg', left < 0);
      $('cb-need').textContent = money(need);
      $('cb-per').textContent = money(Math.ceil(need / pays));
      $('cb-per-lbl').textContent = 'Save per paycheck (' + pays + ' left)';
      $('cb-sum').textContent = 'Gifts for ' + people + ' ' + (people === 1 ? 'person' : 'people') + ' come to ' + money(gifts) + ', plus ' + money(other) + ' for everything else. ' +
        (left < 0 ? 'That is ' + money(-left) + ' over your budget, so trim a few gifts or extras. ' : 'That leaves ' + money(left) + ' spare in your budget. ') +
        'Christmas is ' + days + ' day' + (days === 1 ? '' : 's') + ' away' + (need ? ', so put aside about ' + money(Math.ceil(need / pays)) + ' from each of your next ' + pays + ' paycheck' + (pays === 1 ? '' : 's') + '.' : ' and you have already saved enough.');
      store();
    };
    var saved = null;
    try { saved = JSON.parse(localStorage.getItem(KEY) || 'null'); } catch (e) { saved = null; }
    if (saved && saved.f) FIELDS.forEach(function (id) { if (saved.f[id] != null) $(id).value = saved.f[id]; });
    ((saved && saved.r && saved.r.length) ? saved.r : DEFAULT).forEach(function (r) { row(r[0], r[1]); });
    $('cb-add').addEventListener('click', function () { row('', 25); calc(); var ins = $('cb-rows').lastChild.querySelector('input'); ins.focus(); });
    on(FIELDS, calc); calc();
  }
})();
