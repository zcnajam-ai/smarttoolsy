/* Minimal QR code encoder: byte mode, error correction level M, versions 1–20.
   Exposes QR.make(text) -> { size, get(x, y) } . No dependencies. */
(function (g) {
  'use strict';
  // [blocks, totalPerBlock, dataPerBlock, blocks2, total2, data2] for level M
  var RS = [null,
    [1,26,16],[1,44,28],[1,70,44],[2,50,32],[2,67,43],[4,43,27],[4,49,31],
    [2,60,38,2,61,39],[3,58,36,2,59,37],[4,69,43,1,70,44],[1,80,50,4,81,51],
    [6,58,36,2,59,37],[8,59,37,1,60,38],[4,64,40,5,65,41],[5,65,41,5,66,42],
    [7,73,45,3,74,46],[10,74,46,1,75,47],[9,69,43,4,70,44],[3,70,44,11,71,45],
    [3,67,41,13,68,42]];
  var ALIGN = [null, [], [6,18],[6,22],[6,26],[6,30],[6,34],[6,22,38],[6,24,42],[6,26,46],
    [6,28,50],[6,30,54],[6,32,58],[6,34,62],[6,26,46,66],[6,26,48,70],[6,26,50,74],
    [6,30,54,78],[6,30,56,82],[6,30,58,86],[6,34,62,90]];

  // GF(256) arithmetic, primitive polynomial 0x11D
  var EXP = new Array(512), LOG = new Array(256);
  (function () { var x = 1; for (var i = 0; i < 255; i++) { EXP[i] = x; LOG[x] = i; x <<= 1; if (x & 256) x ^= 0x11D; } for (i = 255; i < 512; i++) EXP[i] = EXP[i - 255]; })();
  function gmul(a, b) { return a && b ? EXP[LOG[a] + LOG[b]] : 0; }
  function genPoly(n) { var p = [1]; for (var i = 0; i < n; i++) { var q = new Array(p.length + 1).fill(0); for (var j = 0; j < p.length; j++) { q[j] ^= p[j]; q[j + 1] ^= gmul(p[j], EXP[i]); } p = q; } return p; }
  function rsEncode(data, n) {
    var gp = genPoly(n), res = data.concat(new Array(n).fill(0));
    for (var i = 0; i < data.length; i++) { var c = res[i]; if (c) for (var j = 0; j < gp.length; j++) res[i + j] ^= gmul(gp[j], c); }
    return res.slice(data.length);
  }
  function utf8(s) { var out = [], b = unescape(encodeURIComponent(s)); for (var i = 0; i < b.length; i++) out.push(b.charCodeAt(i)); return out; }
  function blocksOf(v) { var t = RS[v], r = []; for (var i = 0; i < t.length; i += 3) for (var k = 0; k < t[i]; k++) r.push([t[i + 1], t[i + 2]]); return r; }
  function dataCap(v) { return blocksOf(v).reduce(function (s, b) { return s + b[1]; }, 0); }

  function bch(value, poly) { var pd = 31 - Math.clz32(poly); var v = value << pd; while (31 - Math.clz32(v) >= pd && v) v ^= poly << (31 - Math.clz32(v) - pd); return (value << pd) | v; }

  function make(text) {
    var bytes = utf8(text), v, cb;
    for (v = 1; v <= 20; v++) { cb = v < 10 ? 8 : 16; if (4 + cb + bytes.length * 8 <= dataCap(v) * 8) break; }
    if (v > 20) throw new Error('Text is too long for a QR code. Shorten it to about 600 characters.');
    // bit stream
    var bits = [];
    function put(val, len) { for (var i = len - 1; i >= 0; i--) bits.push((val >>> i) & 1); }
    put(4, 4); put(bytes.length, cb); bytes.forEach(function (b) { put(b, 8); });
    var capBits = dataCap(v) * 8;
    put(0, Math.min(4, capBits - bits.length));
    while (bits.length % 8) bits.push(0);
    var cw = []; for (var i = 0; i < bits.length; i += 8) { var x = 0; for (var j = 0; j < 8; j++) x = (x << 1) | bits[i + j]; cw.push(x); }
    for (var pad = 0; cw.length < dataCap(v); pad++) cw.push(pad % 2 ? 0x11 : 0xEC);
    // split into blocks, add EC, interleave
    var blks = blocksOf(v), dBlocks = [], eBlocks = [], off = 0;
    blks.forEach(function (b) { var d = cw.slice(off, off + b[1]); off += b[1]; dBlocks.push(d); eBlocks.push(rsEncode(d, b[0] - b[1])); });
    var final = [], maxD = Math.max.apply(null, dBlocks.map(function (d) { return d.length; }));
    for (i = 0; i < maxD; i++) dBlocks.forEach(function (d) { if (i < d.length) final.push(d[i]); });
    for (i = 0; i < eBlocks[0].length; i++) eBlocks.forEach(function (e) { final.push(e[i]); });

    var size = v * 4 + 17;
    var m = [], fn = [];
    for (i = 0; i < size; i++) { m.push(new Array(size).fill(0)); fn.push(new Array(size).fill(false)); }
    function set(x, y, dark) { m[y][x] = dark ? 1 : 0; fn[y][x] = true; }
    function finder(cx, cy) {
      for (var dy = -4; dy <= 4; dy++) for (var dx = -4; dx <= 4; dx++) {
        var x = cx + dx, y = cy + dy; if (x < 0 || y < 0 || x >= size || y >= size) continue;
        var d = Math.max(Math.abs(dx), Math.abs(dy)); set(x, y, d !== 2 && d !== 4);
      }
    }
    finder(3, 3); finder(size - 4, 3); finder(3, size - 4);
    for (i = 8; i < size - 8; i++) { set(i, 6, i % 2 === 0); set(6, i, i % 2 === 0); }
    var al = ALIGN[v];
    al.forEach(function (ay) { al.forEach(function (ax) {
      if ((ax === 6 && ay === 6) || (ax === 6 && ay === size - 7) || (ax === size - 7 && ay === 6)) return;
      for (var dy = -2; dy <= 2; dy++) for (var dx = -2; dx <= 2; dx++) set(ax + dx, ay + dy, Math.max(Math.abs(dx), Math.abs(dy)) !== 1);
    }); });
    // reserve format areas + dark module
    for (i = 0; i < 9; i++) { if (!fn[8][i]) set(i, 8, false); if (!fn[i][8]) set(8, i, false); }
    for (i = 0; i < 8; i++) { set(size - 1 - i, 8, false); set(8, size - 1 - i, false); }
    set(8, size - 8, true);
    // version info
    if (v >= 7) {
      var vi = bch(v, 0x1F25);
      for (i = 0; i < 18; i++) { var bit = (vi >> i) & 1, a = size - 11 + (i % 3), b = Math.floor(i / 3); set(a, b, bit); set(b, a, bit); }
    }
    // place data
    var allBits = []; final.forEach(function (c) { for (var k = 7; k >= 0; k--) allBits.push((c >> k) & 1); });
    var idx = 0;
    for (var right = size - 1; right >= 1; right -= 2) {
      if (right === 6) right = 5;
      for (var vert = 0; vert < size; vert++) for (j = 0; j < 2; j++) {
        var xx = right - j, up = ((right + 1) & 2) === 0, yy = up ? size - 1 - vert : vert;
        if (!fn[yy][xx]) { m[yy][xx] = idx < allBits.length ? allBits[idx] : 0; idx++; }
      }
    }
    var MASKS = [
      function (x, y) { return (x + y) % 2 === 0; }, function (x, y) { return y % 2 === 0; },
      function (x) { return x % 3 === 0; }, function (x, y) { return (x + y) % 3 === 0; },
      function (x, y) { return (Math.floor(x / 3) + Math.floor(y / 2)) % 2 === 0; },
      function (x, y) { return (x * y) % 2 + (x * y) % 3 === 0; },
      function (x, y) { return ((x * y) % 2 + (x * y) % 3) % 2 === 0; },
      function (x, y) { return ((x + y) % 2 + (x * y) % 3) % 2 === 0; }];
    function applyFormat(mm, mask) {
      var f = bch((0 << 3) | mask, 0x537) ^ 0x5412; // level M = 00
      for (var k = 0; k <= 5; k++) mm[k][8] = (f >> k) & 1;
      mm[7][8] = (f >> 6) & 1; mm[8][8] = (f >> 7) & 1; mm[8][7] = (f >> 8) & 1;
      for (k = 9; k < 15; k++) mm[8][14 - k] = (f >> k) & 1;
      for (k = 0; k < 8; k++) mm[8][size - 1 - k] = (f >> k) & 1;
      for (k = 8; k < 15; k++) mm[size - 15 + k][8] = (f >> k) & 1;
      mm[size - 8][8] = 1;
    }
    function penalty(mm) {
      var p = 0, y, x, run, c;
      for (y = 0; y < size; y++) { run = 1; for (x = 1; x < size; x++) { if (mm[y][x] === mm[y][x - 1]) { run++; if (x === size - 1 && run >= 5) p += run - 2; } else { if (run >= 5) p += run - 2; run = 1; } } }
      for (x = 0; x < size; x++) { run = 1; for (y = 1; y < size; y++) { if (mm[y][x] === mm[y - 1][x]) { run++; if (y === size - 1 && run >= 5) p += run - 2; } else { if (run >= 5) p += run - 2; run = 1; } } }
      for (y = 0; y < size - 1; y++) for (x = 0; x < size - 1; x++) { c = mm[y][x]; if (c === mm[y][x + 1] && c === mm[y + 1][x] && c === mm[y + 1][x + 1]) p += 3; }
      var pat1 = [1,0,1,1,1,0,1,0,0,0,0], pat2 = [0,0,0,0,1,0,1,1,1,0,1];
      for (y = 0; y < size; y++) for (x = 0; x <= size - 11; x++) {
        var h1 = true, h2 = true, v1 = true, v2 = true;
        for (var k = 0; k < 11; k++) { if (mm[y][x + k] !== pat1[k]) h1 = false; if (mm[y][x + k] !== pat2[k]) h2 = false; if (mm[x + k][y] !== pat1[k]) v1 = false; if (mm[x + k][y] !== pat2[k]) v2 = false; }
        p += 40 * (h1 + h2 + v1 + v2);
      }
      var dark = 0; for (y = 0; y < size; y++) for (x = 0; x < size; x++) dark += mm[y][x];
      p += Math.floor(Math.abs(dark * 20 - size * size * 10) / (size * size)) * 10;
      return p;
    }
    var best = null, bestP = Infinity;
    for (var mk = 0; mk < 8; mk++) {
      var mm = m.map(function (r) { return r.slice(); });
      for (y = 0; y < size; y++) for (x = 0; x < size; x++) if (!fn[y][x] && MASKS[mk](x, y)) mm[y][x] ^= 1;
      applyFormat(mm, mk);
      var pp = penalty(mm); if (pp < bestP) { bestP = pp; best = mm; }
    }
    var y, x;
    return { size: size, version: v, get: function (gx, gy) { return best[gy][gx] === 1; } };
  }
  g.QR = { make: make };
})(typeof window !== 'undefined' ? window : globalThis);
