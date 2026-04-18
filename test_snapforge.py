"""TDD tests for SnapForge static site."""
import re
from pathlib import Path

INDEX = Path(__file__).parent / "index.html"
content = INDEX.read_text(encoding="utf-8")


def test_no_jinja2_template_syntax():
    """Static HTML must not contain unrendered Jinja2 template syntax."""
    jinja_patterns = [r'{%\s*for\b', r'{%\s*endfor\b', r'{%\s*if\b', r'{%\s*endif\b',
                      r'{{\s*\w+\.\w+\s*}}']
    for pat in jinja_patterns:
        matches = re.findall(pat, content)
        assert not matches, f"Found Jinja2 syntax '{pat}' in static HTML: {matches}"


def test_background_cards_rendered():
    """bg-grid must contain actual bg-card elements, not template placeholders."""
    # Count all bg-card divs in the file
    cards = re.findall(r'<div class="bg-card">', content)
    assert len(cards) >= 8, f"Expected >= 8 background cards, found {len(cards)}"


def test_background_cards_have_names():
    """Each bg-card must have visible text (background style name)."""
    # Get all span contents inside bg-card sections
    # Find bg-card blocks and extract their spans
    card_blocks = re.findall(r'<div class="bg-card">(.*?)</div>', content, re.DOTALL)
    assert len(card_blocks) >= 8, f"Expected >= 8 bg-card blocks, found {len(card_blocks)}"

    for block in card_blocks:
        spans = re.findall(r'<span>(.+?)</span>', block)
        assert spans, f"bg-card missing span name: {block[:80]}"
        for s in spans:
            assert s.strip(), "Empty span found in bg-card"
            assert '{{' not in s, f"Unrendered template var in span: {s}"


if __name__ == "__main__":
    test_no_jinja2_template_syntax()
    print("PASS: test_no_jinja2_template_syntax")
    test_background_cards_rendered()
    print("PASS: test_background_cards_rendered")
    test_background_cards_have_names()
    print("PASS: test_background_cards_have_names")
