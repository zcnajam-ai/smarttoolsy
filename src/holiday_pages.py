"""'How many days until <holiday>?' countdown pages.

Each page counts down live in the browser (tools.js: 'days-until'), using the
holiday's date rule, so it rolls over to next year by itself. The static HTML
also carries the answer as of the build date and a table of upcoming dates.

Rules use JavaScript weekday numbers (0 = Sunday ... 6 = Saturday):
  ("fixed", month, day)
  ("nth", month, weekday, n)      n-th weekday of the month (n = -1: last)
  ("easter",)
Any rule can carry a day offset as an extra last item via OFFSET below.
"""
import json
from datetime import date, timedelta

HUB = "/days-until"

# slug, name, rule, offset in days, short description
HOLIDAYS = [
    ("christmas", "Christmas", ("fixed", 12, 25), 0,
     "Christmas Day is on December 25 every year. It is a federal holiday in the United States, so banks, post offices and most offices are closed, and it is the biggest gift-giving day of the year."),
    ("christmas-eve", "Christmas Eve", ("fixed", 12, 24), 0,
     "Christmas Eve is December 24, the night before Christmas. Many families open one present, go to a candlelight service or leave cookies out for Santa. Stores usually close early."),
    ("thanksgiving", "Thanksgiving", ("nth", 11, 4, 4), 0,
     "Thanksgiving in the United States is the fourth Thursday of November, so the date moves between November 22 and 28. It is a federal holiday known for turkey dinners, family travel, parades and football."),
    ("black-friday", "Black Friday", ("nth", 11, 4, 4), 1,
     "Black Friday is the day after Thanksgiving and the traditional start of the holiday shopping season. Stores open early with big discounts, and many online deals start earlier in the week."),
    ("cyber-monday", "Cyber Monday", ("nth", 11, 4, 4), 4,
     "Cyber Monday is the Monday after Thanksgiving, when online stores run their biggest sales of the year. It falls four days after Thanksgiving and three days after Black Friday."),
    ("new-years-eve", "New Year's Eve", ("fixed", 12, 31), 0,
     "New Year's Eve is December 31, the last day of the year. The countdown to midnight is celebrated with fireworks, parties and the ball drop in Times Square, New York."),
    ("new-years", "New Year's Day", ("fixed", 1, 1), 0,
     "New Year's Day is January 1, the first day of the new year and a federal holiday in the United States. It is a popular day to start resolutions."),
    ("halloween", "Halloween", ("fixed", 10, 31), 0,
     "Halloween is October 31 every year. Kids go trick-or-treating in costumes, houses are decorated with pumpkins, and many towns hold parties and haunted houses."),
    ("veterans-day", "Veterans Day", ("fixed", 11, 11), 0,
     "Veterans Day is November 11, honoring everyone who has served in the U.S. armed forces. It is a federal holiday; when it falls on a weekend, the observed day off moves to the nearest weekday."),
    ("valentines-day", "Valentine's Day", ("fixed", 2, 14), 0,
     "Valentine's Day is February 14, the day for cards, flowers, chocolates and dinner dates. It is not a public holiday, so schools and offices stay open."),
    ("st-patricks-day", "St. Patrick's Day", ("fixed", 3, 17), 0,
     "St. Patrick's Day is March 17, celebrating Irish culture with parades, green clothes and shamrocks. Chicago even dyes its river green for the day."),
    ("easter", "Easter", ("easter",), 0,
     "Easter Sunday is the first Sunday after the first full moon on or after March 21, so it falls between March 22 and April 25. The date is set with the same church calculation used for centuries."),
    ("mothers-day", "Mother's Day", ("nth", 5, 0, 2), 0,
     "Mother's Day in the United States is the second Sunday of May. It is one of the busiest days of the year for restaurants, florists and phone calls home."),
    ("memorial-day", "Memorial Day", ("nth", 5, 1, -1), 0,
     "Memorial Day is the last Monday of May, a federal holiday honoring service members who died in military service. It is also seen as the unofficial start of summer."),
    ("fathers-day", "Father's Day", ("nth", 6, 0, 3), 0,
     "Father's Day in the United States is the third Sunday of June, a day to celebrate dads, grandfathers and father figures."),
    ("juneteenth", "Juneteenth", ("fixed", 6, 19), 0,
     "Juneteenth, June 19, marks the end of slavery in the United States and has been a federal holiday since 2021. When it falls on a weekend, the day off moves to the nearest weekday."),
    ("4th-of-july", "4th of July", ("fixed", 7, 4), 0,
     "Independence Day, the 4th of July, celebrates the adoption of the Declaration of Independence in 1776. It is a federal holiday with fireworks, barbecues and parades across the country."),
    ("labor-day", "Labor Day", ("nth", 9, 1, 1), 0,
     "Labor Day is the first Monday of September, a federal holiday honoring American workers. For many families it marks the end of summer and the start of the school year."),
    ("columbus-day", "Columbus Day", ("nth", 10, 1, 2), 0,
     "Columbus Day, also observed as Indigenous Peoples' Day in many states and cities, is the second Monday of October. It is a federal holiday, so banks and post offices close."),
    ("mlk-day", "Martin Luther King Jr. Day", ("nth", 1, 1, 3), 0,
     "Martin Luther King Jr. Day is the third Monday of January, honoring the civil rights leader's birthday (January 15). It is a federal holiday and a national day of service."),
    ("presidents-day", "Presidents' Day", ("nth", 2, 1, 3), 0,
     "Presidents' Day, officially Washington's Birthday, is the third Monday of February. It is a federal holiday known for big retail sales."),
]

RULE_TEXT = {
    "fixed": lambda r: f"{date(2000, r[1], r[2]).strftime('%B')} {r[2]} every year",
    "nth": lambda r: ("the last" if r[3] == -1 else f"the {['first', 'second', 'third', 'fourth', 'fifth'][r[3] - 1]}")
    + f" {['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][r[2]]} of {date(2000, r[1], 1).strftime('%B')}",
    "easter": lambda r: "the first Sunday after the first full moon on or after March 21 (between March 22 and April 25)",
}


def easter(y):
    a = y % 19; b = y // 100; c = y % 100; d = b // 4; e = b % 4
    f = (b + 8) // 25; g = (b - f + 1) // 3; h = (19 * a + b - d - g + 15) % 30
    i = c // 4; k = c % 4; l = (32 + 2 * e + 2 * i - h - k) % 7; m = (a + 11 * h + 22 * l) // 451
    mo = (h + l - 7 * m + 114) // 31; dy = (h + l - 7 * m + 114) % 31 + 1
    return date(y, mo, dy)


def on_year(rule, off, y):
    if rule[0] == "fixed":
        d = date(y, rule[1], rule[2])
    elif rule[0] == "easter":
        d = easter(y)
    else:
        _, mo, wd, n = rule
        py_wd = (wd - 1) % 7  # JS Sunday=0 -> Python Monday=0
        if n == -1:
            nxt = date(y + (mo == 12), mo % 12 + 1, 1)
            d = nxt - timedelta(days=1)
            while d.weekday() != py_wd: d -= timedelta(days=1)
        else:
            d = date(y, mo, 1)
            while d.weekday() != py_wd: d += timedelta(days=1)
            d += timedelta(days=7 * (n - 1))
    return d + timedelta(days=off)


def next_on(rule, off, today):
    d = on_year(rule, off, today.year)
    return d if d >= today else on_year(rule, off, today.year + 1)


def fmt(d):
    return d.strftime("%A, %B ") + str(d.day) + d.strftime(", %Y")


def pl(n, w):
    return f"{n:,} {w}{'' if n == 1 else 's'}"


def holiday_page(hol, today):
    slug, name, rule, off, blurb = hol
    path = f"{HUB}/{slug}"
    nd = next_on(rule, off, today)
    days = (nd - today).days
    Name = name[0].upper() + name[1:]
    rule_txt = RULE_TEXT[rule[0]](rule)
    if off:
        rule_txt = f"{pl(off, 'day')} after Thanksgiving, which is {rule_txt}"
    data = json.dumps({"r": list(rule), "o": off})
    years = [on_year(rule, off, y) for y in range(nd.year, nd.year + 6)]
    rows = "".join(f"<tr><td>{d.year}</td><td>{d.strftime('%A')}</td><td>{d.strftime('%B')} {d.day}</td></tr>" for d in years)
    others = sorted((h for h in HOLIDAYS if h[0] != slug), key=lambda h: next_on(h[2], h[3], today))[:8]
    other_links = "".join(f'<li><a href="{HUB}/{h[0]}">Days until {h[1]}</a> <small>({fmt(next_on(h[2], h[3], today))})</small></li>' for h in others)
    static = "It's today!" if days == 0 else pl(days, "day")
    body = f"""
<div class="result answer" data-hol='{data}' data-hol-name="{name}">
<p class="lbl" style="margin:0 0 4px">Days until {name}</p>
<p class="big" id="du-ans">{static}</p>
<p id="du-sub">{Name} {nd.year} is on {fmt(nd)}. Counted from {fmt(today)}.</p>
</div>
<section class="panel mini" aria-label="Countdown">
<h2>Live countdown</h2>
<p class="big" style="font-size:1.35rem" id="du-clock" aria-live="off">—</p>
<table class="breakdown"><tbody id="du-details"></tbody></table>
</section>
<article class="article">
<h2>When is {name}?</h2>
<p>{blurb}</p>
<p>{Name} is on {rule_txt}. The next one is <strong>{fmt(nd)}</strong>.</p>
<h2>{Name} dates for the next few years</h2>
<table class="breakdown"><thead><tr><th>Year</th><th>Day</th><th>Date</th></tr></thead><tbody>{rows}</tbody></table>
<h2>How the countdown works</h2>
<p>The countdown runs on your device's clock, so it is correct in your own time zone and updates every second. It counts to midnight at the start of {name}. Once the day has passed, it automatically switches to next year's date.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What day is {name} {nd.year}?</summary><p>{Name} {nd.year} is on {fmt(nd)}.</p></details>
<details><summary>How many weeks until {name}?</summary><p>Divide the number of days by 7. The live box above shows the exact weeks and days left, along with the number of weekdays (Monday to Friday) if you are counting working or school days.</p></details>
<details><summary>Is {name} the same date every year?</summary><p>{'Yes. ' if rule[0] == 'fixed' and not off else 'No. '}{Name} is on {rule_txt}.</p></details>
</div>
<h2>Coming up next</h2>
<ul>{other_links}</ul>
<p><a href="{HUB}">All holiday countdowns</a> · <a href="/date-difference-calculator">Days between two dates</a></p>
</article>
"""
    title = f"How Many Days Until {Name} {nd.year}? – Live Countdown"
    desc = f"Live countdown to {name} {nd.year} ({nd.strftime('%A, %B')} {nd.day}): days, hours, minutes and seconds left, plus weeks and weekdays. Updates every second."
    return dict(path=path, title=title, desc=desc, h1=f"How many days until {name}?", lede=f"{Name} {nd.year}: {fmt(nd)}",
                crumbs=[("Home", "/"), ("Days until", HUB), (Name, path)], tool="days-until", body=body,
                related=[(f"Days until {h[1]}", f"{HUB}/{h[0]}") for h in others[:5]] + [("Days until any date", HUB), ("How long until a time", "/how-long-until")])


def hub_page(today):
    items = sorted(HOLIDAYS, key=lambda h: next_on(h[2], h[3], today))
    grid = "".join(
        f'<a href="{HUB}/{h[0]}">{h[1][0].upper() + h[1][1:]}<small>{(next_on(h[2], h[3], today) - today).days} days · {next_on(h[2], h[3], today).strftime("%b")} {next_on(h[2], h[3], today).day}</small></a>'
        for h in items)
    body = f"""
<section class="panel mini" aria-label="Days until a date">
<h2>Days until any date</h2>
<p>Birthday, vacation, wedding, due date or deadline: pick the date to see a live countdown.</p>
<div class="row"><div class="field"><label for="du-d">Date</label><input id="du-d" type="date"></div></div>
<p id="du-out" class="big" style="font-size:1.25rem" aria-live="polite"></p>
<table class="breakdown"><tbody id="du-out-details"></tbody></table>
</section>
<article class="article" style="margin-top:24px">
<h2>U.S. holidays, soonest first</h2>
<p>Day counts are as of {fmt(today)}; each page shows a live countdown.</p>
<div class="yr-grid hol-grid">{grid}</div>
<p>Counting down to a time of day instead? See <a href="/how-long-until">how long until a time</a>.</p>
</article>
"""
    return dict(path=HUB, title="Days Until Christmas, Thanksgiving & Any Date – Countdown",
                desc="Free live countdowns to Christmas, Thanksgiving, New Year and every U.S. holiday, plus a days-until calculator for birthdays and any date.",
                h1="Days until…", lede="Live countdowns to holidays and any date you choose.",
                crumbs=[("Home", "/"), ("Days until", HUB)], tool="days-until", body=body,
                related=[("Days until Christmas", f"{HUB}/christmas"), ("Days until Thanksgiving", f"{HUB}/thanksgiving"),
                         ("How long until a time", "/how-long-until"), ("Date from today", "/date-from-today"), ("Date difference calculator", "/date-difference-calculator")])


def all_pages(today=None):
    today = today or date.today()
    return [hub_page(today)] + [holiday_page(h, today) for h in HOLIDAYS]
