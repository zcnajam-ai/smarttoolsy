"""Guides for batch 4 (paycheck, sleep, time zones) and holiday tipping. Appended to ARTICLES in articles.py."""

NEW_ARTICLES = [
    {
        "slug": "how-much-tax-is-taken-out-of-paycheck",
        "date": "2026-10-29",
        "title": "How Much Tax Is Taken Out of a Paycheck in 2026?",
        "desc": "See what comes out of a US paycheck in 2026: federal income tax brackets, the standard deduction, Social Security and Medicare, with worked examples by salary.",
        "tools": ["paycheck-calculator", "salary-to-hourly"],
        "body": """
<p>If you have ever compared your salary with the amount that lands in your bank account, you know the gap can be large. For most workers, between about 15% and 30% of each paycheck goes to taxes. Exactly how much depends on your pay, your filing status and where you live. This guide explains each deduction using the 2026 figures, and the <a href="/paycheck-calculator">paycheck calculator</a> does the math for you.</p>

<h2>What comes out of a paycheck</h2>
<ul>
<li><strong>Federal income tax</strong>, based on your W-4 and the IRS brackets.</li>
<li><strong>Social Security tax</strong>: 6.2% of wages.</li>
<li><strong>Medicare tax</strong>: 1.45% of wages, plus 0.9% on wages over $200,000.</li>
<li><strong>State and local income tax</strong>, in most states.</li>
<li><strong>Deductions you chose</strong>, such as a 401(k), health insurance or a flexible spending account.</li>
</ul>
<p>Social Security and Medicare together are called FICA taxes. Your employer pays a matching 7.65% on top of your pay, which you never see on your stub.</p>

<h2>2026 federal income tax brackets</h2>
<p>The IRS adjusts the brackets for inflation every year. These apply to taxable income earned in 2026:</p>
<div class="table-wrap"><table>
<thead><tr><th>Rate</th><th>Single</th><th>Married filing jointly</th><th>Head of household</th></tr></thead>
<tbody>
<tr><td>10%</td><td>Up to $12,400</td><td>Up to $24,800</td><td>Up to $17,700</td></tr>
<tr><td>12%</td><td>$12,401 – $50,400</td><td>$24,801 – $100,800</td><td>$17,701 – $67,450</td></tr>
<tr><td>22%</td><td>$50,401 – $105,700</td><td>$100,801 – $211,400</td><td>$67,451 – $105,700</td></tr>
<tr><td>24%</td><td>$105,701 – $201,775</td><td>$211,401 – $403,550</td><td>$105,701 – $201,750</td></tr>
<tr><td>32%</td><td>$201,776 – $256,225</td><td>$403,551 – $512,450</td><td>$201,751 – $256,200</td></tr>
<tr><td>35%</td><td>$256,226 – $640,600</td><td>$512,451 – $768,700</td><td>$256,201 – $640,600</td></tr>
<tr><td>37%</td><td>Over $640,600</td><td>Over $768,700</td><td>Over $640,600</td></tr>
</tbody>
</table></div>
<p>Married people filing separately use the single brackets up to the 35% rate, which ends at $384,350 for them. The <strong>standard deduction</strong> for 2026 is $16,100 for single filers and married filing separately, $32,200 for married filing jointly and $24,150 for heads of household. Federal tax is charged only on income above that amount.</p>

<h2>How brackets really work</h2>
<p>A common worry is that a raise could push you into a higher bracket and leave you with less money. That can’t happen with income tax, because each rate applies only to the slice of income inside its bracket. If you are single with $60,000 of taxable income, you pay 10% on the first $12,400, 12% on the next $38,000 and 22% only on the last $9,600. Your “bracket” is 22%, but your overall federal rate is much lower.</p>

<h2>Worked examples (single, 2026, no other deductions)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Salary</th><th>Federal tax</th><th>Social Security + Medicare</th><th>Take-home per year</th><th>Per biweekly check</th></tr></thead>
<tbody>
<tr><td>$40,000</td><td>$2,620</td><td>$3,060</td><td>$34,320</td><td>$1,320</td></tr>
<tr><td>$60,000</td><td>$5,020</td><td>$4,590</td><td>$50,390</td><td>$1,938</td></tr>
<tr><td>$80,000</td><td>$8,770</td><td>$6,120</td><td>$65,110</td><td>$2,504</td></tr>
<tr><td>$100,000</td><td>$13,170</td><td>$7,650</td><td>$79,180</td><td>$3,045</td></tr>
</tbody>
</table></div>
<p>These figures leave out state tax. In a state with no wage tax, such as Texas or Florida, they are close to what you would actually take home; in a state with a 5% income tax, take-home pay would be roughly 4% to 5% lower.</p>

<h2>Ways to keep more of each paycheck</h2>
<ul>
<li><strong>Pre-tax retirement savings.</strong> Money you put in a traditional 401(k) or 403(b) is not counted for federal income tax this year. Saving $200 per paycheck cuts your take-home pay by only about $156 to $176, depending on whether you are in the 22% or 12% bracket.</li>
<li><strong>Pre-tax benefits.</strong> Health insurance premiums, HSA and FSA contributions taken through your employer usually avoid income tax and FICA.</li>
<li><strong>Update your W-4.</strong> If you got a large refund last year, too much was withheld. If you owed money, add extra withholding. The IRS Tax Withholding Estimator can help.</li>
<li><strong>Claim credits for children.</strong> The child tax credit is $2,200 per qualifying child in 2026. Listing children in Step 3 of the W-4 lowers withholding through the year.</li>
</ul>

<h2>New deductions for tips and overtime</h2>
<p>For tax years 2025 through 2028, workers can deduct up to $25,000 of qualified tips, and up to $12,500 of qualified overtime pay ($25,000 for a married couple filing jointly). The overtime deduction covers only the extra “half” in time-and-a-half pay. Both start to phase out above $150,000 of income ($300,000 for joint filers). They reduce federal income tax only: Social Security and Medicare are still taken out of tips and overtime as usual. Because they are claimed on your tax return, many workers will see the benefit as a larger refund rather than in each check.</p>

<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What percentage of my paycheck goes to taxes?</summary><p>For a single person earning $60,000 in a state without income tax, about 16% goes to federal tax and FICA. At $100,000 it is about 21%. State taxes add more in most states.</p></details>
<details><summary>Why is my first paycheck of the year different?</summary><p>Benefit elections often change in January, and the Social Security wage limit resets. High earners notice this most: once their wages pass $184,500 in 2026, Social Security stops being withheld for the rest of the year.</p></details>
<details><summary>Is overtime taxed more?</summary><p>No. Overtime is taxed at the same rates as other pay, but a large paycheck can make withholding look higher because the payroll system treats it as if you earned that much all year. It evens out when you file your return.</p></details>
</div>
<p>Want to see your own numbers? Try the <a href="/paycheck-calculator">paycheck calculator</a>, or convert between hourly and yearly pay with the <a href="/salary-to-hourly">salary to hourly calculator</a>.</p>
""",
    },
    {
        "slug": "how-much-sleep-do-i-need",
        "date": "2026-10-29",
        "title": "How Much Sleep Do You Need? Hours by Age and the Best Time to Go to Bed",
        "desc": "Recommended hours of sleep for every age, how sleep cycles work, and how to choose a bedtime that fits your wake-up time, with simple tips for sleeping better.",
        "tools": ["sleep-calculator"],
        "body": """
<p>Most adults know they should “get eight hours”, yet about a third of US adults regularly sleep less than they need. The right amount depends mostly on your age, and the right bedtime depends on when you have to get up. Here is what health experts recommend, and how to turn it into a schedule with the <a href="/sleep-calculator">sleep calculator</a>.</p>

<h2>Recommended sleep by age</h2>
<p>These are the CDC’s recommendations for total sleep in a 24-hour period:</p>
<table>
<thead><tr><th>Age</th><th>Recommended sleep</th></tr></thead>
<tbody>
<tr><td>Newborn (0–3 months)</td><td>14–17 hours</td></tr>
<tr><td>Infant (4–12 months)</td><td>12–16 hours, including naps</td></tr>
<tr><td>Toddler (1–2 years)</td><td>11–14 hours, including naps</td></tr>
<tr><td>Preschool (3–5 years)</td><td>10–13 hours, including naps</td></tr>
<tr><td>School age (6–12 years)</td><td>9–12 hours</td></tr>
<tr><td>Teen (13–17 years)</td><td>8–10 hours</td></tr>
<tr><td>Adult (18–60 years)</td><td>7 or more hours</td></tr>
<tr><td>Adult (61–64 years)</td><td>7–9 hours</td></tr>
<tr><td>Adult (65 and older)</td><td>7–8 hours</td></tr>
</tbody>
</table>
<p>These are ranges, not exact targets. Some people feel fine at the low end and others need the top. A good test is whether you wake up without dragging yourself out of bed and stay alert through the afternoon without leaning on caffeine.</p>

<h2>What a sleep cycle is</h2>
<p>Sleep isn’t one long, even stretch. Through the night you repeat cycles that move from light sleep into deep sleep and then into REM sleep, when most dreaming happens. A cycle lasts about 90 minutes on average, though it can be anywhere from roughly 80 to 120 minutes. Early in the night the cycles contain more deep sleep; toward morning they contain more REM.</p>
<p>When your alarm goes off during deep sleep, you are more likely to feel groggy for a while, a state called sleep inertia. Waking near the end of a cycle, when sleep is lighter, tends to feel easier. That is the idea behind planning sleep in 90-minute blocks.</p>

<h2>How to pick your bedtime</h2>
<ol>
<li><strong>Start from your wake-up time,</strong> since that is usually fixed by work or school.</li>
<li><strong>Count back five or six cycles</strong> (7½ or 9 hours). Four cycles, 6 hours, is less than adults are advised to get.</li>
<li><strong>Add the time it takes you to fall asleep,</strong> usually 10 to 20 minutes.</li>
</ol>
<p>For a 6:30 a.m. alarm, that gives a bedtime of about 10:45 p.m. for 7½ hours or 9:15 p.m. for 9 hours. The <a href="/sleep-calculator">sleep calculator</a> works this out for any time, and can also tell you when to set the alarm if you are heading to bed right now.</p>

<h2>Habits that help you sleep better</h2>
<ul>
<li><strong>Keep a regular schedule.</strong> Going to bed and getting up at the same times every day, weekends included, steadies your body clock more than anything else.</li>
<li><strong>Get morning light.</strong> Daylight soon after waking helps you feel sleepy at the right time in the evening.</li>
<li><strong>Make the bedroom dark, quiet and cool.</strong></li>
<li><strong>Cut back on screens before bed.</strong> Bright light and scrolling keep the brain alert.</li>
<li><strong>Watch caffeine and alcohol.</strong> Caffeine can stay in your system for many hours, and alcohol disturbs sleep later in the night.</li>
<li><strong>Be active during the day,</strong> but finish hard workouts a few hours before bed.</li>
</ul>

<h2>When to talk to a doctor</h2>
<p>If you often feel tired even after enough time in bed, snore loudly, stop breathing for moments during sleep, or have trouble falling or staying asleep for weeks at a time, speak to a doctor. Sleep apnea and insomnia are common, and both can be treated.</p>

<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is 6 hours of sleep enough?</summary><p>For most adults, no. The CDC recommends at least 7 hours for adults. Regularly sleeping 6 hours or less is linked to poorer concentration and health over time.</p></details>
<details><summary>Can I catch up on sleep at the weekend?</summary><p>A longer sleep can help you recover from a short night, but large swings between weekday and weekend schedules make Monday mornings harder. Small, regular adjustments work better.</p></details>
<details><summary>Do naps count?</summary><p>For babies and young children, yes: the recommended totals include naps. For adults, a short nap of 20 to 30 minutes can boost alertness, but it doesn’t replace a full night’s sleep.</p></details>
</div>
<p>When the clocks change, your schedule shifts too. See our guide to <a href="/blog/when-does-daylight-saving-time-end">when daylight saving time ends</a> for tips on adjusting.</p>
<p class="count-note">This guide is general information, not medical advice.</p>
""",
    },
    {
        "slug": "us-time-zones",
        "date": "2026-10-29",
        "title": "US Time Zones Explained: Eastern, Central, Mountain, Pacific and More",
        "desc": "The six US time zones and their UTC offsets, which states are split between two zones, how daylight saving time changes them, and quick conversion tables.",
        "tools": ["time-zone-converter"],
        "body": """
<p>The United States spans six time zones in the 50 states, plus more in its territories. If you are scheduling a call between New York and Los Angeles, booking a flight or watching a live event, it helps to know how they fit together. You can convert any time instantly with the <a href="/time-zone-converter">time zone converter</a>.</p>

<h2>The six US time zones</h2>
<table>
<thead><tr><th>Zone</th><th>Winter (standard)</th><th>Summer (daylight)</th><th>Largest cities</th></tr></thead>
<tbody>
<tr><td>Eastern</td><td>EST, UTC−5</td><td>EDT, UTC−4</td><td>New York, Philadelphia, Atlanta, Miami, Boston</td></tr>
<tr><td>Central</td><td>CST, UTC−6</td><td>CDT, UTC−5</td><td>Chicago, Houston, Dallas, San Antonio, Nashville</td></tr>
<tr><td>Mountain</td><td>MST, UTC−7</td><td>MDT, UTC−6</td><td>Denver, El Paso, Albuquerque, Salt Lake City</td></tr>
<tr><td>Pacific</td><td>PST, UTC−8</td><td>PDT, UTC−7</td><td>Los Angeles, San Diego, San Francisco, Seattle, Las Vegas</td></tr>
<tr><td>Alaska</td><td>AKST, UTC−9</td><td>AKDT, UTC−8</td><td>Anchorage, Fairbanks, Juneau</td></tr>
<tr><td>Hawaii-Aleutian</td><td>HST, UTC−10</td><td>Hawaii doesn’t change</td><td>Honolulu</td></tr>
</tbody>
</table>
<p>US territories add more: Puerto Rico and the US Virgin Islands use Atlantic Time (UTC−4), Guam and the Northern Mariana Islands use Chamorro Time (UTC+10), and American Samoa uses Samoa Time (UTC−11). None of them use daylight saving time.</p>

<h2>Quick conversion table</h2>
<p>When it is this time in the Eastern zone, it is:</p>
<table>
<thead><tr><th>Eastern</th><th>Central</th><th>Mountain</th><th>Pacific</th><th>Alaska</th><th>Hawaii (winter)</th></tr></thead>
<tbody>
<tr><td>9:00 a.m.</td><td>8:00 a.m.</td><td>7:00 a.m.</td><td>6:00 a.m.</td><td>5:00 a.m.</td><td>4:00 a.m.</td></tr>
<tr><td>12:00 p.m.</td><td>11:00 a.m.</td><td>10:00 a.m.</td><td>9:00 a.m.</td><td>8:00 a.m.</td><td>7:00 a.m.</td></tr>
<tr><td>3:00 p.m.</td><td>2:00 p.m.</td><td>1:00 p.m.</td><td>12:00 p.m.</td><td>11:00 a.m.</td><td>10:00 a.m.</td></tr>
<tr><td>6:00 p.m.</td><td>5:00 p.m.</td><td>4:00 p.m.</td><td>3:00 p.m.</td><td>2:00 p.m.</td><td>1:00 p.m.</td></tr>
<tr><td>9:00 p.m.</td><td>8:00 p.m.</td><td>7:00 p.m.</td><td>6:00 p.m.</td><td>5:00 p.m.</td><td>4:00 p.m.</td></tr>
</tbody>
</table>
<p>From March to November, while the mainland is on daylight time but Hawaii isn’t, Hawaii is one hour further behind: 9:00 a.m. Eastern is 3:00 a.m. in Honolulu.</p>

<h2>States split between two time zones</h2>
<p>Time zone lines follow county borders rather than state lines, so 13 states are divided:</p>
<ul>
<li><strong>Eastern and Central:</strong> Florida (the western Panhandle is Central), Indiana (a few counties near Chicago and Evansville are Central), Kentucky (the western half is Central), Michigan (four Upper Peninsula counties bordering Wisconsin are Central) and Tennessee (East Tennessee is Eastern; Nashville and Memphis are Central).</li>
<li><strong>Central and Mountain:</strong> Kansas, Nebraska, North Dakota and South Dakota (their western parts are Mountain) and Texas (El Paso and Hudspeth counties are Mountain).</li>
<li><strong>Mountain and Pacific:</strong> Idaho (the northern Panhandle is Pacific) and Oregon (most of Malheur County is Mountain).</li>
<li><strong>Alaska and Hawaii-Aleutian:</strong> Alaska (the western Aleutian Islands use Hawaii-Aleutian time).</li>
</ul>

<h2>Daylight saving time and Arizona</h2>
<p>Most of the US moves its clocks forward one hour on the second Sunday in March and back on the first Sunday in November. In 2026 the clocks fall back on November 1, and in 2027 they spring forward on March 14. Hawaii and most of Arizona stay on standard time all year, so Phoenix shares the same clock time as Los Angeles in summer and as Denver in winter. The Navajo Nation in northeastern Arizona does observe daylight saving time. More detail is in our guide to <a href="/blog/when-does-daylight-saving-time-end">when daylight saving time ends</a>.</p>

<h2>Tips for scheduling across time zones</h2>
<ul>
<li><strong>Always write the zone</strong> in invitations: “2:00 p.m. ET / 11:00 a.m. PT”.</li>
<li><strong>Write “ET” or “PT”</strong> rather than EST or PST if you don’t want to worry about which half of the year it is.</li>
<li><strong>Coast-to-coast sweet spot:</strong> 12:00 p.m. to 5:00 p.m. Eastern falls between 9:00 a.m. and 2:00 p.m. Pacific, inside working hours for both coasts.</li>
<li><strong>Check the date of international calls</strong> around March and late October, when the US and Europe change their clocks on different weekends.</li>
</ul>

<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>How many time zones does the US have?</summary><p>Six across the 50 states (Eastern, Central, Mountain, Pacific, Alaska and Hawaii-Aleutian), and nine counting the territories.</p></details>
<details><summary>What time zone is Texas in?</summary><p>Almost all of Texas is in the Central zone. El Paso and Hudspeth counties in the far west are in the Mountain zone.</p></details>
<details><summary>Is Arizona on Pacific or Mountain time?</summary><p>Arizona is in the Mountain zone but doesn’t use daylight saving time, so in summer its clocks match Pacific Daylight Time.</p></details>
</div>
""",
    },
    {
        "slug": "how-much-to-tip-for-the-holidays",
        "date": "2026-10-29",
        "title": "How Much to Tip for the Holidays: 2026 Holiday Tipping Guide",
        "desc": "Who to tip at the holidays and how much: nannies, house cleaners, mail carriers, teachers, doormen, trash collectors and more, plus how to budget for it.",
        "tools": ["tip-calculator", "christmas-budget-calculator"],
        "body": """
<p>The end of the year is when many people thank the workers who help them all year long, from the babysitter to the building super. There is no law or fixed rule, and a holiday tip is always a choice. Still, most etiquette guides follow a simple idea: give about what one visit, one session or one week of work would cost. The table below turns that into amounts, and the <a href="/christmas-budget-calculator">Christmas budget calculator</a> helps you fit the total into your holiday spending.</p>

<h2>Holiday tipping guide by service</h2>
<div class="table-wrap"><table>
<thead><tr><th>Who</th><th>Typical holiday tip or gift</th></tr></thead>
<tbody>
<tr><td>Full-time nanny</td><td>One to two weeks’ pay, plus a small gift from the children</td></tr>
<tr><td>Regular babysitter</td><td>One evening’s or one day’s pay</td></tr>
<tr><td>Home health aide or caregiver</td><td>Up to one week’s pay or a gift (check the agency’s rules first)</td></tr>
<tr><td>House cleaner</td><td>The cost of one visit</td></tr>
<tr><td>Dog walker or pet sitter</td><td>One week’s pay, or the cost of a visit for occasional help</td></tr>
<tr><td>Hairstylist or barber</td><td>The cost of one appointment</td></tr>
<tr><td>Personal trainer</td><td>The cost of one session</td></tr>
<tr><td>Lawn care or snow removal</td><td>The cost of one visit</td></tr>
<tr><td>Building superintendent</td><td>$100–$200</td></tr>
<tr><td>Doorman or porter</td><td>$25–$100 each, depending on how much they help you</td></tr>
<tr><td>Trash and recycling collectors</td><td>$10–$30 each, if your city allows it</td></tr>
<tr><td>Teacher</td><td>A thoughtful gift or a gift card of around $25, ideally from the whole class</td></tr>
<tr><td>Mail carrier (USPS)</td><td>A non-cash gift worth $20 or less</td></tr>
<tr><td>Package delivery driver</td><td>Snacks, a drink or a small non-cash gift</td></tr>
</tbody>
</table></div>

<h2>Rules for mail carriers and other workers</h2>
<p>Some workers aren’t allowed to accept cash. As federal employees, US Postal Service carriers may accept a gift worth up to $20 per occasion, such as Christmas, and no more than $50 in gifts from one customer in a year. They can never accept cash or anything that works like cash, including checks and prepaid Visa or Mastercard gift cards. A gift card for a specific coffee shop or restaurant, worth $20 or less, is fine. Snacks and drinks to enjoy on the route aren’t counted as gifts at all.</p>
<p>Teachers, nurses, home health aides and city sanitation workers may also be covered by school, employer or city rules, so check before giving cash. A heartfelt card or a group gift is always acceptable.</p>

<h2>What people actually give</h2>
<p>Holiday tipping is far from universal. In Bankrate’s 2024 tipping survey, only about half of Americans planned to tip their house cleaner, childcare provider or children’s teacher, and fewer than a third planned to tip their mail carrier. Typical planned amounts were about $50 for house cleaners and childcare providers, $25 for teachers and around $20 to $30 for landscapers, mail carriers and trash collectors. If your budget is tighter than the amounts above, you are in good company.</p>

<h2>How to decide who to tip</h2>
<ol>
<li><strong>Start with the people you see most,</strong> especially those who work in your home or care for your children or parents.</li>
<li><strong>Consider how long you have known them</strong> and the quality of their work. A nanny of five years deserves more than a sitter you hired twice.</li>
<li><strong>Think about whether you tip all year.</strong> If you already tip your hairstylist 20% at every visit, a smaller holiday gift or a card is enough.</li>
<li><strong>Set a total and divide it.</strong> Add holiday tips as a line in your <a href="/christmas-budget-calculator">Christmas budget</a> so they don’t come as a surprise.</li>
</ol>

<h2>When and how to give</h2>
<ul>
<li>Give in the first two or three weeks of December, before people go on holiday.</li>
<li>Cash in a card with a short handwritten note is the most common way. Many workers also accept payment apps; a gift card is a good choice when cash isn’t allowed.</li>
<li>For workers you rarely see, such as trash collectors or a building’s night staff, leave a labeled envelope with the building manager or attach it to the bin on collection day.</li>
</ul>

<h2>If you can’t afford to tip</h2>
<p>Holiday tips are a thank-you, not a bill. If money is tight this year, a sincere note explaining how much you appreciate someone’s work, homemade treats or a small gift is a kind alternative. Etiquette experts point out that most service workers would rather keep a loyal customer than receive a tip you can’t afford.</p>

<h2>Holiday tipping when you eat out</h2>
<p>For restaurants, bars, delivery and rideshares, nothing changes at the holidays: the usual 15% to 20% applies. Some people tip a little extra on busy days like Christmas Eve or for big holiday party orders. Use the <a href="/tip-calculator">tip calculator</a> to work out the tip and split the bill, and see our everyday guide on <a href="/blog/how-much-to-tip">how much to tip</a> for restaurants and services.</p>

<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Should I tip my mail carrier for Christmas?</summary><p>You can thank your carrier with a gift worth $20 or less, but not with cash, checks or general-purpose gift cards, which USPS rules don’t allow carriers to accept.</p></details>
<details><summary>How much should I give my nanny for Christmas?</summary><p>A common bonus is one to two weeks’ pay for a full-time nanny, often with a small personal gift from the children.</p></details>
<details><summary>Do you tip teachers at Christmas?</summary><p>Cash is unusual and sometimes not allowed. A small gift, a gift card of about $25, or a contribution to a class group gift is typical, along with a note from your child.</p></details>
<details><summary>Do I tip if I already tip every visit?</summary><p>It isn’t expected. If you tip regularly, a card or small gift is a nice gesture, and an extra tip is a bonus rather than an obligation.</p></details>
</div>
""",
    },
]
