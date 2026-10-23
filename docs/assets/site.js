/* SmartToolsy shared helpers */
(function () {
  var root = document.documentElement;
  try { var t = localStorage.getItem('st-theme'); if (t) root.setAttribute('data-theme', t); } catch (e) {}
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.theme-btn');
    if (!b) return;
    var dark = root.getAttribute('data-theme') === 'dark' ||
      (!root.getAttribute('data-theme') && matchMedia('(prefers-color-scheme: dark)').matches);
    var next = dark ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('st-theme', next); } catch (e2) {}
  });
})();

window.ST = {
  $: function (id) { return document.getElementById(id); },
  toast: function (msg) {
    var t = document.querySelector('.toast');
    if (!t) { t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); }
    t.textContent = msg; t.classList.add('show');
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove('show'); }, 1600);
  },
  copy: function (text) {
    var done = function () { ST.toast('Copied'); };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done, function () { ST.fallbackCopy(text); done(); });
    } else { ST.fallbackCopy(text); done(); }
  },
  fallbackCopy: function (text) {
    var ta = document.createElement('textarea'); ta.value = text; document.body.appendChild(ta);
    ta.select(); try { document.execCommand('copy'); } catch (e) {} ta.remove();
  },
  fmt: function (n, d) {
    if (!isFinite(n)) return '—';
    return Number(n).toLocaleString('en-US', { maximumFractionDigits: d === undefined ? 2 : d });
  },
  esc: function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
};

/* Homepage finder */
(function () {
  var input = document.getElementById('finder');
  if (!input) return;
  var chips = document.querySelectorAll('.chip');
  var items = document.querySelectorAll('.tool-list li');
  var groups = document.querySelectorAll('.tool-group');
  var note = document.getElementById('count-note');
  var empty = document.getElementById('empty');
  var cat = 'all';
  function apply() {
    var q = input.value.trim().toLowerCase();
    var shown = 0;
    items.forEach(function (li) {
      var ok = (cat === 'all' || li.dataset.cat === cat) && (!q || li.dataset.search.indexOf(q) !== -1);
      li.hidden = !ok; if (ok) shown++;
    });
    groups.forEach(function (g) { g.hidden = !g.querySelector('li:not([hidden])'); });
    note.textContent = q || cat !== 'all' ? shown + (shown === 1 ? ' tool matches' : ' tools match') : '';
    empty.hidden = shown !== 0;
  }
  input.addEventListener('input', apply);
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      chips.forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      c.setAttribute('aria-pressed', 'true'); cat = c.dataset.cat; apply();
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== input) { e.preventDefault(); input.focus(); }
  });
})();
