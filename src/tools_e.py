"""Tool registry part E: home and construction calculators."""

UNIT_OPTS = '<option value="ft" selected>feet</option><option value="in">inches</option><option value="yd">yards</option><option value="m">meters</option>'


def dim(id, label, val, unit="ft"):
    opts = UNIT_OPTS.replace(' selected', '').replace(f'value="{unit}"', f'value="{unit}" selected')
    return f'<div class="field"><label for="{id}">{label}</label><div class="split"><input id="{id}" type="number" min="0" step="any" value="{val}"><select id="{id}-u" aria-label="{label} unit">{opts}</select></div></div>'


TOOLS_E = [
# ---------------------------------------------------------------- gravel
dict(
slug="gravel-calculator", name="Gravel Calculator", cat="home", ico="Gr",
title="Gravel Calculator – How Much Gravel Do I Need? (Tons & Yards)",
desc="Work out how much gravel you need in cubic yards and tons for a driveway, path or patio, plus the estimated cost. Free gravel estimator.",
short="Cubic yards, tons and cost of gravel for driveways and paths.",
ui="""<div class="row">""" + dim("gv-l", "Length", 40) + dim("gv-w", "Width", 12) + dim("gv-d", "Depth", 4, "in") + """</div>
<div class="row">
 <div class="field"><label for="gv-den">Density (tons per cubic yard)</label><input id="gv-den" type="number" min="0.5" step="0.05" value="1.4"></div>
 <div class="field"><label for="gv-extra">Extra for compaction & waste (%)</label><input id="gv-extra" type="number" min="0" step="1" value="10"></div>
 <div class="field"><label for="gv-price">Price per ton ($, optional)</label><input id="gv-price" type="number" min="0" step="0.5" placeholder="e.g. 45"></div>
</div>
<div class="stats" aria-live="polite">
 <div class="stat"><b id="gv-yd">—</b><span>Cubic yards</span></div>
 <div class="stat"><b id="gv-t">—</b><span>Tons</span></div>
 <div class="stat"><b id="gv-ft">—</b><span>Cubic feet</span></div>
 <div class="stat"><b id="gv-cost">—</b><span>Estimated cost</span></div>
</div>
""",
content="""
<p>The gravel calculator tells you how much gravel to order for a driveway, walkway, patio base or drainage area. Enter the length, width and depth of the area and you get the volume in cubic yards, the weight in tons, and an estimated cost if you know your supplier’s price per ton. Most landscape yards in the US sell gravel by the ton or by the cubic yard, so the calculator shows both.</p>
<h2>How to use it</h2>
<ol>
<li>Measure the length and width of the area. For an irregular shape, split it into rectangles and add the results.</li>
<li>Enter the depth you want, usually in inches.</li>
<li>Leave the density at 1.4 tons per cubic yard unless your supplier gives a different figure for the stone you’re buying.</li>
<li>Keep about 10% extra to allow for compaction and uneven ground.</li>
</ol>
<h2>The formula</h2>
<div class="formula">Cubic yards = length (ft) × width (ft) × depth (ft) ÷ 27<br>Tons = cubic yards × density (tons per cubic yard)</div>
<p>Example: a 40 × 12 ft driveway 4 inches deep is 40 × 12 × 0.333 = 160 cubic feet, or 5.93 cubic yards. At 1.4 tons per cubic yard that’s about 8.3 tons, or roughly 9.1 tons with 10% extra.</p>
<h2>How deep should gravel be?</h2>
<p>Depth depends on the use. Paths and patio bases commonly use 2 to 3 inches. Driveways usually need more, often 4 to 6 inches in total, built up in layers with a coarse base stone covered by a finer top layer. On soft or clay soil, or for heavy vehicles, deeper bases and landscape fabric help prevent ruts. Local contractors can advise on what works in your climate.</p>
<h2>Gravel weight varies</h2>
<p>Different stones weigh different amounts. Many common gravels weigh roughly 1.4 to 1.7 tons per cubic yard, and wet or densely graded material sits at the heavier end. If you buy by the ton, ask the supplier for the weight per cubic yard of that exact product and enter it above.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>How many tons of gravel are in a cubic yard?</summary><p>Typically about 1.4 tons, but it ranges from roughly 1.3 to 1.7 tons depending on the stone size, type and moisture.</p></details>
<details><summary>How much area does a ton of gravel cover?</summary><p>At 1.4 tons per cubic yard, one ton is about 19 cubic feet, enough for roughly 58 square feet at 4 inches deep or about 77 square feet at 3 inches.</p></details>
<details><summary>Should I order extra?</summary><p>Yes. Gravel settles and compacts, and ground is rarely perfectly level. Ordering 5–15% extra avoids a second delivery fee.</p></details>
</div>
"""),
# ---------------------------------------------------------------- cubic yards
dict(
slug="cubic-yard-calculator", name="Cubic Yard Calculator", cat="home", ico="yd³",
title="Cubic Yard Calculator – Yards of Dirt, Mulch, Soil or Concrete",
desc="Calculate cubic yards for dirt, topsoil, mulch, sand or concrete from length, width and depth in feet, inches, yards or meters. Includes bags of mulch.",
short="Cubic yards for dirt, mulch, soil and sand in any units.",
ui="""<div class="field"><span class="lbl">Shape</span>
<label class="check" style="display:inline-flex;margin-right:16px"><input type="radio" name="cy-shape" value="rect" checked> Rectangle</label>
<label class="check" style="display:inline-flex"><input type="radio" name="cy-shape" value="circle"> Circle</label></div>
<div class="row" id="cy-rect">""" + dim("cy-l", "Length", 10) + dim("cy-w", "Width", 10) + """</div>
<div class="row" id="cy-circ" hidden>""" + dim("cy-dia", "Diameter", 8) + """</div>
<div class="row">""" + dim("cy-d", "Depth", 3, "in") + """<div class="field"><label for="cy-q">Number of areas</label><input id="cy-q" type="number" min="1" step="1" value="1"></div></div>
<div class="stats" aria-live="polite">
 <div class="stat"><b id="cy-yd">—</b><span>Cubic yards</span></div>
 <div class="stat"><b id="cy-ft">—</b><span>Cubic feet</span></div>
 <div class="stat"><b id="cy-m">—</b><span>Cubic meters</span></div>
 <div class="stat"><b id="cy-bags">—</b><span>2 cu ft bags</span></div>
</div>
""",
content="""
<p>Bulk landscaping materials such as topsoil, fill dirt, mulch, compost, sand and concrete are sold by the cubic yard in the US. This calculator converts your measurements into cubic yards, and also shows cubic feet, cubic meters and the number of 2-cubic-foot bags, which is the common size for bagged mulch and soil at home improvement stores.</p>
<h2>How to use it</h2>
<ol>
<li>Choose a rectangle (beds, lawns, slabs) or a circle (tree rings, round beds).</li>
<li>Enter the measurements. Each one can use its own unit, so you can mix feet for length and inches for depth.</li>
<li>If you have several identical areas, enter how many.</li>
</ol>
<h2>The formula</h2>
<div class="formula">Cubic yards = length × width × depth (all in feet) ÷ 27<br>Circle: π × (diameter ÷ 2)² × depth ÷ 27</div>
<p>There are 27 cubic feet in a cubic yard because a yard is 3 feet, and 3 × 3 × 3 = 27. A 10 × 10 ft bed covered 3 inches deep needs 10 × 10 × 0.25 = 25 cubic feet, which is about 0.93 cubic yards, or 13 bags of 2 cubic feet.</p>
<h2>Typical depths</h2>
<ul>
<li><strong>Mulch:</strong> 2–4 inches around plants and trees, keeping it away from trunks.</li>
<li><strong>Topsoil for a new lawn:</strong> often 4–6 inches.</li>
<li><strong>Raised garden beds:</strong> the full height of the bed, often 8–12 inches.</li>
<li><strong>Sand under pavers:</strong> about 1 inch of bedding sand over a compacted base.</li>
</ul>
<h2>Bulk or bags?</h2>
<p>One cubic yard equals 13.5 bags of 2 cubic feet. For small jobs bags are convenient; for anything over a couple of cubic yards, bulk delivery is usually cheaper and quicker. For gravel and stone sold by weight, use the <a href="/gravel-calculator">gravel calculator</a>; for concrete with bag counts, use the <a href="/concrete-calculator">concrete calculator</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>How many square feet does a cubic yard cover?</summary><p>324 square feet at 1 inch deep, 108 square feet at 3 inches, and 81 square feet at 4 inches.</p></details>
<details><summary>How much does a cubic yard of dirt weigh?</summary><p>Usually somewhere around a ton or more, depending on soil type and moisture. Check that your vehicle or trailer can carry it before picking up.</p></details>
</div>
"""),
# ---------------------------------------------------------------- concrete
dict(
slug="concrete-calculator", name="Concrete Calculator", cat="home", ico="Cn",
title="Concrete Calculator – Cubic Yards & Bags for Slabs and Footings",
desc="Calculate how much concrete you need for a slab, footing or round column in cubic yards, plus the number of 40, 60 or 80 lb bags of premix.",
short="Cubic yards and 40/60/80 lb bags for slabs and columns.",
ui="""<div class="field"><span class="lbl">Shape</span>
<label class="check" style="display:inline-flex;margin-right:16px"><input type="radio" name="cc-shape" value="slab" checked> Slab, footing or wall</label>
<label class="check" style="display:inline-flex"><input type="radio" name="cc-shape" value="col"> Round column or post hole</label></div>
<div class="row" id="cc-slab">""" + dim("cc-l", "Length", 10) + dim("cc-w", "Width", 10) + dim("cc-t", "Thickness", 4, "in") + """</div>
<div class="row" id="cc-col" hidden>""" + dim("cc-dia", "Diameter", 12, "in") + dim("cc-h", "Depth / height", 3) + """</div>
<div class="row">
 <div class="field"><label for="cc-q">Quantity</label><input id="cc-q" type="number" min="1" step="1" value="1"></div>
 <div class="field"><label for="cc-waste">Extra for waste (%)</label><input id="cc-waste" type="number" min="0" step="1" value="10"></div>
</div>
<div class="stats" aria-live="polite">
 <div class="stat"><b id="cc-yd">—</b><span>Cubic yards</span></div>
 <div class="stat"><b id="cc-ft">—</b><span>Cubic feet</span></div>
 <div class="stat"><b id="cc-80">—</b><span>80 lb bags</span></div>
 <div class="stat"><b id="cc-60">—</b><span>60 lb bags</span></div>
 <div class="stat"><b id="cc-40">—</b><span>40 lb bags</span></div>
</div>
""",
content="""
<p>The concrete calculator estimates the volume of concrete for a slab, patio, footing, wall or round post hole, in cubic yards for ready-mix delivery and in bags for premixed concrete you mix yourself. A small allowance for waste is included because forms bulge, ground is uneven and some concrete is always left in the mixer.</p>
<h2>How to use it</h2>
<ol>
<li>Choose a slab (also use this for footings and walls) or a round column.</li>
<li>Enter the dimensions. Thickness is usually given in inches.</li>
<li>Enter how many identical pours you need, such as the number of fence post holes.</li>
<li>Keep 5–10% extra, more if the ground is uneven.</li>
</ol>
<h2>The formulas</h2>
<div class="formula">Slab: length × width × thickness (ft) ÷ 27 = cubic yards<br>Column: π × (diameter ÷ 2)² × height (ft) ÷ 27</div>
<p>A 10 × 10 ft patio 4 inches thick is 10 × 10 × 0.333 = 33.3 cubic feet, or 1.23 cubic yards. With 10% extra, that’s about 1.36 cubic yards.</p>
<h2>How many bags of concrete?</h2>
<p>Premixed concrete bag yields are printed on the bag. Common figures for standard concrete mix are about 0.60 cubic feet for an 80 lb bag, 0.45 cubic feet for a 60 lb bag and 0.30 cubic feet for a 40 lb bag, which the calculator uses. Check your brand’s label, especially for fast-setting or high-strength mixes. For jobs larger than about one cubic yard, ready-mix delivery is usually easier than mixing dozens of bags by hand.</p>
<h2>Typical thicknesses</h2>
<ul>
<li><strong>Walkways and patios:</strong> commonly 4 inches.</li>
<li><strong>Driveways:</strong> often 4–6 inches, thicker for heavy vehicles.</li>
<li><strong>Footings and post holes:</strong> follow local building code and the post manufacturer’s instructions; frost depth varies widely across the US.</li>
</ul>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>How many 80 lb bags make a cubic yard?</summary><p>About 45, since a cubic yard is 27 cubic feet and each 80 lb bag yields about 0.6 cubic feet.</p></details>
<details><summary>How many 60 lb bags make a cubic yard?</summary><p>About 60 bags, at roughly 0.45 cubic feet per bag.</p></details>
<details><summary>Does this include rebar or gravel base?</summary><p>No. It covers concrete only. Use the <a href="/gravel-calculator">gravel calculator</a> for a compacted stone base.</p></details>
</div>
"""),
# ---------------------------------------------------------------- roofing
dict(
slug="roofing-calculator", name="Roofing Calculator", cat="home", ico="Rf",
title="Roofing Calculator – Roof Area, Squares & Shingle Bundles",
desc="Estimate roof area from your home’s footprint and roof pitch, then get roofing squares and bundles of shingles with waste included. Free roof square footage calculator.",
short="Roof area, squares and shingle bundles from footprint and pitch.",
ui="""<div class="row">
 <div class="field"><label for="rf-l">House length (ft)</label><input id="rf-l" type="number" min="0" step="any" value="50"></div>
 <div class="field"><label for="rf-w">House width (ft)</label><input id="rf-w" type="number" min="0" step="any" value="30"></div>
 <div class="field"><label for="rf-o">Overhang (inches)</label><input id="rf-o" type="number" min="0" step="1" value="12"></div>
</div>
<div class="row">
 <div class="field"><label for="rf-p">Roof pitch (rise per 12 in)</label><select id="rf-p">""" + "".join(f'<option value="{p}"{" selected" if p == 6 else ""}>{p}/12</option>' for p in range(0, 19)) + """</select></div>
 <div class="field"><label for="rf-waste">Waste (%)</label><select id="rf-waste"><option value="10" selected>10% (gable roof)</option><option value="15">15% (hip roof)</option><option value="20">20% (complex roof)</option></select></div>
 <div class="field"><label for="rf-b">Bundles per square</label><input id="rf-b" type="number" min="1" step="1" value="3"></div>
</div>
<div class="stats" aria-live="polite">
 <div class="stat"><b id="rf-area">—</b><span>Roof area (sq ft)</span></div>
 <div class="stat"><b id="rf-sq">—</b><span>Squares (with waste)</span></div>
 <div class="stat"><b id="rf-bun">—</b><span>Bundles of shingles</span></div>
 <div class="stat"><b id="rf-f">—</b><span>Pitch multiplier</span></div>
</div>
""",
content="""
<p>The roofing calculator estimates the area of a roof and the materials to cover it, without climbing a ladder. Enter your home’s length and width (from plans, a tape measure or an online map), the eave overhang and the roof pitch. You get the roof surface area, the number of roofing squares and the bundles of shingles to buy, with a waste allowance included.</p>
<h2>How to use it</h2>
<ol>
<li>Enter the house’s outside length and width in feet.</li>
<li>Add the overhang, the distance the roof extends past the walls. 12 inches is common.</li>
<li>Choose the pitch: how many inches the roof rises for every 12 inches across. Many US homes fall between 4/12 and 9/12.</li>
<li>Pick a waste allowance based on the roof shape.</li>
</ol>
<h2>How roof area is calculated</h2>
<div class="formula">Footprint = (length + 2 × overhang) × (width + 2 × overhang)<br>Pitch multiplier = √(1 + (rise ÷ 12)²)<br>Roof area = footprint × pitch multiplier</div>
<p>A sloped roof has more surface than the ground it covers. The pitch multiplier accounts for that: a 6/12 roof has a multiplier of about 1.118, so a 52 × 32 ft footprint (1,664 sq ft) has about 1,860 sq ft of roof. This works for simple gable and hip roofs; dormers, valleys and multiple levels add area, so measure those sections separately or use a higher waste figure.</p>
<h2>Squares and bundles</h2>
<p>Roofers measure in <strong>squares</strong>: one square is 100 square feet of roof. Most standard asphalt shingles come in bundles that cover about a third of a square, so 3 bundles per square is the usual figure. Check the product label, as some heavier architectural shingles use more bundles per square.</p>
<h2>Why add waste?</h2>
<p>Shingles are cut at edges, ridges, hips and valleys, and starter strips and ridge caps use extra material. Around 10% is typical for a simple gable roof and 15% or more for hip roofs and roofs with several valleys.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>How do I find my roof pitch?</summary><p>Hold a level horizontally against the roof or a rafter, measure 12 inches along it, then measure straight up to the roof surface. That vertical distance in inches is the rise, so 6 inches means a 6/12 pitch.</p></details>
<details><summary>Does this include underlayment and nails?</summary><p>No. It estimates shingles. Underlayment is usually sold in rolls covering a stated number of squares, so use the squares figure to work it out.</p></details>
<details><summary>Is this an accurate quote?</summary><p>It is an estimate for planning and budgeting. A roofer will measure the actual roof and include labor, tear-off and disposal.</p></details>
</div>
"""),
]
