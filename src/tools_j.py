"""Batch 4: paycheck (2026 federal tax + FICA), sleep cycles and time zone converter."""

T3 = "/assets/tools3.js"

TOOLS_J = [
# ---------------------------------------------------------------- paycheck
dict(
slug="paycheck-calculator", name="Paycheck Calculator", cat="calc", ico="PC", scripts=[T3],
title="Paycheck Calculator 2026 – Take-Home Pay After Federal Tax and FICA",
desc="Free 2026 paycheck calculator: enter your salary or hourly wage to see take-home pay per paycheck after federal income tax, Social Security, Medicare, state tax and 401(k).",
short="Take-home pay after 2026 federal tax, FICA and deductions.",
ui="""
<div class="seg" role="group" aria-label="Pay type"><button type="button" data-pc-type="salary" aria-pressed="true">Salary</button><button type="button" data-pc-type="hourly" aria-pressed="false">Hourly</button></div>
<div class="row" style="margin-top:12px">
<div class="field"><label for="pc-amt" id="pc-amt-lbl">Annual salary ($)</label><input id="pc-amt" type="number" min="0" step="100" value="60000"></div>
<div class="field pc-hourly" hidden><label for="pc-hours">Hours per week</label><input id="pc-hours" type="number" min="0" max="100" step="0.5" value="40"></div>
<div class="field pc-hourly" hidden><label for="pc-ot">Overtime hours (1.5×)</label><input id="pc-ot" type="number" min="0" max="60" step="0.5" value="0"></div>
<div class="field"><label for="pc-freq">Pay frequency</label><select id="pc-freq"><option value="52">Weekly</option><option value="26" selected>Every two weeks</option><option value="24">Twice a month</option><option value="12">Monthly</option></select></div>
<div class="field"><label for="pc-status">Filing status</label><select id="pc-status"><option value="single" selected>Single</option><option value="mfj">Married filing jointly</option><option value="mfs">Married filing separately</option><option value="hoh">Head of household</option></select></div>
</div>
<div class="row">
<div class="field"><label for="pc-kids">Children under 17</label><input id="pc-kids" type="number" min="0" max="15" step="1" value="0"></div>
<div class="field"><label for="pc-deps">Other dependents</label><input id="pc-deps" type="number" min="0" max="15" step="1" value="0"></div>
<div class="field"><label for="pc-state">State &amp; local tax (%)</label><input id="pc-state" type="number" min="0" max="15" step="0.1" value="0"></div>
</div>
<div class="row">
<div class="field"><label for="pc-401k">401(k) / 403(b) (%)</label><input id="pc-401k" type="number" min="0" max="100" step="0.5" value="0"></div>
<div class="field"><label for="pc-pretax">Pre-tax benefits ($/check)</label><input id="pc-pretax" type="number" min="0" step="1" value="0"></div>
<div class="field"><label for="pc-post">After-tax ($/check)</label><input id="pc-post" type="number" min="0" step="1" value="0"></div>
</div>
<div class="stats">
<div class="stat"><b id="pc-net">—</b><span>Take-home per paycheck</span></div>
<div class="stat"><b id="pc-net-yr">—</b><span>Take-home per year</span></div>
<div class="stat"><b id="pc-eff">—</b><span>Total tax rate</span></div>
<div class="stat"><b id="pc-marg">—</b><span>Federal tax bracket</span></div>
</div>
<p class="result" id="pc-sum" aria-live="polite"></p>
<div class="table-wrap"><table class="sh-tbl pc-tbl"><thead><tr><th scope="col"></th><th scope="col">Per paycheck</th><th scope="col">Per year</th></tr></thead><tbody id="pc-out"></tbody></table></div>
<p class="count-note">An estimate using 2026 IRS tax brackets and standard deductions, like a W-4 with no extra withholding. Your employer’s exact withholding can differ by a few dollars.</p>
""",
content="""
<p>This paycheck calculator shows how much of your pay you actually take home. Enter an annual salary or an hourly wage, how often you are paid and your filing status, and it works out federal income tax, Social Security, Medicare, state tax and any 401(k) or benefit deductions for each paycheck, using the 2026 tax brackets.</p>
<h2>How take-home pay is calculated</h2>
<ol>
<li><strong>Gross pay</strong> is your salary, or your hourly wage × hours × 52 weeks, divided by the number of paychecks.</li>
<li><strong>Pre-tax deductions</strong> come out first. A traditional 401(k) lowers the pay that federal income tax is charged on; health insurance and other cafeteria-plan benefits also lower the pay that Social Security and Medicare are charged on.</li>
<li><strong>Federal income tax</strong> is worked out on yearly pay minus the standard deduction, using the 2026 brackets, then reduced by the child tax credit.</li>
<li><strong>FICA</strong> is 6.2% for Social Security (on the first $184,500 of 2026 wages) plus 1.45% for Medicare, and an extra 0.9% Medicare tax on wages over $200,000.</li>
<li><strong>Take-home pay</strong> is what is left after all of these and any after-tax deductions.</li>
</ol>
<h2>2026 federal tax brackets</h2>
<table>
<thead><tr><th>Rate</th><th>Single</th><th>Married filing jointly</th></tr></thead>
<tbody>
<tr><td>10%</td><td>$0 – $12,400</td><td>$0 – $24,800</td></tr>
<tr><td>12%</td><td>$12,401 – $50,400</td><td>$24,801 – $100,800</td></tr>
<tr><td>22%</td><td>$50,401 – $105,700</td><td>$100,801 – $211,400</td></tr>
<tr><td>24%</td><td>$105,701 – $201,775</td><td>$211,401 – $403,550</td></tr>
<tr><td>32%</td><td>$201,776 – $256,225</td><td>$403,551 – $512,450</td></tr>
<tr><td>35%</td><td>$256,226 – $640,600</td><td>$512,451 – $768,700</td></tr>
<tr><td>37%</td><td>Over $640,600</td><td>Over $768,700</td></tr>
</tbody>
</table>
<p>The brackets apply to <em>taxable</em> income, after the 2026 standard deduction of $16,100 for single filers, $32,200 for married couples filing jointly and $24,150 for heads of household. Only the part of your income inside each bracket is taxed at that rate, so moving into a higher bracket never lowers your take-home pay.</p>
<h2>Example: $60,000 a year, single, paid every two weeks</h2>
<p>Taxable income is $60,000 − $16,100 = $43,900. Federal tax is 10% of the first $12,400 ($1,240) plus 12% of the remaining $31,500 ($3,780), or $5,020 a year. Social Security is $3,720 and Medicare $870. That leaves about <strong>$50,390 a year, or $1,938 per paycheck</strong>, before any state tax or deductions.</p>
<h2>What the calculator doesn’t include</h2>
<ul>
<li><strong>State tax</strong> is a single flat rate you enter. Texas, Florida, Washington, Nevada, Tennessee, South Dakota, Wyoming, Alaska and New Hampshire have no state tax on wages, so leave it at 0 there.</li>
<li><strong>Tips and overtime deductions:</strong> for 2025 to 2028 you can deduct up to $25,000 of qualified tips and up to $12,500 of the extra “half” of overtime pay ($25,000 if married filing jointly) on your tax return. They lower income tax, not Social Security or Medicare, and are claimed when you file, so they show up as a bigger refund rather than in each paycheck.</li>
<li><strong>Extra W-4 settings</strong> such as a second job or extra withholding per paycheck.</li>
</ul>
<p>For a full walk-through with tables for every filing status, read <a href="/blog/how-much-tax-is-taken-out-of-paycheck">how much tax is taken out of a paycheck in 2026</a>. To convert a salary to an hourly wage first, use the <a href="/salary-to-hourly">salary to hourly calculator</a>, and to total the hours on your timesheet, the <a href="/time-card-calculator">time card calculator</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Why is my paycheck different from the calculator?</summary><p>Employers use the IRS withholding tables and your exact W-4 answers, and may take out benefits, union dues or local taxes the calculator doesn’t know about. Results are usually within a few dollars per paycheck if you enter the same deductions.</p></details>
<details><summary>Does a 401(k) contribution lower my taxes?</summary><p>A traditional 401(k) lowers your federal income tax and, in most states, state income tax. It does not lower Social Security or Medicare. A Roth 401(k) is taken out after tax, so enter it as an after-tax deduction.</p></details>
<details><summary>What is FICA on a paycheck?</summary><p>FICA is Social Security (6.2%) and Medicare (1.45%), 7.65% in total. Your employer pays the same amount again on top of your pay.</p></details>
<details><summary>Biweekly or twice a month: which paycheck is bigger?</summary><p>Twice-a-month pay comes 24 times a year, so each check is slightly larger than a biweekly check, which comes 26 times a year. Your yearly pay is the same.</p></details>
</div>
"""),
# ---------------------------------------------------------------- sleep
dict(
slug="sleep-calculator", name="Sleep Calculator", cat="calc", ico="SL", scripts=[T3],
title="Sleep Calculator – What Time to Go to Bed or Wake Up",
desc="Find the best time to go to bed or wake up based on 90-minute sleep cycles. Enter your wake-up time or bedtime and see times that let you wake up between cycles.",
short="Best bedtimes and wake-up times based on sleep cycles.",
ui="""
<div class="seg" role="group" aria-label="What do you want to work out?"><button type="button" data-sl-mode="wake" aria-pressed="true">I need to wake up at</button><button type="button" data-sl-mode="bed" aria-pressed="false">I’m going to bed at</button></div>
<div class="row" style="margin-top:12px">
<div class="field"><label for="sl-time" id="sl-time-lbl">Wake-up time</label><input id="sl-time" type="time" value="07:00"></div>
<div class="field"><label for="sl-fall">Minutes to fall asleep</label><input id="sl-fall" type="number" min="0" max="90" step="1" value="15"></div>
<div class="field"><label for="sl-cycle">Cycle length (min)</label><input id="sl-cycle" type="number" min="60" max="120" step="5" value="90"></div>
<div class="field"><label for="sl-age">Age</label><select id="sl-age"><option value="3-5">3–5 years</option><option value="6-12">6–12 years</option><option value="13-17">13–17 years</option><option value="18-60" selected>18–60 years</option><option value="61-64">61–64 years</option><option value="65">65 and older</option></select></div>
</div>
<div class="btns"><button class="btn ghost" id="sl-now" type="button">Going to bed now</button></div>
<p class="result" id="sl-sum" aria-live="polite"></p>
<div class="stats sl-out" id="sl-out"></div>
<p class="count-note" id="sl-rec"></p>
""",
content="""
<p>The sleep calculator tells you what time to go to bed so you wake up at the end of a sleep cycle instead of in the middle of one. Enter the time you need to get up and it lists the best bedtimes, or enter when you are going to bed and it shows the best times to set your alarm.</p>
<h2>How the sleep calculator works</h2>
<p>During the night you move through repeating sleep cycles of light sleep, deep sleep and REM (dreaming) sleep. Each cycle lasts roughly 80 to 120 minutes, and about 90 minutes on average. Waking up when a cycle ends, while you are in light sleep, usually feels easier than being woken out of deep sleep, which can leave you groggy.</p>
<div class="formula">Bedtime = wake-up time − (cycles × 90 minutes) − time to fall asleep</div>
<p>Most adults take about 10 to 20 minutes to fall asleep, so the calculator adds 15 minutes by default. Change it if you usually drop off faster or more slowly.</p>
<h2>Bedtimes for common wake-up times</h2>
<p>Five cycles (7½ hours) or six cycles (9 hours) of sleep, plus 15 minutes to fall asleep:</p>
<table>
<thead><tr><th>Wake up at</th><th>Bed for 6 cycles (9 h)</th><th>Bed for 5 cycles (7½ h)</th></tr></thead>
<tbody>
<tr><td>5:00 a.m.</td><td>7:45 p.m.</td><td>9:15 p.m.</td></tr>
<tr><td>6:00 a.m.</td><td>8:45 p.m.</td><td>10:15 p.m.</td></tr>
<tr><td>6:30 a.m.</td><td>9:15 p.m.</td><td>10:45 p.m.</td></tr>
<tr><td>7:00 a.m.</td><td>9:45 p.m.</td><td>11:15 p.m.</td></tr>
<tr><td>7:30 a.m.</td><td>10:15 p.m.</td><td>11:45 p.m.</td></tr>
<tr><td>8:00 a.m.</td><td>10:45 p.m.</td><td>12:15 a.m.</td></tr>
</tbody>
</table>
<h2>How much sleep do you need?</h2>
<p>The CDC recommends at least 7 hours a night for adults aged 18 to 60, 7 to 9 hours from 61 to 64, and 7 to 8 hours from age 65. Teenagers need 8 to 10 hours and children aged 6 to 12 need 9 to 12. For most adults, that means five or six full cycles. Our guide <a href="/blog/how-much-sleep-do-i-need">how much sleep do you need</a> has the full table by age and tips for sleeping better.</p>
<h2>Tips for waking up refreshed</h2>
<ul>
<li>Keep the same wake-up time every day, including weekends. A steady schedule matters more than hitting an exact cycle.</li>
<li>Get daylight soon after you wake up, and dim screens and lights in the hour before bed.</li>
<li>Avoid caffeine in the afternoon and large meals or alcohol close to bedtime.</li>
<li>If you are often tired despite enough hours in bed, talk to a doctor; conditions such as sleep apnea are common and treatable.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is it better to sleep 6 or 7.5 hours?</summary><p>For most adults, 7½ hours is better because it gives you more total sleep. Four cycles (6 hours) is less than the 7 hours adults are advised to get, even if you wake up between cycles.</p></details>
<details><summary>Are sleep cycles always 90 minutes?</summary><p>No. Ninety minutes is an average; cycles vary between people and through the night. If you often wake up a little before your alarm, try a cycle length of 85 or 95 minutes.</p></details>
<details><summary>What time should I go to bed to wake up at 6 a.m.?</summary><p>For 7½ hours of sleep, go to bed around 10:15 p.m.; for 9 hours, around 8:45 p.m. Both include 15 minutes to fall asleep.</p></details>
</div>
<p class="count-note">This calculator is for general information and isn’t medical advice.</p>
"""),
# ---------------------------------------------------------------- time zones
dict(
slug="time-zone-converter", name="Time Zone Converter", cat="convert", ico="TZ", scripts=[T3],
title="Time Zone Converter – Convert Time Between EST, PST, GMT and More",
desc="Convert a time between US and world time zones: Eastern, Central, Mountain, Pacific, London, India, Tokyo and hundreds more. Daylight saving time handled automatically.",
short="Convert a time between US and world time zones.",
ui="""
<div class="row">
<div class="field"><label for="tz-date">Date</label><input id="tz-date" type="date"></div>
<div class="field"><label for="tz-time">Time</label><input id="tz-time" type="time" value="09:00"></div>
<div class="field"><label for="tz-from">Time zone</label><select id="tz-from"></select></div>
</div>
<div class="btns"><button class="btn ghost" id="tz-now" type="button">Use current time</button></div>
<label class="check"><input id="tz-24" type="checkbox"> Show 24-hour clock</label>
<p class="result" id="tz-sum" aria-live="polite"></p>
<div class="table-wrap"><table class="tz-tbl"><thead><tr><th scope="col">Place</th><th scope="col">Time</th><th scope="col">UTC offset</th><th scope="col"><span class="sr-only">Remove</span></th></tr></thead><tbody id="tz-out"></tbody></table></div>
<div class="row" style="margin-top:12px">
<div class="field"><label for="tz-add">Add a time zone</label><select id="tz-add"></select></div>
</div>
<p class="count-note">Daylight saving time is applied automatically for the date you pick, using your browser’s time zone database. Your list of places is remembered in this browser only.</p>
""",
content="""
<p>The time zone converter changes a time in one place to the matching time anywhere else. Pick a date, a time and a time zone, and it shows the time in Eastern, Central, Mountain and Pacific time and in cities around the world. Add or remove places to build your own list, which is handy for scheduling calls and meetings across time zones.</p>
<h2>US time zones</h2>
<table>
<thead><tr><th>Time zone</th><th>Standard time</th><th>Daylight time</th><th>Example cities</th></tr></thead>
<tbody>
<tr><td>Eastern (ET)</td><td>EST, UTC−5</td><td>EDT, UTC−4</td><td>New York, Atlanta, Miami</td></tr>
<tr><td>Central (CT)</td><td>CST, UTC−6</td><td>CDT, UTC−5</td><td>Chicago, Dallas, Houston</td></tr>
<tr><td>Mountain (MT)</td><td>MST, UTC−7</td><td>MDT, UTC−6</td><td>Denver, Salt Lake City</td></tr>
<tr><td>Arizona</td><td>MST, UTC−7</td><td>No change</td><td>Phoenix, Tucson</td></tr>
<tr><td>Pacific (PT)</td><td>PST, UTC−8</td><td>PDT, UTC−7</td><td>Los Angeles, Seattle, Las Vegas</td></tr>
<tr><td>Alaska (AKT)</td><td>AKST, UTC−9</td><td>AKDT, UTC−8</td><td>Anchorage</td></tr>
<tr><td>Hawaii (HT)</td><td>HST, UTC−10</td><td>No change</td><td>Honolulu</td></tr>
</tbody>
</table>
<p>Within the mainland US, each zone is one hour apart, so 12:00 p.m. Eastern is 11:00 a.m. Central, 10:00 a.m. Mountain and 9:00 a.m. Pacific. Most of Arizona doesn’t use daylight saving time, so in summer it matches Pacific time and in winter it matches Mountain time.</p>
<h2>Why the gap between countries changes</h2>
<p>Countries change their clocks on different dates, and many never change at all. In 2026, the UK and the EU set their clocks back on October 25, while the US does so a week later, on November 1, so for that week New York is only 4 hours behind London instead of the usual 5. India, Pakistan, China, Japan and most of Asia don’t use daylight saving time, so their gap to the US changes by an hour twice a year. The converter applies the correct rules for whatever date you choose. Read more in <a href="/blog/when-does-daylight-saving-time-end">when daylight saving time ends</a>.</p>
<h2>How to convert time zones by hand</h2>
<ol>
<li>Find both places’ UTC offsets for that date (for example, New York is UTC−4 in summer, India is UTC+5:30 all year).</li>
<li>Subtract the first offset from the second: +5:30 − (−4) = 9½ hours.</li>
<li>Add that difference to the time. 9:00 a.m. in New York is 6:30 p.m. in India.</li>
</ol>
<p>If the answer goes past midnight, the date moves forward a day; if it goes below zero, it moves back a day. For a full guide to the US zones and which states are split between two of them, see <a href="/blog/us-time-zones">US time zones explained</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is EST the same as ET?</summary><p>Not quite. ET (Eastern Time) is the zone’s name. EST is Eastern Standard Time, UTC−5, used in winter; EDT is Eastern Daylight Time, UTC−4, used from March to November. Many people say “EST” all year, but the converter shows the correct one for the date.</p></details>
<details><summary>What is the difference between GMT and UTC?</summary><p>For everyday use they’re the same time. UTC is the modern scientific standard; GMT is the time zone used in the UK in winter. In summer the UK switches to BST, which is UTC+1.</p></details>
<details><summary>How do I schedule a meeting across time zones?</summary><p>Enter the proposed time in your own zone, add everyone’s locations, and check that the time falls in working hours for all of them. Then put the time zone in the invitation, for example “2:00 p.m. ET”.</p></details>
</div>
"""),
]
