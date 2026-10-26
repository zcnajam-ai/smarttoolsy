/* SmartToolsy Background Remover.
 * Runs the U-2-Net (small) salient-object model (Apache-2.0) in the browser with
 * ONNX Runtime Web, so photos never leave the device. The model file is served by
 * SmartToolsy; the runtime is loaded once from jsDelivr (pinned version).
 */
(function () {
  'use strict';
  if (document.body.getAttribute('data-tool') !== 'background-remover') return;
  var ORT_VER = '1.20.1';
  var ORT_BASE = 'https://cdn.jsdelivr.net/npm/onnxruntime-web@' + ORT_VER + '/dist/';
  var MODEL = '/assets/models/u2netp.onnx';
  var SIZE = 320, MAX_SIDE = 4096;
  var MEAN = [0.485, 0.456, 0.406], STD = [0.229, 0.224, 0.225];
  var $ = function (id) { return document.getElementById(id); };
  var session = null, loading = null, current = null, cutCanvas = null, outUrl = null;

  function loadScript(src) {
    return new Promise(function (res, rej) { var s = document.createElement('script'); s.src = src; s.async = true; s.crossOrigin = 'anonymous'; s.onload = res; s.onerror = function () { rej(new Error('script')); }; document.head.appendChild(s); });
  }
  function getSession() {
    if (session) return Promise.resolve(session);
    if (loading) return loading;
    loading = (window.ort ? Promise.resolve() : loadScript(ORT_BASE + 'ort.wasm.min.js')).then(function () {
      var ort = window.ort;
      ort.env.wasm.wasmPaths = ORT_BASE;
      ort.env.wasm.numThreads = window.crossOriginIsolated ? Math.min(4, navigator.hardwareConcurrency || 2) : 1;
      return ort.InferenceSession.create(MODEL, { executionProviders: ['wasm'], graphOptimizationLevel: 'all' });
    }).then(function (s) { session = s; return s; }).catch(function (e) { loading = null; throw e; });
    return loading;
  }

  function preprocess(bmp) {
    var c = document.createElement('canvas'); c.width = SIZE; c.height = SIZE;
    var x = c.getContext('2d', { willReadFrequently: true }); x.imageSmoothingQuality = 'high';
    x.drawImage(bmp, 0, 0, SIZE, SIZE);
    var d = x.getImageData(0, 0, SIZE, SIZE).data, n = SIZE * SIZE, f = new Float32Array(3 * n);
    for (var i = 0; i < n; i++) {
      for (var ch = 0; ch < 3; ch++) f[ch * n + i] = (d[i * 4 + ch] / 255 - MEAN[ch]) / STD[ch];
    }
    return f;
  }

  function maskCanvas(pred) {
    var n = SIZE * SIZE, lo = Infinity, hi = -Infinity, i;
    for (i = 0; i < n; i++) { if (pred[i] < lo) lo = pred[i]; if (pred[i] > hi) hi = pred[i]; }
    var span = hi - lo || 1, c = document.createElement('canvas'); c.width = SIZE; c.height = SIZE;
    var x = c.getContext('2d'), img = x.createImageData(SIZE, SIZE);
    for (i = 0; i < n; i++) {
      var v = (pred[i] - lo) / span;
      v = v <= 0.08 ? 0 : v >= 0.92 ? 1 : (v - 0.08) / 0.84; // firm up the edges a little
      v = v * v * (3 - 2 * v);
      img.data[i * 4 + 3] = Math.round(v * 255);
    }
    x.putImageData(img, 0, 0);
    return c;
  }

  function fitSize(w, h) { var s = Math.min(1, MAX_SIDE / Math.max(w, h)); return [Math.round(w * s), Math.round(h * s)]; }

  async function run(file) {
    var msg = $('bg-msg'), go = $('bg-out');
    go.hidden = true;
    if (!/^image\//.test(file.type) && !/\.(jpe?g|png|webp)$/i.test(file.name)) { msg.textContent = 'Please choose a JPG, PNG or WebP image.'; return; }
    msg.textContent = session ? 'Removing the background…' : 'Loading the AI model (about 5 MB, only the first time)…';
    try {
      var bmp = await createImageBitmap(file);
      var s = await getSession();
      msg.textContent = 'Removing the background…';
      await new Promise(function (r) { setTimeout(r, 30); });
      var input = new window.ort.Tensor('float32', preprocess(bmp), [1, 3, SIZE, SIZE]);
      var feeds = {}; feeds[s.inputNames[0]] = input;
      var out = await s.run(feeds);
      var pred = out[s.outputNames[0]].data;
      var wh = fitSize(bmp.width, bmp.height), W = wh[0], H = wh[1];
      var cut = document.createElement('canvas'); cut.width = W; cut.height = H;
      var cx = cut.getContext('2d'); cx.imageSmoothingQuality = 'high';
      cx.drawImage(bmp, 0, 0, W, H);
      cx.globalCompositeOperation = 'destination-in';
      cx.drawImage(maskCanvas(pred), 0, 0, W, H);
      cx.globalCompositeOperation = 'source-over';
      cutCanvas = cut; current = { name: file.name, w: W, h: H };
      await render();
      msg.textContent = 'Done. Choose a background, then download.' + (W < bmp.width ? ' Large photos are scaled to ' + MAX_SIDE + ' px on the longest side.' : '');
      go.hidden = false;
    } catch (e) {
      console.error(e);
      msg.textContent = /script|fetch|wasm|network/i.test(String(e && e.message)) ? 'The AI model couldn’t be loaded. Check your connection, turn off any content blocker for this site, and try again.' : 'This image couldn’t be processed. Try a JPG or PNG under 20 MB.';
    }
  }

  function bgChoice() { var r = document.querySelector('input[name="bg-bg"]:checked'); return r ? r.value : 'none'; }

  function compose() {
    var c = document.createElement('canvas'); c.width = cutCanvas.width; c.height = cutCanvas.height;
    var x = c.getContext('2d'), b = bgChoice();
    if (b !== 'none') { x.fillStyle = b === 'custom' ? $('bg-color').value : b; x.fillRect(0, 0, c.width, c.height); }
    x.drawImage(cutCanvas, 0, 0);
    return c;
  }

  async function render() {
    if (!cutCanvas) return;
    var c = compose(), b = bgChoice(), png = b === 'none';
    var blob = await new Promise(function (r) { c.toBlob(r, png ? 'image/png' : 'image/jpeg', 0.92); });
    if (outUrl) URL.revokeObjectURL(outUrl);
    outUrl = URL.createObjectURL(blob);
    var img = $('bg-preview'); img.src = outUrl; img.className = png ? 'bg-prev checker' : 'bg-prev';
    var a = $('bg-dl'); a.href = outUrl; a.download = (current.name.replace(/\.[^.]+$/, '') || 'image') + (png ? '-no-bg.png' : '-new-bg.jpg');
    a.textContent = 'Download ' + (png ? 'PNG (transparent)' : 'JPG');
    $('bg-size').textContent = current.w + ' × ' + current.h + ' px · ' + (blob.size / 1024 < 1024 ? (blob.size / 1024).toFixed(0) + ' KB' : (blob.size / 1048576).toFixed(1) + ' MB');
  }

  var input = $('bg-file');
  input.addEventListener('change', function () { if (input.files[0]) run(input.files[0]); });
  var drop = input.closest('.drop');
  ['dragover', 'dragenter'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('over'); }); });
  ['dragleave', 'drop'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('over'); }); });
  drop.addEventListener('drop', function (e) { var f = e.dataTransfer && e.dataTransfer.files[0]; if (f) run(f); });
  document.addEventListener('paste', function (e) { var it = [].slice.call((e.clipboardData || {}).items || []).find(function (i) { return /^image\//.test(i.type); }); if (it) run(it.getAsFile()); });
  document.querySelectorAll('input[name="bg-bg"]').forEach(function (r) { r.addEventListener('change', render); });
  $('bg-color').addEventListener('input', function () { var c = document.querySelector('input[name="bg-bg"][value="custom"]'); c.checked = true; render(); });
  // warm up the model while the visitor picks a file
  input.addEventListener('click', function () { getSession().catch(function () {}); }, { once: true });
  window.__stBgTest = { preprocess: preprocess, maskCanvas: maskCanvas };
})();
