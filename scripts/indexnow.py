"""Tell Bing (and other IndexNow engines) about new or changed URLs.

Usage: python3 scripts/indexnow.py [--all] [BASE_REF]
Without --all, submits only URLs that are new in docs/sitemap.xml compared
with BASE_REF (default HEAD~1). The key file lives in static/<key>.txt.
"""
import glob, json, os, re, subprocess, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = "www.smarttoolsy.tech"
key_file = [f for f in glob.glob(os.path.join(ROOT, "static", "*.txt")) if re.fullmatch(r"[0-9a-f]{32}\.txt", os.path.basename(f))][0]
KEY = open(key_file).read().strip()


def urls(xml):
    return set(re.findall(r"<loc>(.*?)</loc>", xml))


now = urls(open(os.path.join(ROOT, "docs", "sitemap.xml"), encoding="utf-8").read())
args = [a for a in sys.argv[1:] if a != "--all"]
if "--all" in sys.argv:
    todo = now
else:
    base = args[0] if args else "HEAD~1"
    try:
        old = subprocess.run(["git", "show", f"{base}:docs/sitemap.xml"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        old = ""
    todo = now - urls(old)
if not todo:
    print("No new URLs to submit."); sys.exit(0)

# Wait until the deploy with the key file is live.
key_url = f"https://{HOST}/{KEY}.txt"
for _ in range(30):
    try:
        if urllib.request.urlopen(key_url, timeout=20).read().decode().strip() == KEY: break
    except Exception:
        pass
    time.sleep(20)
else:
    print("Key file not live yet; giving up."); sys.exit(1)

todo = sorted(todo)
for i in range(0, len(todo), 10000):
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": key_url, "urlList": todo[i:i + 10000]}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=60) as r:
        print(f"Submitted {len(todo[i:i + 10000])} URLs: HTTP {r.status}")
