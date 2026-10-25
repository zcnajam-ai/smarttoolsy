"""Generate social share images (1200 x 630) into static/og/.

Run after adding a tool or guide:   python3 src/og.py
Needs Node with Playwright (renders src/og_render.js). Existing images are
kept unless you pass --all. build.py falls back to /og/default.jpg for any
page without its own image.
"""
import json, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tools_a import TOOLS_A
from tools_b import TOOLS_B
from tools_c import TOOLS_C
from tools_d import TOOLS_D
from tools_e import TOOLS_E
from tools_f import TOOLS_F
from tools_g import TOOLS_G
from articles import ARTICLES
from icons import tool_svg, cat_svg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "static", "og")
TOOLS = TOOLS_A + TOOLS_B + TOOLS_C + TOOLS_D + TOOLS_E + TOOLS_F + TOOLS_G
BY = {t["slug"]: t for t in TOOLS}
COLOR = {"pdf": "#DC3545", "seo": "#0B7A5A", "calc": "#2F5BEA", "home": "#D9480F", "text": "#7048E8",
         "image": "#0F9D58", "convert": "#0C8599", "generate": "#C2255C", "dev": "#495A78"}
CAT_ORDER = ["pdf", "seo", "calc", "home", "text", "image", "convert", "generate", "dev"]


def specs():
    out = [{"file": "default.jpg", "kind": "home", "title": "Free tools for everyday jobs",
            "sub": "PDF, SEO, calculators, converters and more. No sign-up, nothing to install.",
            "tiles": [{"svg": cat_svg(c), "color": COLOR[c]} for c in CAT_ORDER]}]
    for t in TOOLS:
        seo = t["cat"] == "seo"
        out.append({"file": t["slug"] + ".jpg", "kind": "tool", "title": t["name"], "sub": t["short"],
                    "svg": tool_svg(t["slug"]), "color": COLOR[t["cat"]],
                    "chips": ["Free", "No sign-up", "Instant report"] if seo else ["Free", "No sign-up", "Private: runs in your browser"]})
    for a in ARTICLES:
        t = BY[a["tools"][0]]
        out.append({"file": "blog-" + a["slug"] + ".jpg", "kind": "guide", "title": a["title"], "sub": "",
                    "svg": tool_svg(t["slug"]), "color": COLOR[t["cat"]], "chips": ["Free guide", "Step by step"]})
    return out


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    items = specs()
    if "--all" not in sys.argv:
        items = [s for s in items if not os.path.exists(os.path.join(OUT, s["file"]))]
    if not items:
        print("All share images already exist.")
        sys.exit(0)
    spec_path = os.path.join(OUT, ".spec.json")
    with open(spec_path, "w", encoding="utf-8") as f:
        json.dump({"out": OUT, "items": items}, f)
    try:
        subprocess.run(["node", os.path.join(ROOT, "src", "og_render.js"), spec_path], check=True)
    finally:
        os.remove(spec_path)
    print(f"Rendered {len(items)} share images into static/og/")
