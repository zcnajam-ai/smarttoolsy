// Renders share images described in a spec file (see src/og.py). Usage: node src/og_render.js spec.json
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const LOGO = '<svg viewBox="0 0 32 32" width="52" height="52"><rect width="32" height="32" rx="8" fill="#2F5BEA"/><path d="M9 21.5c1.4 1.3 3.3 2 5.4 2 3 0 5-1.5 5-3.8 0-2.2-1.6-3.1-4.4-3.8-2.2-.5-3-1-3-2 0-1 .9-1.6 2.4-1.6 1.4 0 2.6.5 3.6 1.3" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><circle cx="23.5" cy="9" r="3" fill="#F2B33D"/></svg>';
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const tint = (hex, a) => hex + Math.round(a * 255).toString(16).padStart(2, '0');
const icon = (svg, size) => svg.replace('<svg ', `<svg width="${size}" height="${size}" `);

function page(it) {
  const c = it.color || '#2F5BEA';
  const chips = (it.chips || []).map((x) => `<span class="chip">${esc(x)}</span>`).join('');
  let main;
  if (it.kind === 'home') {
    main = `<div class="txt"><h1 class="fit" style="font-size:72px;max-height:170px">${esc(it.title)}</h1><p class="sub">${esc(it.sub)}</p>
      <div class="tiles">${it.tiles.map((t) => `<span class="tile sm" style="background:${tint(t.color, .13)};color:${t.color}">${icon(t.svg, 46)}</span>`).join('')}</div></div>`;
  } else if (it.kind === 'tool') {
    main = `<span class="tile" style="background:${tint(c, .13)};color:${c}">${icon(it.svg, 96)}</span>
      <div class="txt"><h1 class="fit" style="font-size:88px;max-height:176px">${esc(it.title)}</h1><p class="sub">${esc(it.sub)}</p><div class="chips">${chips}</div></div>`;
  } else {
    main = `<div class="txt"><span class="label" style="background:${tint(c, .13)};color:${c}">GUIDE</span><h1 class="fit guide" style="font-size:70px">${esc(it.title)}</h1><div class="chips">${chips}</div></div>`;
  }
  const deco = it.svg ? `<div class="deco" style="color:${c}">${icon(it.svg, 520)}</div>` : '';
  return `<!doctype html><html><head><meta charset="utf-8"><style>
  *{box-sizing:border-box;margin:0}
  body{width:1200px;height:630px;overflow:hidden;font-family:Inter,"DejaVu Sans",sans-serif;color:#1B2540;
    background:radial-gradient(circle at 92% 18%, ${tint(c, .16)} 0, transparent 46%), linear-gradient(135deg,#FFFFFF 0%,#F1F4FA 100%);position:relative}
  .bar{position:absolute;left:0;top:0;bottom:0;width:14px;background:${c}}
  .deco{position:absolute;right:-90px;bottom:-110px;opacity:.09;transform:rotate(-10deg)}
  .top{position:absolute;left:84px;top:62px;display:flex;align-items:center;gap:16px;font-weight:800;font-size:36px;letter-spacing:-.01em}
  .main{position:absolute;left:84px;right:84px;top:150px;bottom:118px;display:flex;align-items:center;gap:44px}
  .tile{flex:none;width:168px;height:168px;border-radius:40px;display:grid;place-items:center}
  .tile svg{fill:currentColor}
  .tile.sm{width:84px;height:84px;border-radius:22px}
  .tiles{display:flex;gap:16px;margin-top:34px}
  .txt{min-width:0;flex:1}
  h1{font-family:"Inter Display",Inter,sans-serif;font-weight:800;line-height:1.08;letter-spacing:-.025em;max-height:300px;overflow:hidden}
  h1.guide{line-height:1.08;max-height:310px}
  .sub{font-size:32px;line-height:1.3;color:#56617A;margin-top:14px;max-width:880px}
  .label{display:inline-block;font-weight:800;font-size:24px;letter-spacing:.12em;padding:8px 18px;border-radius:999px;margin-bottom:22px}
  .chips{display:flex;gap:12px;margin-top:22px;flex-wrap:wrap}
  .chip{font-size:26px;font-weight:600;padding:9px 20px;border-radius:999px;background:#fff;border:2px solid #D9DFEA;color:#33405E}
  .foot{position:absolute;left:84px;right:84px;bottom:54px;display:flex;justify-content:flex-end;font-size:30px;font-weight:700;color:#56617A}
  .foot b{color:${c}}
  </style></head><body><div class="bar"></div>${deco}
  <div class="top">${LOGO}<span>SmartToolsy</span></div>
  <div class="main">${main}</div>
  <div class="foot"><span>smarttoolsy<b>.tech</b></span></div></body></html>`;
}

(async () => {
  const browser = await chromium.launch();
  const pg = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  for (const it of spec.items) {
    await pg.setContent(page(it), { waitUntil: 'load' });
    // shrink the headline until it fits its box
    await pg.evaluate(() => {
      const h = document.querySelector('.fit'); if (!h) return;
      let s = parseFloat(h.style.fontSize);
      const max = parseFloat(getComputedStyle(h).maxHeight);
      while ((h.scrollHeight > max || h.scrollWidth > h.clientWidth + 2) && s > 40) { s -= 2; h.style.fontSize = s + 'px'; }
    });
    await pg.screenshot({ path: path.join(spec.out, it.file), type: 'jpeg', quality: 86 });
  }
  await browser.close();
})();
