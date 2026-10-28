"""Batch 3: holiday season tools (turkey calculator, Christmas budget)."""

TOOLS_I = [
    {
        "slug": "turkey-calculator",
        "name": "Turkey Size & Cooking Time Calculator",
        "cat": "home",
        "ico": "TK",
        "scripts": ["/assets/holiday.js"],
        "title": "Turkey Calculator – What Size Turkey and How Long to Cook It",
        "desc": "How big a turkey do you need and how long to cook it? Enter your guests to get the turkey size, USDA roasting time at 325°F, thawing time and a start-time plan for Thanksgiving.",
        "short": "Turkey size, thawing and roasting time for your guests.",
        "ui": """
<h2 class="mini-h">1. How big a turkey?</h2>
<div class="row">
<div class="field"><label for="tk-adults">Adults</label><input id="tk-adults" type="number" min="0" step="1" value="8"></div>
<div class="field"><label for="tk-kids">Children</label><input id="tk-kids" type="number" min="0" step="1" value="2"></div>
<div class="field"><label for="tk-left">Leftovers</label><select id="tk-left"><option value="1">No leftovers (1 lb each)</option><option value="1.5" selected>Some leftovers (1.5 lb each)</option><option value="2">Lots of leftovers (2 lb each)</option></select></div>
</div>
<div class="stats">
<div class="stat"><b id="tk-size">—</b><span>Turkey to buy</span></div>
<div class="stat"><b id="tk-breast">—</b><span>Or a bone-in breast</span></div>
</div>
<h2 class="mini-h">2. Thawing and roasting</h2>
<div class="row">
<div class="field"><label for="tk-lb">Turkey weight (lb)</label><input id="tk-lb" type="number" min="4" max="30" step="0.5" value="14"></div>
<div class="field"><label for="tk-stuffed">Stuffing</label><select id="tk-stuffed"><option value="0" selected>Unstuffed</option><option value="1">Stuffed</option></select></div>
<div class="field"><label for="tk-frozen">Starting from</label><select id="tk-frozen"><option value="0" selected>Thawed</option><option value="1">Frozen (no time to thaw)</option></select></div>
</div>
<div class="row">
<div class="field"><label for="tk-date">Dinner date</label><input id="tk-date" type="date"></div>
<div class="field"><label for="tk-time">Dinner time</label><input id="tk-time" type="time" value="16:00"></div>
</div>
<p class="result" id="tk-sum" aria-live="polite"></p>
<table class="sh-tbl tk-plan"><tbody id="tk-plan"></tbody></table>
<p class="count-note">Times follow the USDA chart for a whole turkey roasted at 325°F. Always check that the thickest part of the breast, the innermost thigh and the wing reach 165°F.</p>
""",
        "content": """
<p>This turkey calculator answers the two big Thanksgiving questions: how big a turkey to buy and how long it takes to cook. Enter your guests to get the size, then the weight to get thawing time, roasting time and a simple timetable that works back from when you want to eat.</p>
<h2>How much turkey per person?</h2>
<p>The USDA suggests about <strong>1 pound of whole turkey per person</strong>, because much of the weight is bone. If you want leftovers for sandwiches, plan on 1½ pounds each; for lots of leftovers, 2 pounds. Children usually eat about half an adult portion, which is how the calculator counts them.</p>
<table>
<thead><tr><th>Guests</th><th>No leftovers</th><th>Some leftovers</th></tr></thead>
<tbody>
<tr><td>4</td><td>4–6 lb (or a breast)</td><td>6–8 lb</td></tr>
<tr><td>6</td><td>6–8 lb</td><td>9–10 lb</td></tr>
<tr><td>8</td><td>8–10 lb</td><td>12–14 lb</td></tr>
<tr><td>10</td><td>10–12 lb</td><td>15–16 lb</td></tr>
<tr><td>12</td><td>12–14 lb</td><td>18–20 lb</td></tr>
<tr><td>16</td><td>16–18 lb</td><td>24 lb, or two smaller birds</td></tr>
</tbody>
</table>
<h2>Turkey cooking times at 325°F</h2>
<p>These are the USDA's approximate roasting times for a thawed whole turkey in a 325°F oven. Ovens vary, so start checking the temperature about 30 minutes before the shortest time.</p>
<table>
<thead><tr><th>Weight</th><th>Unstuffed</th><th>Stuffed</th></tr></thead>
<tbody>
<tr><td>8–12 lb</td><td>2¾–3 hours</td><td>3–3½ hours</td></tr>
<tr><td>12–14 lb</td><td>3–3¾ hours</td><td>3½–4 hours</td></tr>
<tr><td>14–18 lb</td><td>3¾–4¼ hours</td><td>4–4¼ hours</td></tr>
<tr><td>18–20 lb</td><td>4¼–4½ hours</td><td>4¼–4¾ hours</td></tr>
<tr><td>20–24 lb</td><td>4½–5 hours</td><td>4¾–5¼ hours</td></tr>
</tbody>
</table>
<p>Cooking a turkey straight from frozen is safe but takes about 50% longer. Let the cooked turkey rest for about 20 minutes before carving so the juices settle; the calculator builds that into the timetable.</p>
<h2>How long to thaw a turkey</h2>
<ul>
<li><strong>In the refrigerator:</strong> about 24 hours for every 4 to 5 pounds. A 16 lb turkey needs around 4 days, so move it to the fridge on the Sunday before Thanksgiving.</li>
<li><strong>In cold water:</strong> about 30 minutes per pound, with the turkey in its wrapper, fully submerged, and the water changed every 30 minutes. Cook it straight away.</li>
</ul>
<p>Never thaw a turkey on the counter. For the full timeline, read our guide on <a href="/blog/how-long-to-cook-a-turkey">how long to cook a turkey</a>, and count down to the big day with <a href="/days-until/thanksgiving">days until Thanksgiving</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What temperature should a turkey be when it is done?</summary><p>165°F, measured with a food thermometer in the thickest part of the breast, the innermost part of the thigh and the wing. If the turkey is stuffed, the center of the stuffing must also reach 165°F.</p></details>
<details><summary>Should I cook my turkey at 325 or 350?</summary><p>The USDA cooking chart is for 325°F, which cooks the turkey evenly without drying out the breast. A hotter oven shortens the time, but check the temperature often.</p></details>
<details><summary>Is it better to buy one big turkey or two small ones?</summary><p>For more than about 20 guests, two 12 to 14 lb turkeys cook faster and more evenly than one 24 lb bird, and they fit more easily in a home oven.</p></details>
</div>
""",
    },
    {
        "slug": "christmas-budget-calculator",
        "name": "Christmas Budget Calculator",
        "cat": "calc",
        "ico": "XB",
        "scripts": ["/assets/holiday.js"],
        "title": "Christmas Budget Calculator – Plan Gifts and Holiday Spending",
        "desc": "Plan your Christmas budget: list gifts by person, add food, travel and decorations, see your total, what is left and how much to save each week or paycheck until Christmas.",
        "short": "Plan gift and holiday spending and how much to save.",
        "ui": """
<div class="row">
<div class="field"><label for="cb-budget">Total holiday budget ($)</label><input id="cb-budget" type="number" min="0" step="10" value="1000"></div>
<div class="field"><label for="cb-saved">Already saved ($)</label><input id="cb-saved" type="number" min="0" step="10" value="200"></div>
<div class="field"><label for="cb-pay">I get paid</label><select id="cb-pay"><option value="7">Weekly</option><option value="14" selected>Every two weeks</option><option value="15">Twice a month</option><option value="30">Monthly</option></select></div>
</div>
<h2 class="mini-h">Gifts</h2>
<div class="table-wrap"><table class="gpa-tbl cb-tbl"><thead><tr><th>Person</th><th>Gift budget ($)</th><th></th></tr></thead><tbody id="cb-rows"></tbody></table></div>
<div class="btns"><button class="btn ghost" id="cb-add" type="button">+ Add person</button></div>
<h2 class="mini-h">Everything else</h2>
<div class="row">
<div class="field"><label for="cb-food">Food &amp; drinks ($)</label><input id="cb-food" type="number" min="0" step="5" value="200"></div>
<div class="field"><label for="cb-travel">Travel ($)</label><input id="cb-travel" type="number" min="0" step="5" value="0"></div>
<div class="field"><label for="cb-decor">Decorations &amp; tree ($)</label><input id="cb-decor" type="number" min="0" step="5" value="75"></div>
<div class="field"><label for="cb-wrap">Cards, wrapping, shipping ($)</label><input id="cb-wrap" type="number" min="0" step="5" value="40"></div>
</div>
<div class="stats">
<div class="stat"><b id="cb-total">—</b><span>Planned spending</span></div>
<div class="stat"><b id="cb-left">—</b><span>Left in budget</span></div>
<div class="stat"><b id="cb-need">—</b><span>Still to save</span></div>
<div class="stat"><b id="cb-per">—</b><span id="cb-per-lbl">Save per paycheck</span></div>
</div>
<p class="result" id="cb-sum" aria-live="polite"></p>
<p class="count-note">Your list stays in this browser only; nothing is sent anywhere.</p>
""",
        "content": """
<p>The Christmas budget calculator helps you plan holiday spending before the shopping starts. Set your total budget, list the people you are buying for, add food, travel and decorations, and it shows what you have planned, what is left, and how much to put aside from each paycheck between now and Christmas.</p>
<h2>How to set a Christmas budget</h2>
<ol>
<li><strong>Start with what you can afford,</strong> not what you spent last year. Look at your savings and how many paychecks are left before December 25.</li>
<li><strong>List everyone you buy for</strong> and give each person a number. It is easier to stick to $40 for a coworker than to a vague total.</li>
<li><strong>Count the extras.</strong> Holiday food, travel, the tree, wrapping paper and shipping often add up to as much as the gifts.</li>
<li><strong>Divide what is left to save by your paychecks.</strong> Saving a set amount each payday avoids a big credit card bill in January.</li>
</ol>
<h2>Ways to cut the total</h2>
<ul>
<li>Draw names (a Secret Santa) for large families or office groups so each person buys one gift.</li>
<li>Set a spending limit with friends, or swap experiences and homemade gifts.</li>
<li>Shop sales such as Black Friday and Cyber Monday for gifts already on your list, not extra items.</li>
<li>Order early to avoid paying for express shipping in December.</li>
</ul>
<p>See how much time you have with <a href="/days-until/christmas">days until Christmas</a>, and read our <a href="/blog/how-to-make-a-christmas-budget">guide to making a Christmas budget</a>. Remember to include year-end tips for people like your sitter or house cleaner; our guide on <a href="/blog/how-much-to-tip-for-the-holidays">how much to tip for the holidays</a> suggests amounts.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>How is the amount per paycheck worked out?</summary><p>The calculator counts how many paydays are left before December 25 based on how often you are paid, then divides the amount you still need to save by that number. If Christmas has passed, it plans for next year.</p></details>
<details><summary>Is my list saved?</summary><p>It stays only in your own browser so it is still there when you come back on the same device. Nothing is uploaded.</p></details>
</div>
""",
    },
]
