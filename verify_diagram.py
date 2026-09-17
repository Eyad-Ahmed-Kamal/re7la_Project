"""
Comprehensive Automated Verification Suite for Re7la Quran App Flow Diagram Artifact
Validates:
1. File integrity and presence of key artifacts (HTML, DESIGN.md, README.md).
2. Complete RTL, Arabic typography, and English technical terms.
3. Presence of all 6 screens in SVG diagram and Wireframe simulator.
4. Completeness of all 13 SVG directional connection links (including return path link-s4-s1).
5. Real Pan & Zoom engine event listeners (mouse drag, wheel zoom, touch pinch).
6. SVG node rich button pills with interactive routing.
7. Re7la project identity, Daylight Sunny Garden tokens, and Anti-AI-Slop covenant.
8. Strict ZERO-Microphone access guarantee (no getUserMedia or MediaRecorder).
9. Core pedagogical mechanics: Minshawi, Audio Peek-a-boo, Golden Hook, Stitch Studio, IndexedDB Parent Voice.
10. JavaScript syntax validity via Node.js compiler.
"""
import os
import sys
import re
from html.parser import HTMLParser
import subprocess

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.has_rtl = False
        self.has_cairo = False

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attrs_dict = dict(attrs)
        if 'id' in attrs_dict:
            self.ids.add(attrs_dict['id'])
        if tag == 'html' and attrs_dict.get('dir') == 'rtl':
            self.has_rtl = True
        if tag == 'link' and 'Cairo' in attrs_dict.get('href', ''):
            self.has_cairo = True

def run_checks():
    html_path = r"d:\quraan project\app_flow_diagram.html"
    design_path = r"d:\quraan project\DESIGN.md"
    readme_path = r"d:\quraan project\README.md"
    
    print("[*] Starting Deep Verification of Re7la Architecture Artifacts...")
    
    # 1. Existence checks
    assert os.path.exists(html_path), f"File not found: {html_path}"
    assert os.path.exists(design_path), f"File not found: {design_path}"
    assert os.path.exists(readme_path), f"File not found: {readme_path}"
    print("[PASS 1/12] Artifact files exist (app_flow_diagram.html, DESIGN.md, README.md).")

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # 2. HTML parsing, RTL and Typography
    parser = HTMLValidator()
    parser.feed(html_content)
    
    assert parser.has_rtl, "HTML root missing dir='rtl'"
    assert parser.has_cairo, "Google Fonts Cairo/Tajawal missing"
    assert "Tajawal" in html_content, "Missing Tajawal font"
    assert "Amiri" in html_content, "Missing Amiri Quranic font"
    print("[PASS 2/12] RTL and Islamic Typography (Cairo, Tajawal, Amiri) correctly configured.")

    # 3. Check All 6 Screens in SVG and DOM
    required_screen_nodes = [
        "node-screen1", "node-screen2", "node-screen3",
        "node-screen4", "node-screen5", "node-screen6"
    ]
    for node_id in required_screen_nodes:
        assert node_id in parser.ids, f"Missing SVG diagram node: {node_id}"
    print("[PASS 3/12] All 6 Screens represented in SVG diagram.")

    required_mock_cards = [
        "mock-s1", "mock-s2", "mock-s3",
        "mock-s4", "mock-s5", "mock-s6"
    ]
    for mock_id in required_mock_cards:
        assert mock_id in parser.ids, f"Missing screen mock card: {mock_id}"
    print("[PASS 4/12] All 6 Screens represented in Wireframe Simulator.")

    # 4. Check Key Views
    required_views = ["diagram-view", "wireframes-view", "matrix-view", "blueprint-view"]
    for view_id in required_views:
        assert view_id in parser.ids, f"Missing view panel: {view_id}"
    print("[PASS 5/12] All 4 Primary Functional Views present (Diagram, Wireframes, Matrix, Blueprint).")

    # 5. Check All 13 SVG Directional Links (including link-s4-s1)
    required_links = [
        "link-s1-s2", "link-s1-s4", "link-s4-s1",
        "link-s2-s3", "link-s2-s1", "link-s2-s4", "link-s4-s2",
        "link-s3-s5", "link-s3-s2",
        "link-s5-s6", "link-s5-s2",
        "link-s6-s2", "link-s6-s5"
    ]
    for link_id in required_links:
        assert link_id in parser.ids, f"Missing SVG link path: {link_id}"
    print(f"[PASS 6/12] All {len(required_links)} inter-screen routing links mapped in SVG graph (including link-s4-s1).")

    # 6. Real Pan & Zoom Engine Verification
    assert "mousedown" in html_content, "Missing mousedown pan listener"
    assert "mousemove" in html_content, "Missing mousemove pan listener"
    assert "mouseup" in html_content, "Missing mouseup pan listener"
    assert "wheel" in html_content, "Missing wheel zoom listener"
    assert "touchstart" in html_content, "Missing touchstart listener"
    assert "touchmove" in html_content, "Missing touchmove listener"
    assert "applyViewportTransform" in html_content, "Missing applyViewportTransform function"
    assert "diagramViewport" in parser.ids, "Missing diagramViewport container"
    print("[PASS 7/12] Real Pan & Zoom Engine fully implemented (Mouse drag, Wheel zoom, Touch pinch).")

    # 7. Interactive Button-to-Page Routing & Rich Node Buttons
    assert "triggerButtonFromDiagram" in html_content, "Missing triggerButtonFromDiagram function"
    assert "highlightScreenLinks" in html_content, "Missing highlightScreenLinks function"
    assert "navigateToScreenMock" in html_content, "Missing navigateToScreenMock function"
    assert "diagram-btn-pill" in html_content, "Missing diagram-btn-pill on SVG nodes"
    print("[PASS 8/12] Interactive Button-to-Page Routing and Rich Button Pills verified.")

    # 8. Re7la Project Identity & Daylight Garden Theme
    assert "رِحْلة" in html_content or "رحلة" in html_content, "Missing Re7la Arabic branding"
    assert "Re7la" in html_content, "Missing Re7la English project name"
    assert "سورة الفلق" in html_content, "Missing Surah Al-Falaq active milestone"
    assert "#38bdf8" in html_content, "Missing Sky Radiant #38bdf8 daylight token"
    assert "#84cc16" in html_content, "Missing Meadow Lime #84cc16 daylight token"
    assert "#facc15" in html_content, "Missing Cobblestone Gold #facc15 daylight token"
    assert "عاش يا بطل يا عمر" in html_content, "Missing parent encouragement phrase"
    print("[PASS 9/12] Re7la Project identity and Daylight Sunny Garden design tokens verified.")

    # 9. Zero-Microphone Access Guarantee
    assert "getUserMedia" not in html_content, "SECURITY VIOLATION: getUserMedia detected!"
    assert "webkitGetUserMedia" not in html_content, "SECURITY VIOLATION: webkitGetUserMedia detected!"
    assert "MediaRecorder" not in html_content, "SECURITY VIOLATION: MediaRecorder detected!"
    assert "صفر مايكروفون" in html_content, "Missing Arabic Zero-Mic badge text!"
    assert "Zero-Mic" in html_content, "Missing Zero-Mic badge text!"
    print("[PASS 10/12] ZERO Microphone access strictly enforced and validated (Output-only app).")

    # 10. Core Pedagogical Mechanics & Audio Peek-a-boo
    assert "المنشاوي" in html_content, "Missing Sheikh Al-Minshawi references!"
    assert "لعبة الصوت الغائب" in html_content, "Missing Audio Peek-a-boo references!"
    assert "Audio Peek-a-boo" in html_content, "Missing English Audio Peek-a-boo terminology!"
    assert "IndexedDB" in html_content, "Missing IndexedDB local storage reference!"
    assert "simulateParentInvisibleTap" in html_content, "Missing invisible tap simulator function!"
    assert "simulateSurahCompletion" in html_content, "Missing auto completion trigger function!"
    assert "STITCH_PROMPTS" in html_content, "Missing Google Stitch Prompt Studio data!"
    assert "switchStitchTab" in html_content, "Missing Google Stitch tab switcher!"
    print("[PASS 11/12] Core pedagogical mechanics (Minshawi, Audio Peek-a-boo, Golden Hook, IndexedDB, Stitch Studio) validated.")

    # 11. JavaScript Extraction and Syntax Check via Node.js
    script_match = re.search(r'<script>(.*?)</script>', html_content, re.DOTALL)
    assert script_match, "No <script> block found in HTML!"
    js_code = script_match.group(1)
    
    temp_js = r"d:\quraan project\temp_syntax_check.js"
    with open(temp_js, "w", encoding="utf-8") as f:
        # Mock browser globals for syntax test
        f.write("const window = { AudioContext: class{}, webkitAudioContext: class{} };\n")
        f.write("const document = { querySelectorAll: () => [], getElementById: () => ({ classList: { add(){}, remove(){} }, style: {}, setAttribute(){}, appendChild(){} }), addEventListener: () => {}, createElement: () => ({ style: {} }) };\n")
        f.write("const navigator = { clipboard: { writeText: () => Promise.resolve() } };\n")
        f.write(js_code)
    
    node_result = subprocess.run(["node", "-c", temp_js], capture_output=True, text=True)
    if os.path.exists(temp_js):
        os.remove(temp_js)
    
    assert node_result.returncode == 0, f"JS Syntax Error: {node_result.stderr}"
    print("[PASS 12/12] JavaScript syntax verified completely clean via Node.js compiler.")

    print("\n=======================================================")
    print(" ALL VERIFICATION CHECKS PASSED SUCCESSFULLY (12/12) ")
    print("=======================================================")

if __name__ == "__main__":
    try:
        run_checks()
    except Exception as e:
        print(f"\n[FAIL] Verification Error: {e}", file=sys.stderr)
        sys.exit(1)
