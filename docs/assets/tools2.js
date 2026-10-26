/* SmartToolsy batch 2: image resizer, cropper, converters, character counter, GPA, time card, tip, salary. */
(function () {
  'use strict';
  var tool = document.body.getAttribute('data-tool');
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var money = function (n) { return '$' + (isFinite(n) ? n : 0).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); };
  var num = function (n, d) { return (isFinite(n) ? n : 0).toLocaleString('en-US', { maximumFractionDigits: d == null ? 2 : d }); };
  var kb = function (n) { return n < 1024 * 1024 ? (n / 1024).toFixed(n < 10240 ? 1 : 0) + ' KB' : (n / 1048576).toFixed(2) + ' MB'; };
  var on = function (ids, fn) { ids.forEach(function (id) { var el = $(id); if (el) { el.addEventListener('input', fn); el.addEventListener('change', fn); } }); };
  function toBlob(canvas, type, q) { return new Promise(function (r) { canvas.toBlob(r, type, q); }); }
  function baseName(n) { return (n || 'image').replace(/\.[^.]+$/, ''); }
  function wireDrop(inputId, handler) {
    var input = $(inputId); if (!input) return;
    input.addEventListener('change', function () { handler(input.files); });
    var drop = input.closest('.drop'); if (!drop) return;
    ['dragover', 'dragenter'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
    ['dragleave', 'drop'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); }); });
    drop.addEventListener('drop', function (e) { if (e.dataTransfer && e.dataTransfer.files.length) handler(e.dataTransfer.files); });
  }
  // high-quality downscale: halve repeatedly, then draw the final size
  function scaled(src, w, h) {
    var cw = src.width, ch = src.height, cur = src;
    while (cw / 2 >= w && ch / 2 >= h) {
      var t = document.createElement('canvas'); t.width = Math.round(cw / 2); t.height = Math.round(ch / 2);
      var tx = t.getContext('2d'); tx.imageSmoothingQuality = 'high'; tx.drawImage(cur, 0, 0, t.width, t.height);
      cur = t; cw = t.width; ch = t.height;
    }
    var c = document.createElement('canvas'); c.width = w; c.height = h;
    var x = c.getContext('2d'); x.imageSmoothingQuality = 'high'; x.drawImage(cur, 0, 0, w, h);
    return c;
  }
  function flatten(canvas, color) {
    var c = document.createElement('canvas'); c.width = canvas.width; c.height = canvas.height;
    var x = c.getContext('2d'); x.fillStyle = color || '#ffffff'; x.fillRect(0, 0, c.width, c.height); x.drawImage(canvas, 0, 0); return c;
  }
  function canvasOf(bmp) { var c = document.createElement('canvas'); c.width = bmp.width; c.height = bmp.height; c.getContext('2d').drawImage(bmp, 0, 0); return c; }
  // store-only ZIP for batch downloads
  var CRC = (function () { var t = new Uint32Array(256); for (var n = 0; n < 256; n++) { var c = n; for (var k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; t[n] = c >>> 0; } return t; })();
  function crc32(a) { var c = 0xFFFFFFFF; for (var i = 0; i < a.length; i++) c = CRC[(c ^ a[i]) & 0xFF] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; }
  function zip(files) {
    var parts = [], central = [], off = 0, enc = new TextEncoder();
    files.forEach(function (f) {
      var name = enc.encode(f.name), crc = crc32(f.bytes), n = f.bytes.length, h = new DataView(new ArrayBuffer(30)), c = new DataView(new ArrayBuffer(46));
      h.setUint32(0, 0x04034b50, true); h.setUint16(4, 20, true); h.setUint16(6, 0x0800, true); h.setUint32(14, crc, true); h.setUint32(18, n, true); h.setUint32(22, n, true); h.setUint16(26, name.length, true);
      c.setUint32(0, 0x02014b50, true); c.setUint16(4, 20, true); c.setUint16(6, 20, true); c.setUint16(8, 0x0800, true); c.setUint32(16, crc, true); c.setUint32(20, n, true); c.setUint32(24, n, true); c.setUint16(28, name.length, true); c.setUint32(42, off, true);
      parts.push(new Uint8Array(h.buffer), name, f.bytes); central.push(new Uint8Array(c.buffer), name); off += 30 + name.length + n;
    });
    var size = 0; central.forEach(function (x) { size += x.length; });
    var e = new DataView(new ArrayBuffer(22)); e.setUint32(0, 0x06054b50, true); e.setUint16(8, files.length, true); e.setUint16(10, files.length, true); e.setUint32(12, size, true); e.setUint32(16, off, true);
    return new Blob(parts.concat(central, [new Uint8Array(e.buffer)]), { type: 'application/zip' });
  }
  function saveBlob(blob, name) { var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name; document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000); }

  /* ============================================================ Image resizer */
  if (tool === 'image-resizer') {
    var src = null, srcFile = null, lock = true, outUrl = null;
    var fmtOf = function () { var f = $('rs-fmt').value; return f === 'same' ? (srcFile && /png/.test(srcFile.type) ? 'image/png' : srcFile && /webp/.test(srcFile.type) ? 'image/webp' : 'image/jpeg') : f; };
    var sync = function (from) {
      if (!src) return;
      var mode = $('rs-mode').value;
      $('rs-px').hidden = mode !== 'px'; $('rs-pct-f').hidden = mode !== 'pct';
      if (mode === 'px' && lock) {
        var r = src.height / src.width;
        if (from === 'w') $('rs-h').value = Math.max(1, Math.round(($('rs-w').value || 0) * r));
        if (from === 'h') $('rs-w').value = Math.max(1, Math.round(($('rs-h').value || 0) / r));
      }
      $('rs-q-f').hidden = fmtOf() === 'image/png';
    };
    var dims = function () {
      if ($('rs-mode').value === 'pct') { var p = Math.max(1, +$('rs-pct').value || 100) / 100; return [Math.max(1, Math.round(src.width * p)), Math.max(1, Math.round(src.height * p))]; }
      return [Math.max(1, Math.min(16000, +$('rs-w').value || src.width)), Math.max(1, Math.min(16000, +$('rs-h').value || src.height))];
    };
    var go = async function () {
      if (!src) return;
      var d = dims(), type = fmtOf(), c = scaled(src, d[0], d[1]), q = (+$('rs-q').value || 85) / 100, target = +$('rs-kb').value * 1024, blob;
      if (type === 'image/jpeg') c = flatten(c, '#ffffff');
      if (target && type !== 'image/png') {
        var lo = 0.05, hi = 0.95, best = null;
        for (var i = 0; i < 8; i++) { var mid = (lo + hi) / 2, b = await toBlob(c, type, mid); if (b.size <= target) { best = b; lo = mid; } else hi = mid; }
        blob = best || await toBlob(c, type, 0.05);
        $('rs-note').textContent = blob.size > target ? 'Couldn’t reach ' + num(target / 1024, 0) + ' KB at this size; reduce the dimensions as well.' : 'Quality adjusted automatically to fit under ' + num(target / 1024, 0) + ' KB.';
      } else { blob = await toBlob(c, type, q); $('rs-note').textContent = ''; }
      if (outUrl) URL.revokeObjectURL(outUrl); outUrl = URL.createObjectURL(blob);
      var ext = type === 'image/png' ? 'png' : type === 'image/webp' ? 'webp' : 'jpg';
      $('rs-prev').src = outUrl; $('rs-dl').href = outUrl; $('rs-dl').download = baseName(srcFile.name) + '-' + d[0] + 'x' + d[1] + '.' + ext;
      $('rs-info').textContent = src.width + ' × ' + src.height + ' (' + kb(srcFile.size) + ') → ' + d[0] + ' × ' + d[1] + ' (' + kb(blob.size) + ')';
      $('rs-out').hidden = false;
    };
    wireDrop('rs-file', async function (files) {
      var f = files[0]; if (!f) return;
      try { srcFile = f; src = canvasOf(await createImageBitmap(f)); } catch (e) { $('rs-info').textContent = 'That file couldn’t be opened as an image.'; return; }
      $('rs-w').value = src.width; $('rs-h').value = src.height; $('rs-opts').hidden = false; sync(); go();
    });
    $('rs-lock').addEventListener('change', function () { lock = $('rs-lock').checked; sync('w'); });
    $('rs-w').addEventListener('input', function () { sync('w'); }); $('rs-h').addEventListener('input', function () { sync('h'); });
    on(['rs-mode', 'rs-fmt'], function () { sync(); });
    $('rs-go').addEventListener('click', go);
    document.querySelectorAll('[data-rs]').forEach(function (b) { b.addEventListener('click', function () { if (!src) return; var p = b.getAttribute('data-rs').split('x'); $('rs-mode').value = 'px'; lock = false; $('rs-lock').checked = false; $('rs-w').value = p[0]; $('rs-h').value = p[1]; sync(); go(); }); });
  }

  /* ============================================================ Image cropper */
  if (tool === 'image-cropper') {
    var img = null, file = null, box = { x: 0, y: 0, w: 0, h: 0 }, ratio = 0, stage = $('cr-stage'), view = $('cr-img'), rect = $('cr-box');
    var scale = function () { return img.width / view.clientWidth; };
    var clamp = function () {
      box.w = Math.max(10, Math.min(box.w, img.width)); box.h = Math.max(10, Math.min(box.h, img.height));
      if (ratio) { if (box.w / box.h > ratio) box.w = Math.round(box.h * ratio); else box.h = Math.round(box.w / ratio); }
      box.x = Math.max(0, Math.min(box.x, img.width - box.w)); box.y = Math.max(0, Math.min(box.y, img.height - box.h));
    };
    var draw = function () {
      var s = scale();
      rect.style.left = box.x / s + 'px'; rect.style.top = box.y / s + 'px'; rect.style.width = box.w / s + 'px'; rect.style.height = box.h / s + 'px';
      $('cr-x').value = Math.round(box.x); $('cr-y').value = Math.round(box.y); $('cr-w').value = Math.round(box.w); $('cr-h').value = Math.round(box.h);
    };
    var setRatio = function (r) {
      ratio = r;
      if (img) { if (r) { var w = img.width, h = Math.round(w / r); if (h > img.height) { h = img.height; w = Math.round(h * r); } box = { x: (img.width - w) / 2, y: (img.height - h) / 2, w: w, h: h }; } clamp(); draw(); }
    };
    wireDrop('cr-file', async function (files) {
      file = files[0]; if (!file) return;
      try { img = canvasOf(await createImageBitmap(file)); } catch (e) { $('cr-msg').textContent = 'That file couldn’t be opened as an image.'; return; }
      view.src = URL.createObjectURL(file); $('cr-work').hidden = false; $('cr-msg').textContent = '';
      view.onload = function () { box = { x: img.width * 0.1, y: img.height * 0.1, w: img.width * 0.8, h: img.height * 0.8 }; setRatio(ratio); };
    });
    document.querySelectorAll('[data-ratio]').forEach(function (b) {
      b.addEventListener('click', function () {
        document.querySelectorAll('[data-ratio]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        var v = b.getAttribute('data-ratio'), p = v.split(':'); setRatio(v === 'free' ? 0 : +p[0] / +p[1]);
      });
    });
    var drag = null;
    rect.addEventListener('pointerdown', function (e) {
      if (!img) return; e.preventDefault(); rect.setPointerCapture(e.pointerId);
      drag = { mode: e.target.getAttribute('data-h') || 'move', sx: e.clientX, sy: e.clientY, b: Object.assign({}, box) };
    });
    rect.addEventListener('pointermove', function (e) {
      if (!drag) return; var s = scale(), dx = (e.clientX - drag.sx) * s, dy = (e.clientY - drag.sy) * s, b = drag.b, m = drag.mode;
      if (m === 'move') { box.x = b.x + dx; box.y = b.y + dy; }
      else {
        var x0 = b.x, y0 = b.y, x1 = b.x + b.w, y1 = b.y + b.h;
        if (m.indexOf('w') >= 0) x0 = Math.min(x1 - 10, Math.max(0, b.x + dx)); if (m.indexOf('e') >= 0) x1 = Math.max(x0 + 10, Math.min(img.width, x1 + dx));
        if (m.indexOf('n') >= 0) y0 = Math.min(y1 - 10, Math.max(0, b.y + dy)); if (m.indexOf('s') >= 0) y1 = Math.max(y0 + 10, Math.min(img.height, y1 + dy));
        box = { x: x0, y: y0, w: x1 - x0, h: y1 - y0 };
        if (ratio) { var nh = box.w / ratio; if (m.indexOf('n') >= 0) box.y = y1 - nh; box.h = nh; if (box.y < 0 || box.y + box.h > img.height) { box.h = m.indexOf('n') >= 0 ? y1 : img.height - box.y; box.y = m.indexOf('n') >= 0 ? y1 - box.h : box.y; box.w = box.h * ratio; if (m.indexOf('w') >= 0) box.x = x1 - box.w; } }
      }
      clamp(); draw();
    });
    ['pointerup', 'pointercancel'].forEach(function (ev) { rect.addEventListener(ev, function () { drag = null; }); });
    on(['cr-x', 'cr-y', 'cr-w', 'cr-h'], function () { if (!img) return; box = { x: +$('cr-x').value || 0, y: +$('cr-y').value || 0, w: +$('cr-w').value || 10, h: +$('cr-h').value || 10 }; clamp(); draw(); });
    window.addEventListener('resize', function () { if (img) draw(); });
    $('cr-go').addEventListener('click', async function () {
      if (!img) return; var w = Math.round(box.w), h = Math.round(box.h), c = document.createElement('canvas'); c.width = w; c.height = h;
      c.getContext('2d').drawImage(img, Math.round(box.x), Math.round(box.y), w, h, 0, 0, w, h);
      var type = /png/.test(file.type) ? 'image/png' : /webp/.test(file.type) ? 'image/webp' : 'image/jpeg';
      if ($('cr-circle').checked) { var k = c.getContext('2d'); k.globalCompositeOperation = 'destination-in'; k.beginPath(); k.ellipse(w / 2, h / 2, w / 2, h / 2, 0, 0, Math.PI * 2); k.fill(); type = 'image/png'; }
      var blob = await toBlob(c, type, 0.92), ext = type === 'image/png' ? 'png' : type === 'image/webp' ? 'webp' : 'jpg';
      saveBlob(blob, baseName(file.name) + '-cropped.' + ext);
      $('cr-msg').textContent = 'Saved a ' + w + ' × ' + h + ' px image (' + kb(blob.size) + ').';
    });
  }

  /* ============================================================ Converters */
  if (tool === 'png-to-jpg' || tool === 'webp-to-jpg') {
    var results = [];
    var outType = function () { return tool === 'png-to-jpg' ? 'image/jpeg' : $('cv-fmt').value; };
    var convert = async function (files) {
      results.forEach(function (r) { if (r.url) URL.revokeObjectURL(r.url); }); results = [];
      var list = $('cv-list'); list.innerHTML = ''; var arr = [].slice.call(files || []); if (!arr.length) return;
      var type = outType(), ext = type === 'image/png' ? 'png' : 'jpg', q = (+$('cv-q').value || 92) / 100, bg = $('cv-bg') ? $('cv-bg').value : '#ffffff';
      $('cv-msg').textContent = 'Converting ' + arr.length + ' file' + (arr.length > 1 ? 's' : '') + '…';
      for (var i = 0; i < arr.length; i++) {
        var f = arr[i], li = document.createElement('li'); li.className = 'cv-item';
        try {
          var c = canvasOf(await createImageBitmap(f)); if (type === 'image/jpeg') c = flatten(c, bg);
          var blob = await toBlob(c, type, q), url = URL.createObjectURL(blob), name = baseName(f.name) + '.' + ext;
          results.push({ name: name, blob: blob, url: url });
          li.innerHTML = '<img src="' + url + '" alt=""><div><b>' + esc(name) + '</b><span>' + c.width + ' × ' + c.height + ' · ' + kb(f.size) + ' → ' + kb(blob.size) + '</span></div><a class="btn ghost" href="' + url + '" download="' + esc(name) + '">Download</a>';
        } catch (e) { li.innerHTML = '<div><b>' + esc(f.name) + '</b><span class="mr-err">Couldn’t read this file. Use PNG, JPG or WebP images.</span></div>'; }
        list.appendChild(li);
      }
      $('cv-msg').textContent = results.length + ' of ' + arr.length + ' converted.'; $('cv-all').hidden = results.length < 2;
      last = arr;
    };
    var last = null;
    wireDrop('cv-file', convert);
    on(['cv-q', 'cv-bg', 'cv-fmt'], function () { if (last) convert(last); });
    $('cv-all').addEventListener('click', async function () {
      var used = {}, files = [];
      for (var i = 0; i < results.length; i++) { var n = results[i].name, k = 2; while (used[n]) n = results[i].name.replace(/(\.[^.]+)$/, '-' + k++ + '$1'); used[n] = 1; files.push({ name: n, bytes: new Uint8Array(await results[i].blob.arrayBuffer()) }); }
      saveBlob(zip(files), 'converted-images.zip');
    });
  }

  /* ============================================================ Character counter */
  if (tool === 'character-counter') {
    var GSM = '@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞÆæßÉ !"#¤%&\'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà^{}\\[~]|€';
    var LIMITS = [['X (Twitter) post', 280], ['Instagram caption', 2200], ['LinkedIn post', 3000], ['Facebook post', 63206], ['YouTube title', 100], ['YouTube description', 5000], ['Pinterest pin description', 500], ['Google title (approx.)', 60], ['Meta description (approx.)', 160]];
    var run = function () {
      var t = $('cc-text').value, chars = [...t].length;
      var words = (t.match(/[\p{L}\p{N}]+(?:[-'’][\p{L}\p{N}]+)*/gu) || []).length;
      $('cc-chars').textContent = num(chars, 0); $('cc-nosp').textContent = num([...t.replace(/\s/g, '')].length, 0); $('cc-words').textContent = num(words, 0);
      $('cc-lines').textContent = num(t ? t.split('\n').length : 0, 0); $('cc-bytes').textContent = num(new TextEncoder().encode(t).length, 0);
      var gsm = [...t].every(function (ch) { return GSM.indexOf(ch) >= 0; }), per = gsm ? (chars <= 160 ? 160 : 153) : (chars <= 70 ? 70 : 67), seg = chars ? Math.ceil(chars / per) : 0;
      $('cc-sms').textContent = seg + ' SMS' + (seg === 1 ? '' : ' messages') + ' · ' + (gsm ? 'standard text (160 per message)' : 'contains emoji or special characters (70 per message)');
      $('cc-limits').innerHTML = LIMITS.map(function (l) {
        var pct = Math.min(100, chars / l[1] * 100), over = chars > l[1];
        return '<li><span>' + esc(l[0]) + '</span><div class="meter ' + (over ? 'm-bad' : chars ? 'm-good' : 'm-none') + '"><i style="width:' + pct.toFixed(1) + '%"></i><span>' + num(chars, 0) + ' / ' + num(l[1], 0) + (over ? ' · ' + num(chars - l[1], 0) + ' over' : '') + '</span></div></li>';
      }).join('');
    };
    on(['cc-text'], run); run();
  }

  /* ============================================================ GPA */
  if (tool === 'gpa-calculator') {
    var PTS = { 'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7, 'F': 0 };
    var BONUS = { reg: 0, hon: 0.5, ap: 1 };
    var row = function (name, grade, cr, lvl) {
      var tr = document.createElement('tr');
      tr.innerHTML = '<td><input type="text" aria-label="Course name" placeholder="Course" value="' + esc(name || '') + '"></td>' +
        '<td><select aria-label="Grade">' + Object.keys(PTS).map(function (g) { return '<option' + (g === (grade || 'A') ? ' selected' : '') + '>' + g + '</option>'; }).join('') + '</select></td>' +
        '<td><input type="number" aria-label="Credits" min="0" step="0.5" value="' + (cr == null ? 3 : cr) + '"></td>' +
        '<td><select aria-label="Course level"><option value="reg"' + (lvl === 'reg' || !lvl ? ' selected' : '') + '>Regular</option><option value="hon"' + (lvl === 'hon' ? ' selected' : '') + '>Honors</option><option value="ap"' + (lvl === 'ap' ? ' selected' : '') + '>AP / IB</option></select></td>' +
        '<td><button type="button" class="icon-btn" aria-label="Remove course">×</button></td>';
      tr.querySelector('button').addEventListener('click', function () { tr.remove(); calc(); });
      tr.querySelectorAll('input,select').forEach(function (el) { el.addEventListener('input', calc); el.addEventListener('change', calc); });
      $('gpa-rows').appendChild(tr);
    };
    var calc = function () {
      var cr = 0, unw = 0, w = 0;
      [].slice.call($('gpa-rows').children).forEach(function (tr) {
        var s = tr.querySelectorAll('select'), c = +tr.querySelector('input[type=number]').value || 0, p = PTS[s[0].value];
        cr += c; unw += p * c; w += (p > 0 ? Math.min(5, p + BONUS[s[1].value]) : 0) * c;
      });
      var pc = +$('gpa-prev-cr').value || 0, pg = +$('gpa-prev').value || 0;
      var u = cr ? unw / cr : 0, wt = cr ? w / cr : 0, cum = (cr + pc) ? (unw + pg * pc) / (cr + pc) : 0;
      $('gpa-unw').textContent = cr ? u.toFixed(2) : '—'; $('gpa-w').textContent = cr ? wt.toFixed(2) : '—';
      $('gpa-cum').textContent = pc ? cum.toFixed(2) : '—'; $('gpa-cr').textContent = num(cr, 1);
    };
    [['English', 'A', 3, 'reg'], ['Algebra II', 'B+', 3, 'hon'], ['AP Biology', 'A-', 4, 'ap'], ['U.S. History', 'B', 3, 'reg']].forEach(function (r) { row(r[0], r[1], r[2], r[3]); });
    $('gpa-add').addEventListener('click', function () { row('', 'A', 3, 'reg'); calc(); });
    on(['gpa-prev', 'gpa-prev-cr'], calc); calc();
  }

  /* ============================================================ Time card */
  if (tool === 'time-card-calculator') {
    var DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    var mins = function (v) { if (!v) return null; var p = v.split(':'); return +p[0] * 60 + +p[1]; };
    var hm = function (m) { m = Math.round(m); return Math.floor(m / 60) + ':' + String(m % 60).padStart(2, '0'); };
    $('tc-rows').innerHTML = DAYS.map(function (d, i) {
      var wk = i < 5;
      return '<tr><th scope="row">' + d.slice(0, 3) + '</th><td><input type="time" aria-label="' + d + ' start" value="' + (wk ? '09:00' : '') + '"></td><td><input type="time" aria-label="' + d + ' end" value="' + (wk ? '17:30' : '') + '"></td><td><input type="number" min="0" step="5" aria-label="' + d + ' break minutes" value="' + (wk ? 30 : 0) + '"></td><td class="tc-day">—</td></tr>';
    }).join('');
    var calc = function () {
      var total = 0;
      [].slice.call($('tc-rows').children).forEach(function (tr) {
        var inp = tr.querySelectorAll('input'), s = mins(inp[0].value), e = mins(inp[1].value), br = +inp[2].value || 0, cell = tr.querySelector('.tc-day');
        if (s == null || e == null) { cell.textContent = '—'; return; }
        var m = e - s; if (m < 0) m += 1440; m = Math.max(0, m - br); total += m;
        cell.textContent = hm(m) + ' (' + (m / 60).toFixed(2) + ')';
      });
      var rate = +$('tc-rate').value || 0, otAfter = (+$('tc-ot').value || 40) * 60, otRate = +$('tc-otx').value || 1.5;
      var reg = Math.min(total, otAfter), ot = Math.max(0, total - otAfter);
      $('tc-total').textContent = hm(total); $('tc-dec').textContent = (total / 60).toFixed(2);
      $('tc-otm').textContent = hm(ot); $('tc-pay').textContent = rate ? money(reg / 60 * rate + ot / 60 * rate * otRate) : '—';
    };
    on(['tc-rate', 'tc-ot', 'tc-otx'], calc);
    $('tc-rows').addEventListener('input', calc); $('tc-rows').addEventListener('change', calc); calc();
  }

  /* ============================================================ Tip */
  if (tool === 'tip-calculator') {
    var calcT = function () {
      var bill = +$('tp-bill').value || 0, pct = +$('tp-pct').value || 0, ppl = Math.max(1, Math.round(+$('tp-ppl').value || 1)), tax = +$('tp-tax').value || 0;
      var base = $('tp-pretax').checked ? Math.max(0, bill - tax) : bill, tip = base * pct / 100, total = bill + tip, each = total / ppl;
      if ($('tp-round').checked && ppl) { each = Math.ceil(each); total = each * ppl; tip = total - bill; }
      $('tp-tip').textContent = money(tip); $('tp-total').textContent = money(total); $('tp-each').textContent = money(each); $('tp-tipeach').textContent = money(tip / ppl);
      $('tp-eff').textContent = bill ? (tip / bill * 100).toFixed(1) + '% of the bill' : '';
    };
    document.querySelectorAll('[data-tip]').forEach(function (b) { b.addEventListener('click', function () { $('tp-pct').value = b.getAttribute('data-tip'); document.querySelectorAll('[data-tip]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); calcT(); }); });
    on(['tp-bill', 'tp-pct', 'tp-ppl', 'tp-tax', 'tp-pretax', 'tp-round'], calcT); calcT();
  }

  /* ============================================================ Salary <-> hourly */
  if (tool === 'salary-to-hourly') {
    var calcS = function () {
      var amt = +$('sh-amt').value || 0, per = $('sh-per').value, hpw = +$('sh-hours').value || 40, wpy = +$('sh-weeks').value || 52;
      var hoursYear = hpw * wpy, annual = { hour: amt * hoursYear, day: amt * wpy * 5, week: amt * wpy, biweek: amt * wpy / 2, semimonth: amt * 24, month: amt * 12, year: amt }[per];
      var rows = [['Hourly', annual / hoursYear], ['Daily (' + num(hpw / 5, 1) + ' h)', annual / (wpy * 5)], ['Weekly', annual / wpy], ['Every two weeks', annual / wpy * 2], ['Twice a month', annual / 24], ['Monthly', annual / 12], ['Yearly', annual]];
      $('sh-out').innerHTML = rows.map(function (r) { return '<tr><th scope="row">' + r[0] + '</th><td>' + money(r[1]) + '</td></tr>'; }).join('');
      $('sh-sum').textContent = amt ? money(annual) + ' a year is about ' + money(annual / hoursYear) + ' an hour at ' + num(hpw, 1) + ' hours a week for ' + num(wpy, 1) + ' weeks.' : '';
    };
    on(['sh-amt', 'sh-per', 'sh-hours', 'sh-weeks'], calcS); calcS();
  }
})();
