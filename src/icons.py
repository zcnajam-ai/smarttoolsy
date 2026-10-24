"""Tool and category icons.

SVGs are Material Design Icons by Pictogrammers (see icons/LICENSE),
vendored in src/icons so the build has no outside dependency.
"""
import os
import re

_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
_cache = {}

TOOL_ICON = {
    # PDF
    "merge-pdf": "file-multiple-outline",
    "split-pdf": "content-cut",
    "jpg-to-pdf": "file-image-outline",
    "pdf-to-jpg": "file-jpg-box",
    "delete-pdf-pages": "file-remove-outline",
    "add-pages-to-pdf": "file-plus-outline",
    "txt-to-pdf": "file-document-outline",
    # Calculators
    "age-calculator": "cake-variant-outline",
    "bmi-calculator": "human-male-height-variant",
    "percentage-calculator": "percent-outline",
    "loan-calculator": "cash-multiple",
    "discount-calculator": "tag-outline",
    "date-difference-calculator": "calendar-range",
    "mortgage-calculator": "home-percent-outline",
    "amortization-calculator": "table-large",
    # Home & construction
    "gravel-calculator": "dump-truck",
    "cubic-yard-calculator": "cube-outline",
    "concrete-calculator": "wheel-barrow",
    "roofing-calculator": "home-outline",
    # Text
    "word-counter": "counter",
    "case-converter": "format-letter-case",
    "lorem-ipsum-generator": "text-long",
    "text-cleaner": "broom",
    "slug-generator": "link-variant",
    # Image
    "image-compressor": "image-size-select-large",
    # Converters
    "unit-converter": "ruler",
    "color-converter": "palette-outline",
    # Generators
    "password-generator": "key-variant",
    "qr-code-generator": "qrcode",
    "random-number-generator": "dice-5-outline",
    # Developer
    "base64-encoder-decoder": "swap-horizontal",
    "unix-timestamp-converter": "clock-outline",
    "json-formatter": "code-json",
}

CAT_ICON = {
    "pdf": "file-pdf-box",
    "calc": "calculator-variant-outline",
    "home": "hammer-wrench",
    "text": "format-text",
    "image": "image-outline",
    "convert": "swap-horizontal",
    "generate": "auto-fix",
    "dev": "code-braces",
}


def svg(name, cls="ico-svg"):
    """Inline SVG for an icon name, coloured with currentColor and hidden from screen readers."""
    if name not in _cache:
        with open(os.path.join(_DIR, name + ".svg"), encoding="utf-8") as f:
            raw = f.read().strip()
        _cache[name] = re.sub(r"^<svg ", '<svg focusable="false" aria-hidden="true" fill="currentColor" ', raw)
    return _cache[name].replace("<svg ", f'<svg class="{cls}" ', 1)


def tool_svg(slug, cls="ico-svg"):
    return svg(TOOL_ICON[slug], cls)


def cat_svg(cat, cls="ico-svg"):
    return svg(CAT_ICON[cat], cls)
