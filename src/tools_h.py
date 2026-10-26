"""Tool registry part H: background remover, image utilities, converters and everyday calculators."""
from tools_c import drop

T2 = "/assets/tools2.js"

TOOLS_H = [
# ---------------------------------------------------------------- background remover
dict(
slug="background-remover", name="Background Remover", cat="image", ico="BG", scripts=["/assets/bg-remover.js"],
title="Background Remover – Remove Image Background Free (No Upload)",
desc="Remove the background from any photo in seconds with AI that runs in your browser. Download a transparent PNG or add a white or colored background. Free, no sign-up, no upload.",
short="AI cut-outs with a transparent, white or colored background.",
ui=drop("bg-file", "image/jpeg,image/png,image/webp,.jpg,.jpeg,.png,.webp", "Choose a photo", "JPG, PNG or WebP. You can also paste an image. It never leaves your device.") + """
<p id="bg-msg" class="count-note" aria-live="polite"></p>
<div id="bg-out" hidden>
<div class="bg-opts" role="radiogroup" aria-label="Background">
<label><input type="radio" name="bg-bg" value="none" checked> Transparent</label>
<label><input type="radio" name="bg-bg" value="#ffffff"> White</label>
<label><input type="radio" name="bg-bg" value="#000000"> Black</label>
<label><input type="radio" name="bg-bg" value="custom"> Color <input type="color" id="bg-color" value="#2f5bea" aria-label="Background color"></label>
</div>
<img id="bg-preview" class="bg-prev checker" alt="Your image with the background removed">
<p class="count-note" id="bg-size"></p>
<div class="btns"><a class="btn" id="bg-dl" download="image-no-bg.png">Download PNG</a></div>
</div>
""",
content="""
<p>The background remover cuts the main subject out of a photo automatically. Choose an image and an AI model finds the person, product, pet or object in front, removes everything behind it, and gives you a PNG with a transparent background. You can also put the subject on white, black or any color you like, ready for a product listing, profile picture, presentation or design.</p>
<p>Unlike most background removers, this one doesn’t upload your photo. The AI runs inside your browser, so the image stays on your device. It’s free, with no sign-up, no watermark and no credits to buy.</p>
<h2>How to remove a background</h2>
<ol>
<li>Click “Choose a photo”, drag one in, or paste an image with Ctrl+V (Cmd+V on a Mac).</li>
<li>Wait a few seconds. The first time, your browser downloads the AI model (about 5 MB); after that it’s instant.</li>
<li>Pick Transparent, White, Black or a custom color.</li>
<li>Click Download. Transparent images save as PNG; images with a color background save as JPG.</li>
</ol>
<h2>What works best</h2>
<ul>
<li><strong>One clear subject</strong> that stands out from the background: a product on a table, a person, a pet, a car.</li>
<li><strong>Good contrast and lighting.</strong> A dark subject on a dark background is harder to separate.</li>
<li><strong>Sharp photos.</strong> Blurry edges make blurry cut-outs.</li>
</ul>
<p>Fine details such as flyaway hair, fur, glass and smoke are the hardest part for any background remover. The tool keeps soft edges where it isn’t sure, which usually looks more natural than a hard cut. For a perfect result on a tricky image, use it as a starting point and touch up the edges in an editor.</p>
<h2>Common uses</h2>
<ul>
<li><strong>Online store photos:</strong> marketplaces such as Amazon ask for product images on a pure white background.</li>
<li><strong>Profile pictures and headshots</strong> on a clean, consistent color.</li>
<li><strong>Stickers, logos and designs</strong> that need a transparent PNG.</li>
<li><strong>Slides and documents</strong> where a cut-out looks cleaner than a rectangle.</li>
</ul>
<p>To get the size right afterwards, use the <a href="/image-resizer">image resizer</a> or <a href="/image-cropper">image cropper</a>. Before sharing photos online, the <a href="/image-metadata-remover">metadata remover</a> strips hidden location data.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Is my photo uploaded to a server?</summary><p>No. The AI model is downloaded to your browser and the image is processed on your device. SmartToolsy never receives your photo.</p></details>
<details><summary>Is the background remover really free?</summary><p>Yes. There are no credits, watermarks or limits on resolution beyond 4,096 pixels on the longest side, which covers almost every use.</p></details>
<details><summary>Why is it slow the first time?</summary><p>Your browser downloads the AI model once (about 5 MB) and the engine that runs it. After that it’s cached, and each photo takes a second or two depending on your device.</p></details>
<details><summary>Which AI model does it use?</summary><p>U-2-Net, an open-source salient-object detection model released under the Apache 2.0 license, run with Microsoft’s ONNX Runtime for the web.</p></details>
<details><summary>Can I remove the background from a logo?</summary><p>Usually, yes, if the logo stands out clearly. For simple flat logos on a solid color, an editor’s “magic wand” or “remove color” option can give even crisper edges.</p></details>
</div>
"""),
# ---------------------------------------------------------------- image resizer
dict(
slug="image-resizer", name="Image Resizer", cat="image", ico="RS", scripts=[T2],
title="Image Resizer – Resize Images in Pixels, Percent or to a File Size (KB)",
desc="Resize JPG, PNG and WebP images to exact pixels, a percentage, or under a target size like 100 KB. Presets for social media and passport-style photos. Free, no upload.",
short="Exact pixels, percent or a target size in KB.",
ui=drop("rs-file", "image/*", "Choose an image", "JPG, PNG or WebP. Processed on your device.") + """
<div id="rs-opts" hidden>
<div class="row">
<div class="field"><label for="rs-mode">Resize by</label><select id="rs-mode"><option value="px">Pixels</option><option value="pct">Percentage</option></select></div>
<div class="field"><label for="rs-fmt">Save as</label><select id="rs-fmt"><option value="same">Same format</option><option value="image/jpeg">JPG</option><option value="image/png">PNG</option><option value="image/webp">WebP</option></select></div>
</div>
<div class="row" id="rs-px">
<div class="field"><label for="rs-w">Width (px)</label><input id="rs-w" type="number" min="1" max="16000"></div>
<div class="field"><label for="rs-h">Height (px)</label><input id="rs-h" type="number" min="1" max="16000"></div>
<div class="field"><label class="check" style="margin-top:30px"><input id="rs-lock" type="checkbox" checked> Keep proportions</label></div>
</div>
<div class="field" id="rs-pct-f" hidden><label for="rs-pct">Percentage of original size</label><input id="rs-pct" type="number" min="1" max="400" value="50"></div>
<div class="row">
<div class="field" id="rs-q-f"><label for="rs-q">Quality (1–100)</label><input id="rs-q" type="number" min="1" max="100" value="85"></div>
<div class="field"><label for="rs-kb">Max file size in KB (optional)</label><input id="rs-kb" type="number" min="5" placeholder="e.g. 100"></div>
</div>
<p class="lbl">Presets</p>
<div class="chips"><button class="chip" type="button" data-rs="1080x1080">Instagram square 1080×1080</button><button class="chip" type="button" data-rs="1080x1350">Instagram portrait 1080×1350</button><button class="chip" type="button" data-rs="1200x630">Link preview 1200×630</button><button class="chip" type="button" data-rs="1280x720">YouTube thumbnail 1280×720</button><button class="chip" type="button" data-rs="600x600">2×2 in at 300 DPI (600×600)</button></div>
<div class="btns"><button class="btn" id="rs-go" type="button">Resize</button></div>
</div>
<div id="rs-out" hidden>
<p class="count-note" id="rs-info"></p><p class="count-note" id="rs-note"></p>
<img id="rs-prev" class="bg-prev" alt="Resized image preview">
<div class="btns"><a class="btn" id="rs-dl" download>Download resized image</a></div>
</div>
""",
content="""
<p>The image resizer changes the dimensions of a photo or graphic in a couple of clicks. Set an exact width and height in pixels, scale by a percentage, or enter a maximum file size, such as 100 KB, and the tool finds the best quality that fits. It works with JPG, PNG and WebP, and your images are resized on your own device, never uploaded.</p>
<h2>How to resize an image</h2>
<ol>
<li>Choose an image. Its current size appears in the width and height boxes.</li>
<li>Type a new width; the height follows automatically while “Keep proportions” is ticked. Or switch to Percentage.</li>
<li>Optionally choose a format and a maximum file size in KB.</li>
<li>Click Resize, check the preview and size, then download.</li>
</ol>
<h2>Resizing to a specific file size</h2>
<p>Many application forms and websites limit uploads to a size such as 50 KB, 100 KB or 2 MB. Enter the limit in “Max file size” and the tool lowers the JPG or WebP quality step by step until the file fits. If it still can’t, reduce the width and height too; fewer pixels always means a smaller file. PNG files are lossless, so a size limit only works by shrinking dimensions; switch to JPG for photos.</p>
<h2>Will resizing reduce quality?</h2>
<p>Making an image smaller keeps it sharp. The tool scales down in steps for smooth, clean results. Making an image larger can’t add detail that isn’t there, so enlarged photos look softer; for print, start from the largest original you have.</p>
<p>Need a particular shape, not just a size? Use the <a href="/image-cropper">image cropper</a> first. To make files smaller without changing dimensions, try the <a href="/image-compressor">image compressor</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What does “keep proportions” do?</summary><p>It locks the aspect ratio, so changing the width updates the height automatically and the picture isn’t stretched or squashed.</p></details>
<details><summary>What size is a 2 × 2 inch photo in pixels?</summary><p>At 300 pixels per inch it’s 600 × 600 pixels. Check the exact requirements of the office or website you’re submitting to, as rules on background, head size and file size vary.</p></details>
<details><summary>Are my images uploaded?</summary><p>No. Everything happens in your browser using the canvas feature built into every modern browser.</p></details>
</div>
"""),
# ---------------------------------------------------------------- cropper
dict(
slug="image-cropper", name="Image Cropper", cat="image", ico="CR", scripts=[T2],
title="Crop Image Online – Free Image Cropper with Aspect Ratios & Circle Crop",
desc="Crop photos to any size or a fixed ratio like 1:1, 4:5, 16:9 or 9:16, or make a circle crop for profile pictures. Drag to adjust. Free, no upload.",
short="Crop to 1:1, 16:9, 4:5, 9:16 or a circle.",
ui=drop("cr-file", "image/*", "Choose an image", "JPG, PNG or WebP. Processed on your device.") + """
<p id="cr-msg" class="count-note" aria-live="polite"></p>
<div id="cr-work" hidden>
<div class="seg" role="group" aria-label="Aspect ratio"><button type="button" data-ratio="free" aria-pressed="true">Free</button><button type="button" data-ratio="1:1" aria-pressed="false">1:1</button><button type="button" data-ratio="4:5" aria-pressed="false">4:5</button><button type="button" data-ratio="16:9" aria-pressed="false">16:9</button><button type="button" data-ratio="9:16" aria-pressed="false">9:16</button><button type="button" data-ratio="3:2" aria-pressed="false">3:2</button></div>
<div class="cr-stage" id="cr-stage"><img id="cr-img" alt="Image to crop" draggable="false"><div class="cr-box" id="cr-box"><span data-h="nw"></span><span data-h="ne"></span><span data-h="sw"></span><span data-h="se"></span></div></div>
<div class="row row4">
<div class="field"><label for="cr-x">X</label><input id="cr-x" type="number" min="0"></div>
<div class="field"><label for="cr-y">Y</label><input id="cr-y" type="number" min="0"></div>
<div class="field"><label for="cr-w">Width</label><input id="cr-w" type="number" min="10"></div>
<div class="field"><label for="cr-h">Height</label><input id="cr-h" type="number" min="10"></div>
</div>
<label class="check"><input id="cr-circle" type="checkbox"> Circle crop (saves as PNG with transparent corners)</label>
<div class="btns"><button class="btn" id="cr-go" type="button">Crop and download</button></div>
</div>
""",
content="""
<p>The image cropper trims a photo to exactly the part you want. Drag the frame to choose the area, or lock it to a common shape: square for profile pictures, 4:5 for Instagram portraits, 16:9 for YouTube and presentations, or 9:16 for stories and reels. Tick “Circle crop” for round profile images with transparent corners. Your image is cropped on your own device.</p>
<h2>How to crop an image</h2>
<ol>
<li>Choose an image.</li>
<li>Pick an aspect ratio, or leave it on Free.</li>
<li>Drag the frame to move it and drag its corners to resize. For exact numbers, type the X, Y, width and height in pixels.</li>
<li>Click “Crop and download”.</li>
</ol>
<h2>Common aspect ratios</h2>
<table>
<thead><tr><th>Ratio</th><th>Used for</th></tr></thead>
<tbody>
<tr><td>1:1</td><td>Profile pictures, Instagram square posts, product photos</td></tr>
<tr><td>4:5</td><td>Instagram portrait posts</td></tr>
<tr><td>16:9</td><td>YouTube thumbnails, slides, laptop and TV screens</td></tr>
<tr><td>9:16</td><td>Instagram and Facebook Stories, Reels, TikTok, YouTube Shorts</td></tr>
<tr><td>3:2</td><td>Standard camera photos and 4 × 6 inch prints</td></tr>
</tbody>
</table>
<p>After cropping, use the <a href="/image-resizer">image resizer</a> to hit an exact pixel size, or the <a href="/background-remover">background remover</a> to cut out the subject.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Does cropping reduce quality?</summary><p>No. Cropping keeps the original pixels in the area you choose; it only removes the rest. JPG files are saved again at high quality.</p></details>
<details><summary>How do I crop a picture into a circle?</summary><p>Choose 1:1 so the frame is square, position it, tick “Circle crop” and download. The result is a PNG with transparent corners.</p></details>
<details><summary>Are my photos uploaded?</summary><p>No. Cropping happens in your browser and nothing is sent to a server.</p></details>
</div>
"""),
# ---------------------------------------------------------------- png to jpg
dict(
slug="png-to-jpg", name="PNG to JPG Converter", cat="convert", ico="PJ", scripts=[T2],
title="PNG to JPG Converter – Convert PNG to JPG Online Free (Batch)",
desc="Convert PNG images to JPG in your browser. Choose the quality and the color that replaces transparency, convert many files at once and download as ZIP. Free, no upload.",
short="Batch convert PNG to JPG with quality and background color.",
ui=drop("cv-file", "image/png,image/*", "Choose PNG images", "Select one or many. Files stay on your device.", True) + """
<div class="row">
<div class="field"><label for="cv-q">JPG quality (1–100)</label><input id="cv-q" type="number" min="1" max="100" value="92"></div>
<div class="field"><label for="cv-bg">Fill transparent areas with</label><input id="cv-bg" type="color" value="#ffffff"></div>
</div>
<p id="cv-msg" class="count-note" aria-live="polite"></p>
<ul id="cv-list" class="cv-list"></ul>
<div class="btns"><button class="btn" id="cv-all" type="button" hidden>Download all as ZIP</button></div>
""",
content="""
<p>The PNG to JPG converter turns PNG images into JPG files, which are usually much smaller and accepted everywhere. Add one file or a whole batch, choose the quality, and download each JPG or all of them in one ZIP. Conversion happens in your browser, so your images are never uploaded.</p>
<h2>How to convert PNG to JPG</h2>
<ol>
<li>Choose one or more PNG files.</li>
<li>Adjust the JPG quality if you like; 85–92 is a good balance of size and sharpness.</li>
<li>Pick the color for transparent areas (white by default), since JPG can’t store transparency.</li>
<li>Download each file, or click “Download all as ZIP”.</li>
</ol>
<h2>When to convert PNG to JPG</h2>
<ul>
<li><strong>Photos saved as PNG</strong>, such as screenshots of pictures or exports from design apps, are often several times larger than they need to be. JPG shrinks them a lot.</li>
<li><strong>Upload limits:</strong> forms and websites often accept only JPG, or have size limits PNG files exceed.</li>
<li><strong>Email and messaging:</strong> smaller files send faster.</li>
</ul>
<p>Keep PNG for logos, icons, screenshots of text and anything needing transparency. For more on the difference, read <a href="/blog/png-vs-jpg">PNG vs JPG: which should you use?</a></p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What happens to transparent backgrounds?</summary><p>JPG doesn’t support transparency, so transparent areas are filled with the color you choose. If you need to keep transparency, stay with PNG or use WebP.</p></details>
<details><summary>Will converting lose quality?</summary><p>JPG uses lossy compression, but at quality 90 or above the difference is very hard to see in photos. Sharp text and flat graphics can show slight blurring; keep those as PNG.</p></details>
<details><summary>Can I convert JPG to PNG?</summary><p>Yes, with the <a href="/webp-to-jpg">image converter</a>, which saves JPG and WebP images as PNG. Converting won’t restore detail already lost in a JPG, though.</p></details>
</div>
"""),
# ---------------------------------------------------------------- webp converter
dict(
slug="webp-to-jpg", name="WebP to JPG / PNG Converter", cat="convert", ico="WJ", scripts=[T2],
title="WebP to JPG Converter – Convert WebP to JPG or PNG Free",
desc="Convert WebP images to JPG or PNG in your browser, one at a time or in a batch, then download individually or as a ZIP. Also converts JPG to PNG. Free, no upload.",
short="Convert WebP (and other images) to JPG or PNG in a batch.",
ui=drop("cv-file", "image/webp,image/*", "Choose WebP images", "Select one or many. Files stay on your device.", True) + """
<div class="row">
<div class="field"><label for="cv-fmt">Convert to</label><select id="cv-fmt"><option value="image/jpeg">JPG</option><option value="image/png">PNG (keeps transparency)</option></select></div>
<div class="field"><label for="cv-q">JPG quality (1–100)</label><input id="cv-q" type="number" min="1" max="100" value="92"></div>
<div class="field"><label for="cv-bg">JPG background</label><input id="cv-bg" type="color" value="#ffffff"></div>
</div>
<p id="cv-msg" class="count-note" aria-live="polite"></p>
<ul id="cv-list" class="cv-list"></ul>
<div class="btns"><button class="btn" id="cv-all" type="button" hidden>Download all as ZIP</button></div>
""",
content="""
<p>WebP is a modern image format that many websites use to load faster, but plenty of apps, printers and upload forms still don’t accept it. This converter turns WebP images into JPG or PNG files that work everywhere. Convert one image or a batch, then download them separately or as a ZIP. It also converts JPG and other images to PNG. Everything runs in your browser.</p>
<h2>How to convert WebP to JPG</h2>
<ol>
<li>Choose one or more WebP files.</li>
<li>Pick JPG (smaller files) or PNG (keeps transparency).</li>
<li>Download the converted images, or all of them as a ZIP.</li>
</ol>
<h2>JPG or PNG?</h2>
<ul>
<li><strong>JPG</strong> for photos: small files, accepted by every app and website. Transparent areas are filled with the background color you choose.</li>
<li><strong>PNG</strong> for graphics, logos and anything with transparency: lossless, but larger for photos.</li>
</ul>
<p>Read more in <a href="/blog/what-is-a-webp-file">What is a WebP file, and how do you open it?</a> Converting PNGs? Use the <a href="/png-to-jpg">PNG to JPG converter</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Why do images download as WebP?</summary><p>Websites serve WebP because it’s smaller than JPG and PNG at the same quality, so pages load faster. When you save an image from such a site, you get the WebP file.</p></details>
<details><summary>Does converting reduce quality?</summary><p>Converting to PNG keeps every pixel. Converting to JPG uses lossy compression, but at quality 90+ the difference is hard to see.</p></details>
<details><summary>Are my files uploaded?</summary><p>No. Conversion uses your browser’s built-in image tools, so files never leave your device.</p></details>
</div>
"""),
# ---------------------------------------------------------------- character counter
dict(
slug="character-counter", name="Character Counter", cat="text", ico="CC", scripts=[T2],
title="Character Counter – Count Characters With & Without Spaces",
desc="Count characters with and without spaces, words, lines and bytes as you type, and check limits for X, Instagram, LinkedIn, YouTube, SMS and Google snippets. Free.",
short="Characters, words and social media limits as you type.",
ui="""
<div class="field"><label for="cc-text">Your text</label><textarea id="cc-text" rows="8" placeholder="Type or paste text…"></textarea></div>
<div class="stats">
<div class="stat"><b id="cc-chars">0</b><span>Characters</span></div>
<div class="stat"><b id="cc-nosp">0</b><span>Without spaces</span></div>
<div class="stat"><b id="cc-words">0</b><span>Words</span></div>
<div class="stat"><b id="cc-lines">0</b><span>Lines</span></div>
<div class="stat"><b id="cc-bytes">0</b><span>Bytes (UTF-8)</span></div>
</div>
<p class="count-note" id="cc-sms"></p>
<h3 class="seo-h">Platform limits</h3>
<ul class="cc-limits" id="cc-limits"></ul>
""",
content="""
<p>The character counter shows how many characters are in your text, with and without spaces, as you type. It also counts words, lines and bytes, works out how many SMS messages the text would take, and compares it against the limits of popular platforms so you can see at a glance whether your post, caption or title will fit.</p>
<h2>How characters are counted</h2>
<ul>
<li><strong>Characters</strong> includes letters, numbers, punctuation, spaces and line breaks. Each emoji counts as one character here, though some platforms count certain emoji as two.</li>
<li><strong>Without spaces</strong> leaves out spaces, tabs and line breaks, a figure some assignments and forms ask for.</li>
<li><strong>Bytes</strong> is the size in UTF-8, useful for database fields and technical limits. Accented letters take two bytes and most emoji four.</li>
</ul>
<h2>Character limits to know</h2>
<table>
<thead><tr><th>Where</th><th>Limit</th></tr></thead>
<tbody>
<tr><td>X (Twitter) post</td><td>280 characters (longer for paid accounts)</td></tr>
<tr><td>Instagram caption</td><td>2,200 characters</td></tr>
<tr><td>LinkedIn post</td><td>3,000 characters</td></tr>
<tr><td>YouTube title / description</td><td>100 / 5,000 characters</td></tr>
<tr><td>Pinterest pin description</td><td>500 characters</td></tr>
<tr><td>Text message (SMS)</td><td>160 characters, or 70 with emoji or special characters</td></tr>
<tr><td>Google title / meta description</td><td>About 60 / 160 characters before they’re cut</td></tr>
</tbody>
</table>
<p>See every limit in one place in our <a href="/blog/social-media-character-limits">social media character limits guide</a>. For reading time and keyword counts, use the <a href="/word-counter">word counter</a>; for search snippets, the <a href="/serp-preview-tool">SERP preview tool</a> measures in pixels.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Do spaces count as characters?</summary><p>Yes, on almost every platform and form. That’s why the main total includes spaces; the “without spaces” figure is shown separately.</p></details>
<details><summary>Why does my text message split into several messages?</summary><p>A standard SMS holds 160 characters. Longer texts are split into parts of 153 characters each. Any emoji or special character switches the whole message to a different encoding with only 70 characters per message (67 per part).</p></details>
<details><summary>Is my text saved?</summary><p>No. Counting happens in your browser and nothing is sent anywhere.</p></details>
</div>
"""),
# ---------------------------------------------------------------- GPA
dict(
slug="gpa-calculator", name="GPA Calculator", cat="calc", ico="GP", scripts=[T2],
title="GPA Calculator – Weighted & Unweighted GPA for High School and College",
desc="Calculate your unweighted and weighted GPA on a 4.0 scale from letter grades and credits, with Honors and AP/IB courses, plus your new cumulative GPA. Free.",
short="Weighted and unweighted GPA from grades and credits.",
ui="""
<div class="table-wrap"><table class="gpa-tbl"><thead><tr><th>Course</th><th>Grade</th><th>Credits</th><th>Level</th><th></th></tr></thead><tbody id="gpa-rows"></tbody></table></div>
<div class="btns"><button class="btn ghost" id="gpa-add" type="button">+ Add course</button></div>
<div class="row" style="margin-top:12px">
<div class="field"><label for="gpa-prev">Current cumulative GPA (optional)</label><input id="gpa-prev" type="number" min="0" max="5" step="0.01" placeholder="e.g. 3.40"></div>
<div class="field"><label for="gpa-prev-cr">Credits completed so far</label><input id="gpa-prev-cr" type="number" min="0" step="0.5" placeholder="e.g. 30"></div>
</div>
<div class="stats">
<div class="stat"><b id="gpa-unw">—</b><span>Unweighted GPA</span></div>
<div class="stat"><b id="gpa-w">—</b><span>Weighted GPA</span></div>
<div class="stat"><b id="gpa-cum">—</b><span>New cumulative GPA</span></div>
<div class="stat"><b id="gpa-cr">0</b><span>Credits this term</span></div>
</div>
""",
content="""
<p>The GPA calculator works out your grade point average from your letter grades and course credits. It shows both the unweighted GPA on the standard 4.0 scale and a weighted GPA that gives extra points for Honors and AP or IB classes. Add your current GPA and credits to see your new cumulative GPA after this term.</p>
<h2>How to calculate your GPA</h2>
<ol>
<li>Enter each course, choose the letter grade and type the credits (or hours). Use 1 credit per class if your school doesn’t use credits.</li>
<li>Set the level to Honors or AP/IB for weighted classes.</li>
<li>Read your unweighted and weighted GPA. Add your previous GPA and credits for a cumulative figure.</li>
</ol>
<h2>The 4.0 grade scale</h2>
<table>
<thead><tr><th>Grade</th><th>Points</th><th>Grade</th><th>Points</th></tr></thead>
<tbody>
<tr><td>A+ / A</td><td>4.0</td><td>C+</td><td>2.3</td></tr>
<tr><td>A-</td><td>3.7</td><td>C</td><td>2.0</td></tr>
<tr><td>B+</td><td>3.3</td><td>C-</td><td>1.7</td></tr>
<tr><td>B</td><td>3.0</td><td>D+ / D / D-</td><td>1.3 / 1.0 / 0.7</td></tr>
<tr><td>B-</td><td>2.7</td><td>F</td><td>0</td></tr>
</tbody>
</table>
<div class="formula">GPA = sum of (grade points × credits) ÷ total credits</div>
<h2>Weighted vs unweighted GPA</h2>
<p>An unweighted GPA treats every class the same, so the maximum is 4.0. A weighted GPA adds a bonus for harder classes; a common system adds 0.5 for Honors and 1.0 for AP and IB, so an A in an AP class counts as 5.0. Schools differ, and some count A+ as 4.3, so check your school’s policy. Colleges often recalculate GPAs their own way, which is why many applications ask for both.</p>
<p>For a step-by-step explanation with examples, read <a href="/blog/how-to-calculate-gpa">how to calculate your GPA</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>What is a good GPA?</summary><p>On a 4.0 scale, 3.0 (a B average) is generally considered solid, 3.5 and above strong, and 3.7 or higher very strong for selective colleges. What counts as good depends on your goals.</p></details>
<details><summary>Do pass/fail classes count?</summary><p>Usually not. Leave pass/fail courses out, since they don’t have grade points.</p></details>
<details><summary>How do I raise my cumulative GPA?</summary><p>Enter your current GPA and credits, then try different grades for this term’s classes to see how much each one moves the total. Classes with more credits have the biggest effect.</p></details>
</div>
"""),
# ---------------------------------------------------------------- time card
dict(
slug="time-card-calculator", name="Time Card Calculator", cat="calc", ico="TC", scripts=[T2],
title="Time Card Calculator – Hours Worked, Breaks, Overtime & Pay",
desc="Add up hours worked for the week from start and end times, minus breaks, with overnight shifts, decimal hours, overtime over 40 hours and total pay. Free timesheet calculator.",
short="Weekly hours with breaks, overtime and pay.",
ui="""
<div class="table-wrap"><table class="tc-tbl"><thead><tr><th>Day</th><th>Start</th><th>End</th><th>Break (min)</th><th>Hours</th></tr></thead><tbody id="tc-rows"></tbody></table></div>
<div class="row" style="margin-top:12px">
<div class="field"><label for="tc-rate">Hourly rate ($, optional)</label><input id="tc-rate" type="number" min="0" step="0.01" placeholder="e.g. 18.50"></div>
<div class="field"><label for="tc-ot">Overtime after (hours/week)</label><input id="tc-ot" type="number" min="0" value="40"></div>
<div class="field"><label for="tc-otx">Overtime rate</label><input id="tc-otx" type="number" min="1" step="0.25" value="1.5"></div>
</div>
<div class="stats">
<div class="stat"><b id="tc-total">0:00</b><span>Total hours (h:mm)</span></div>
<div class="stat"><b id="tc-dec">0.00</b><span>Decimal hours</span></div>
<div class="stat"><b id="tc-otm">0:00</b><span>Overtime</span></div>
<div class="stat"><b id="tc-pay">—</b><span>Gross pay</span></div>
</div>
""",
content="""
<p>The time card calculator adds up the hours worked in a week. Enter a start and end time for each day and any unpaid break, and it totals the hours in both hours-and-minutes and decimal form, splits out overtime, and works out gross pay if you add an hourly rate. Shifts that run past midnight are handled automatically.</p>
<h2>How to use the time card calculator</h2>
<ol>
<li>Enter the start and end time for each day you worked. Leave days off blank.</li>
<li>Add unpaid break minutes, such as a 30-minute lunch.</li>
<li>Optionally enter your hourly rate and overtime rules.</li>
<li>Read the total hours, decimal hours, overtime and pay.</li>
</ol>
<h2>Why decimal hours matter</h2>
<p>Payroll systems multiply hours by a rate, so they need hours as decimals: 7 hours 45 minutes is 7.75 hours, not 7.45. To convert, divide the minutes by 60. Our guide to <a href="/blog/how-to-calculate-hours-worked">calculating hours worked</a> has a full minutes-to-decimal table.</p>
<h2>Overtime</h2>
<p>Under the US Fair Labor Standards Act, non-exempt employees must be paid at least 1.5 times their regular rate for hours over 40 in a workweek. Some states add daily overtime rules; California, for example, generally requires overtime after 8 hours in a day. This calculator uses a weekly threshold you can change; check your state’s rules and your employer’s policy for your exact situation.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>How do I enter an overnight shift?</summary><p>Just enter the real times, for example 10:00 PM to 6:30 AM. When the end time is earlier than the start, the calculator assumes the shift ended the next day.</p></details>
<details><summary>Should paid breaks be subtracted?</summary><p>No. Only enter unpaid breaks. Under federal rules, short breaks of about 5 to 20 minutes are normally paid work time, while meal periods of 30 minutes or more, when you’re fully relieved of duty, usually aren’t.</p></details>
<details><summary>Is this the same as my paycheck?</summary><p>The pay shown is gross pay before taxes and deductions. Your take-home pay will be lower.</p></details>
</div>
"""),
# ---------------------------------------------------------------- tip
dict(
slug="tip-calculator", name="Tip Calculator", cat="calc", ico="TP", scripts=[T2],
title="Tip Calculator – Work Out the Tip and Split the Bill",
desc="Calculate a tip at 15%, 18%, 20% or any rate, tip before or after tax, split the bill between any number of people and round up. Free tip and split calculator.",
short="Tip at any percentage and split the bill.",
ui="""
<div class="row">
<div class="field"><label for="tp-bill">Bill total ($)</label><input id="tp-bill" type="number" min="0" step="0.01" value="64.50"></div>
<div class="field"><label for="tp-ppl">Number of people</label><input id="tp-ppl" type="number" min="1" step="1" value="2"></div>
</div>
<div class="chips" role="group" aria-label="Tip percentage"><button class="chip" type="button" data-tip="15" aria-pressed="false">15%</button><button class="chip" type="button" data-tip="18" aria-pressed="false">18%</button><button class="chip" type="button" data-tip="20" aria-pressed="true">20%</button><button class="chip" type="button" data-tip="22" aria-pressed="false">22%</button><button class="chip" type="button" data-tip="25" aria-pressed="false">25%</button></div>
<div class="row" style="margin-top:12px">
<div class="field"><label for="tp-pct">Tip (%)</label><input id="tp-pct" type="number" min="0" step="0.5" value="20"></div>
<div class="field"><label for="tp-tax">Tax included in the bill ($, optional)</label><input id="tp-tax" type="number" min="0" step="0.01" placeholder="e.g. 5.20"></div>
</div>
<label class="check"><input id="tp-pretax" type="checkbox"> Tip on the amount before tax</label>
<label class="check"><input id="tp-round" type="checkbox"> Round each person’s share up to the nearest dollar</label>
<div class="stats">
<div class="stat"><b id="tp-tip">$0.00</b><span>Tip</span></div>
<div class="stat"><b id="tp-total">$0.00</b><span>Total with tip</span></div>
<div class="stat"><b id="tp-each">$0.00</b><span>Each person pays</span></div>
<div class="stat"><b id="tp-tipeach">$0.00</b><span>Tip per person</span></div>
</div>
<p class="count-note" id="tp-eff"></p>
""",
content="""
<p>The tip calculator works out how much to tip and what everyone owes when you split the bill. Enter the bill, choose a tip percentage, and set the number of people. You can tip on the amount before tax and round each share up to a whole dollar to make paying easier.</p>
<h2>How to calculate a tip</h2>
<div class="formula">Tip = bill × tip percentage ÷ 100<br>Each person = (bill + tip) ÷ number of people</div>
<p>A quick mental shortcut for 20%: move the decimal point one place left to get 10%, then double it. On a $64.50 bill, 10% is $6.45, so 20% is $12.90.</p>
<h2>How much to tip in the US</h2>
<p>Customs vary by region and service, but these are common ranges:</p>
<table>
<thead><tr><th>Service</th><th>Typical tip</th></tr></thead>
<tbody>
<tr><td>Sit-down restaurant</td><td>15–20%, more for great service</td></tr>
<tr><td>Bar</td><td>$1–2 per drink or 15–20% of the tab</td></tr>
<tr><td>Food delivery</td><td>15–20%, with a few dollars minimum</td></tr>
<tr><td>Taxi or rideshare</td><td>15–20%</td></tr>
<tr><td>Hair salon or barber</td><td>15–20%</td></tr>
</tbody>
</table>
<p>Our guide on <a href="/blog/how-much-to-tip">how much to tip</a> covers more situations, including counter service and hotels.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>Should I tip on the total before or after tax?</summary><p>Either is acceptable. Etiquette guides traditionally suggest tipping on the pre-tax amount, but many people tip on the total for simplicity. Tick “Tip on the amount before tax” and enter the tax to calculate it the traditional way.</p></details>
<details><summary>Is a service charge the same as a tip?</summary><p>Not always. Check the bill: if a service charge or gratuity is already included, an additional tip is optional.</p></details>
</div>
"""),
# ---------------------------------------------------------------- salary
dict(
slug="salary-to-hourly", name="Salary to Hourly Calculator", cat="calc", ico="SH", scripts=[T2],
title="Salary to Hourly Calculator – Convert Annual Salary to Hourly Pay",
desc="Convert a yearly salary to hourly, daily, weekly, biweekly and monthly pay, or an hourly wage to annual salary. Adjust hours per week and weeks per year. Free.",
short="Convert between hourly, weekly, monthly and yearly pay.",
ui="""
<div class="row">
<div class="field"><label for="sh-amt">Pay amount ($)</label><input id="sh-amt" type="number" min="0" step="0.01" value="60000"></div>
<div class="field"><label for="sh-per">Per</label><select id="sh-per"><option value="year" selected>Year</option><option value="month">Month</option><option value="semimonth">Twice a month</option><option value="biweek">Every two weeks</option><option value="week">Week</option><option value="day">Day</option><option value="hour">Hour</option></select></div>
<div class="field"><label for="sh-hours">Hours per week</label><input id="sh-hours" type="number" min="1" max="100" step="0.5" value="40"></div>
<div class="field"><label for="sh-weeks">Weeks worked per year</label><input id="sh-weeks" type="number" min="1" max="52" step="1" value="52"></div>
</div>
<p class="result" id="sh-sum"></p>
<table class="sh-tbl"><tbody id="sh-out"></tbody></table>
<p class="count-note">Figures are before taxes and deductions.</p>
""",
content="""
<p>The salary to hourly calculator converts pay between hourly, daily, weekly, biweekly, twice-monthly, monthly and yearly amounts. Enter a salary to see what it works out to per hour, or enter an hourly wage to see the annual equivalent. Adjust the hours per week and weeks per year to match your job.</p>
<h2>How to convert salary to hourly</h2>
<div class="formula">Hourly pay = annual salary ÷ (hours per week × weeks per year)</div>
<p>A full-time US job is usually counted as 40 hours a week for 52 weeks, or 2,080 hours a year. So $60,000 ÷ 2,080 = about <strong>$28.85 an hour</strong>.</p>
<h2>Quick reference (40 hours a week, 52 weeks)</h2>
<table>
<thead><tr><th>Yearly</th><th>Hourly</th><th>Monthly</th></tr></thead>
<tbody>
<tr><td>$30,000</td><td>$14.42</td><td>$2,500</td></tr>
<tr><td>$40,000</td><td>$19.23</td><td>$3,333</td></tr>
<tr><td>$50,000</td><td>$24.04</td><td>$4,167</td></tr>
<tr><td>$60,000</td><td>$28.85</td><td>$5,000</td></tr>
<tr><td>$75,000</td><td>$36.06</td><td>$6,250</td></tr>
<tr><td>$100,000</td><td>$48.08</td><td>$8,333</td></tr>
</tbody>
</table>
<p>A handy shortcut: roughly halve the annual salary and drop the thousands. $60,000 a year is about $30 an hour; $40,000 is about $20.</p>
<h2>Things the simple conversion leaves out</h2>
<ul>
<li><strong>Taxes:</strong> all figures are gross. Federal and state income tax, Social Security and Medicare reduce take-home pay.</li>
<li><strong>Unpaid time off:</strong> if you’re paid hourly and take two unpaid weeks, use 50 weeks.</li>
<li><strong>Overtime and benefits:</strong> salaried roles may include health insurance and retirement contributions worth thousands a year; hourly roles may pay overtime.</li>
</ul>
<p>For a full table of common salaries, see <a href="/blog/salary-to-hourly-wage-table">what common salaries are per hour</a>. To total actual hours worked, use the <a href="/time-card-calculator">time card calculator</a>.</p>
<h2>Frequently asked questions</h2>
<div class="faq">
<details><summary>How many work hours are in a year?</summary><p>2,080 at 40 hours a week for 52 weeks. Subtract hours for unpaid holidays or time off if they apply to you.</p></details>
<details><summary>Biweekly or semimonthly: what’s the difference?</summary><p>Biweekly pay comes every two weeks, 26 times a year. Semimonthly pay comes twice a month, 24 times a year, so each paycheck is slightly larger.</p></details>
</div>
"""),
]
