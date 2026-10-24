"""Programmatic time and date lookup pages.

Answers depend on the visitor's current time, so every value is computed live
in the browser (tools.js: 'rel-time' and 'until'). Date-based pages also carry
the answer as of the build date so the static HTML is meaningful on its own.
"""
from datetime import date, timedelta
import calendar

MIN_LIST = [1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
HOUR_LIST = list(range(1, 25))
DAY_LIST = [1, 2, 3, 4, 5, 6, 7, 10, 14, 15, 20, 21, 25, 28, 30, 31, 40, 45, 50, 60, 65, 75, 90, 100, 120, 150, 180, 200, 365]
WEEK_LIST = list(range(1, 53))
MONTH_LIST = list(range(1, 25))
YEAR_LIST = list(range(1, 81))

HUBS = {
    "/time-ago": ("Time ago calculator", "What time was it… ago? Hours and minutes ago"),
    "/time-from-now": ("Time from now calculator", "What time will it be in… hours and minutes from now"),
    "/date-from-today": ("Date from today calculator", "Days, weeks and months from today"),
    "/date-ago": ("Date ago calculator", "Days and months ago from today"),
    "/years-ago": ("Years ago calculator", "What year was it… years ago?"),
    "/how-long-until": ("How long until a time", "Countdown to any time of day"),
}


def pl(n, w):
    return f"{n} {w}{'' if n == 1 else 's'}"


def add_months(d, n):
    m = d.month - 1 + n
    y = d.year + m // 12
    m = m % 12 + 1
    return date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def mk_slug(slug_t, n, unit):
    s = slug_t.format(n=n)
    return s.replace(f"-{unit}s-", f"-{unit}-") if n == 1 else s


def fmt_date(d):
    return d.strftime("%A, %B ") + str(d.day) + d.strftime(", %Y")


FAMILIES = [
    # key, hub, unit, direction, numbers, slug, question
    ("minutes-ago", "/time-ago", "minute", -1, MIN_LIST, "{n}-minutes-ago", "What time was it {N} ago?"),
    ("hours-ago", "/time-ago", "hour", -1, HOUR_LIST, "{n}-hours-ago", "What time was it {N} ago?"),
    ("minutes-from-now", "/time-from-now", "minute", 1, MIN_LIST, "{n}-minutes-from-now", "What time will it be {N} from now?"),
    ("hours-from-now", "/time-from-now", "hour", 1, HOUR_LIST, "{n}-hours-from-now", "What time will it be {N} from now?"),
    ("days-from-today", "/date-from-today", "day", 1, DAY_LIST, "{n}-days-from-today", "What is {N} from today?"),
    ("weeks-from-today", "/date-from-today", "week", 1, WEEK_LIST, "{n}-weeks-from-today", "What is {N} from today?"),
    ("months-from-today", "/date-from-today", "month", 1, MONTH_LIST, "{n}-months-from-today", "What is {N} from today?"),
    ("days-ago", "/date-ago", "day", -1, DAY_LIST, "{n}-days-ago", "What was the date {N} ago?"),
    ("months-ago", "/date-ago", "month", -1, MONTH_LIST, "{n}-months-ago", "What was the date {N} ago?"),
    ("years-ago", "/years-ago", "year", -1, YEAR_LIST, "{n}-years-ago", "What year was it {N} ago?"),
]

UNIT_NOTE = {
    "minute": "The answer uses the clock on your device, in your own time zone, and updates every second. If the result crosses midnight, the date is shown as well.",
    "hour": "The answer uses the clock on your device, in your own time zone, and updates every second. If the result crosses midnight, the date changes too. Daylight saving time changes are handled by your device’s clock, so on the night the clocks change, an “hour ago” is measured in real elapsed time.",
    "day": "Every calendar day counts, including weekends and public holidays. Today is day zero, so 1 day from today is tomorrow. If you need working days only, the business-day count below excludes Saturdays and Sundays (but not holidays, which vary by country and employer).",
    "week": "One week is exactly 7 days, so the result always falls on the same weekday as today. Weeks are popular for planning pregnancies, school terms, notice periods and training programs.",
    "month": "Months have different lengths, so the result keeps the same day of the month where possible. If that day doesn’t exist in the target month, such as the 31st in a 30-day month or the 29th to 31st in February, the last day of that month is used instead. This matches how most banks, billing systems and lawyers count months.",
    "year": "The year is simply this year minus the number of years. The full date shows the same month and day in that year; for February 29 in a non-leap year, February 28 is used.",
}


def rel_page(fam, n, today):
    key, hub, unit, sign, nums, slug_t, q = fam
    N = pl(n, unit)
    slug = mk_slug(slug_t, n, unit)
    path = f"{hub}/{slug}"
    h1 = q.format(N=N)
    static_ans, static_sub, ex_rows = "—", "", ""
    if unit in ("day", "week", "month", "year"):
        if unit == "day": tgt = today + timedelta(days=sign * n)
        elif unit == "week": tgt = today + timedelta(days=sign * 7 * n)
        elif unit == "month": tgt = add_months(today, sign * n)
        else:
            y = today.year - n
            tgt = date(y, today.month, min(today.day, calendar.monthrange(y, today.month)[1]))
        static_ans = str(tgt.year) if unit == "year" else fmt_date(tgt)
        static_sub = f"Calculated from {fmt_date(today)}."
        diff = abs((tgt - today).days)
        ex_rows = f"<p>For example, counted from {fmt_date(today)}, {N} {'from today' if sign > 0 else 'ago'} {'is' if sign > 0 else 'was'} {fmt_date(tgt)}, {pl(diff, 'day')} {'later' if sign > 0 else 'earlier'}.</p>"
    near = [k for k in nums if k != n]
    near = sorted(near, key=lambda k: abs(k - n))[:8]
    near_links = "".join(f'<li><a href="{hub}/{mk_slug(slug_t, k, unit)}">{q.format(N=pl(k, unit)).rstrip("?")}</a></li>' for k in sorted(near))
    dir_word = "from now" if sign > 0 and unit in ("minute", "hour") else ("from today" if sign > 0 else "ago")
    body = f"""
<div class="result answer" data-rel-unit="{unit}" data-rel-n="{n}" data-rel-dir="{sign}">
<p class="lbl" style="margin:0 0 4px">{N} {dir_word}</p>
<p class="big" id="rt-ans">{static_ans}</p>
<p id="rt-sub">{static_sub}</p>
</div>
<section class="panel mini" aria-label="Details">
<h2>Details</h2>
<table class="breakdown"><tbody id="rt-details"></tbody></table>
</section>
<section class="panel mini" aria-label="Calculator">
<h2>Try a different amount</h2>
<div class="row">
 <div class="field"><label for="rc-n">Amount</label><input id="rc-n" type="number" min="0" value="{n}"></div>
 <div class="field"><label for="rc-u">Unit</label><select id="rc-u">{''.join(f'<option value="{u}"{" selected" if u == unit else ""}>{u.capitalize()}s</option>' for u in ("minute", "hour", "day", "week", "month", "year"))}</select></div>
 <div class="field"><label for="rc-d">Direction</label><select id="rc-d"><option value="1"{" selected" if sign > 0 else ""}>From now</option><option value="-1"{" selected" if sign < 0 else ""}>Ago</option></select></div>
</div>
<p id="rc-out" class="big" style="font-size:1.25rem" aria-live="polite"></p>
</section>
<article class="article">
<h2>How this is calculated</h2>
<p>{UNIT_NOTE[unit]}</p>
{ex_rows}
<h2>Nearby</h2>
<ul>{near_links}</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Does this use my time zone?</summary><p>Yes. Everything is calculated from the date and time on your own device, so the answer is correct wherever you are.</p></details>
<details><summary>How many {unit}s is that in other units?</summary><p>{rel_conv(unit, n)}</p></details>
</div>
<p><a href="{hub}">More {HUBS[hub][0].lower()}s</a></p>
</article>
"""
    title = f"{h1.rstrip('?')} – {'Live ' if unit in ('minute', 'hour') else ''}Answer"
    if unit in ("day", "week", "month"):
        title = f"{h1.rstrip('?')}? – Date Calculator"
    if unit == "year":
        title = f"What Year Was It {pl(n, 'Year').title()} Ago? – Years Ago Calculator"
    desc = {
        "minute": f"See exactly what time it {'was' if sign < 0 else 'will be'} {N} {dir_word}, calculated live from your device’s clock and time zone.",
        "hour": f"See exactly what time it {'was' if sign < 0 else 'will be'} {N} {dir_word}, with the date if it crosses midnight. Calculated live in your time zone.",
        "day": f"Find the date {N} {dir_word}, with the day of the week, week number and business days. Updates automatically every day.",
        "week": f"Find the date {N} {dir_word} and its day of the week. Includes day count and business days, updated daily.",
        "month": f"Find the date {N} {dir_word}, handling short months correctly. Shows the weekday and total days, updated daily.",
        "year": f"Find what year it was {N} ago and the exact date, plus how many days that is. Updated automatically.",
    }[unit]
    return dict(path=path, title=title, desc=desc, h1=h1, lede="Live answer based on your device’s current date and time.",
                crumbs=[("Home", "/"), (HUBS[hub][0], hub), (h1.rstrip("?"), path)], tool="rel-time", body=body,
                related=[(q.format(N=pl(k, unit)).rstrip("?"), f"{hub}/{mk_slug(slug_t, k, unit)}") for k in sorted(near)[:6]] + [(HUBS[hub][0], hub), ("Date difference calculator", "/date-difference-calculator")])


def rel_conv(unit, n):
    if unit == "minute": return f"{pl(n, 'minute')} is {n * 60:,} seconds" + (f", or {n / 60:g} hours." if n % 60 == 0 else f", or {n / 60:.2f} hours.")
    if unit == "hour": return f"{pl(n, 'hour')} is {n * 60:,} minutes, or {n * 3600:,} seconds."
    if unit == "day": return f"{pl(n, 'day')} is {n * 24:,} hours, or about {n / 7:.1f} weeks."
    if unit == "week": return f"{pl(n, 'week')} is {n * 7} days, or {n * 168:,} hours."
    if unit == "month": return f"{pl(n, 'month')} is about {n * 30.44:.0f} days on average, or {n / 12:.2f} years."
    return f"{pl(n, 'year')} is {n * 12} months, or about {n * 365.25:,.0f} days including leap years."


def until_times():
    out = []
    for h in range(24):
        for m in (0, 15, 30, 45):
            out.append((h, m))
    return out


def tlabel(h, m):
    ap = "AM" if h < 12 else "PM"
    hh = h % 12 or 12
    return f"{hh}:{m:02d} {ap}"


def tslug(h, m):
    ap = "am" if h < 12 else "pm"
    return f"{h % 12 or 12}-{m:02d}-{ap}"


def until_page(h, m):
    L = tlabel(h, m)
    path = f"/how-long-until/{tslug(h, m)}"
    times = until_times()
    i = times.index((h, m))
    near = [times[(i + k) % len(times)] for k in (-4, -3, -2, -1, 1, 2, 3, 4)]
    near_links = "".join(f'<li><a href="/how-long-until/{tslug(*t)}">How long until {tlabel(*t)}</a></li>' for t in near)
    h24 = f"{h:02d}:{m:02d}"
    body = f"""
<div class="result answer" data-until-h="{h}" data-until-m="{m}">
<p class="lbl" style="margin:0 0 4px">Time left until {L}</p>
<p class="big" id="ut-ans">—</p>
<p id="ut-sub"></p>
</div>
<section class="panel mini" aria-label="Details">
<h2>Details</h2>
<table class="breakdown"><tbody id="ut-details"></tbody></table>
</section>
<section class="panel mini" aria-label="Countdown to another time">
<h2>Count down to another time</h2>
<div class="row"><div class="field"><label for="uc-t">Time</label><input id="uc-t" type="time" value="{h24}"></div></div>
<p id="uc-out" class="big" style="font-size:1.25rem" aria-live="polite"></p>
</section>
<article class="article">
<h2>How the countdown works</h2>
<p>The countdown uses the clock on your device and updates every second. If {L} has already passed today, it counts down to {L} tomorrow. {L} is {h24} in 24-hour (military) time{', which is noon' if (h, m) == (12, 0) else ', which is midnight' if (h, m) == (0, 0) else ''}.</p>
<p>Handy for timing the end of a work shift, a class, a meeting, a cooking timer or a store opening. Keep the page open and the timer keeps running.</p>
<h2>Other times</h2>
<ul>{near_links}</ul>
<p><a href="/how-long-until">All times of day</a> · <a href="/time-from-now">Time from now</a></p>
</article>
"""
    return dict(path=path, title=f"How Long Until {L}? – Live Countdown Timer", desc=f"Live countdown showing exactly how many hours, minutes and seconds until {L}, in your time zone. Counts to tomorrow if {L} has passed.",
                h1=f"How long until {L}?", lede="Live countdown in your own time zone.",
                crumbs=[("Home", "/"), ("How long until", "/how-long-until"), (L, path)], tool="until", body=body,
                related=[(f"Until {tlabel(*t)}", f"/how-long-until/{tslug(*t)}") for t in near[2:6]] + [("Time from now", "/time-from-now"), ("Time ago", "/time-ago")])


def hub_page(hub, today):
    name, lede = HUBS[hub]
    if hub == "/how-long-until":
        groups = {"Morning": [], "Afternoon": [], "Evening and night": []}
        for h, m in until_times():
            g = "Morning" if 5 <= h < 12 else "Afternoon" if 12 <= h < 17 else "Evening and night"
            groups[g].append(f'<a href="/how-long-until/{tslug(h, m)}">{tlabel(h, m)}</a>')
        blocks = "".join(f"<h2>{g}</h2><p class='yr-grid'>{''.join(v)}</p>" for g, v in groups.items())
        intro = "<p>Pick a time to see a live countdown. If the time has passed today, the countdown runs to the same time tomorrow.</p>"
        calc = ""
    else:
        fams = [f for f in FAMILIES if f[1] == hub]
        blocks = ""
        for key, _, unit, sign, nums, slug_t, q in fams:
            blocks += f"<h2>{unit.capitalize()}s {'ago' if sign < 0 else ('from now' if unit in ('minute', 'hour') else 'from today')}</h2><p class='yr-grid'>" + "".join(
                f'<a href="{hub}/{mk_slug(slug_t, k, unit)}">{pl(k, unit)}</a>' for k in nums) + "</p>"
        intro = f"<p>Choose an amount to see the answer calculated live from your device’s date and time, or use the calculator.</p>"
        u0, s0 = fams[0][2], fams[0][3]
        calc = f"""<section class="panel mini" aria-label="Calculator" data-rel-unit="{u0}" data-rel-n="1" data-rel-dir="{s0}"><h2>Calculator</h2><div class="row">
 <div class="field"><label for="rc-n">Amount</label><input id="rc-n" type="number" min="0" value="1"></div>
 <div class="field"><label for="rc-u">Unit</label><select id="rc-u">{''.join(f'<option value="{u}"{" selected" if u == u0 else ""}>{u.capitalize()}s</option>' for u in ("minute", "hour", "day", "week", "month", "year"))}</select></div>
 <div class="field"><label for="rc-d">Direction</label><select id="rc-d"><option value="1"{" selected" if s0 > 0 else ""}>From now</option><option value="-1"{" selected" if s0 < 0 else ""}>Ago</option></select></div>
</div><p id="rc-out" class="big" style="font-size:1.25rem" aria-live="polite"></p></section>"""
    return dict(path=hub, title=f"{name} – {lede}", desc=f"{lede}. Free, live answers calculated in your own time zone.",
                h1=name, lede=lede, crumbs=[("Home", "/"), (name, hub)], tool="rel-hub" if calc else "",
                body=calc + f"<article class='article' style='margin-top:{0 if not calc else 24}px'>{intro}{blocks}</article>",
                related=[(HUBS[k][0], k) for k in HUBS if k != hub])


def all_pages(today=None):
    today = today or date.today()
    pages = [hub_page(h, today) for h in HUBS]
    for fam in FAMILIES:
        pages += [rel_page(fam, n, today) for n in fam[4]]
    pages += [until_page(h, m) for h, m in until_times()]
    return pages
