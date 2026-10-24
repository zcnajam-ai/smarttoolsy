"""Programmatic age lookup pages.

/how-old-am-i/born-in-YYYY/      "How old am I if I was born in YYYY?"
/what-year-was-i-born/if-im-N/   "What year was I born if I'm N?"

Every page carries values calculated for that specific year or age (age now,
generation, Chinese zodiac, Social Security full retirement age, milestone
years) and a small live calculator. Numbers are computed for the build year
and refreshed in the browser by tools.js, so they stay correct after New Year.
"""
from datetime import date

YEARS = range(1940, 2021)
AGES = range(10, 81)
ZODIAC = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def generation(y):
    # Pew Research Center definitions; Gen Alpha start year is the commonly used 2013.
    if y <= 1927: return ("the Greatest Generation", "1901–1927")
    if y <= 1945: return ("the Silent Generation", "1928–1945")
    if y <= 1964: return ("the Baby Boomers", "1946–1964")
    if y <= 1980: return ("Generation X", "1965–1980")
    if y <= 1996: return ("the Millennials (Generation Y)", "1981–1996")
    if y <= 2012: return ("Generation Z", "1997–2012")
    return ("Generation Alpha", "2013 onward")


def zodiac(y):
    return ZODIAC[(y - 4) % 12], ZODIAC[(y - 5) % 12]


def leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def fra(y):
    """Social Security full retirement age by birth year (SSA table)."""
    if y <= 1937: return (65, 0)
    if y <= 1942: return (65, {1938: 2, 1939: 4, 1940: 6, 1941: 8, 1942: 10}[y])
    if y <= 1954: return (66, 0)
    if y <= 1959: return (66, {1955: 2, 1956: 4, 1957: 6, 1958: 8, 1959: 10}[y])
    return (67, 0)


def fra_text(y):
    a, m = fra(y)
    return f"{a}" + (f" and {m} months" if m else "")


def weekday_jan1(y):
    return date(y, 1, 1).strftime("%A")


def us_grade(age):
    """Typical US grade for a child of this age during most of the school year."""
    g = age - 5
    if g <= 0: return None
    names = {1: "1st", 2: "2nd", 3: "3rd"}
    a = names.get(g, f"{g}th")
    if g > 12: return None
    b = names.get(g - 1, f"{g-1}th") if g > 1 else "kindergarten"
    return f"{b} or {a} grade"


MILESTONES = [
    (16, "Full driver’s license possible in many US states"),
    (18, "Voting age in US elections"),
    (21, "Legal drinking age in the US"),
    (25, "Car rental usually without a young-driver fee"),
    (26, "Coverage on a parent’s health plan ends (Affordable Care Act)"),
    (30, None), (35, "Old enough to be President of the United States"),
    (40, None), (50, None),
    (62, "Earliest age to claim (reduced) Social Security benefits"),
    (65, "Medicare eligibility"),
]


def _plural(n, w):
    return f"{n} {w}{'' if n == 1 else 's'}"


def born_in_page(y, now):
    a_after, a_before = now - y, now - y - 1
    gen, gen_range = generation(y)
    zod, zod_prev = zodiac(y)
    fy, fm = fra(y)
    rows = []
    for age, what in MILESTONES:
        yr = y + age
        verb = "turned" if yr < now else ("turns" if yr == now else "will turn")
        rows.append(f"<tr><td>{age}</td><td>{yr}</td><td>{verb.capitalize()} {age}" + (f". {what}" if what else "") + "</td></tr>")
    ages_table = "".join(f"<tr><td>{yr}</td><td>{yr - y}</td></tr>" for yr in range(max(y, now - 5), now + 6))
    near = [n for n in range(y - 3, y + 4) if n != y and n in YEARS]
    near_links = " · ".join(f'<a href="/how-old-am-i/born-in-{n}">{n}</a>' for n in near)
    body = f"""
<div class="result answer" data-age-year="{y}">
<p class="big"><span class="age-a">{a_after}</span> years old</p>
<p>If you were born in {y}, you are <strong><span class="age-a">{a_after}</span></strong> if you have already had your birthday in <span class="yr-now">{now}</span>, or <strong><span class="age-b">{a_before}</span></strong> if your birthday is still to come this year.</p>
</div>
<section class="panel mini" aria-label="Exact age calculator">
<h2>Get your exact age</h2>
<div class="row">
 <div class="field"><label for="ya-m">Birth month</label><select id="ya-m">{''.join(f'<option value="{i}">{m}</option>' for i, m in enumerate(MONTHS))}</select></div>
 <div class="field"><label for="ya-d">Day</label><select id="ya-d">{''.join(f'<option>{d}</option>' for d in range(1, 32))}</select></div>
</div>
<p id="ya-out" class="big" style="font-size:1.3rem" aria-live="polite"></p>
<p style="margin:0">Need more detail? The <a href="/age-calculator">age calculator</a> shows total days, weeks and months.</p>
</section>
<article class="article">
<h2>Quick facts for people born in {y}</h2>
<table class="breakdown"><tbody>
<tr><td>Age in <span class="yr-now">{now}</span></td><td><span class="age-b">{a_before}</span> or <span class="age-a">{a_after}</span></td></tr>
<tr><td>Generation</td><td>{gen[4:] if gen.startswith('the ') else gen} ({gen_range})</td></tr>
<tr><td>Chinese zodiac</td><td>{zod} (from Lunar New Year)</td></tr>
<tr><td>Leap year</td><td>{'Yes, ' + str(y) + ' had 366 days' if leap(y) else 'No, ' + str(y) + ' had 365 days'}</td></tr>
<tr><td>January 1, {y} fell on</td><td>a {weekday_jan1(y)}</td></tr>
<tr><td>Social Security full retirement age</td><td>{fra_text(y)}</td></tr>
<tr><td>Medicare eligibility (age 65)</td><td>{y + 65}</td></tr>
</tbody></table>

<h2>How the answer is worked out</h2>
<p>Subtract your birth year from the current year: <span class="yr-now">{now}</span> − {y} = <span class="age-a">{a_after}</span>. That is your age once your birthday has passed this year. Until then you are one year younger, <span class="age-b">{a_before}</span>. For example, someone born in March {y} is <span class="age-a">{a_after}</span> from March onward, while someone born in November {y} stays <span class="age-b">{a_before}</span> until their November birthday.</p>

<h2>What generation is {y}?</h2>
<p>People born in {y} belong to {gen}. The Pew Research Center, whose definitions are the most widely used in the US, places this generation from {gen_range.replace('–', ' to ')}. Generation boundaries are conventions rather than strict rules, so you may also see slightly different ranges elsewhere.</p>

<h2>Chinese zodiac for {y}</h2>
<p>{y} is the Year of the {zod}. The Chinese zodiac follows the lunar calendar, and Lunar New Year falls in late January or February. If you were born in January or early February {y}, before that year’s Lunar New Year, your sign is the {zod_prev} instead.</p>

<h2>Retirement and Medicare</h2>
<p>For people born in {y}, the Social Security Administration sets the full retirement age at {fra_text(y)}. You can start reduced benefits as early as 62, which for this birth year was or will be {y + 62}, and Medicare eligibility begins at 65, in {y + 65}. The SSA notes that anyone born on January 1 should use the rules for the previous year.</p>

<h2>Milestones for people born in {y}</h2>
<div style="overflow-x:auto"><table class="sched" style="width:100%;border-collapse:collapse"><thead><tr><th>Age</th><th>Year</th><th>Milestone</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>

<h2>Your age by year</h2>
<p>Age reached on your birthday in each year:</p>
<div style="overflow-x:auto"><table class="sched" style="width:100%;border-collapse:collapse"><thead><tr><th>Year</th><th>Age on birthday</th></tr></thead><tbody>{ages_table}</tbody></table></div>

<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>If I was born in {y}, how old will I be in {now + 10}?</summary><p>You will turn {now + 10 - y} on your birthday in {now + 10}.</p></details>
<details><summary>How old was someone born in {y} in 2000?</summary><p>{'They were not born yet.' if y > 2000 else f'They turned {2000 - y} on their birthday in 2000.'}</p></details>
<details><summary>Is {y} a leap year?</summary><p>{'Yes. ' + str(y) + ' had a February 29, so people born on that date celebrate on February 28 or March 1 in other years.' if leap(y) else 'No. ' + str(y) + ' had 365 days and no February 29.'}</p></details>
</div>
<p>Other birth years: {near_links} · <a href="/how-old-am-i">all years</a></p>
</article>
"""
    return dict(
        path=f"/how-old-am-i/born-in-{y}",
        title=f"How Old Am I If I Was Born in {y}? ({now} Age Calculator)",
        desc=f"Born in {y}? You are {a_before} or {a_after} in {now}, depending on whether your birthday has passed. See your exact age, generation, zodiac and retirement age.",
        h1=f"How old am I if I was born in {y}?",
        lede=f"Your age in {now}, plus the facts and milestones for the {y} birth year.",
        crumbs=[("Home", "/"), ("Age by birth year", "/how-old-am-i"), (str(y), f"/how-old-am-i/born-in-{y}")],
        tool="age-year", body=body,
        related=[(f"Born in {n}", f"/how-old-am-i/born-in-{n}") for n in near[:6]] + [("Age calculator", "/age-calculator"), ("What year was I born?", "/what-year-was-i-born")],
    )


def if_im_page(n, now):
    y_after, y_before = now - n, now - n - 1
    gen_a, _ = generation(y_after)
    gen_b, _ = generation(y_before)
    gens = gen_a if gen_a == gen_b else f"{gen_b} or {gen_a}"
    grade = us_grade(n)
    facts = [f"<tr><td>Born in</td><td><span class='yb-b'>{y_before}</span> or <span class='yb-a'>{y_after}</span></td></tr>",
             f"<tr><td>Generation</td><td>{gens[0].upper() + gens[1:]}</td></tr>",
             f"<tr><td>Chinese zodiac</td><td>{zodiac(y_before)[0]} ({y_before}) or {zodiac(y_after)[0]} ({y_after})</td></tr>"]
    if grade: facts.append(f"<tr><td>Typical US school grade</td><td>{grade}</td></tr>")
    facts.append(f"<tr><td>Days old (approximately)</td><td>{n * 365 + n // 4:,} to {(n + 1) * 365 + (n + 1) // 4 - 1:,}</td></tr>")
    ms = [(a, w) for a, w in MILESTONES if w]
    passed = [f"<li><strong>{a}</strong> ({y_before + a} or {y_after + a}): {w}</li>" for a, w in ms if a <= n]
    coming = [f"<li><strong>{a}</strong> ({y_before + a} or {y_after + a}): {w}</li>" for a, w in ms if a > n]
    fra_note = f"<p>If you were born in {y_after}, your Social Security full retirement age is {fra_text(y_after)}; for {y_before} it is {fra_text(y_before)}.</p>" if n >= 18 else ""
    near = [k for k in range(n - 3, n + 4) if k != n and k in AGES]
    near_links = " · ".join(f'<a href="/what-year-was-i-born/if-im-{k}">{k}</a>' for k in near)
    body = f"""
<div class="result answer" data-age-n="{n}">
<p class="big">Born in <span class="yb-a">{y_after}</span> or <span class="yb-b">{y_before}</span></p>
<p>If you are {n} years old in <span class="yr-now">{now}</span>, you were born in <strong><span class="yb-a">{y_after}</span></strong> if you have already had your birthday this year, or in <strong><span class="yb-b">{y_before}</span></strong> if your birthday is still to come.</p>
</div>
<section class="panel mini" aria-label="Birth year finder">
<h2>Find your exact birth year</h2>
<label class="check"><input type="radio" name="yn-had" value="1" checked> I have already had my birthday this year</label>
<label class="check"><input type="radio" name="yn-had" value="0"> My birthday is still to come this year</label>
<p id="yn-out" class="big" style="font-size:1.3rem" aria-live="polite"></p>
</section>
<article class="article">
<h2>Quick facts if you are {n}</h2>
<table class="breakdown"><tbody>{''.join(facts)}</tbody></table>

<h2>How to work it out</h2>
<p>Subtract your age from the current year: <span class="yr-now">{now}</span> − {n} = <span class="yb-a">{y_after}</span>. That is your birth year if your birthday has already happened this year. If it hasn’t, subtract one more year: <span class="yb-b">{y_before}</span>. The same rule works for any age, and you can check the result the other way round with our <a href="/how-old-am-i/born-in-{y_after}">born in {y_after}</a> page.</p>

<h2>Milestones</h2>
{('<p>Milestones you have already reached:</p><ul>' + ''.join(passed) + '</ul>') if passed else ''}
{('<p>Milestones still ahead:</p><ul>' + ''.join(coming) + '</ul>') if coming else ''}
{fra_note}

<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>If I’m {n}, what year will I turn {n + 10}?</summary><p>In {y_after + n + 10} if your birthday has passed this year, otherwise in {y_before + n + 10}.</p></details>
<details><summary>What year did I turn 18 if I’m {n}?</summary><p>{'You have not turned 18 yet. You will turn 18 in ' + str(y_after + 18) + ' or ' + str(y_before + 18) + '.' if n < 18 else 'In ' + str(y_after + 18) + ' if your birthday has passed this year, otherwise in ' + str(y_before + 18) + '.'}</p></details>
</div>
<p>Other ages: {near_links} · <a href="/what-year-was-i-born">all ages</a></p>
</article>
"""
    return dict(
        path=f"/what-year-was-i-born/if-im-{n}",
        title=f"What Year Was I Born If I'm {n}? ({now})",
        desc=f"If you are {n} in {now}, you were born in {y_after} (birthday already passed) or {y_before} (birthday still to come). See generation, zodiac and milestones.",
        h1=f"What year was I born if I’m {n}?",
        lede=f"Your birth year from your age in {now}, with the facts that go with it.",
        crumbs=[("Home", "/"), ("Birth year by age", "/what-year-was-i-born"), (f"Age {n}", f"/what-year-was-i-born/if-im-{n}")],
        tool="age-n", body=body,
        related=[(f"If I’m {k}", f"/what-year-was-i-born/if-im-{k}") for k in near[:6]] + [(f"Born in {y_after}", f"/how-old-am-i/born-in-{y_after}"), ("Age calculator", "/age-calculator")],
    )


def hub_born(now):
    by_decade = {}
    for y in YEARS:
        by_decade.setdefault(y // 10 * 10, []).append(y)
    blocks = "".join(f"<h2>{d}s</h2><p class='yr-grid'>" + "".join(
        f'<a href="/how-old-am-i/born-in-{y}">{y}<small>{now - y - 1}–{now - y}</small></a>' for y in ys) + "</p>" for d, ys in sorted(by_decade.items(), reverse=True))
    return dict(path="/how-old-am-i", title=f"How Old Am I? Age by Birth Year Chart ({now})",
                desc=f"Find how old you are in {now} from your birth year. Pick your year from 1940 to 2020 to see your age, generation and milestones.",
                h1="How old am I? Age by birth year", lede=f"Pick your birth year to see your age in {now}.",
                crumbs=[("Home", "/"), ("Age by birth year", "/how-old-am-i")], tool="", related=[("Age calculator", "/age-calculator"), ("What year was I born?", "/what-year-was-i-born")],
                body=f"<article class='article' style='margin-top:0'><p>Each year shows the two possible ages in {now}: the lower one before your birthday and the higher one after it. For an exact answer in years, months and days, use the <a href='/age-calculator'>age calculator</a>.</p>{blocks}</article>")


def hub_ifim(now):
    links = "".join(f'<a href="/what-year-was-i-born/if-im-{n}">{n}<small>{now - n - 1} or {now - n}</small></a>' for n in AGES)
    return dict(path="/what-year-was-i-born", title=f"What Year Was I Born? Birth Year by Age Chart ({now})",
                desc=f"Find your birth year from your age in {now}. Choose an age from 10 to 80 to see the two possible birth years.",
                h1="What year was I born? Birth year by age", lede=f"Pick your age to see your birth year.",
                crumbs=[("Home", "/"), ("Birth year by age", "/what-year-was-i-born")], tool="", related=[("Age calculator", "/age-calculator"), ("How old am I?", "/how-old-am-i")],
                body=f"<article class='article' style='margin-top:0'><p>Your birth year is the current year minus your age, or one year earlier if your birthday hasn’t happened yet this year.</p><p class='yr-grid'>{links}</p></article>")


def all_pages(now=None):
    now = now or date.today().year
    return [hub_born(now), hub_ifim(now)] + [born_in_page(y, now) for y in YEARS] + [if_im_page(n, now) for n in AGES]
