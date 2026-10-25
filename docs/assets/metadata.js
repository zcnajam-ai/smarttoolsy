/* SmartToolsy Image Metadata Remover.
 * Strips EXIF (incl. GPS), XMP, IPTC, C2PA/JUMBF, comments and AI-generation text
 * from JPEG, PNG and WebP files without re-encoding the image, so quality is untouched.
 * A JPEG's orientation is kept in a tiny new EXIF block so photos don't turn sideways.
 * The core functions also run under Node for tests (module.exports).
 */
(function (root) {
  'use strict';
  var td = typeof TextDecoder !== 'undefined' ? new TextDecoder('latin1') : null;
  function ascii(b, s, n) { var o = ''; for (var i = 0; i < n && s + i < b.length; i++) o += String.fromCharCode(b[s + i]); return o; }
  function u16(b, o, le) { return le ? b[o] | (b[o + 1] << 8) : (b[o] << 8) | b[o + 1]; }
  function u32(b, o, le) { return le ? (b[o] | (b[o + 1] << 8) | (b[o + 2] << 16) | (b[o + 3] << 24)) >>> 0 : ((b[o] << 24) | (b[o + 1] << 16) | (b[o + 2] << 8) | b[o + 3]) >>> 0; }

  /* ------------------------------------------------------------ EXIF (TIFF) reader */
  var TAGS = { 0x010F: 'make', 0x0110: 'model', 0x0131: 'software', 0x0132: 'date', 0x0112: 'orientation', 0x013B: 'artist', 0x8298: 'copyright', 0x010E: 'description',
    0x9003: 'dateOriginal', 0xA434: 'lens', 0xA431: 'serial', 0xA435: 'lensSerial', 0x9286: 'userComment', 0xA420: 'uniqueId', 0xA430: 'owner' };
  function readTiff(b, start, end) {
    var out = {}; if (end - start < 8) return out;
    var le = b[start] === 0x49; if (!le && b[start] !== 0x4D) return out;
    function val(type, count, off) {
      var sizes = { 1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 7: 1, 9: 4, 10: 8 }, sz = (sizes[type] || 1) * count;
      var p = sz <= 4 ? off : start + u32(b, off, le);
      if (p < start || p + sz > end) return null;
      if (type === 2 || type === 7) return ascii(b, p, count).replace(/\0+$/, '').trim();
      if (type === 3) return count === 1 ? u16(b, p, le) : null;
      if (type === 4) return count === 1 ? u32(b, p, le) : null;
      if (type === 5) { var r = []; for (var i = 0; i < count; i++) { var d = u32(b, p + i * 8 + 4, le); r.push(d ? u32(b, p + i * 8, le) / d : 0); } return r; }
      return null;
    }
    function ifd(off, into, gps) {
      var p = start + off; if (p + 2 > end) return 0;
      var n = u16(b, p, le), ptrs = {};
      for (var i = 0; i < n && p + 2 + i * 12 + 12 <= end; i++) {
        var e = p + 2 + i * 12, tag = u16(b, e, le), type = u16(b, e + 2, le), count = u32(b, e + 4, le);
        if (tag === 0x8769 || tag === 0x8825) { ptrs[tag] = u32(b, e + 8, le); continue; }
        if (gps) { var gv = val(type, count, e + 8); if (gv != null) into['gps' + tag] = gv; continue; }
        if (TAGS[tag]) { var v = val(type, count, e + 8); if (v !== null && v !== '') into[TAGS[tag]] = v; }
      }
      return ptrs;
    }
    try {
      var ptrs = ifd(u32(b, start + 4, le), out, false);
      if (ptrs && ptrs[0x8769]) ifd(ptrs[0x8769], out, false);
      if (ptrs && ptrs[0x8825]) {
        var g = {}; ifd(ptrs[0x8825], g, true);
        if (g.gps2 && g.gps4) {
          var lat = g.gps2[0] + g.gps2[1] / 60 + g.gps2[2] / 3600, lon = g.gps4[0] + g.gps4[1] / 60 + g.gps4[2] / 3600;
          if (/S/i.test(g.gps1 || '')) lat = -lat; if (/W/i.test(g.gps3 || '')) lon = -lon;
          if (isFinite(lat) && isFinite(lon) && (lat || lon)) out.gps = { lat: lat, lon: lon };
        } else if (Object.keys(g).length) out.gpsPartial = true;
      }
    } catch (err) { /* unreadable EXIF: still removed */ }
    return out;
  }

  function orientationApp1(o) {
    // "Exif\0\0" + big-endian TIFF with one IFD entry: Orientation (0x0112) SHORT = o
    var a = [0xFF, 0xE1, 0, 34, 0x45, 0x78, 0x69, 0x66, 0, 0, 0x4D, 0x4D, 0, 0x2A, 0, 0, 0, 8, 0, 1, 0x01, 0x12, 0, 3, 0, 0, 0, 1, 0, o, 0, 0, 0, 0, 0, 0];
    return new Uint8Array(a);
  }

  /* ------------------------------------------------------------ JPEG */
  function jpeg(b) {
    var found = { types: [], exif: {} }, keep = [], i = 2, orientation = 1;
    function add(t) { if (found.types.indexOf(t) < 0) found.types.push(t); }
    keep.push(b.subarray(0, 2));
    while (i + 4 <= b.length) {
      if (b[i] !== 0xFF) throw new Error('This JPEG file looks damaged.');
      var m = b[i + 1];
      if (m === 0xFF) { i++; continue; }
      if (m === 0xD8 || (m >= 0xD0 && m <= 0xD7) || m === 0x01) { keep.push(b.subarray(i, i + 2)); i += 2; continue; }
      var len = u16(b, i + 2), segEnd = i + 2 + len;
      if (len < 2 || segEnd > b.length) throw new Error('This JPEG file looks damaged.');
      if (m === 0xDA) {
        // start of scan: image data runs to the first EOI (FFD9); anything after it (extra images, appended data) is dropped
        var j = segEnd, eoi = -1;
        while (j < b.length - 1) { if (b[j] === 0xFF && b[j + 1] === 0xD9) { eoi = j; break; } j++; }
        if (eoi < 0) eoi = b.length - 2;
        keep.push(b.subarray(i, eoi + 2));
        if (eoi + 2 < b.length - 16) add('Extra data after the image');
        break;
      }
      var id = ascii(b, i + 4, Math.min(30, len - 2)), drop = false;
      if (m === 0xE1 && id.indexOf('Exif\0') === 0) {
        found.exif = readTiff(b, i + 10, segEnd); add('EXIF');
        if (found.exif.orientation >= 2 && found.exif.orientation <= 8) orientation = found.exif.orientation;
        drop = true;
      } else if (m === 0xE1) { add(/xap|xmp/i.test(id) ? 'XMP' : 'APP1 data'); drop = true; if (/c2pa|contentauth/i.test(ascii(b, i + 4, Math.min(len, 4000)))) add('Content Credentials (C2PA)'); }
      else if (m === 0xE2) { if (id.indexOf('ICC_PROFILE') === 0) { drop = false; } else { add(id.indexOf('MPF') === 0 ? 'Multi-picture data' : 'APP2 data'); drop = true; } }
      else if (m === 0xED) { add('IPTC / Photoshop'); drop = true; }
      else if (m === 0xEB) { add('Content Credentials (C2PA)'); drop = true; }
      else if (m === 0xEE && id.indexOf('Adobe') === 0) { drop = false; }        // colour transform flag, needed to decode
      else if (m === 0xE0 && id.indexOf('JFIF') === 0) { drop = false; }
      else if (m >= 0xE0 && m <= 0xEF) { add('Other app data'); drop = true; }
      else if (m === 0xFE) { add('Comment'); drop = true; }
      if (!drop) keep.push(b.subarray(i, segEnd));
      if (m === 0xE0 && !drop && orientation === 1) { /* placeholder: orientation inserted after JFIF below */ }
      i = segEnd;
    }
    if (orientation !== 1) {
      var app1 = orientationApp1(orientation), at = 1;
      if (keep[1] && keep[1][1] === 0xE0) at = 2; // after JFIF APP0
      keep.splice(at, 0, app1);
    }
    found.orientation = orientation;
    return { parts: keep, found: found };
  }

  /* ------------------------------------------------------------ PNG */
  var CRC = (function () { var t = new Uint32Array(256); for (var n = 0; n < 256; n++) { var c = n; for (var k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; t[n] = c >>> 0; } return t; })();
  function crc32(arr, c) { c = c === undefined ? 0xFFFFFFFF : c; for (var i = 0; i < arr.length; i++) c = CRC[(c ^ arr[i]) & 0xFF] ^ (c >>> 8); return c; }
  var PNG_KEEP = { IHDR: 1, PLTE: 1, IDAT: 1, IEND: 1, tRNS: 1, gAMA: 1, cHRM: 1, sRGB: 1, iCCP: 1, sBIT: 1, pHYs: 1, bKGD: 1, acTL: 1, fcTL: 1, fdAT: 1, cICP: 1, mDCv: 1, cLLi: 1 };
  function png(b) {
    var found = { types: [], exif: {}, text: [] }, keep = [b.subarray(0, 8)], i = 8;
    function add(t) { if (found.types.indexOf(t) < 0) found.types.push(t); }
    while (i + 12 <= b.length) {
      var len = u32(b, i), type = ascii(b, i + 4, 4), end = i + 12 + len;
      if (end > b.length) throw new Error('This PNG file looks damaged.');
      if (PNG_KEEP[type]) keep.push(b.subarray(i, end));
      else {
        if (type === 'tEXt' || type === 'iTXt' || type === 'zTXt') {
          var d = i + 8, z = d; while (z < d + len && b[z] !== 0) z++;
          var key = ascii(b, d, z - d); found.text.push(key);
          add(/^(parameters|prompt|workflow|Dream|sd-metadata|invokeai)/i.test(key) ? 'AI generation data' : /XML:com.adobe.xmp/i.test(key) ? 'XMP' : 'Text notes');
        } else if (type === 'eXIf') { found.exif = readTiff(b, i + 8, i + 8 + len); add('EXIF'); }
        else if (type === 'tIME') add('Last-modified time');
        else if (type === 'caBX') add('Content Credentials (C2PA)');
        else add('Other data (' + type + ')');
      }
      i = end;
      if (type === 'IEND') break;
    }
    return { parts: keep, found: found };
  }

  /* ------------------------------------------------------------ WebP */
  function webp(b) {
    var found = { types: [], exif: {} }, chunks = [], i = 12, vp8x = -1;
    function add(t) { if (found.types.indexOf(t) < 0) found.types.push(t); }
    while (i + 8 <= b.length) {
      var type = ascii(b, i, 4), len = u32(b, i + 4, true), end = i + 8 + len + (len & 1);
      if (i + 8 + len > b.length) throw new Error('This WebP file looks damaged.');
      if (type === 'EXIF') { var s = i + 8; if (ascii(b, s, 6) === 'Exif\0\0') s += 6; found.exif = readTiff(b, s, i + 8 + len); add('EXIF'); }
      else if (type === 'XMP ') add('XMP');
      else { if (type === 'VP8X') vp8x = chunks.length; chunks.push(b.subarray(i, Math.min(end, b.length))); }
      i = end;
    }
    if (vp8x >= 0) { var c = new Uint8Array(chunks[vp8x]); c[8] &= ~0x0C; chunks[vp8x] = c; }
    var size = 4; chunks.forEach(function (c) { size += c.length; });
    var head = new Uint8Array(12); head.set(b.subarray(0, 12));
    head[4] = size & 255; head[5] = (size >>> 8) & 255; head[6] = (size >>> 16) & 255; head[7] = (size >>> 24) & 255;
    return { parts: [head].concat(chunks), found: found };
  }

  function detect(b) {
    if (b[0] === 0xFF && b[1] === 0xD8) return 'jpeg';
    if (b[0] === 0x89 && ascii(b, 1, 3) === 'PNG') return 'png';
    if (ascii(b, 0, 4) === 'RIFF' && ascii(b, 8, 4) === 'WEBP') return 'webp';
    if (ascii(b, 4, 4) === 'ftyp' && /heic|heix|mif1|avif/.test(ascii(b, 8, 4))) return 'heic';
    return null;
  }

  function clean(u8) {
    var kind = detect(u8);
    if (!kind) throw new Error('Unsupported file. Use JPG, PNG or WebP images.');
    if (kind === 'heic') throw new Error('HEIC/AVIF photos aren’t supported yet. On iPhone, set Camera → Formats → Most Compatible, or convert to JPG first.');
    var r = kind === 'jpeg' ? jpeg(u8) : kind === 'png' ? png(u8) : webp(u8);
    var total = 0; r.parts.forEach(function (p) { total += p.length; });
    var out = new Uint8Array(total), o = 0; r.parts.forEach(function (p) { out.set(p, o); o += p.length; });
    r.found.kind = kind;
    return { bytes: out, found: r.found, mime: kind === 'jpeg' ? 'image/jpeg' : 'image/' + kind };
  }

  /* ------------------------------------------------------------ ZIP (store only) */
  function zip(files) {
    var parts = [], central = [], offset = 0, enc = new TextEncoder();
    files.forEach(function (f) {
      var name = enc.encode(f.name), crc = (crc32(f.bytes) ^ 0xFFFFFFFF) >>> 0, n = f.bytes.length;
      var h = new DataView(new ArrayBuffer(30));
      h.setUint32(0, 0x04034b50, true); h.setUint16(4, 20, true); h.setUint16(6, 0x0800, true); h.setUint32(14, crc, true); h.setUint32(18, n, true); h.setUint32(22, n, true); h.setUint16(26, name.length, true);
      parts.push(new Uint8Array(h.buffer), name, f.bytes);
      var c = new DataView(new ArrayBuffer(46));
      c.setUint32(0, 0x02014b50, true); c.setUint16(4, 20, true); c.setUint16(6, 20, true); c.setUint16(8, 0x0800, true); c.setUint32(16, crc, true); c.setUint32(20, n, true); c.setUint32(24, n, true); c.setUint16(28, name.length, true); c.setUint32(42, offset, true);
      central.push(new Uint8Array(c.buffer), name);
      offset += 30 + name.length + n;
    });
    var csize = 0; central.forEach(function (x) { csize += x.length; });
    var e = new DataView(new ArrayBuffer(22));
    e.setUint32(0, 0x06054b50, true); e.setUint16(8, files.length, true); e.setUint16(10, files.length, true); e.setUint32(12, csize, true); e.setUint32(16, offset, true);
    return new Blob(parts.concat(central, [new Uint8Array(e.buffer)]), { type: 'application/zip' });
  }

  var api = { clean: clean, readTiff: readTiff, detect: detect };
  if (typeof module !== 'undefined' && module.exports) { module.exports = api; return; }
  root.STMeta = api;

  /* ------------------------------------------------------------ page UI */
  if (document.body.getAttribute('data-tool') !== 'image-metadata-remover') return;
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
  var kb = function (n) { return n < 1024 ? n + ' B' : n < 1048576 ? (n / 1024).toFixed(1) + ' KB' : (n / 1048576).toFixed(2) + ' MB'; };
  var results = [], urls = [];
  var input = $('mr-file'), list = $('mr-list'), msg = $('mr-msg');

  function describe(f) {
    var e = f.exif || {}, rows = [];
    if (e.gps) rows.push(['Location (GPS)', e.gps.lat.toFixed(5) + ', ' + e.gps.lon.toFixed(5), true]);
    else if (e.gpsPartial) rows.push(['Location (GPS)', 'GPS fields present', true]);
    if (e.make || e.model) rows.push(['Camera', [e.make, e.model].filter(Boolean).join(' ')]);
    if (e.lens) rows.push(['Lens', e.lens]);
    if (e.serial || e.lensSerial) rows.push(['Serial number', e.serial || e.lensSerial, true]);
    if (e.dateOriginal || e.date) rows.push(['Taken / edited', e.dateOriginal || e.date]);
    if (e.software) rows.push(['Software', e.software]);
    if (e.artist || e.owner) rows.push(['Author / owner', e.artist || e.owner, true]);
    if (e.copyright) rows.push(['Copyright', e.copyright]);
    if (e.description || e.userComment) rows.push(['Description', String(e.description || e.userComment).slice(0, 80)]);
    if (f.text && f.text.length) rows.push(['Text fields', f.text.slice(0, 6).join(', ')]);
    return rows;
  }

  function renderItem(r) {
    var li = document.createElement('li'); li.className = 'mr-item';
    if (r.error) { li.innerHTML = '<div class="mr-name">' + esc(r.name) + '</div><p class="mr-err">' + esc(r.error) + '</p>'; return li; }
    var rows = describe(r.found), types = r.found.types;
    var saved = r.before - r.after;
    var head = '<div class="mr-name">' + esc(r.name) + '</div><p class="mr-sum">' + (types.length ?
      '<b class="mr-bad">Removed:</b> ' + types.map(esc).join(', ') + ' (' + kb(Math.max(0, saved)) + ')' :
      '<b class="mr-ok">No hidden metadata found.</b> The file was already clean.') + '</p>';
    var table = rows.length ? '<table class="mr-tbl"><tbody>' + rows.map(function (x) { return '<tr' + (x[2] ? ' class="mr-risk"' : '') + '><th>' + esc(x[0]) + '</th><td>' + esc(x[1]) + '</td></tr>'; }).join('') + '</tbody></table>' : '';
    var keepNote = r.found.orientation && r.found.orientation !== 1 ? '<p class="count-note">Kept: the photo’s rotation, so it still displays the right way up.</p>' : '';
    li.innerHTML = head + table + keepNote + '<a class="btn" download="' + esc(r.outName) + '" href="' + r.url + '">Download clean file</a>';
    return li;
  }

  function outName(name) { var m = name.match(/^(.*?)(\.[^.]+)?$/); return (m[1] || 'image') + '-clean' + (m[2] || ''); }

  async function handle(files) {
    urls.forEach(function (u) { URL.revokeObjectURL(u); }); urls = []; results = []; list.innerHTML = '';
    var arr = Array.prototype.slice.call(files || []);
    if (!arr.length) return;
    msg.textContent = 'Cleaning ' + arr.length + ' file' + (arr.length > 1 ? 's' : '') + '…';
    for (var k = 0; k < arr.length; k++) {
      var f = arr[k], r = { name: f.name, before: f.size };
      try {
        var res = clean(new Uint8Array(await f.arrayBuffer()));
        var blob = new Blob([res.bytes], { type: res.mime });
        r.after = res.bytes.length; r.found = res.found; r.bytes = res.bytes; r.outName = outName(f.name); r.url = URL.createObjectURL(blob); urls.push(r.url);
      } catch (err) { r.error = err.message || 'This file couldn’t be read.'; }
      results.push(r); list.appendChild(renderItem(r));
    }
    var ok = results.filter(function (x) { return !x.error; });
    var risky = ok.filter(function (x) { return x.found.exif && (x.found.exif.gps || x.found.exif.gpsPartial); }).length;
    msg.textContent = ok.length + ' of ' + results.length + ' file' + (results.length > 1 ? 's' : '') + ' cleaned.' + (risky ? ' ' + risky + ' contained GPS location data.' : '');
    var all = $('mr-all'); all.hidden = ok.length < 2;
  }

  input.addEventListener('change', function () { handle(input.files); });
  var drop = input.closest('.drop') || input.parentNode;
  ['dragover', 'dragenter'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
  ['dragleave', 'drop'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); }); });
  drop.addEventListener('drop', function (e) { if (e.dataTransfer && e.dataTransfer.files) handle(e.dataTransfer.files); });
  $('mr-all').addEventListener('click', function () {
    var ok = results.filter(function (x) { return !x.error; }), used = {};
    var files = ok.map(function (x) { var n = x.outName, i = 2; while (used[n]) { n = x.outName.replace(/(\.[^.]+)?$/, '-' + i++ + '$1'); } used[n] = 1; return { name: n, bytes: x.bytes }; });
    var a = document.createElement('a'); a.href = URL.createObjectURL(zip(files)); a.download = 'clean-images.zip'; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
  });
})(typeof window !== 'undefined' ? window : this);
