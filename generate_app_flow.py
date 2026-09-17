# -*- coding: utf-8 -*-
"""
Generator for production-grade Re7la Quran App Flow Diagram artifact.
Incorporates:
- True Pan & Zoom SVG engine (mouse drag, wheel zoom with cursor focus, touch drag, pinch zoom)
- Rich SVG screen cards displaying ALL buttons as clickable pills
- Complete 13 Bézier connection paths including missing return path link-s4-s1
- Interactive button route highlighting with animated flow pulses
- Wireframes simulator with live smooth navigation between phone mockups
- Screen 5 interactive Audio Peek-a-boo recitation simulator with Al-Minshawi
- Google Stitch Prompt Studio with 7 dedicated screen-by-screen tabs
- Web Audio API sound effects with mute toggle
- Full RTL and ECC 2.2 design engineering principles
"""
import os
import sys

def get_html_content():
    # We will build the content in cleanly separated blocks
    parts = []
    
    # BLOCK 1: HEAD & STYLES
    parts.append("""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>رِحْلة (Re7la Project) | المخطط التفاعلي الشامل لتدفق الصفحات والأزرار والهندسة المعمارية</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cairo:wght@400;500;600;700;800;900&family=Tajawal:wght@400;500;700;900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      /* Brand Palette - Re7la Daylight Sunny Garden */
      /* Re7la Daylight Sunny Garden Tokens */
      --sky-500: #38bdf8;
      --sky-600: #0284c7;
      --sky-700: #0369a1;
      --sky-100: #e0f2fe;

      --meadow-500: #84cc16;
      --meadow-600: #65a30d;
      --meadow-400: #a3e635;
      --meadow-100: #ecfccb;

      --gold-500: #facc15;
      --gold-600: #eab308;
      --gold-700: #ca8a04;
      --gold-100: #fef9c3;
      --gold-50: #fefce8;

      --mosque-teal: #0d9488;
      --mosque-teal-dark: #0f766e;
      --mosque-teal-light: #ccfbf1;

      --coral-500: #f43f5e;
      --coral-600: #e11d48;
      --coral-100: #ffe4e6;

      --primary-950: #022c22;
      --primary-900: #064e3b;
      --primary-800: #065f46;
      --primary-700: #047857;
      --primary-600: #059669;
      --primary-500: #10b981;
      --primary-400: #34d399;
      --primary-200: #a7f3d0;
      --primary-100: #d1fae5;
      --primary-50: #ecfdf5;

      --gold-700: #b45309;
      --gold-600: #d97706;
      --gold-500: #f59e0b;
      --gold-400: #fbbf24;
      --gold-200: #fde68a;
      --gold-100: #fef3c7;
      --gold-50: #fffbeb;

      --sky-700: #0369a1;
      --sky-600: #0284c7;
      --sky-500: #0ea5e9;
      --sky-100: #e0f2fe;

      --coral-600: #e11d48;
      --coral-500: #f43f5e;
      --coral-100: #ffe4e6;

      --purple-700: #6d28d9;
      --purple-600: #7c3aed;
      --purple-500: #8b5cf6;
      --purple-100: #f3e8ff;

      --slate-950: #020617;
      --slate-900: #0f172a;
      --slate-850: #131d36;
      --slate-800: #1e293b;
      --slate-700: #334155;
      --slate-600: #475569;
      --slate-400: #94a3b8;
      --slate-300: #cbd5e1;
      --slate-200: #e2e8f0;
      --slate-100: #f1f5f9;
      --slate-50: #f8fafc;

      --bg-canvas: #f8faf9;
      --surface-card: #ffffff;
      --surface-border: #e2e8f0;
      --surface-border-subtle: #edf2f7;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-light: #64748b;

      --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.04);
      --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.07), 0 1px 2px -1px rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 8px -1px rgb(0 0 0 / 0.08), 0 2px 5px -2px rgb(0 0 0 / 0.05);
      --shadow-lg: 0 10px 18px -3px rgb(0 0 0 / 0.09), 0 4px 8px -4px rgb(0 0 0 / 0.05);
      --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.05);
      --shadow-glow: 0 0 30px -5px rgba(16, 185, 129, 0.3);
      --shadow-gold: 0 0 30px -5px rgba(245, 158, 11, 0.35);

      /* ECC Concentric Radii */
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-xl: 28px;
      --radius-full: 9999px;

      --font-cairo: 'Cairo', system-ui, -apple-system, sans-serif;
      --font-tajawal: 'Tajawal', system-ui, -apple-system, sans-serif;
      --font-amiri: 'Amiri', serif;
      --font-mono: 'JetBrains Mono', Consolas, monospace;
    }

    /* Dark theme support */
    body.dark-mode {
      --bg-canvas: #090e17;
      --surface-card: #121a2d;
      --surface-border: #1e293b;
      --surface-border-subtle: #172138;
      --text-main: #f8fafc;
      --text-muted: #cbd5e1;
      --text-light: #94a3b8;
      --slate-50: #0f172a;
      --slate-100: #1e293b;
      --slate-200: #334155;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    body {
      font-family: var(--font-cairo);
      background-color: var(--bg-canvas);
      color: var(--text-main);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    /* Scrollbars */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg-canvas);
    }
    ::-webkit-scrollbar-thumb {
      background: var(--slate-300);
      border-radius: var(--radius-full);
    }
    body.dark-mode ::-webkit-scrollbar-thumb {
      background: var(--slate-700);
    }

    /* Header */
    header.app-header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--surface-border);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }
    body.dark-mode header.app-header {
      background: rgba(18, 26, 45, 0.94);
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-icon {
      width: 44px;
      height: 44px;
      background: linear-gradient(135deg, var(--primary-600), var(--primary-800));
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      font-size: 1.5rem;
      box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);
      position: relative;
    }
    .brand-icon::after {
      content: "⭐";
      position: absolute;
      top: -4px;
      right: -4px;
      font-size: 0.75rem;
    }
    .brand-text h1 {
      font-size: 1.25rem;
      font-weight: 900;
      line-height: 1.2;
      color: var(--primary-900);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    body.dark-mode .brand-text h1 {
      color: #34d399;
    }
    .brand-text .tagline {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    /* Nav Tabs */
    .nav-tabs {
      display: flex;
      align-items: center;
      background: var(--slate-100);
      padding: 4px;
      border-radius: var(--radius-full);
      gap: 4px;
      border: 1px solid var(--surface-border);
    }
    body.dark-mode .nav-tabs {
      background: var(--slate-900);
    }
    .nav-tab-btn {
      background: transparent;
      border: none;
      padding: 8px 18px;
      border-radius: var(--radius-full);
      font-family: var(--font-cairo);
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .nav-tab-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.6);
    }
    body.dark-mode .nav-tab-btn:hover {
      background: rgba(255, 255, 255, 0.08);
    }
    .nav-tab-btn.active {
      background: var(--surface-card);
      color: var(--primary-700);
      box-shadow: var(--shadow-sm);
    }
    body.dark-mode .nav-tab-btn.active {
      background: var(--primary-700);
      color: #ffffff;
    }

    /* Actions in Header */
    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-header {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: var(--radius-md);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      font-family: var(--font-cairo);
      transition: all 0.2s;
      border: 1px solid var(--surface-border);
      background: var(--surface-card);
      color: var(--text-main);
    }
    .btn-header:hover {
      background: var(--slate-100);
      border-color: var(--slate-300);
    }
    .btn-header.primary-action {
      background: linear-gradient(135deg, var(--gold-500), var(--gold-600));
      color: #ffffff;
      border: none;
      box-shadow: 0 4px 12px rgba(245, 158, 11, 0.35);
    }
    .btn-header.primary-action:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(245, 158, 11, 0.45);
    }
    .badge-ecc {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1d4ed8;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      font-family: var(--font-mono);
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    body.dark-mode .badge-ecc {
      background: rgba(30, 58, 138, 0.3);
      border-color: #1e40af;
      color: #93c5fd;
    }

    /* Main Container */
    main.main-content {
      flex: 1;
      padding: 20px 24px 40px;
      max-width: 1700px;
      margin: 0 auto;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Hero Overview Banner */
    .overview-hero {
      background: linear-gradient(135deg, var(--primary-900) 0%, var(--primary-800) 45%, #064032 100%);
      border-radius: var(--radius-xl);
      padding: 24px 32px;
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      box-shadow: var(--shadow-lg), 0 0 40px rgba(6, 78, 59, 0.25);
      position: relative;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .overview-hero::before {
      content: "";
      position: absolute;
      top: -50%;
      right: -20%;
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, rgba(245, 158, 11, 0.18) 0%, transparent 70%);
      pointer-events: none;
    }
    .overview-hero-content {
      position: relative;
      z-index: 2;
      max-width: 850px;
    }
    .hero-pill-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.16);
      backdrop-filter: blur(8px);
      padding: 4px 12px;
      border-radius: var(--radius-full);
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--gold-400);
      margin-bottom: 10px;
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .overview-hero-content h2 {
      font-size: 1.75rem;
      font-weight: 900;
      margin-bottom: 8px;
      line-height: 1.3;
    }
    .overview-hero-content p {
      font-size: 0.94rem;
      color: #e2e8f0;
      line-height: 1.6;
    }
    .overview-hero-stats {
      display: flex;
      gap: 14px;
      position: relative;
      z-index: 2;
      flex-wrap: wrap;
    }
    .hero-stat-card {
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 12px 18px;
      border-radius: var(--radius-lg);
      text-align: center;
      min-width: 100px;
      transition: transform 0.2s;
    }
    .hero-stat-card:hover {
      transform: translateY(-2px);
      background: rgba(255, 255, 255, 0.18);
    }
    .hero-stat-card .val {
      font-size: 1.65rem;
      font-weight: 900;
      color: #ffffff;
      line-height: 1.1;
      font-variant-numeric: tabular-nums;
    }
    .hero-stat-card .lbl {
      font-size: 0.76rem;
      color: var(--gold-100);
      font-weight: 700;
      margin-top: 4px;
    }

    /* Views */
    .view-panel {
      display: none;
      flex-direction: column;
      gap: 18px;
    }
    .view-panel.active {
      display: flex;
    }

    /* Control Toolbar */
    .view-toolbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      background: var(--surface-card);
      padding: 12px 18px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--surface-border);
      box-shadow: var(--shadow-xs);
    }
    .filter-pills {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .filter-btn {
      background: var(--slate-100);
      border: 1px solid transparent;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 0.82rem;
      font-family: var(--font-cairo);
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    body.dark-mode .filter-btn {
      background: var(--slate-850);
    }
    .filter-btn:hover {
      background: var(--slate-200);
      color: var(--text-main);
    }
    .filter-btn.active {
      background: var(--primary-100);
      color: var(--primary-800);
      border-color: var(--primary-300);
      font-weight: 800;
    }
    body.dark-mode .filter-btn.active {
      background: rgba(16, 185, 129, 0.2);
      color: var(--primary-300);
      border-color: var(--primary-600);
    }
    .search-box {
      display: flex;
      align-items: center;
      background: var(--slate-50);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-md);
      padding: 6px 12px;
      gap: 8px;
      min-width: 260px;
    }
    body.dark-mode .search-box {
      background: var(--slate-900);
    }
    .search-box input {
      border: none;
      background: transparent;
      color: var(--text-main);
      font-family: var(--font-cairo);
      font-size: 0.85rem;
      outline: none;
      width: 100%;
    }

    /* Diagram Interactive Canvas Workspace */
    .diagram-workspace {
      display: grid;
      grid-template-columns: 1fr 420px;
      gap: 20px;
      min-height: 750px;
    }
    @media (max-width: 1280px) {
      .diagram-workspace {
        grid-template-columns: 1fr;
      }
    }

    .diagram-canvas-container {
      background: var(--surface-card);
      border-radius: var(--radius-xl);
      border: 1px solid var(--surface-border);
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      height: 760px;
    }
    .canvas-controls-floating {
      position: absolute;
      top: 16px;
      left: 16px;
      z-index: 20;
      display: flex;
      flex-direction: column;
      gap: 6px;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(10px);
      padding: 6px;
      border-radius: var(--radius-md);
      border: 1px solid var(--surface-border);
      box-shadow: var(--shadow-md);
    }
    body.dark-mode .canvas-controls-floating {
      background: rgba(18, 26, 45, 0.92);
    }
    .canvas-tool-btn {
      width: 34px;
      height: 34px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: transparent;
      border: none;
      border-radius: var(--radius-sm);
      color: var(--text-main);
      cursor: pointer;
      font-weight: bold;
      font-size: 1.1rem;
      transition: all 0.15s;
    }
    .canvas-tool-btn:hover {
      background: var(--primary-100);
      color: var(--primary-800);
    }
    body.dark-mode .canvas-tool-btn:hover {
      background: rgba(16, 185, 129, 0.2);
      color: var(--primary-300);
    }
    .canvas-hint-pill {
      position: absolute;
      bottom: 16px;
      left: 16px;
      z-index: 20;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      color: #ffffff;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-size: 0.75rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
      pointer-events: none;
    }

    .diagram-svg-wrapper {
      flex: 1;
      width: 100%;
      height: 100%;
      cursor: grab;
      position: relative;
      background-image: radial-gradient(var(--slate-200) 1.2px, transparent 1.2px);
      background-size: 24px 24px;
      user-select: none;
      overflow: hidden;
    }
    body.dark-mode .diagram-svg-wrapper {
      background-image: radial-gradient(var(--slate-800) 1.2px, transparent 1.2px);
    }
    .diagram-svg-wrapper:active {
      cursor: grabbing;
    }

    svg.diagram-svg {
      width: 100%;
      height: 100%;
      display: block;
      touch-action: none;
    }

    /* SVG Links & Nodes */
    .link-path {
      fill: none;
      stroke: var(--slate-300);
      stroke-width: 2.5;
      stroke-linecap: round;
      stroke-linejoin: round;
      transition: stroke 0.3s, stroke-width 0.3s, opacity 0.3s;
    }
    body.dark-mode .link-path {
      stroke: var(--slate-700);
    }
    .link-path.active-link {
      stroke: var(--primary-500) !important;
      stroke-width: 4.5 !important;
      filter: drop-shadow(0 0 8px rgba(16, 185, 129, 0.7));
      stroke-dasharray: 8 4;
      animation: dashMove 1s linear infinite;
    }
    .link-path.parent-link {
      stroke: var(--gold-500);
      stroke-dasharray: 4 4;
    }
    .link-path.parent-link.active-link {
      stroke: var(--gold-500) !important;
      stroke-width: 4.5 !important;
      filter: drop-shadow(0 0 8px rgba(245, 158, 11, 0.7));
      stroke-dasharray: 8 4;
      animation: dashMove 1s linear infinite;
    }
    @keyframes dashMove {
      to {
        stroke-dashoffset: -24;
      }
    }

    .diagram-node {
      cursor: pointer;
      transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .diagram-node:hover {
      filter: drop-shadow(0 12px 24px rgba(0, 0, 0, 0.12));
    }
    .node-rect {
      rx: 16;
      ry: 16;
      fill: #ffffff;
      stroke: var(--surface-border);
      stroke-width: 2;
      filter: drop-shadow(0 8px 16px rgba(0,0,0,0.06));
      transition: all 0.25s;
    }
    body.dark-mode .node-rect {
      fill: #162035;
      stroke: #25334d;
    }
    .diagram-node.selected .node-rect {
      stroke: var(--primary-500);
      stroke-width: 3.5;
      filter: drop-shadow(0 0 20px rgba(16, 185, 129, 0.35));
    }
    .diagram-node.target-highlight .node-rect {
      stroke: var(--gold-500);
      stroke-width: 3.5;
      animation: pulseTarget 1s infinite alternate;
    }
    @keyframes pulseTarget {
      from { filter: drop-shadow(0 0 8px rgba(245, 158, 11, 0.4)); }
      to { filter: drop-shadow(0 0 24px rgba(245, 158, 11, 0.9)); }
    }

    /* Diagram SVG Button Pill */
    .diagram-btn-pill {
      cursor: pointer;
      transition: all 0.15s;
    }
    .diagram-btn-pill:hover rect {
      filter: brightness(0.95);
      stroke-width: 1.5;
    }
    .diagram-btn-pill.active-btn rect {
      stroke: #059669;
      stroke-width: 2;
      filter: drop-shadow(0 0 6px rgba(16, 185, 129, 0.5));
    }

    /* Inspector Sidebar */
    .inspector-panel {
      background: var(--surface-card);
      border-radius: var(--radius-xl);
      border: 1px solid var(--surface-border);
      box-shadow: var(--shadow-md);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      height: 760px;
    }
    .inspector-header {
      padding: 18px 22px;
      background: var(--slate-50);
      border-bottom: 1px solid var(--surface-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }
    body.dark-mode .inspector-header {
      background: var(--slate-900);
    }
    .inspector-header h3 {
      font-size: 1.05rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .inspector-body {
      flex: 1;
      padding: 20px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .screen-meta-badge {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .meta-tag {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .meta-tag.core { background: #dbeafe; color: #1e40af; }
    .meta-tag.child { background: #dcfce7; color: #166534; }
    .meta-tag.parent { background: #fef3c7; color: #92400e; }
    body.dark-mode .meta-tag.core { background: #1e3a8a; color: #bfdbfe; }
    body.dark-mode .meta-tag.child { background: #14532d; color: #bbf7d0; }
    body.dark-mode .meta-tag.parent { background: #78350f; color: #fde68a; }

    .detail-card {
      background: var(--slate-50);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-md);
      padding: 14px;
      font-size: 0.88rem;
    }
    body.dark-mode .detail-card {
      background: var(--slate-900);
    }
    .detail-card h4 {
      font-size: 0.88rem;
      font-weight: 800;
      margin-bottom: 6px;
      color: var(--primary-800);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    body.dark-mode .detail-card h4 {
      color: var(--primary-400);
    }

    .buttons-list-group {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .btn-inspector-card {
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-md);
      padding: 12px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
    }
    .btn-inspector-card:hover {
      border-color: var(--primary-500);
      transform: translateX(-4px);
      box-shadow: var(--shadow-sm);
    }
    .btn-inspector-card.active-inspected {
      border-color: var(--primary-600);
      background: var(--primary-50);
      box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2);
    }
    body.dark-mode .btn-inspector-card.active-inspected {
      background: rgba(16, 185, 129, 0.15);
    }
    .btn-inspector-card.parent-btn {
      border-right: 4px solid var(--gold-500);
    }
    .btn-inspector-card.child-btn {
      border-right: 4px solid var(--primary-500);
    }
    .btn-card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 4px;
    }
    .btn-title {
      font-weight: 800;
      font-size: 0.88rem;
      color: var(--text-main);
    }
    .btn-dest-tag {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      background: var(--slate-100);
      color: var(--text-muted);
    }
    body.dark-mode .btn-dest-tag {
      background: var(--slate-800);
      color: var(--slate-300);
    }
    .btn-desc {
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.4;
    }
    .btn-action-code {
      margin-top: 6px;
      font-size: 0.72rem;
      color: var(--primary-700);
      font-family: var(--font-mono);
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    body.dark-mode .btn-action-code {
      color: var(--primary-300);
    }
    .jump-to-dest-btn {
      background: var(--primary-100);
      color: var(--primary-800);
      border: none;
      padding: 2px 8px;
      border-radius: var(--radius-sm);
      font-size: 0.7rem;
      cursor: pointer;
      font-weight: 700;
      transition: background 0.15s;
    }
    .jump-to-dest-btn:hover {
      background: var(--primary-200);
    }

    /* VIEW 2: Screen Mockups & Phone Simulator */
    .journey-bar {
      background: var(--surface-card);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-lg);
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      overflow-x: auto;
      gap: 12px;
      box-shadow: var(--shadow-xs);
    }
    .journey-step-node {
      display: flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      padding: 6px 12px;
      border-radius: var(--radius-full);
      transition: all 0.2s;
      white-space: nowrap;
    }
    .journey-step-node:hover {
      background: var(--slate-100);
    }
    .journey-step-node.active {
      background: var(--primary-100);
      font-weight: 800;
    }
    body.dark-mode .journey-step-node.active {
      background: rgba(16, 185, 129, 0.2);
    }
    .step-circle {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--slate-200);
      color: var(--text-main);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.8rem;
    }
    .journey-step-node.active .step-circle {
      background: var(--primary-600);
      color: #ffffff;
    }
    .step-arrow {
      color: var(--slate-400);
      font-size: 0.85rem;
    }

    .phones-grid-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
      gap: 24px;
    }
    .mock-phone-card {
      background: var(--surface-card);
      border-radius: var(--radius-xl);
      border: 1px solid var(--surface-border);
      box-shadow: var(--shadow-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.25s, box-shadow 0.25s, border-color 0.25s;
      position: relative;
    }
    .mock-phone-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-xl);
    }
    .mock-phone-card.phone-highlight-pulse {
      border-color: var(--primary-500) !important;
      box-shadow: 0 0 30px rgba(16, 185, 129, 0.4) !important;
      animation: phonePulse 1.2s ease-in-out;
    }
    @keyframes phonePulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.02); }
      100% { transform: scale(1); }
    }
    .phone-mock-card-header {
      padding: 14px 18px;
      background: var(--slate-50);
      border-bottom: 1px solid var(--surface-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }
    body.dark-mode .phone-mock-card-header {
      background: var(--slate-900);
    }
    .phone-mock-card-header h3 {
      font-size: 0.95rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .screen-number-badge {
      background: var(--primary-700);
      color: #ffffff;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 800;
    }

    /* Phone Bezel Frame */
    .phone-bezel {
      background: #0f172a;
      border: 10px solid #1e293b;
      border-radius: 36px;
      padding: 0;
      margin: 16px auto;
      width: 280px;
      height: 520px;
      box-shadow: 0 16px 32px rgba(0, 0, 0, 0.25);
      position: relative;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    .phone-notch {
      width: 110px;
      height: 18px;
      background: #1e293b;
      border-radius: 0 0 12px 12px;
      margin: 0 auto;
      z-index: 10;
    }
    .phone-screen-content {
      flex: 1;
      background: #fdfbf7;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      padding: 12px;
      position: relative;
      color: #0f172a;
      font-family: var(--font-cairo);
    }

    
    /* Daylight Sunny Garden UI Helpers */
    .garden-landscape-box {
      background: linear-gradient(180deg, #38bdf8 0%, #bae6fd 30%, #84cc16 70%, #65a30d 100%);
      border-radius: var(--radius-lg);
      padding: 10px;
      position: relative;
      overflow: hidden;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.08);
    }
    .golden-path-ribbon {
      background: linear-gradient(180deg, #fef08a 0%, #facc15 50%, #eab308 100%);
      border: 2px dashed #ca8a04;
      border-radius: var(--radius-md);
      padding: 8px 10px;
      color: #78350f;
      font-weight: 800;
      text-align: center;
      box-shadow: 0 4px 10px rgba(234, 179, 8, 0.3);
    }
    .garden-signboard {
      background: #78350f;
      color: #fef08a;
      border: 2px solid #ca8a04;
      border-radius: var(--radius-sm);
      padding: 4px 8px;
      font-size: 0.72rem;
      font-weight: 800;
      text-align: center;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      box-shadow: 0 3px 6px rgba(0,0,0,0.18);
    }
    .verse-pearl-pill {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 900;
      background: #ffffff;
      border: 2px solid #cbd5e1;
      color: #64748b;
      transition: all 0.25s;
    }
    .verse-pearl-pill.active {
      background: #facc15;
      border-color: #ca8a04;
      color: #78350f;
      transform: scale(1.15);
      box-shadow: 0 0 10px rgba(250, 204, 21, 0.7);
    }
    .verse-pearl-pill.done {
      background: #84cc16;
      border-color: #4d7c0f;
      color: #ffffff;
    }
    .luxury-quran-card {
      background: #ffffff;
      border-radius: var(--radius-xl);
      border: 2px solid #bae6fd;
      padding: 14px;
      text-align: center;
      box-shadow: 0 8px 20px rgba(56, 189, 248, 0.15);
    }
    .parent-voice-banner {
      background: linear-gradient(135deg, #fef3c7, #fde68a);
      border: 1.5px solid #f59e0b;
      border-radius: var(--radius-md);
      padding: 8px 10px;
      color: #78350f;
      font-size: 0.75rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .repetition-circle-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 2px solid #cbd5e1;
      background: #ffffff;
      color: #334155;
      font-weight: 900;
      font-size: 0.82rem;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }
    .repetition-circle-btn.active {
      background: #f43f5e;
      border-color: #e11d48;
      color: #ffffff;
      transform: scale(1.1);
      box-shadow: 0 4px 8px rgba(244, 63, 94, 0.4);
    }

    /* Common Mock Elements */
    .mock-btn {
      background: var(--primary-600);
      color: #ffffff;
      border: none;
      padding: 10px 14px;
      border-radius: var(--radius-md);
      font-family: var(--font-cairo);
      font-weight: 800;
      font-size: 0.85rem;
      cursor: pointer;
      text-align: center;
      transition: all 0.15s;
      box-shadow: var(--shadow-sm);
    }
    .mock-btn:hover {
      background: var(--primary-700);
      transform: translateY(-1px);
    }
    .mock-btn.secondary {
      background: var(--slate-200);
      color: var(--text-main);
    }
    .mock-btn.subtle {
      background: transparent;
      border: 1px solid var(--surface-border);
      color: var(--text-muted);
    }
    .mock-btn.gold {
      background: linear-gradient(135deg, var(--gold-500), var(--gold-600));
      color: #ffffff;
    }

    /* Recitation Peek-a-boo Mock */
    .peekaboo-visualizer {
      background: linear-gradient(180deg, #ecfdf5 0%, #d1fae5 100%);
      border: 2px dashed #059669;
      border-radius: var(--radius-lg);
      padding: 16px;
      text-align: center;
      margin: 10px 0;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: all 0.2s;
    }
    .peekaboo-visualizer:hover {
      background: #a7f3d0;
      transform: scale(1.02);
    }
    .wave-bars {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      height: 32px;
      margin: 10px 0;
    }
    .wave-bar {
      width: 4px;
      height: 12px;
      background: #059669;
      border-radius: 2px;
      animation: wavePulse 1s ease-in-out infinite alternate;
    }
    .wave-bar:nth-child(2) { animation-delay: 0.2s; height: 24px; }
    .wave-bar:nth-child(3) { animation-delay: 0.4s; height: 18px; }
    .wave-bar:nth-child(4) { animation-delay: 0.1s; height: 28px; }
    .wave-bar:nth-child(5) { animation-delay: 0.3s; height: 14px; }
    @keyframes wavePulse {
      0% { transform: scaleY(0.4); }
      100% { transform: scaleY(1.3); }
    }

    /* VIEW 3: Router Matrix Table */
    .router-matrix-container {
      background: var(--surface-card);
      border-radius: var(--radius-xl);
      border: 1px solid var(--surface-border);
      box-shadow: var(--shadow-md);
      overflow: hidden;
    }
    .matrix-table-wrapper {
      overflow-x: auto;
    }
    table.matrix-table {
      width: 100%;
      border-collapse: collapse;
      text-align: right;
      font-size: 0.88rem;
    }
    table.matrix-table th {
      background: var(--slate-50);
      padding: 14px 18px;
      font-weight: 800;
      color: var(--text-main);
      border-bottom: 2px solid var(--surface-border);
      white-space: nowrap;
    }
    body.dark-mode table.matrix-table th {
      background: var(--slate-900);
    }
    table.matrix-table td {
      padding: 12px 18px;
      border-bottom: 1px solid var(--surface-border);
      vertical-align: middle;
      color: var(--text-main);
    }
    table.matrix-table tr:hover {
      background: var(--slate-50);
      cursor: pointer;
    }
    body.dark-mode table.matrix-table tr:hover {
      background: var(--slate-850);
    }
    .code-badge {
      font-family: var(--font-mono);
      background: var(--slate-100);
      padding: 3px 6px;
      border-radius: 4px;
      font-size: 0.78rem;
      color: var(--primary-700);
      font-weight: 700;
    }
    body.dark-mode .code-badge {
      background: var(--slate-800);
      color: var(--primary-300);
    }

    /* VIEW 4: Architectural Blueprint */
    .blueprint-article {
      background: var(--surface-card);
      border-radius: var(--radius-xl);
      border: 1px solid var(--surface-border);
      box-shadow: var(--shadow-md);
      padding: 32px;
      display: flex;
      flex-direction: column;
      gap: 28px;
    }
    .blueprint-section h3 {
      font-size: 1.25rem;
      font-weight: 900;
      color: var(--primary-850);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    body.dark-mode .blueprint-section h3 {
      color: #34d399;
    }
    .blueprint-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin-top: 14px;
    }
    .blueprint-feature-card {
      background: var(--slate-50);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-lg);
      padding: 18px;
    }
    body.dark-mode .blueprint-feature-card {
      background: var(--slate-900);
    }
    .blueprint-feature-card h4 {
      font-size: 0.95rem;
      font-weight: 800;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Google Stitch Modal & Prompt Studio */
    .stitch-modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(8px);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .stitch-modal-overlay.active {
      display: flex;
    }
    .stitch-modal-card {
      background: var(--surface-card);
      border-radius: var(--radius-xl);
      border: 1px solid var(--surface-border);
      box-shadow: var(--shadow-xl);
      width: 100%;
      max-width: 900px;
      max-height: 88vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    .stitch-modal-header {
      padding: 16px 24px;
      background: var(--slate-50);
      border-bottom: 1px solid var(--surface-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    body.dark-mode .stitch-modal-header {
      background: var(--slate-900);
    }
    .stitch-tabs-row {
      display: flex;
      overflow-x: auto;
      background: var(--slate-100);
      border-bottom: 1px solid var(--surface-border);
      padding: 6px 12px;
      gap: 6px;
    }
    body.dark-mode .stitch-tabs-row {
      background: var(--slate-900);
    }
    .stitch-tab-btn {
      background: transparent;
      border: none;
      padding: 6px 12px;
      border-radius: var(--radius-md);
      font-family: var(--font-cairo);
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      color: var(--text-muted);
      white-space: nowrap;
      transition: all 0.15s;
    }
    .stitch-tab-btn:hover {
      background: rgba(255, 255, 255, 0.5);
      color: var(--text-main);
    }
    .stitch-tab-btn.active {
      background: var(--surface-card);
      color: var(--primary-700);
      box-shadow: var(--shadow-xs);
    }
    body.dark-mode .stitch-tab-btn.active {
      background: var(--primary-700);
      color: #ffffff;
    }
    .stitch-modal-body {
      flex: 1;
      padding: 20px;
      overflow-y: auto;
    }
    .stitch-code-block {
      background: #0f172a;
      color: #f8fafc;
      padding: 16px;
      border-radius: var(--radius-md);
      font-family: var(--font-mono);
      font-size: 0.82rem;
      line-height: 1.6;
      white-space: pre-wrap;
      direction: ltr;
      text-align: left;
    }
    .stitch-modal-footer {
      padding: 14px 24px;
      background: var(--slate-50);
      border-top: 1px solid var(--surface-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    body.dark-mode .stitch-modal-footer {
      background: var(--slate-900);
    }

    /* Toast Notification */
    .toast-container {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 3000;
      display: flex;
      flex-direction: column;
      gap: 10px;
      pointer-events: none;
    }
    .toast-msg {
      background: rgba(15, 23, 42, 0.95);
      color: #ffffff;
      padding: 12px 20px;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-xl);
      font-size: 0.88rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
      border-right: 4px solid var(--primary-500);
      animation: slideToast 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      pointer-events: auto;
      backdrop-filter: blur(8px);
    }
    @keyframes slideToast {
      from { transform: translateX(100%); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }

    /* Footer */
    footer.app-footer {
      background: var(--surface-card);
      border-top: 1px solid var(--surface-border);
      padding: 18px 24px;
      font-size: 0.82rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }
  </style>
</head>
<body>
""")

    # BLOCK 2: HEADER & HERO BANNER
    parts.append("""
  <!-- Top App Header -->
  <header class="app-header">
    <div class="brand-group">
      <div class="brand-icon">رِحْلة</div>
      <div class="brand-text">
        <h1>مشروع رِحْلة (Re7la Project) <span class="badge-ecc">ECC 2.2 Enterprise</span></h1>
        <div class="tagline">رحلة حفظ جزء عم للأطفال (3-5 سنوات) &bull; تصميم ستوديو نهاري مبهج (Strict Anti-AI-Slop) &bull; صوت الأب الحقيقي والمنشاوي المعلم</div>
      </div>
    </div>

    <!-- Navigation Views Tabs -->
    <nav class="nav-tabs" role="tablist">
      <button class="nav-tab-btn active" onclick="switchView('diagram-view', this)">
        <span>🗺️</span> مخطط التدفق والأزرار
      </button>
      <button class="nav-tab-btn" onclick="switchView('wireframes-view', this)">
        <span>📱</span> محاكي الشاشات التفاعلي
      </button>
      <button class="nav-tab-btn" onclick="switchView('matrix-view', this)">
        <span>📊</span> مصفوفة التوجيه الشاملة
      </button>
      <button class="nav-tab-btn" onclick="switchView('blueprint-view', this)">
        <span>🏛️</span> الميثاق المعماري
      </button>
    </nav>

    <!-- Header Quick Actions -->
    <div class="header-actions">
      <button class="btn-header" id="soundToggleBtn" onclick="toggleAudioFx()" title="تشغيل أو كتم المؤثرات الصوتية">
        <span id="soundIcon">🔊</span> صوت
      </button>
      <button class="btn-header" onclick="toggleDarkMode()" title="تبديل النمط النهاري والليلي">
        <span id="themeIcon">🌙</span>
      </button>
      <button class="btn-header primary-action" onclick="openStitchModal()">
        <span>🎨</span> تصدير لـ Google Stitch
      </button>
    </div>
  </header>

  <!-- Main Content Body -->
  <main class="main-content">

    <!-- Hero Architecture Overview -->
    <section class="overview-hero">
      <div class="overview-hero-content">
        <div class="hero-pill-badge">
          <span>☀️</span> حديقة القرآن المشمسة للأطفال (3 - 5 سنوات)
        </div>
        <h2>مخطط هندسة التدفق والصفحات والأزرار لمشروع «رِحْلة»</h2>
        <p>
          خريطة معمارية بصرية وبيانية شاملة لـ <strong>«مشروع رِحْلة» (Re7la Project)</strong>. يوضح هذا المخطط كل شاشة من شاشات البرنامج الست المطابقة لبروتوتايب الصور والـ PDF، وكافة عناصر التحكم والأزرار والإيماءات ومسارات التنقل بينها، مع التزام تام بميثاق <strong>"مناهضة الرداءة النمطية" (Strict Anti-AI-Slop)</strong>، و<strong>"صفر مايكروفون أثناء الترديد" (Zero-Mic Co-learning)</strong>، وتسجيل <strong>صوت الأب الحقيقي والتشجيع محلياً 100% في IndexedDB</strong>، وميكانيكا <strong>"لعبة الصوت الغائب" (Audio Peek-a-boo)</strong> مع فضيلة الشيخ المنشاوي المعلم، و<strong>"خطاف الهدية المرتقبة" (The Golden Hook)</strong>.
        </p>
      </div>
      <div class="overview-hero-stats">
        <div class="hero-stat-card">
          <div class="val">6</div>
          <div class="lbl">شاشات محورية</div>
        </div>
        <div class="hero-stat-card">
          <div class="val">13</div>
          <div class="lbl">مسار تنقل وتوجيه</div>
        </div>
        <div class="hero-stat-card">
          <div class="val">37</div>
          <div class="lbl">سورة من جزء عم</div>
        </div>
        <div class="hero-stat-card">
          <div class="val" style="color: var(--primary-400);">0</div>
          <div class="lbl">مايكروفون (Output Only)</div>
        </div>
      </div>
    </section>
""")

    # BLOCK 3: VIEW 1 - DIAGRAM & SVG CANVAS & INSPECTOR
    parts.append("""
    <!-- VIEW 1: Interactive Diagram & Inspector -->
    <div id="diagram-view" class="view-panel active">
      
      <!-- Toolbar for filters & search -->
      <div class="view-toolbar">
        <div class="filter-pills">
          <span style="font-size: 0.85rem; font-weight: 700; color: var(--text-muted); margin-left: 6px;">فلترة مسارات التدفق:</span>
          <button class="filter-btn active" onclick="filterDiagramFlow('all', this)">كل المسارات (All Flows)</button>
          <button class="filter-btn" onclick="filterDiagramFlow('child', this)">👶 رحلة الطفل الأساسية (Child Flow)</button>
          <button class="filter-btn" onclick="filterDiagramFlow('parent', this)">👨‍👩‍👧 تحكم الوالدين الهادئ (Parent Gate)</button>
          <button class="filter-btn" onclick="filterDiagramFlow('reward', this)">🎁 حلقة المكافأة والهدية (Golden Hook)</button>
        </div>
        <div class="search-box">
          <span>🔍</span>
          <input type="text" id="diagramSearchInput" placeholder="ابحث عن صفحة، زر، أو مسار..." oninput="handleDiagramSearch(this.value)">
        </div>
      </div>

      <!-- Diagram Canvas and Inspector Area -->
      <div class="diagram-workspace">
        
        <!-- SVG Canvas Area with Real Pan & Zoom -->
        <div class="diagram-canvas-container" id="canvasContainer">
          
          <div class="canvas-controls-floating">
            <button class="canvas-tool-btn" onclick="zoomDiagram(1.2)" title="تكبير (+)">+</button>
            <button class="canvas-tool-btn" onclick="zoomDiagram(0.83)" title="تصغير (−)">−</button>
            <button class="canvas-tool-btn" onclick="resetDiagramZoom()" title="إعادة ضبط الرؤية">⟲</button>
            <button class="canvas-tool-btn" onclick="fitDiagramToScreen()" title="ملاءمة الشاشة">⛶</button>
          </div>

          <div class="canvas-hint-pill">
            <span>🖱️</span> اسحب بالفأرة للتحريك (Pan) &bull; عجلات الفأرة للتكبير (Zoom) &bull; انقر على أي زر لفحص مساره
          </div>

          <div class="diagram-svg-wrapper" id="svgContainer">
            <svg id="appDiagramSvg" class="diagram-svg" viewBox="0 0 1350 780" preserveAspectRatio="xMidYMid meet">
              <defs>
                <!-- Arrow Markers -->
                <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
                  <path d="M 0 1 L 9 5 L 0 9 z" fill="#10b981" />
                </marker>
                <marker id="arrow-gold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
                  <path d="M 0 1 L 9 5 L 0 9 z" fill="#f59e0b" />
                </marker>
                <marker id="arrow-gray" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">
                  <path d="M 0 1 L 9 5 L 0 9 z" fill="#94a3b8" />
                </marker>
              </defs>

              <!-- Viewport for Pan & Zoom Transform -->
              <g id="diagramViewport" transform="matrix(1 0 0 1 0 0)">
                
                <!-- Connection Curves Group (SVG Paths) -->
                <g id="linksGroup">
                  
                  <!-- S1 -> S2: Primary Start Flow (Right to Left in Arabic) -->
                  <path id="link-s1-s2" class="link-path child-flow" d="M 950 200 C 880 200, 850 200, 810 200" marker-end="url(#arrow-green)" />
                  <text x="880" y="190" font-size="11" fill="#047857" font-weight="800" text-anchor="middle">ابدأ الرحلة ➔</text>

                  <!-- S1 -> S4: Direct Parent Gate Access from S1 -->
                  <path id="link-s1-s4" class="link-path parent-link parent-flow" d="M 1020 320 C 1020 390, 960 420, 920 440" marker-end="url(#arrow-gold)" />
                  <text x="1005" y="390" font-size="11" fill="#b45309" font-weight="800" text-anchor="middle">بوابة الوالدين 🔒</text>

                  <!-- S4 -> S1: Return from settings back to S1 -->
                  <path id="link-s4-s1" class="link-path parent-link parent-flow" d="M 940 440 C 970 410, 1050 380, 1050 320" marker-end="url(#arrow-gold)" />
                  <text x="1070" y="410" font-size="10" fill="#92400e" font-weight="700" text-anchor="middle">عودة للرئيسية ↩</text>

                  <!-- S2 -> S3: Surah Selection to Gift Selection -->
                  <path id="link-s2-s3" class="link-path child-flow reward-flow" d="M 560 200 C 490 200, 460 200, 420 200" marker-end="url(#arrow-green)" />
                  <text x="490" y="190" font-size="11" fill="#047857" font-weight="800" text-anchor="middle">اختر السورة ➔</text>

                  <!-- S2 -> S1: Back button from Surahs to Home -->
                  <path id="link-s2-s1" class="link-path" d="M 810 240 C 860 240, 890 240, 950 240" marker-end="url(#arrow-gray)" />
                  <text x="880" y="255" font-size="10" fill="#64748b" font-weight="700" text-anchor="middle">🔙 رجوع للرئيسية</text>

                  <!-- S2 -> S4: Surah Screen to Parent Settings -->
                  <path id="link-s2-s4" class="link-path parent-link parent-flow" d="M 685 320 C 685 380, 750 410, 790 440" marker-end="url(#arrow-gold)" />
                  <text x="710" y="380" font-size="11" fill="#b45309" font-weight="800" text-anchor="middle">إعدادات الوالد ⚙️</text>

                  <!-- S4 -> S2: Return from settings back to Surahs -->
                  <path id="link-s4-s2" class="link-path parent-link parent-flow" d="M 760 490 C 720 460, 650 390, 650 320" marker-end="url(#arrow-gold)" />
                  <text x="645" y="420" font-size="10" fill="#92400e" font-weight="700" text-anchor="middle">عودة للسور ↩</text>

                  <!-- S3 -> S5: Lock Gift to Active Recitation (Down to Row 2) -->
                  <path id="link-s3-s5" class="link-path child-flow reward-flow" d="M 295 320 C 295 370, 295 400, 295 440" marker-end="url(#arrow-green)" />
                  <text x="235" y="380" font-size="11" fill="#047857" font-weight="800" text-anchor="middle">أغلق الصندوق وابدأ ➔</text>

                  <!-- S3 -> S2: Back button from Gift to Surahs -->
                  <path id="link-s3-s2" class="link-path" d="M 420 240 C 470 240, 510 240, 560 240" marker-end="url(#arrow-gray)" />
                  <text x="490" y="255" font-size="10" fill="#64748b" font-weight="700" text-anchor="middle">🔙 رجوع للسور</text>

                  <!-- S5 -> S6: Active Recitation to Celebration Screen -->
                  <path id="link-s5-s6" class="link-path child-flow reward-flow" d="M 430 560 C 450 560, 460 560, 470 560" marker-end="url(#arrow-green)" />
                  <text x="450" y="545" font-size="11" fill="#047857" font-weight="800" text-anchor="middle">اكتمال السورة 🏆</text>

                  <!-- S5 -> S2: Parent Secret Double-Tap Safe Exit -->
                  <path id="link-s5-s2" class="link-path parent-link parent-flow" d="M 380 440 C 440 370, 540 330, 580 320" marker-end="url(#arrow-gold)" />
                  <text x="470" y="340" font-size="10.5" fill="#b45309" font-weight="800" text-anchor="middle">خروج آمن (نقرتان خفيتان)</text>

                  <!-- S6 -> S2: New Surah CTA -->
                  <path id="link-s6-s2" class="link-path child-flow" d="M 595 440 C 610 390, 630 360, 640 320" marker-end="url(#arrow-green)" />
                  <text x="645" y="380" font-size="10.5" fill="#047857" font-weight="800" text-anchor="middle">سورة جديدة 🚀</text>

                  <!-- S6 -> S5: Replay Surah CTA -->
                  <path id="link-s6-s5" class="link-path child-flow" d="M 470 610 C 450 610, 440 610, 430 610" marker-end="url(#arrow-green)" />
                  <text x="450" y="630" font-size="10.5" fill="#047857" font-weight="800" text-anchor="middle">إعادة التلاوة 🔁</text>
                </g>

                <!-- Screen Nodes Group -->
                <g id="nodesGroup">
                  
                  <!-- Screen 1: Onboarding & Hero Selection (Top Right) -->
                  <g id="node-screen1" class="diagram-node selected" transform="translate(950, 80)" onclick="selectScreenNode(1)">
                    <rect class="node-rect" width="250" height="240" />
                    <rect x="0" y="0" width="250" height="38" rx="16" ry="16" fill="#047857" />
                    <text x="125" y="24" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle">1. الشاشة الرئيسية | اختيار البطل</text>
                    <text x="125" y="60" font-size="11.5" font-weight="800" fill="#0f172a" text-anchor="middle">Onboarding & Hero Selection</text>
                    <text x="125" y="78" font-size="10" fill="#059669" font-weight="700" text-anchor="middle">👤 المستخدم: الطفل والوالد معاً</text>
                    <line x1="15" y1="90" x2="235" y2="90" stroke="#e2e8f0" stroke-width="1" />
                    
                    <!-- Button Pills on Screen 1 -->
                    <g class="diagram-btn-pill" transform="translate(15, 100)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s1-boy', 1, null, 'SET_AVATAR(\\'boy\\')')">
                      <rect width="105" height="26" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
                      <text x="52" y="17" font-size="10" font-weight="700" fill="#065f46" text-anchor="middle">👦 بطل ولد (عمر)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(130, 100)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s1-girl', 1, null, 'SET_AVATAR(\\'girl\\')')">
                      <rect width="105" height="26" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
                      <text x="52" y="17" font-size="10" font-weight="700" fill="#065f46" text-anchor="middle">👧 بطلة بنت (مريم)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 136)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s1-start', 1, 2, 'NAVIGATE_TO(\\'screen_surahs\\')', 'link-s1-s2')">
                      <rect width="220" height="30" rx="8" fill="#10b981" />
                      <text x="110" y="20" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">🚀 زر: انطلق في مسار السور (CTA)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 176)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s1-parent', 1, 4, 'OPEN_PARENT_GATE()', 'link-s1-s4')">
                      <rect width="220" height="26" rx="6" fill="#fffbeb" stroke="#fde68a" />
                      <text x="110" y="17" font-size="10" font-weight="700" fill="#b45309" text-anchor="middle">🔒 ترس بوابة الوالدين (Math Gate)</text>
                    </g>
                    <text x="125" y="222" font-size="9.5" fill="#64748b" text-anchor="middle">🛡️ صفر مايكروفون (Output Only)</text>
                  </g>

                  <!-- Screen 2: Surah Selection (Top Middle) -->
                  <g id="node-screen2" class="diagram-node" transform="translate(560, 80)" onclick="selectScreenNode(2)">
                    <rect class="node-rect" width="250" height="240" />
                    <rect x="0" y="0" width="250" height="38" rx="16" ry="16" fill="#047857" />
                    <text x="125" y="24" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle">2. شاشة اختيار السورة | جزء عم</text>
                    <text x="125" y="60" font-size="11.5" font-weight="800" fill="#0f172a" text-anchor="middle">Surah Selection (37 Surahs)</text>
                    <text x="125" y="78" font-size="10" fill="#059669" font-weight="700" text-anchor="middle">📖 الترتيب القرآني من النبأ للناس</text>
                    <line x1="15" y1="90" x2="235" y2="90" stroke="#e2e8f0" stroke-width="1" />
                    
                    <!-- Button Pills on Screen 2 -->
                    <g class="diagram-btn-pill" transform="translate(15, 100)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s2-card', 2, 3, 'SELECT_SURAH(id)', 'link-s2-s3')">
                      <rect width="220" height="30" rx="8" fill="#e0f2fe" stroke="#7dd3fc" />
                      <text x="110" y="19" font-size="10.5" font-weight="800" fill="#0369a1" text-anchor="middle">📖 بطاقة السورة (37 سورة) ➔ للهدية</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 138)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s2-back', 2, 1, 'NAVIGATE_TO(\\'screen_onboarding\\')', 'link-s2-s1')">
                      <rect width="105" height="26" rx="6" fill="#f1f5f9" stroke="#cbd5e1" />
                      <text x="52" y="17" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">🔙 رجوع للرئيسية</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(130, 138)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s2-parent', 2, 4, 'OPEN_PARENT_GATE()', 'link-s2-s4')">
                      <rect width="105" height="26" rx="6" fill="#fffbeb" stroke="#fde68a" />
                      <text x="52" y="17" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">⚙️ إعدادات الوالد</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 174)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s2-filter', 2, null, 'FILTER_SURAHS()')">
                      <rect width="220" height="24" rx="6" fill="#faf5ff" stroke="#e9d5ff" />
                      <text x="110" y="16" font-size="9.5" font-weight="700" fill="#7e22ce" text-anchor="middle">🏷️ فلترة قصار السور / البحث</text>
                    </g>
                    <text x="125" y="222" font-size="9.5" fill="#64748b" text-anchor="middle">⭐ نيل النجوم وفتح المكافآت</text>
                  </g>

                  <!-- Screen 3: Gift Selection (Top Left) -->
                  <g id="node-screen3" class="diagram-node" transform="translate(170, 80)" onclick="selectScreenNode(3)">
                    <rect class="node-rect" width="250" height="240" />
                    <rect x="0" y="0" width="250" height="38" rx="16" ry="16" fill="#d97706" />
                    <text x="125" y="24" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle">3. اختيار الهدية | الخطاف الذهبي</text>
                    <text x="125" y="60" font-size="11.5" font-weight="800" fill="#0f172a" text-anchor="middle">The Golden Hook Selection</text>
                    <text x="125" y="78" font-size="10" fill="#b45309" font-weight="700" text-anchor="middle">🎁 تحفيز الدوبامين الذاتي قبل التلاوة</text>
                    <line x1="15" y1="90" x2="235" y2="90" stroke="#e2e8f0" stroke-width="1" />
                    
                    <!-- Button Pills on Screen 3 -->
                    <g class="diagram-btn-pill" transform="translate(15, 100)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s3-tabs', 3, null, 'FILTER_GIFTS(cat)')">
                      <rect width="220" height="24" rx="6" fill="#fef3c7" stroke="#fde68a" />
                      <text x="110" y="16" font-size="9.5" font-weight="700" fill="#92400e" text-anchor="middle">🏷️ فئات الهدايا (سيارات/حيوانات/ألغاز)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 132)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s3-toy', 3, null, 'SELECT_GIFT(toyId)')">
                      <rect width="105" height="26" rx="6" fill="#fffbeb" stroke="#fde68a" />
                      <text x="52" y="17" font-size="9.5" font-weight="700" fill="#b45309" text-anchor="middle">🏎️ معاينة اللعبة</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(130, 132)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s3-back', 3, 2, 'NAVIGATE_TO(\\'screen_surahs\\')', 'link-s3-s2')">
                      <rect width="105" height="26" rx="6" fill="#f1f5f9" stroke="#cbd5e1" />
                      <text x="52" y="17" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">🔙 رجوع للسور</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 168)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s3-lock', 3, 5, 'LOCK_CHEST_AND_START()', 'link-s3-s5')">
                      <rect width="220" height="32" rx="8" fill="#f59e0b" />
                      <text x="110" y="21" font-size="10.5" font-weight="900" fill="#ffffff" text-anchor="middle">🔒 ضع الهدية في الصندوق وابدأ! 🎁</text>
                    </g>
                    <text x="125" y="222" font-size="9.5" fill="#64748b" text-anchor="middle">✨ يغلق الصندوق وينتقل للترديد</text>
                  </g>

                  <!-- Screen 5: Active Recitation Screen (Audio Peek-a-boo) -->
                  <g id="node-screen5" class="diagram-node" transform="translate(170, 440)" onclick="selectScreenNode(5)">
                    <rect class="node-rect" width="260" height="255" />
                    <rect x="0" y="0" width="260" height="38" rx="16" ry="16" fill="#047857" />
                    <text x="130" y="24" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle">5. الترديد النشط | سورة الفلق والمنشاوي</text>
                    <text x="130" y="60" font-size="11.5" font-weight="800" fill="#0f172a" text-anchor="middle">Active Recitation (Audio Peek-a-boo)</text>
                    <text x="130" y="78" font-size="10" fill="#dc2626" font-weight="800" text-anchor="middle">🛡️ صفر مايكروفون (الطفل يقرأ لوالديه)</text>
                    <line x1="15" y1="90" x2="245" y2="90" stroke="#e2e8f0" stroke-width="1" />
                    
                    <!-- Button / Gesture Pills on Screen 5 -->
                    <g class="diagram-btn-pill" transform="translate(15, 96)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s5-tap', 5, null, 'AUDIO_TOGGLE_OR_REPEAT()')">
                      <rect width="230" height="28" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
                      <text x="115" y="18" font-size="10" font-weight="800" fill="#065f46" text-anchor="middle">👆 لمسة خفية بأي مكان (إيقاف/إعادة)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 130)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s5-exit', 5, 2, 'SAFE_EXIT_TO_SURAHS()', 'link-s5-s2')">
                      <rect width="230" height="28" rx="6" fill="#fffbeb" stroke="#fde68a" />
                      <text x="115" y="18" font-size="10" font-weight="800" fill="#92400e" text-anchor="middle">✌️ نقرتان بالزاوية (خروج الوالد الآمن)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 166)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s5-auto', 5, 6, 'AUTO_TRIGGER_CELEBRATION()', 'link-s5-s6')">
                      <rect width="230" height="32" rx="8" fill="#10b981" />
                      <text x="115" y="21" font-size="10.5" font-weight="900" fill="#ffffff" text-anchor="middle">⏱️ اكتمال آيات السورة ➔ للاحتفال 🏆</text>
                    </g>
                    <text x="130" y="222" font-size="9.5" fill="#047857" font-weight="700" text-anchor="middle">عمر يقف تحت الشجرة ممسكاً بمصحفه</text>
                    <text x="130" y="238" font-size="9" fill="#64748b" text-anchor="middle">صندوق الهدية مغلق أمامه يهتز شوقاً للفتح</text>
                  </g>

                  <!-- Screen 6: Celebration & Unboxing (Bottom Middle) -->
                  <g id="node-screen6" class="diagram-node" transform="translate(470, 440)" onclick="selectScreenNode(6)">
                    <rect class="node-rect" width="250" height="250" />
                    <rect x="0" y="0" width="250" height="38" rx="16" ry="16" fill="#7c3aed" />
                    <text x="125" y="24" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle">6. الاحتفال وفتح صندوق الهدية</text>
                    <text x="125" y="60" font-size="11.5" font-weight="800" fill="#0f172a" text-anchor="middle">Celebration & Unboxing (The Reward)</text>
                    <text x="125" y="78" font-size="10" fill="#7c3aed" font-weight="700" text-anchor="middle">🎉 انفجار الصندوق وإطلاق اللعبة بالحديقة</text>
                    <line x1="15" y1="90" x2="235" y2="90" stroke="#e2e8f0" stroke-width="1" />
                    
                    <!-- Button Pills on Screen 6 -->
                    <g class="diagram-btn-pill" transform="translate(15, 100)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s6-play', 6, null, 'TRIGGER_TOY_INTERACTION()')">
                      <rect width="220" height="28" rx="6" fill="#f3e8ff" stroke="#d8b4fe" />
                      <text x="110" y="18" font-size="10" font-weight="800" fill="#6b21a8" text-anchor="middle">🎮 العب بالهدية في الحديقة (حركة وصوت)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 136)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s6-next', 6, 2, 'NAVIGATE_TO(\\'screen_surahs\\')', 'link-s6-s2')">
                      <rect width="220" height="30" rx="8" fill="#7c3aed" />
                      <text x="110" y="20" font-size="10.5" font-weight="900" fill="#ffffff" text-anchor="middle">🚀 سورة جديدة وهدية جديدة (CTA)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 174)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s6-repeat', 6, 5, 'RESTART_SURAH()', 'link-s6-s5')">
                      <rect width="220" height="28" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
                      <text x="110" y="18" font-size="10" font-weight="800" fill="#047857" text-anchor="middle">🔁 إعادة تلاوة السورة للتثبيت</text>
                    </g>
                    <text x="125" y="230" font-size="9.5" fill="#64748b" text-anchor="middle">حفظ الوسام في سجل إنجازات البطل</text>
                  </g>

                  <!-- Screen 4: Play Settings, Parent Voice & Gate -->
                  <g id="node-screen4" class="diagram-node parent-gate" transform="translate(760, 440)" onclick="selectScreenNode(4)">
                    <rect class="node-rect" width="260" height="255" />
                    <rect x="0" y="0" width="260" height="38" rx="16" ry="16" fill="#ca8a04" />
                    <text x="130" y="24" font-size="13" font-weight="900" fill="#ffffff" text-anchor="middle">4. نافذة إعدادات اللعب وصوت الأهل 🔒</text>
                    <text x="130" y="60" font-size="11.5" font-weight="800" fill="#0f172a" text-anchor="middle">Play Settings, Parent Voice & Gate</text>
                    <text x="130" y="78" font-size="10" fill="#854d0e" font-weight="700" text-anchor="middle">مودال عائم فوق الحديقة | عمر يجلس بالأعلى</text>
                    <line x1="15" y1="90" x2="245" y2="90" stroke="#e2e8f0" stroke-width="1" />
                    
                    <!-- Button / Controls Pills on Screen 4 -->
                    <g class="diagram-btn-pill" transform="translate(15, 96)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s4-math', 4, null, 'VERIFY_CHALLENGE()')">
                      <rect width="230" height="24" rx="6" fill="#fffbeb" stroke="#fde68a" />
                      <text x="115" y="16" font-size="9.5" font-weight="800" fill="#92400e" text-anchor="middle">🔢 مسألة الأمان للوالدين (8 + 5 = 13)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 126)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s4-repeat', 4, null, 'SET_REPETITIONS(n)')">
                      <rect width="110" height="24" rx="6" fill="#f8fafc" stroke="#cbd5e1" />
                      <text x="55" y="16" font-size="9" font-weight="700" fill="#334155" text-anchor="middle">🔁 تكرار [1, 2, 3, 4, 5]</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(130, 126)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s4-pause', 4, null, 'RECORD_PARENT_VOICE()')">
                      <rect width="115" height="24" rx="6" fill="#fef2f2" stroke="#fca5a5" />
                      <text x="57" y="16" font-size="9" font-weight="800" fill="#b91c1c" text-anchor="middle">🎙️ صوت الأب (Local)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 156)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s4-link', 4, null, 'TOGGLE_AUTO_PLAY()')">
                      <rect width="230" height="24" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
                      <text x="115" y="16" font-size="9.5" font-weight="700" fill="#065f46" text-anchor="middle">⚡ تشغيل تلقائي بدون لمس (Toggle)</text>
                    </g>
                    <g class="diagram-btn-pill" transform="translate(15, 186)" onclick="event.stopPropagation(); triggerButtonFromDiagram('btn-s4-close', 4, 2, 'SAVE_AND_CLOSE()', 'link-s4-s2')">
                      <rect width="230" height="30" rx="6" fill="#d97706" />
                      <text x="115" y="20" font-size="10.5" font-weight="900" fill="#ffffff" text-anchor="middle">✕ حفظ الإعدادات وإغلاق النافذة</text>
                    </g>
                    <text x="130" y="230" font-size="9" fill="#0369a1" font-weight="700" text-anchor="middle">📸 صورة الطفل و🎙️ صوت الأب في IndexedDB</text>
                    <text x="130" y="244" font-size="8.5" fill="#64748b" text-anchor="middle">تعود للشاشة السابقة (الخريطة 1 أو السور 2)</text>
                  </g>

                </g>
              </g>
            </svg>
          </div>
        </div>

        <!-- Right Side Inspector Panel -->
        <aside class="inspector-panel" id="inspectorSidebar">
          <div class="inspector-header">
            <h3 id="inspectTitle"><span>📱</span> تفاصيل الشاشة المختارة</h3>
            <span class="meta-tag core" id="inspectBadge">الشاشة 1</span>
          </div>
          <div class="inspector-body" id="inspectContent">
            <!-- Populated dynamically via JS -->
          </div>
        </aside>

      </div>
    </div>
""")

    # BLOCK 4: VIEW 2 - WIREFRAMES & INTERACTIVE SIMULATOR
    parts.append("""
    <!-- VIEW 2: Screen Mockups & Phone Simulator -->
    <div id="wireframes-view" class="view-panel">
      
      <!-- Interactive Flow Journey Bar -->
      <div class="journey-bar">
        <div class="journey-step-node active" id="journeyStep1" onclick="scrollToMockCard('mock-s1')">
          <div class="step-circle">1</div>
          <div class="step-name">اختيار البطل</div>
        </div>
        <div class="step-arrow">➔</div>
        <div class="journey-step-node" id="journeyStep2" onclick="scrollToMockCard('mock-s2')">
          <div class="step-circle">2</div>
          <div class="step-name">اختيار السورة</div>
        </div>
        <div class="step-arrow">➔</div>
        <div class="journey-step-node" id="journeyStep3" onclick="scrollToMockCard('mock-s3')">
          <div class="step-circle">3</div>
          <div class="step-name">الهدية المرتقبة</div>
        </div>
        <div class="step-arrow">➔</div>
        <div class="journey-step-node" id="journeyStep5" onclick="scrollToMockCard('mock-s5')">
          <div class="step-circle">5</div>
          <div class="step-name">الترديد مع المنشاوي</div>
        </div>
        <div class="step-arrow">➔</div>
        <div class="journey-step-node" id="journeyStep6" onclick="scrollToMockCard('mock-s6')">
          <div class="step-circle">6</div>
          <div class="step-name">الاحتفال والمكافأة</div>
        </div>
        <div style="margin-right: auto; padding-right: 14px;">
          <span class="meta-tag parent" onclick="scrollToMockCard('mock-s4')" style="cursor: pointer;">
            🔒 نافذة بوابة الوالدين (شاشة 4)
          </span>
        </div>
      </div>

      <!-- 6 Phones Grid Simulator -->
      <div class="phones-grid-container">
        
        <!-- Phone Mockup 1: Winding Golden Roadmap & Hero Selection -->
        <div class="mock-phone-card" id="mock-s1">
          <div class="phone-mock-card-header">
            <span class="screen-number-badge">1</span>
            <h3>1. خريطة طريق رحلة حفظ القرآن</h3>
            <span class="meta-tag child">واجهة الطفل</span>
          </div>
          <div class="phone-bezel">
            <div class="phone-notch"></div>
            <div class="phone-screen-content" style="background: linear-gradient(180deg, #e0f2fe 0%, #f0fdf4 40%, #fefce8 100%);">
              
              <!-- Top HUD -->
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <span style="font-weight: 900; color: #0284c7; font-size: 1.05rem;">رِحْلة ⭐</span>
                  <span style="background: #e0f2fe; color: #0369a1; font-size: 0.68rem; font-weight: 800; padding: 2px 6px; border-radius: 10px;">جزء عم: 1/30</span>
                </div>
                <button class="mock-btn subtle" style="padding: 3px 8px; font-size: 0.75rem;" onclick="navigateToScreenMock(4, 'فتح إعدادات اللعب وصوت الأهل', 'btn-s1-parent')" title="بوابة الوالدين">⚙️ 🔒</button>
              </div>

              <!-- Hero Rank Chip -->
              <div style="background: #ffffff; padding: 6px 10px; border-radius: var(--radius-md); border: 1.5px solid #bae6fd; display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.04);">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <span id="phone1AvatarEmoji" style="font-size: 1.4rem;">👦</span>
                  <div>
                    <div id="phone1AvatarName" style="font-size: 0.8rem; font-weight: 900; color: #0369a1;">البطل عُمَر</div>
                    <div style="font-size: 0.65rem; color: #64748b; font-weight: 700;">الرتبة: مستكشف صغير 🌿</div>
                  </div>
                </div>
                <span style="font-size: 0.72rem; background: #fef08a; color: #78350f; font-weight: 800; padding: 2px 6px; border-radius: 6px;">⭐ 1 سورة</span>
              </div>

              <!-- Winding Garden Road Mini Visual -->
              <div class="garden-landscape-box" style="margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                  <span style="font-size: 1.1rem;" title="مسجد القبة الخضراء">🕌</span>
                  <span style="font-size: 0.7rem; font-weight: 800; color: #ffffff; text-shadow: 0 1px 2px rgba(0,0,0,0.3);">طريق الحديقة الذهبي ☀️</span>
                  <span style="font-size: 1.1rem;" title="شجرة الحديقة الظليلة">🌳</span>
                </div>
                
                <!-- Winding Milestones -->
                <div style="display: flex; flex-direction: column; gap: 4px;">
                  <!-- Locked next milestone: Al-Ikhlas -->
                  <div style="background: rgba(255,255,255,0.7); border-radius: 8px; padding: 3px 8px; display: flex; justify-content: space-between; align-items: center; font-size: 0.68rem; color: #475569;">
                    <span>سورة الإخلاص</span>
                    <span>🔒🎁 هدية</span>
                  </div>
                  <!-- ACTIVE MILESTONE: Al-Falaq (Omar stands here!) -->
                  <div style="background: linear-gradient(135deg, #fef08a, #facc15); border: 2px solid #ca8a04; border-radius: 8px; padding: 4px 8px; display: flex; justify-content: space-between; align-items: center; font-size: 0.72rem; font-weight: 900; color: #78350f; box-shadow: 0 2px 8px rgba(234,179,8,0.5);" class="animate-pulse">
                    <span>🌟 سورة الفلق (المحطة الحالية)</span>
                    <span style="font-size: 0.9rem;">👦📖</span>
                  </div>
                  <!-- Completed milestone: An-Nas -->
                  <div style="background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 8px; padding: 3px 8px; display: flex; justify-content: space-between; align-items: center; font-size: 0.68rem; color: #065f46; font-weight: 700;">
                    <span>سورة الناس</span>
                    <span>✓ مكتملة ⭐</span>
                  </div>
                </div>
              </div>

              <!-- Signboard & Avatar Selector -->
              <div style="text-align: center; margin-bottom: 8px;">
                <div class="garden-signboard">كل يوم آية جديدة ❤️</div>
              </div>

              <div style="display: flex; gap: 6px; margin-bottom: 8px;">
                <button class="mock-btn secondary" style="flex: 1; padding: 6px; font-size: 0.75rem;" onclick="setPhoneHero('boy')">👦 عمر</button>
                <button class="mock-btn secondary" style="flex: 1; padding: 6px; font-size: 0.75rem;" onclick="setPhoneHero('girl')">👧 مريم</button>
              </div>

              <!-- Primary CTA -->
              <div style="margin-top: auto; padding-bottom: 6px;">
                <button class="mock-btn" style="width: 100%; padding: 12px; font-size: 0.9rem; background: #0284c7; font-weight: 900;" onclick="navigateToScreenMock(2, 'انطلق في مسار السور', 'btn-s1-start')">
                  انطلق في مسار السور 🚀
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Phone Mockup 2: Surah Winding Path Progression -->
        <div class="mock-phone-card" id="mock-s2">
          <div class="phone-mock-card-header">
            <span class="screen-number-badge">2</span>
            <h3>2. مسار اختيار السورة والتقدم</h3>
            <span class="meta-tag core">تشاركي</span>
          </div>
          <div class="phone-bezel">
            <div class="phone-notch"></div>
            <div class="phone-screen-content" style="background: linear-gradient(180deg, #f0fdf4 0%, #ffffff 100%);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <button class="mock-btn subtle" style="padding: 2px 8px; font-size: 0.75rem;" onclick="navigateToScreenMock(1, 'العودة لخريطة الطريق', 'btn-s2-back')">🔙</button>
                <span style="font-weight: 800; font-size: 0.88rem; color: #0f172a;">مسار السور الذهبي 📖</span>
                <button class="mock-btn subtle" style="padding: 2px 8px; font-size: 0.75rem;" onclick="navigateToScreenMock(4, 'فتح إعدادات الوالد', 'btn-s2-parent')">⚙️</button>
              </div>

              <!-- Star Counter & Rank -->
              <div style="background: #fef3c7; border: 1px solid #fde68a; border-radius: var(--radius-sm); padding: 5px 8px; font-size: 0.72rem; font-weight: 700; color: #92400e; margin-bottom: 8px; display: flex; justify-content: space-between;">
                <span>⭐ إنجازات عمر: 1 سورة</span>
                <span>🏆 وسام المستكشف الصغير</span>
              </div>

              <!-- Surahs List (Ascending Road Progression) -->
              <div style="display: flex; flex-direction: column; gap: 6px; overflow-y: auto; flex: 1;">
                
                <!-- 1. An-Nas (Done) -->
                <div class="mock-surah-row" style="background: #f0fdf4; border: 1.5px solid #a7f3d0; border-radius: var(--radius-md); padding: 8px 10px; display: flex; align-items: center; justify-content: space-between; cursor: pointer;" onclick="navigateToScreenMock(3, 'اختيار سورة الناس', 'btn-s2-card')">
                  <div>
                    <div style="font-family: var(--font-amiri); font-size: 1.05rem; font-weight: bold; color: #047857;">سُورَةُ النَّاسِ</div>
                    <div style="font-size: 0.68rem; color: #059669; font-weight: 700;">6 آيات &bull; تم الحفظ بنجاح ✓</div>
                  </div>
                  <span style="font-size: 1.1rem;">⭐</span>
                </div>

                <!-- 2. Al-Falaq (CURRENT ACTIVE MILESTONE) -->
                <div class="mock-surah-row" style="background: linear-gradient(135deg, #fefce8, #fef08a); border: 2px solid #facc15; border-radius: var(--radius-md); padding: 8px 10px; display: flex; align-items: center; justify-content: space-between; cursor: pointer; box-shadow: 0 4px 10px rgba(250, 204, 21, 0.35);" onclick="navigateToScreenMock(3, 'اختيار سورة الفلق (المحطة الحالية)', 'btn-s2-card')">
                  <div>
                    <div style="display: flex; align-items: center; gap: 6px;">
                      <span style="font-family: var(--font-amiri); font-size: 1.15rem; font-weight: bold; color: #78350f;">سُورَةُ الفَلَقِ</span>
                      <span style="background: #eab308; color: #ffffff; font-size: 0.62rem; font-weight: 900; padding: 2px 5px; border-radius: 6px;">ابدأ الآن 🌟</span>
                    </div>
                    <div style="font-size: 0.68rem; color: #92400e; font-weight: 700;">5 آيات &bull; المحطة الحالية لعمر</div>
                  </div>
                  <span style="font-size: 1.3rem;">👦🎁</span>
                </div>

                <!-- 3. Al-Ikhlas (Next Reward) -->
                <div class="mock-surah-row" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: var(--radius-md); padding: 8px 10px; display: flex; align-items: center; justify-content: space-between; cursor: pointer;" onclick="navigateToScreenMock(3, 'اختيار سورة الإخلاص', 'btn-s2-card')">
                  <div>
                    <div style="font-family: var(--font-amiri); font-size: 1.05rem; font-weight: bold; color: #047857;">سُورَةُ الإِخْلَاصِ</div>
                    <div style="font-size: 0.68rem; color: #64748b;">4 آيات &bull; الهدية التالية المرتقبة</div>
                  </div>
                  <span style="font-size: 1.1rem;">🎁</span>
                </div>

                <!-- 4. Al-Masad (Locked) -->
                <div class="mock-surah-row" style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: var(--radius-md); padding: 7px 10px; display: flex; align-items: center; justify-content: space-between; opacity: 0.75;">
                  <div>
                    <div style="font-family: var(--font-amiri); font-size: 1rem; color: #64748b;">سُورَةُ المَسَدِ</div>
                    <div style="font-size: 0.65rem; color: #94a3b8;">5 آيات &bull; في الانتظار</div>
                  </div>
                  <span style="font-size: 0.9rem;">🔒</span>
                </div>

              </div>

              <div style="text-align: center; margin-top: 6px; font-size: 0.7rem; color: #0284c7; font-weight: 800;">
                اضغط على سورة الفلق لاختيار هديتك وبدء الترديد ➔
              </div>
            </div>
          </div>
        </div>

        <!-- Phone Mockup 3: The Golden Hook (Gift Selection) -->
        <div class="mock-phone-card" id="mock-s3">
          <div class="phone-mock-card-header">
            <span class="screen-number-badge">3</span>
            <h3>شاشة الهدية المرتقبة (الخطاف)</h3>
            <span class="meta-tag core">ميكانيكا الدوبامين</span>
          </div>
          <div class="phone-bezel">
            <div class="phone-notch"></div>
            <div class="phone-screen-content" style="background: linear-gradient(180deg, #fffbeb 0%, #fef3c7 100%);">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <button class="mock-btn subtle" style="padding: 2px 8px; font-size: 0.75rem;" onclick="navigateToScreenMock(2, 'العودة لاختيار السورة', 'btn-s3-back')">🔙</button>
                <span style="font-weight: 800; font-size: 0.88rem; color: #92400e;">اختر هديتك يا بطل! 🎁</span>
                <span>✨</span>
              </div>

              <!-- Category Pills -->
              <div style="display: flex; gap: 4px; margin-bottom: 12px;">
                <button class="mock-btn gold" style="flex: 1; padding: 4px 6px; font-size: 0.72rem;">سيارات 🏎️</button>
                <button class="mock-btn secondary" style="flex: 1; padding: 4px 6px; font-size: 0.72rem;">حيوانات 🦁</button>
                <button class="mock-btn secondary" style="flex: 1; padding: 4px 6px; font-size: 0.72rem;">طائرات ✈️</button>
              </div>

              <!-- Selected Toy Showcase -->
              <div style="background: #ffffff; border-radius: var(--radius-lg); border: 2px solid #f59e0b; padding: 14px; text-align: center; margin-bottom: 12px;">
                <div style="font-size: 3.5rem; filter: drop-shadow(0 6px 10px rgba(0,0,0,0.15));">🏎️</div>
                <div style="font-weight: 800; color: #b45309; font-size: 0.95rem; margin-top: 4px;">سيارة السباق الحمراء السريعة</div>
                <div style="font-size: 0.72rem; color: #78350f;">ستوضع بالصندوق لتفتحها بعد إتمام السورة!</div>
              </div>

              <!-- Closed Chest Preview -->
              <div style="background: rgba(180, 83, 9, 0.08); border-radius: var(--radius-md); padding: 8px; text-align: center; margin-bottom: 12px; display: flex; align-items: center; justify-content: center; gap: 8px;">
                <span style="font-size: 1.8rem;">📦🔒</span>
                <span style="font-size: 0.75rem; font-weight: 700; color: #78350f;">الصندوق مقفل وينتظر تلاوتك المتقنة!</span>
              </div>

              <!-- Lock & Recite CTA -->
              <div style="margin-top: auto; padding-bottom: 10px;">
                <button class="mock-btn gold" style="width: 100%; padding: 12px; font-size: 0.9rem; font-weight: 900;" onclick="navigateToScreenMock(5, 'قفل الصندوق وبدء التلاوة', 'btn-s3-lock')">
                  ضعها بالصندوق وابدأ! 🔒✨
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Phone Mockup 4: Parental Math Gate & Settings -->
        <div class="mock-phone-card" id="mock-s4">
          <div class="phone-mock-card-header">
            <span class="screen-number-badge">4</span>
            <h3>4. نافذة إعدادات اللعب وصوت الأهل</h3>
            <span class="meta-tag parent">محلي 100% (IndexedDB)</span>
          </div>
          <div class="phone-bezel">
            <div class="phone-notch"></div>
            <div class="phone-screen-content" style="background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);">
              
              <!-- Floating Modal Top Edge with Omar sitting -->
              <div style="text-align: center; margin-top: -6px; margin-bottom: 4px;">
                <span style="font-size: 1.8rem;">👦</span>
                <div style="font-size: 0.65rem; color: #0369a1; font-weight: 800;">عمر يجلس فوق حافة نافذة الإعدادات ❤️</div>
              </div>

              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 900; font-size: 0.88rem; color: #b45309;">إعدادات اللعب وصوت الأهل ⚙️</span>
                <button class="mock-btn subtle" style="padding: 2px 8px; font-size: 0.75rem;" onclick="navigateToScreenMock(2, 'إغلاق نافذة الإعدادات والعودة', 'btn-s4-close')">✕</button>
              </div>

              <!-- Child Avatar & Photo Upload (IndexedDB) -->
              <div style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: var(--radius-md); padding: 7px 9px; margin-bottom: 8px;">
                <div style="font-size: 0.7rem; color: #047857; font-weight: 800; margin-bottom: 4px;">أفاتار الطفل وصورة الوجه (محلياً 100%):</div>
                <div style="display: flex; gap: 4px;">
                  <button class="mock-btn" style="flex: 1; padding: 4px; font-size: 0.7rem; background: #059669;">👦 عمر</button>
                  <button class="mock-btn subtle" style="flex: 1; padding: 4px; font-size: 0.7rem;">👧 مريم</button>
                  <button class="mock-btn subtle" style="flex: 1.2; padding: 4px; font-size: 0.68rem; background: #ecfdf5; color: #047857; border: 1px dashed #10b981;" onclick="showToast('📸 صورة الطفل تُدمج على الأفاتار وتُحفظ في IndexedDB')">📸 صورة الطفل</button>
                </div>
              </div>

              <!-- Parent Voice Recording (IndexedDB) -->
              <div style="background: #fefce8; border: 1.5px solid #fde047; border-radius: var(--radius-md); padding: 7px 9px; margin-bottom: 8px;">
                <div style="font-size: 0.7rem; color: #854d0e; font-weight: 800; margin-bottom: 4px;">صوت تشجيع الأب الحقيقي (IndexedDB):</div>
                <div style="display: flex; align-items: center; justify-content: space-between; gap: 6px;">
                  <button class="mock-btn" style="background: #e11d48; padding: 4px 8px; font-size: 0.68rem;" onclick="playTone(440, 0.2, 'sine', 0.2); showToast('🎙️ جاري تسجيل صوت الأب... تم الحفظ في IndexedDB')">🎙️ سجّل صوتك</button>
                  <span style="font-size: 0.65rem; color: #78350f; font-weight: 700;">"عاش يا بطل يا عمر!"</span>
                  <button class="mock-btn subtle" style="padding: 2px 6px; font-size: 0.65rem;" onclick="playChime('chime'); showToast('🔊 تشغيل صوت الأب المسجل')">▶️ استمع</button>
                </div>
              </div>

              <!-- Verse Repetitions [1..5] -->
              <div style="margin-bottom: 8px;">
                <div style="font-size: 0.7rem; color: #334155; font-weight: 800; margin-bottom: 4px;">تكرار الآية للطفل:</div>
                <div style="display: flex; justify-content: space-between; gap: 4px;">
                  <div class="repetition-circle-btn">1</div>
                  <div class="repetition-circle-btn">2</div>
                  <div class="repetition-circle-btn active">3</div>
                  <div class="repetition-circle-btn">4</div>
                  <div class="repetition-circle-btn">5</div>
                </div>
              </div>

              <!-- Auto-play Toggle -->
              <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: var(--radius-sm); padding: 6px 8px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-size: 0.7rem; color: #1e293b; font-weight: 700;">تشغيل تلقائي للآيات بدون لمس:</span>
                <span style="color: #10b981; font-weight: 900; font-size: 0.75rem;">مُفَعَّل ✓</span>
              </div>

              <!-- Math Challenge (Security) -->
              <div style="background: #f1f5f9; border-radius: var(--radius-sm); padding: 5px 8px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 0.68rem; color: #64748b;">مسألة أمان الوالد: 8 + 5 = </span>
                <span style="font-weight: 900; color: #059669; font-size: 0.75rem;">13 ✓ تم التحقق</span>
              </div>

              <!-- Save CTA -->
              <div style="margin-top: auto; padding-bottom: 4px;">
                <button class="mock-btn" style="width: 100%; padding: 10px; background: #ca8a04; font-size: 0.85rem; font-weight: 900;" onclick="navigateToScreenMock(2, 'حفظ الإعدادات في الهاتف والعودة', 'btn-s4-close')">
                  حفظ التعديلات وإغلاق ✓
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Phone Mockup 5: Active Recitation Screen (Audio Peek-a-boo) -->
        <div class="mock-phone-card" id="mock-s5">
          <div class="phone-mock-card-header">
            <span class="screen-number-badge">5</span>
            <h3>5. الترديد النشط (سورة الفلق والمنشاوي)</h3>
            <span class="meta-tag core" style="background:#fee2e2; color:#991b1b;">🛡️ صفر مايكروفون</span>
          </div>
          <div class="phone-bezel">
            <div class="phone-notch"></div>
            <div class="phone-screen-content" style="background: linear-gradient(180deg, #e0f2fe 0%, #f0fdf4 45%, #ffffff 100%);">
              
              <!-- Top Secret Parent Exit & Surah Title -->
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <div onclick="navigateToScreenMock(2, 'نقرتان خفيتان ➔ خروج آمن للسور', 'btn-s5-exit')" title="نقرتان خفيتان للخروج الآمن" style="width: 22px; height: 22px; border-radius: 50%; background: rgba(0,0,0,0.04); cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 0.65rem; color: #64748b;">
                  🔒
                </div>
                <span style="font-family: var(--font-amiri); font-weight: bold; font-size: 1.1rem; color: #047857;">سُورَةُ الفَلَقِ</span>
                <span style="font-size: 0.7rem; color: #0369a1; font-weight: 800;">الآية 1 من 5</span>
              </div>

              <!-- 5 Verse Progress Circles (Surat Al-Falaq) -->
              <div style="display: flex; justify-content: center; gap: 8px; margin: 4px 0;" id="pearlsContainer">
                <span class="verse-pearl-pill active" id="pearl1">1</span>
                <span class="verse-pearl-pill" id="pearl2">2</span>
                <span class="verse-pearl-pill" id="pearl3">3</span>
                <span class="verse-pearl-pill" id="pearl4">4</span>
                <span class="verse-pearl-pill" id="pearl5">5</span>
              </div>

              <!-- Central Luxury Quranic Card -->
              <div class="luxury-quran-card" style="margin: 6px 0;">
                <div style="font-size: 0.68rem; color: #0284c7; font-weight: 800; margin-bottom: 4px;">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
                <div style="font-family: var(--font-amiri); font-size: 1.35rem; font-weight: 900; color: #0f172a; line-height: 1.8; margin-bottom: 6px;" id="quranVerseText">
                  ﴿ قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ ﴾
                </div>
                <!-- Recitation Mode Toggles -->
                <div style="display: flex; gap: 4px; justify-content: center;">
                  <button class="mock-btn" style="background: #059669; padding: 4px 8px; font-size: 0.65rem; font-weight: 800;">🌿 الشيخ والأطفال</button>
                  <button class="mock-btn subtle" style="padding: 4px 8px; font-size: 0.65rem;">🌊 الشيخ فقط</button>
                  <button class="mock-btn subtle" style="padding: 4px 8px; font-size: 0.65rem;" onclick="showToast('الانتقال للآية التالية ⏭️')">⏭️ تخطي</button>
                </div>
              </div>

              <!-- Dynamic Avatar Under Shady Tree Stage -->
              <div style="text-align: center; margin: 4px 0; display: flex; align-items: center; justify-content: center; gap: 8px;">
                <div style="font-size: 2.2rem;">🌳</div>
                <div id="simAvatarGraphic" style="font-size: 3rem; filter: drop-shadow(0 6px 12px rgba(0,0,0,0.1));" class="animate-bounce">👦📖</div>
                <div style="text-align: right;">
                  <div style="font-size: 0.72rem; font-weight: 900; color: #047857;">عمر يستمع تحت الشجرة</div>
                  <div style="font-size: 0.62rem; color: #64748b;">ممسكاً بمصحفه الأخضر</div>
                </div>
              </div>

              <!-- Interactive Wave Visualizer / Peek-a-boo Tap Area -->
              <div class="peekaboo-visualizer" onclick="simulateParentInvisibleTap()" title="اضغط لمحاكاة لمسة الوالد الخفية" style="padding: 6px;">
                <div style="font-size: 0.72rem; font-weight: 800; color: #047857;" id="simWaveTitle">
                  تلاوة المنشاوي المعلم (سورة الفلق)
                </div>
                <div class="wave-bars" id="simWaveBars">
                  <div class="wave-bar"></div>
                  <div class="wave-bar"></div>
                  <div class="wave-bar"></div>
                  <div class="wave-bar"></div>
                  <div class="wave-bar"></div>
                </div>
                <div style="font-size: 0.68rem; color: #065f46; font-weight: 700;" id="simWaveSubtext">
                  👆 اضغط هنا لمحاكاة لمسة الوالد الخفية (لعبة الصوت الغائب)
                </div>
              </div>

              <!-- Closed Treasure Box Foreground -->
              <div style="margin-top: auto; text-align: center; padding-bottom: 4px;">
                <div style="display: flex; align-items: center; justify-content: center; gap: 6px;">
                  <span style="font-size: 1.8rem;" id="simTreasureBox" class="animate-pulse">📦🔒</span>
                  <span style="font-size: 0.68rem; color: #92400e; font-weight: 800;">سيارة السباق بالداخل 🏎️ (تهتز شوقاً للفتح!)</span>
                </div>
                <div style="margin-top: 4px;">
                  <button class="mock-btn primary" style="width: 100%; padding: 7px; font-size: 0.78rem; background: #10b981; font-weight: 900;" onclick="simulateSurahCompletion()">
                    🏆 محاكاة اكتمال السورة ➔ للاحتفال وصوت الأب
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Phone Mockup 6: Celebration & Unboxing -->
        <div class="mock-phone-card" id="mock-s6">
          <div class="phone-mock-card-header">
            <span class="screen-number-badge">6</span>
            <h3>6. الاحتفال وفتح الكنز وصوت الأب</h3>
            <span class="meta-tag core" style="background:#f3e8ff; color:#6b21a8;">صوت الأب الحقيقي</span>
          </div>
          <div class="phone-bezel">
            <div class="phone-notch"></div>
            <div class="phone-screen-content" style="background: linear-gradient(180deg, #fdf4ff 0%, #fae8ff 40%, #ffffff 100%);">
              <div style="text-align: center; margin-top: 4px;">
                <div style="font-size: 1.4rem;">🎉 ✨ 🌟</div>
                <div style="font-size: 1.15rem; font-weight: 900; color: #6b21a8; margin-top: 2px;">مُبَارَكٌ يَا عُمَر! 🏆</div>
                <div style="font-size: 0.72rem; color: #7c3aed; font-weight: 700;">أتممت تلاوة سورة الفلق بنجاح باهر!</div>
              </div>

              <!-- Parent Voice Cheering Audio Banner -->
              <div class="parent-voice-banner" style="margin: 6px 0;">
                <span style="font-size: 1.2rem;">🎙️</span>
                <div>
                  <div style="font-weight: 900; font-size: 0.75rem; color: #b45309;">صوت الأب يصدح الآن:</div>
                  <div style="font-size: 0.7rem; font-weight: 800; color: #78350f;">"عاش يا بطل يا عمر! أنا فخور بيك يا حبيبي ومبارك حفظ سورة الفلق!"</div>
                </div>
              </div>

              <!-- Unboxed Toy Garden Stage -->
              <div style="background: radial-gradient(circle, #f5d0fe 0%, transparent 70%); padding: 14px; text-align: center; margin: 4px 0; border-radius: var(--radius-lg); position: relative;">
                <div id="unboxedToy" style="font-size: 3.8rem; filter: drop-shadow(0 10px 20px rgba(124, 58, 237, 0.3)); transition: transform 0.4s;" class="animate-bounce">🏎️</div>
                <div style="font-size: 1.6rem; margin-top: -8px;">📦🔓✨</div>
                <div style="font-size: 0.78rem; font-weight: 900; color: #581c87; margin-top: 4px;">انفتحت هدية سيارة السباق في الحديقة!</div>
              </div>

              <!-- Action Buttons -->
              <div style="display: flex; flex-direction: column; gap: 6px; margin-top: auto; padding-bottom: 6px;">
                <button class="mock-btn" style="background: #7c3aed; padding: 8px; font-size: 0.82rem; font-weight: 800;" onclick="triggerToyPlayAnimation()">
                  العب بالهدية في الحديقة 🎮
                </button>
                <button class="mock-btn primary" style="background: #059669; padding: 8px; font-size: 0.82rem; font-weight: 800;" onclick="navigateToScreenMock(2, 'سورة جديدة وهدية جديدة', 'btn-s6-next')">
                  سورة جديدة وهدية جديدة 🚀
                </button>
                <button class="mock-btn subtle" style="padding: 5px; font-size: 0.72rem;" onclick="navigateToScreenMock(5, 'إعادة تلاوة سورة الفلق للتثبيت', 'btn-s6-repeat')">
                  إعادة تلاوة سورة الفلق 🔁
                </button>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
""")

    # BLOCK 5: VIEW 3 - ROUTER MATRIX TABLE
    parts.append("""
    <!-- VIEW 3: Full Router & Button Matrix Table -->
    <div id="matrix-view" class="view-panel">
      <div class="view-toolbar">
        <div>
          <h3 style="font-weight: 800;">مصفوفة التوجيه الشاملة لكافة الأزرار والصفحات (Full Routing Matrix)</h3>
          <p style="font-size: 0.85rem; color: var(--text-muted);">
            جدول تفصيلي ومحدد لكافة عناصر التحكم، الأزرار، الإيماءات الخفية، والأحداث التلقائية مع المسار البرمجي والتأثير في التطبيق.
          </p>
        </div>
        <div class="search-box">
          <span>🔍</span>
          <input type="text" id="matrixSearchInput" placeholder="تصفية حسب الزر أو الشاشة..." oninput="handleMatrixSearch(this.value)">
        </div>
      </div>

      <div class="router-matrix-container">
        <div class="matrix-table-wrapper">
          <table class="matrix-table" id="matrixTable">
            <thead>
              <tr>
                <th>شاشة الانطلاق (Source)</th>
                <th>اسم عنصر التفاعل / الزر</th>
                <th>الفئة المستهدفة</th>
                <th>نوع الحدث (Trigger)</th>
                <th>الشاشة أو الحالة المستهدفة (Destination)</th>
                <th>المعرف البرمجي (Action / Route)</th>
                <th>إجراء سريع</th>
              </tr>
            </thead>
            <tbody>
              <tr onclick="selectScreenNode(1)">
                <td><strong>1. الشاشة الرئيسية</strong></td>
                <td>بطاقة اختيار الولد (عمر)</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click</td>
                <td>تحديث بطل الرحلة لولد فورياً</td>
                <td><span class="code-badge">SET_AVATAR('boy')</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(1)">اعرض بالمخطط</button></td>
              </tr>
              <tr onclick="selectScreenNode(1)">
                <td><strong>1. الشاشة الرئيسية</strong></td>
                <td>بطاقة اختيار البنت (مريم)</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click</td>
                <td>تحديث بطل الرحلة لبنت فورياً</td>
                <td><span class="code-badge">SET_AVATAR('girl')</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(1)">اعرض بالمخطط</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s1-start', 1, 2, 'NAVIGATE_TO(\\'screen_surahs\\')', 'link-s1-s2')">
                <td><strong>1. الشاشة الرئيسية</strong></td>
                <td>زر "انطلق في مسار السور" (CTA)</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click</td>
                <td>2. شاشة اختيار السورة</td>
                <td><span class="code-badge">NAVIGATE_TO('screen_surahs')</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(2)">انتقل للسور ➔</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s1-parent', 1, 4, 'OPEN_PARENT_GATE()', 'link-s1-s4')">
                <td><strong>1. الشاشة الرئيسية</strong></td>
                <td>ترس وقفل بوابة الوالدين (Parent Lock)</td>
                <td><span class="meta-tag parent">الوالد</span></td>
                <td>Click + Math</td>
                <td>4. نافذة إعدادات الوالدين (Modal)</td>
                <td><span class="code-badge">OPEN_PARENT_GATE_MODAL()</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(4)">افتح البوابة 🔒</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s2-card', 2, 3, 'SELECT_SURAH(id)', 'link-s2-s3')">
                <td><strong>2. اختيار السورة</strong></td>
                <td>بطاقات السور (37 سورة من جزء عم)</td>
                <td><span class="meta-tag core">تشاركي</span></td>
                <td>Click</td>
                <td>3. شاشة اختيار الهدية المرتقبة</td>
                <td><span class="code-badge">SELECT_SURAH(id) -> NAV('screen_gift')</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(3)">انتقل للهدية ➔</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s2-back', 2, 1, 'NAVIGATE_TO(\\'screen_onboarding\\')', 'link-s2-s1')">
                <td><strong>2. اختيار السورة</strong></td>
                <td>زر العودة للشاشة الرئيسية 🔙</td>
                <td><span class="meta-tag core">تشاركي</span></td>
                <td>Click</td>
                <td>1. الشاشة الرئيسية واختيار البطل</td>
                <td><span class="code-badge">NAVIGATE_TO('screen_onboarding')</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(1)">عودة للرئيسية ↩</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s2-parent', 2, 4, 'OPEN_PARENT_GATE()', 'link-s2-s4')">
                <td><strong>2. اختيار السورة</strong></td>
                <td>ترس إعدادات الوالدين في الرأس ⚙️</td>
                <td><span class="meta-tag parent">الوالد</span></td>
                <td>Click + Math</td>
                <td>4. نافذة إعدادات الوالدين (Modal)</td>
                <td><span class="code-badge">OPEN_PARENT_GATE_MODAL()</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(4)">افتح الإعدادات ⚙️</button></td>
              </tr>
              <tr onclick="selectScreenNode(3)">
                <td><strong>3. اختيار الهدية</strong></td>
                <td>تبويبات تصنيفات الهدايا (سيارات/حيوانات)</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click</td>
                <td>تحديث معروض الألعاب في الشبكة</td>
                <td><span class="code-badge">FILTER_GIFTS(category)</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(3)">اعرض بالهدية</button></td>
              </tr>
              <tr onclick="selectScreenNode(3)">
                <td><strong>3. اختيار الهدية</strong></td>
                <td>بطاقة الهدية المحددة (Toy Card)</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click</td>
                <td>معاينة اللعبة داخل الصندوق ثلاثياً</td>
                <td><span class="code-badge">SELECT_GIFT(toyId)</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(3)">اعرض بالهدية</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s3-lock', 3, 5, 'LOCK_CHEST_AND_START()', 'link-s3-s5')">
                <td><strong>3. اختيار الهدية</strong></td>
                <td>زر "ضع الهدية في الصندوق وابدأ!" 🎁🔒</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click (CTA)</td>
                <td>5. شاشة الترديد النشط مع المنشاوي</td>
                <td><span class="code-badge">LOCK_CHEST_AND_START()</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(5)">ابدأ التلاوة ➔</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s3-back', 3, 2, 'NAVIGATE_TO(\\'screen_surahs\\')', 'link-s3-s2')">
                <td><strong>3. اختيار الهدية</strong></td>
                <td>زر العودة لاختيار السورة 🔙</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click</td>
                <td>2. شاشة اختيار السورة</td>
                <td><span class="code-badge">NAVIGATE_TO('screen_surahs')</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(2)">عودة للسور ↩</button></td>
              </tr>
              <tr onclick="selectScreenNode(4)">
                <td><strong>4. بوابة الوالدين</strong></td>
                <td>مسألة الجمع العشوائية (Math Gate)</td>
                <td><span class="meta-tag parent">الوالد</span></td>
                <td>Numeric Input</td>
                <td>فتح قفل الأمان للتحكم في الإعدادات</td>
                <td><span class="code-badge">VERIFY_CHALLENGE(answer)</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(4)">اعرض بالبوابة</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s4-close', 4, 2, 'SAVE_AND_CLOSE()', 'link-s4-s2')">
                <td><strong>4. بوابة الوالدين</strong></td>
                <td>زر حفظ التعديلات وإغلاق ✕</td>
                <td><span class="meta-tag parent">الوالد</span></td>
                <td>Click</td>
                <td>العودة للشاشة السابقة (الرئيسية 1 أو السور 2)</td>
                <td><span class="code-badge">CLOSE_PARENT_GATE()</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(2)">إغلاق وعودة ↩</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s5-tap', 5, null, 'AUDIO_TOGGLE_OR_REPEAT()')">
                <td><strong>5. الترديد النشط</strong></td>
                <td>لمسة خفية في أي مكان (Invisible Tap)</td>
                <td><span class="meta-tag parent">الوالد سراً</span></td>
                <td>Screen Tap</td>
                <td>إيقاف مؤقت أو إعادة فورية للآية الحالية</td>
                <td><span class="code-badge">AUDIO_TOGGLE_OR_REPEAT()</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(5)">اعرض بالترديد</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s5-exit', 5, 2, 'SAFE_EXIT_TO_SURAHS()', 'link-s5-s2')">
                <td><strong>5. الترديد النشط</strong></td>
                <td>نقرتان خفيتان في الزاوية العلوية</td>
                <td><span class="meta-tag parent">الوالد سراً</span></td>
                <td>Double Tap</td>
                <td>2. شاشة اختيار السورة (خروج هادئ)</td>
                <td><span class="code-badge">SAFE_EXIT_TO_SURAHS()</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(2)">خروج آمن ➔</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s5-auto', 5, 6, 'AUTO_TRIGGER_CELEBRATION()', 'link-s5-s6')">
                <td><strong>5. الترديد النشط</strong></td>
                <td>اكتمال تلاوة آيات السورة (حدث تلقائي)</td>
                <td><span class="meta-tag core">تلقائي</span></td>
                <td>Audio Finish</td>
                <td>6. شاشة الاحتفال وفتح صندوق الهدية</td>
                <td><span class="code-badge">TRIGGER_CELEBRATION()</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(6)">للاحتفال 🏆</button></td>
              </tr>
              <tr onclick="selectScreenNode(6)">
                <td><strong>6. الاحتفال والمكافأة</strong></td>
                <td>زر "العب بالهدية في الحديقة" 🎮</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click</td>
                <td>تفعيل حركة اللعبة وصوتها المبهج</td>
                <td><span class="code-badge">TRIGGER_TOY_INTERACTION()</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(6)">اعرض بالاحتفال</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s6-next', 6, 2, 'NAVIGATE_TO(\\'screen_surahs\\')', 'link-s6-s2')">
                <td><strong>6. الاحتفال والمكافأة</strong></td>
                <td>زر "سورة جديدة وهدية جديدة" 🚀</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click (CTA)</td>
                <td>2. شاشة اختيار السورة مع حفظ الوسام</td>
                <td><span class="code-badge">SAVE_PROGRESS() -> NAV('surahs')</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(2)">انتقل للسور ➔</button></td>
              </tr>
              <tr onclick="triggerButtonFromDiagram('btn-s6-repeat', 6, 5, 'RESTART_SURAH()', 'link-s6-s5')">
                <td><strong>6. الاحتفال والمكافأة</strong></td>
                <td>زر "إعادة تلاوة السورة" 🔁</td>
                <td><span class="meta-tag child">الطفل</span></td>
                <td>Click</td>
                <td>5. شاشة الترديد النشط لنفس السورة</td>
                <td><span class="code-badge">RESTART_SURAH('screen_recite')</span></td>
                <td><button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(5)">أعد التلاوة 🔁</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
""")

    # BLOCK 6: VIEW 4 - BLUEPRINT & ECC
    parts.append("""
    <!-- VIEW 4: Architectural Blueprint & ECC 2.2 Framework -->
    <div id="blueprint-view" class="view-panel">
      <article class="blueprint-article">
        
        <div class="blueprint-section">
          <h3><span>🏛️</span> 1. الهوية والفلسفة التأسيسية لمشروع "رِحْلة"</h3>
          <p>
            مشروع <strong>"رِحْلة - طريق رحلة حفظ القرآن"</strong> هو بيئة تربوية مصممة خصيصاً لمرحلة الطفولة المبكرة (الأعمار من 3 إلى 5 سنوات، مثل بطلنا الصغير "عُمَر"). ينطلق المشروع من قناعة راسخة بأن تعليم القرآن في هذه السن الذهبية هو <strong>طقس عاطفي وتشاركي (Shared Co-learning Ritual)</strong> يجلس فيه الوالد أو الوالدة بجوار الطفل، لا تطبيقاً يُترك فيه الطفل وحيداً أمام الشاشة.
          </p>
          <div class="blueprint-grid">
            <div class="blueprint-feature-card">
              <h4>🛡️ ميثاق صفر مايكروفون (Zero-Mic Architecture)</h4>
              <p>حظر قطعي لأي استخدام لمايكروفون الهاتف أو تسجيل صوت الطفل. محركات التعرف على الصوت عاجزة عن تقييم مخارج حروف أطفال سن 3-5 بدقة وتسبب إحباطاً شديداً عند التقييم الخاطئ. الطفل يقرأ لوالديه في الغرفة، والتطبيق يقدم الصوت المرجعي والبيئة المشجعة.</p>
            </div>
            <div class="blueprint-feature-card">
              <h4>🎙️ ميكانيكا لعبة الصوت الغائب (Audio Peek-a-boo)</h4>
              <p>استثمار الأداء الإعجازي للشيخ محمد صديق المنشاوي (المعلم). يتلو الشيخ الآية الكريمة، ثم يسكت التطبيق لفترة زمنية مبرمجة ومدروسة، يتحول فيها الأفاتار لدعوة الطفل لترديد الآية في الغرفة كأنه يلعب "استغماية صوتية".</p>
            </div>
            <div class="blueprint-feature-card">
              <h4>🎁 خطاف الهدية المرتقبة (The Golden Hook)</h4>
              <p>حل معضلة تشتت انتباه الأطفال: يختار الطفل هديته المبهجة (سيارة، طائرة، ديناصور) <em>قبل</em> بدء التلاوة، وتوضع في صندوق كنز مغلق أمام الأفاتار، ليظل متشوقاً لرؤية الصندوق ينفتح في نهاية السورة.</p>
            </div>
            <div class="blueprint-feature-card">
              <h4>🔒 بوابة الأمان الحسابية (Parental Math Gate)</h4>
              <p>منع تام لخروج الطفل العرضي من الجلسة أو العبث بالإعدادات عبر مسألة جمع عشوائية لا يستطيع طفل الـ 3-5 سنوات حلها، مما يمنح الوالدين تحكماً هادئاً وسلساً.</p>
            </div>
          </div>
        </div>

        <div class="blueprint-section">
          <h3><span>⚡</span> 2. تطبيق معايير هندسة البرمجيات والتصميم (ECC 2.2 Framework)</h3>
          <p>
            تم بناء هذا المخطط والمعمارية بالاعتماد على أدوات وحزم <strong>Everything Claude Code (ECC)</strong>، وتحديداً:
          </p>
          <ul style="padding-right: 24px; color: var(--text-muted); font-size: 0.9rem; line-height: 1.8;">
            <li><strong>وكيل التخطيط المعماري (Architect & Planner Agent):</strong> نمذجة حالات التطبيق على شكل آلة حالات قطعية (Deterministic State Machine) تضمن عدم حدوث أي تضارب بين المشغل الصوتي وتحديثات الواجهة.</li>
            <li><strong>مبادئ هندسة الواجهات (Make Interfaces Feel Better & Concentric Radius):</strong> التزام صارم بالنسب البصرية (Concentric Radius: outer = inner + padding)، واستبعاد كافة عناصر الذكاء الاصطناعي الرديئة (AI Slop) مثل التدرجات البنفسجية المبتذلة والبطاقات المتكدسة.</li>
            <li><strong>هندسة التدفق التناغمي (Harmonic Motion & Feedback):</strong> تفاعلات حركية هادفة تحافظ على سكينة القرآن الكريم مع إضفاء البهجة الطفولية في شاشة الاحتفال.</li>
            <li><strong>توافق صارم مع الخصوصية (COPPA & Privacy First):</strong> خلو التطبيق من أية أكواد تتبع أو وصول لأجهزة الاستشعار الصوتية أو الكاميرا.</li>
          </ul>
        </div>

        <div class="blueprint-section">
          <h3><span>🎨</span> 3. مواصفات شاشات Google Stitch للخطوة القادمة</h3>
          <p>
            هذا المخطط هو حجر الأساس البرمجي والفكري الذي سنبني عليه شاشات <strong>Google Stitch</strong>. عند فتح نافذة التصدير، ستحصل على برومبت هندسي فائق التفصيل لكل شاشة من الشاشات الست، محدد فيه موضع كل عنصر ولونه وحجمه بخط النسخ العربي الأصيل وأسلوب الرسم الكرتوني ثلاثي الأبعاد المريح للأطفال.
          </p>
        </div>

      </article>
    </div>
""")

    # BLOCK 7: GOOGLE STITCH PROMPT STUDIO MODAL
    parts.append("""
    <!-- Google Stitch Prompt Export Studio Modal -->
    <div class="stitch-modal-overlay" id="stitchModal" onclick="closeStitchModal(event)">
      <div class="stitch-modal-card" onclick="event.stopPropagation()">
        <div class="stitch-modal-header">
          <h3><span>🎨</span> استوديو موجهات Google Stitch (Screen Design Prompts)</h3>
          <button class="mock-btn subtle" onclick="closeStitchModal(null)">✕</button>
        </div>
        
        <!-- Tabbed selection for each screen -->
        <div class="stitch-tabs-row">
          <button class="stitch-tab-btn active" onclick="switchStitchTab(0, this)">التوجيه العام (Design System)</button>
          <button class="stitch-tab-btn" onclick="switchStitchTab(1, this)">شاشة 1: البطل والاسم</button>
          <button class="stitch-tab-btn" onclick="switchStitchTab(2, this)">شاشة 2: اختيار السورة</button>
          <button class="stitch-tab-btn" onclick="switchStitchTab(3, this)">شاشة 3: الهدية المرتقبة</button>
          <button class="stitch-tab-btn" onclick="switchStitchTab(4, this)">شاشة 4: بوابة الوالدين</button>
          <button class="stitch-tab-btn" onclick="switchStitchTab(5, this)">شاشة 5: الترديد مع المنشاوي</button>
          <button class="stitch-tab-btn" onclick="switchStitchTab(6, this)">شاشة 6: الاحتفال والمكافأة</button>
        </div>

        <div class="stitch-modal-body">
          <pre class="stitch-code-block" id="stitchPromptText">
=== GOOGLE STITCH SYSTEM DESIGN SPECIFICATION: RE7LA QURAN APP ===
Project: Re7la (رِحْلة - طريق رحلة حفظ القرآن)
Target Audience: Children aged 3-5 with co-learning parents
Art Direction: Warm modern Islamic garden aesthetic, 3D gentle clay/cartoon style (Pixar quality), emerald green (#047857), honey gold (#f59e0b), cream paper canvas (#faf8f5), rounded friendly geometry.
Typography: High-legibility Quranic Naskh / Cairo Arabic font with complete RTL.
          </pre>
        </div>
        
        <div class="stitch-modal-footer">
          <button class="mock-btn secondary" onclick="copyAllStitchPrompts()"><span>📑</span> نسخ كامل برومبتات المشروع</button>
          <button class="mock-btn primary" onclick="copyCurrentStitchPrompt()"><span>📋</span> نسخ برومبت هذه الشاشة فقط</button>
        </div>
      </div>
    </div>

    <!-- Toast Notification Container -->
    <div class="toast-container" id="toastBox"></div>

    <!-- Footer -->
    <footer class="app-footer">
      <div>
        <strong>مشروع رِحْلة (Re7la Project)</strong> &bull; رحلة قرآنية تربوية للطفل والوالدين &bull; تصميم معماري متكامل
      </div>
      <div style="font-family: var(--font-mono); font-size: 0.75rem;">
        ECC-Plugin v2.2.0 &bull; Everything Claude Code &bull; Standalone Artifact &bull; RTL Quranic UX
      </div>
    </footer>
  </main>
""")

    # BLOCK 8: COMPLETE JAVASCRIPT LOGIC
    parts.append("""
  <!-- Interactive JavaScript Engine -->
  <script>
    // Audio Synthesizer (Web Audio API - No external assets required)
    let audioCtx = null;
    let isSoundEnabled = true;

    function playTone(freq, duration = 0.12, type = 'sine', gainVal = 0.15) {
      if (!isSoundEnabled) return;
      try {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(gainVal, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + duration);
      } catch (e) {
        // AudioContext not allowed before user gesture
      }
    }

    function playChime(kind = 'click') {
      if (!isSoundEnabled) return;
      if (kind === 'click') {
        playTone(587.33, 0.08, 'sine', 0.12); // D5
      } else if (kind === 'start') {
        playTone(523.25, 0.1, 'triangle', 0.2); // C5
        setTimeout(() => playTone(659.25, 0.15, 'triangle', 0.2), 90); // E5
        setTimeout(() => playTone(783.99, 0.25, 'triangle', 0.25), 180); // G5
      } else if (kind === 'lock') {
        playTone(220.00, 0.12, 'square', 0.15); // Low wood thump
        setTimeout(() => playTone(440.00, 0.1, 'sine', 0.15), 60);
      } else if (kind === 'celebrate') {
        playTone(523.25, 0.15, 'triangle', 0.2);
        setTimeout(() => playTone(659.25, 0.15, 'triangle', 0.2), 100);
        setTimeout(() => playTone(783.99, 0.15, 'triangle', 0.25), 200);
        setTimeout(() => playTone(1046.50, 0.35, 'triangle', 0.3), 300);
      }
    }

    function toggleAudioFx() {
      isSoundEnabled = !isSoundEnabled;
      const icon = document.getElementById("soundIcon");
      icon.textContent = isSoundEnabled ? "🔊" : "🔇";
      showToast(isSoundEnabled ? "تم تفعيل المؤثرات الصوتية 🔊" : "تم كتم المؤثرات الصوتية 🔇");
    }

    // Screens Full Data Store
    const SCREENS_DATA = {
      1: {
        id: 1,
        title: "الشاشة الرئيسية: اختيار البطل والاسم",
        code: "Screen_Onboarding_Hero",
        persona: "الطفل (3-5 سنوات) بمصاحبة الوالد",
        badge: "شاشة 1: البداية والتخصيص",
        purpose: "الترحيب بالطفل وإشعاره بالفخر والشخصنة من خلال اختيار جنس البطل (عمر أو مريم) واسمه في بيئة بصرية دافئة ومبهجة.",
        micStatus: "🛡️ صفر مايكروفون (لا يطلب أي أذونات نهائياً)",
        buttons: [
          {
            id: "btn-s1-boy",
            name: "بطاقة البطل الولد (عمر)",
            type: "نقر اختيار",
            dest: "تحديث الأفاتار فورياً",
            action: "SET_AVATAR('boy')",
            desc: "تغيير المظهر الكرتوني لبطل ولد مبتسم يرتدي زياً إسلامياً مريحاً.",
            linkId: null
          },
          {
            id: "btn-s1-girl",
            name: "بطاقة البطلة البنت (مريم)",
            type: "نقر اختيار",
            dest: "تحديث الأفاتار فورياً",
            action: "SET_AVATAR('girl')",
            desc: "تغيير المظهر لبطلة كرتونية مبتسمة بملابس لطيفة.",
            linkId: null
          },
          {
            id: "btn-s1-start",
            name: "زر انطلق في مسار السور (CTA)",
            type: "زر رئيسي عريض",
            dest: "2. شاشة اختيار السورة",
            action: "NAVIGATE_TO('screen_surahs')",
            desc: "الانتقال المباشر لخريطة سور جزء عم الـ 37 مع حفظ بيانات الطفل المختارة.",
            linkId: "link-s1-s2",
            targetScreen: 2
          },
          {
            id: "btn-s1-parent",
            name: "ترس بوابة الوالدين الهادئ 🔒",
            type: "أيقونة بالزاوية العلوية",
            dest: "4. نافذة إعدادات الوالدين",
            action: "OPEN_PARENT_GATE_MODAL()",
            desc: "طلب حل مسألة الأمان الحسابية لفتح نافذة التكرارات والتحكم الصوتي.",
            linkId: "link-s1-s4",
            targetScreen: 4
          }
        ]
      },
      2: {
        id: 2,
        title: "شاشة اختيار السورة (سور جزء عم)",
        code: "Screen_Surah_Selection",
        persona: "تشاركي (الطفل بمساعدة الوالد)",
        badge: "شاشة 2: سور جزء عم",
        purpose: "استعراض سور جزء عم الـ 37 بالترتيب القرآني التوقيفي الشريف، وتحديد السورة المستهدفة للحفظ اليومي.",
        micStatus: "🛡️ صفر مايكروفون (واجهة رسومية خالية تماماً من التسجيل)",
        buttons: [
          {
            id: "btn-s2-card",
            name: "بطاقة السورة (37 سورة)",
            type: "نقر بطاقة السورة",
            dest: "3. شاشة اختيار الهدية",
            action: "SELECT_SURAH(id) -> NAV('screen_gift')",
            desc: "اختيار سورة محددة (مثل الإخلاص، الفلق، الناس) ونقل الطفل فوراً لمرحلة حجز هديته المرتقبة.",
            linkId: "link-s2-s3",
            targetScreen: 3
          },
          {
            id: "btn-s2-back",
            name: "زر الرجوع للشاشة الرئيسية 🔙",
            type: "زر تنقل عودة",
            dest: "1. الشاشة الرئيسية",
            action: "NAVIGATE_TO('screen_onboarding')",
            desc: "العودة لتغيير البطل أو الاسم إذا رغب الطفل.",
            linkId: "link-s2-s1",
            targetScreen: 1
          },
          {
            id: "btn-s2-parent",
            name: "أيقونة إعدادات الوالد ⚙️",
            type: "نقر مباشر",
            dest: "4. نافذة إعدادات الوالدين",
            action: "OPEN_PARENT_GATE_MODAL()",
            desc: "الوصول السريع لضبط تكرار الآيات وسرعة الشيخ ومسألة الأمان.",
            linkId: "link-s2-s4",
            targetScreen: 4
          },
          {
            id: "btn-s2-filter",
            name: "فلترة قصار السور / البحث",
            type: "تبويب تصفية",
            dest: "تحديث قائمة السور",
            action: "FILTER_SURAHS()",
            desc: "تصفية السور حسب الطول أو البحث بالاسم.",
            linkId: null
          }
        ]
      },
      3: {
        id: 3,
        title: "شاشة اختيار الهدية المرتقبة (الخطاف الذهبي)",
        code: "Screen_Gift_Hook_Selection",
        persona: "الطفل (ميكانيكا الدوبامين الذاتي)",
        badge: "شاشة 3: الهدية المرتقبة",
        purpose: "تطبيق ميكانيكا الهدية المرتقبة (The Golden Hook). يختار الطفل مكافأته قبل التلاوة، وتوضع في صندوق كنز مغلق يرافقه في شاشة الترديد.",
        micStatus: "🛡️ صفر مايكروفون (تفاعل حركي وصوتي ممتع دون تسجيل)",
        buttons: [
          {
            id: "btn-s3-tabs",
            name: "تبويبات فئات الألعاب (سيارات/حيوانات)",
            type: "نقر تبويب",
            dest: "تحديث معروض الألعاب",
            action: "FILTER_GIFTS(cat)",
            desc: "تصفية الألعاب المناسبة للأولاد والبنات (سيارة سباق، طائرة، ديناصور لطيف، دمية).",
            linkId: null
          },
          {
            id: "btn-s3-toy",
            name: "بطاقة اللعبة المحددة",
            type: "نقر اختيار",
            dest: "معاينة اللعبة داخل الصندوق",
            action: "SELECT_GIFT(toyId)",
            desc: "سماع نغمة بهيجة ودوران اللعبة تمهيداً لوضعها في الصندوق.",
            linkId: null
          },
          {
            id: "btn-s3-lock",
            name: "زر: ضع الهدية في الصندوق وابدأ! 🎁",
            type: "زر تأكيد وبدء التلاوة (CTA)",
            dest: "5. شاشة الترديد النشط",
            action: "LOCK_CHEST_AND_START()",
            desc: "إغلاق قفل الصندوق بصوت كرتوني مميز والانتقال الفوري للجلسة القرآنية.",
            linkId: "link-s3-s5",
            targetScreen: 5
          },
          {
            id: "btn-s3-back",
            name: "زر الرجوع لاختيار السورة 🔙",
            type: "زر تنقل عودة",
            dest: "2. شاشة اختيار السورة",
            action: "NAVIGATE_TO('screen_surahs')",
            desc: "العودة لتغيير السورة المستهدفة.",
            linkId: "link-s3-s2",
            targetScreen: 2
          }
        ]
      },
      4: {
        id: 4,
        title: "نافذة إعدادات الوالدين وبوابة الأمان الحسابية",
        code: "Modal_Parental_Math_Gate",
        persona: "الوالد والوالدة فقط (Protected)",
        badge: "شاشة 4: بوابة الأمان",
        purpose: "حماية الجلسة من عبث الطفل وتمكين الوالد من تخصيص تكرارات الشيخ وسرعته ومدد الوقف المناسبة للطفل.",
        micStatus: "🛡️ صفر مايكروفون (حماية خصوصية وأمان تام)",
        buttons: [
          {
            id: "btn-s4-math",
            name: "بوابة الأمان الحسابية (Math Challenge)",
            type: "إدخال حسابي",
            dest: "فتح القفل الرقمي",
            action: "VERIFY_CHALLENGE(answer)",
            desc: "حل مسألة جمع عشوائية لمنع الطفل من تغيير الإعدادات.",
            linkId: null
          },
          {
            id: "btn-s4-repeat",
            name: "خيارات تكرار الآية (1x, 2x, 3x, 5x)",
            type: "أزرار اختيار متعدد",
            dest: "تحديث مشغل التلاوة",
            action: "SET_REPETITIONS(n)",
            desc: "تحديد عدد مرات تلاوة الشيخ للآية الواحدة قبل الانتقال للآية التالية.",
            linkId: null
          },
          {
            id: "btn-s4-pause",
            name: "محدد مدة الوقف الصوتي للترديد",
            type: "شريط تمرير نسبي",
            dest: "تحديث وقفة المنشاوي",
            action: "SET_PAUSE_RATIO(1.0x - 2.0x)",
            desc: "زيادة زمن صمت الشيخ ليتمكن الطفل الأصغر سناً من الترديد على مهل دون عجلة.",
            linkId: null
          },
          {
            id: "btn-s4-link",
            name: "مفتاح ربط الآيات التراكمي",
            type: "مفتاح تبديل (Toggle)",
            dest: "تحديث منطق التلاوة",
            action: "TOGGLE_LINKING(bool)",
            desc: "تلاوة الآية السابقة مع الحالية لترسيخ الذاكرة التراكمية للحفظ.",
            linkId: null
          },
          {
            id: "btn-s4-close",
            name: "زر حفظ وإغلاق ✕",
            type: "زر إغلاق النافذة",
            dest: "العودة للشاشة السابقة (1 أو 2)",
            action: "CLOSE_PARENT_GATE()",
            desc: "حفظ الإعدادات في الذاكرة المحلية والعودة لمتابعة التدفق.",
            linkId: "link-s4-s2",
            targetScreen: 2
          }
        ]
      },
      5: {
        id: 5,
        title: "شاشة الترديد النشط مع المنشاوي (لعبة الصوت الغائب)",
        code: "Screen_Active_Recitation_ZeroMic",
        persona: "تشاركية: استماع وترديد في الغرفة مع الوالد",
        badge: "شاشة 5: قلب التطبيق والترديد",
        purpose: "التجربة القرآنية الخالصة. لا توجد أي أزرار ظاهرة للطفل على الإطلاق. المنشاوي يتلو، والأفاتار ينصت ثم يدعو الطفل للترديد لوالديه، مع صندوق الهدية المغلق الذي يهتز شوقاً للفتح.",
        micStatus: "🛡️ صفر مايكروفون قطعي (The Child recites to Parent, NOT to phone)",
        buttons: [
          {
            id: "btn-s5-tap",
            name: "لمسة خفية في أي مكان (Invisible Tap)",
            type: "إيماءة الوالد السرية",
            dest: "إيقاف مؤقت / إعادة فورية",
            action: "AUDIO_TOGGLE_OR_REPEAT()",
            desc: "يضغط الوالد بإصبعه في أي مكان خلسة لإيقاف التلاوة أو إعادة الآية إذا تعثر الطفل.",
            linkId: null
          },
          {
            id: "btn-s5-exit",
            name: "نقرتان خفيتان في الزاوية العلوية",
            type: "إيماءة خروج الوالد",
            dest: "2. شاشة اختيار السورة",
            action: "SAFE_EXIT_TO_SURAHS()",
            desc: "الخروج الآمن والهادئ من الجلسة في أي وقت دون إرباك الطفل.",
            linkId: "link-s5-s2",
            targetScreen: 2
          },
          {
            id: "btn-s5-auto",
            name: "اكتمال تلاوة آيات السورة (حدث تلقائي)",
            type: "مشغل صوتي تلقائي",
            dest: "6. شاشة الاحتفال وفتح الصندوق",
            action: "TRIGGER_CELEBRATION()",
            desc: "عند اكتمال آخر آية، ينطلق صوت التكبير الاحتفالي فوراً وينتقل المشهد لفتح الصندوق.",
            linkId: "link-s5-s6",
            targetScreen: 6
          }
        ]
      },
      6: {
        id: 6,
        title: "شاشة الاحتفال وفتح صندوق الهدية",
        code: "Screen_Celebration_Unboxing",
        persona: "الطفل والوالدان (ذروة الدوبامين والبهجة)",
        badge: "شاشة 6: المكافأة والاحتفال",
        purpose: "الاحتفال بإنجاز السورة، فتح صندوق الكنز بانفجار ضوئي برّاق، وانطلاق اللعبة التي اختارها الطفل ليلعب بها مع الأفاتار في الحديقة.",
        micStatus: "🛡️ صفر مايكروفون (مؤثرات بصرية وصوتية احتفالية فقط)",
        buttons: [
          {
            id: "btn-s6-play",
            name: "زر العب بالهدية في الحديقة 🎮",
            type: "نقر تفاعلي",
            dest: "أنيميشن حركة اللعبة",
            action: "TRIGGER_TOY_INTERACTION()",
            desc: "تتحرك السيارة وتطلق بوقاً مبهجاً، أو يطير الصاروخ في حديقة الأفاتار.",
            linkId: null
          },
          {
            id: "btn-s6-next",
            name: "زر سورة جديدة وهدية جديدة 🚀",
            type: "زر تقدم رئيسي (CTA)",
            dest: "2. شاشة اختيار السورة",
            action: "SAVE_PROGRESS() -> NAV('screen_surahs')",
            desc: "حفظ وسام السورة في سجل الطفل والعودة لاختيار سورة تالية بهدية جديدة.",
            linkId: "link-s6-s2",
            targetScreen: 2
          },
          {
            id: "btn-s6-repeat",
            name: "زر إعادة تلاوة السورة 🔁",
            type: "زر تكرار للتثبيت",
            dest: "5. شاشة الترديد النشط",
            action: "RESTART_SURAH('screen_recite')",
            desc: "الاستمتاع بتلاوة نفس السورة مرة أخرى لترسيخ الحفظ في الذاكرة.",
            linkId: "link-s6-s5",
            targetScreen: 5
          }
        ]
      }
    };

    // Google Stitch Prompt Data Library
    const STITCH_PROMPTS = [
      `=== GOOGLE STITCH: GLOBAL SYSTEM & ART DIRECTION ===
Project: Re7la (مشروع رِحْلة - طريق رحلة حفظ القرآن)
Target Audience: Children aged 3-5 with co-learning parents (Co-learning Shared Ritual)
Philosophy: Output-only app (ZERO MICROPHONE ACCESS DURING CHILD RECITATION). Sheikh Al-Minshawi Audio Peek-a-boo. Anticipated Gift Hook unboxing. Real parent's cheering voice stored locally in IndexedDB.
Art Direction:
- Theme: Sunny Daylight Garden aesthetic with soft natural sunlight (Daylight Meadow).
- Character Style: 3D playful cartoon render (Pixar & Studio Ghibli sunny quality), Omar the 3-year-old hero holding his green Quran.
- Scene Elements: Rolling green hills, lush meadow, mosque with emerald green turquoise dome on left, big shady leafy tree on right, winding golden cobblestone path with Surah milestones ascending.
- Color Palette:
  * Sky Radiant (#38bdf8, #e0f2fe)
  * Meadow Lime (#84cc16, #ecfccb)
  * Cobblestone Gold (#facc15, #ca8a04)
  * Mosque Teal (#0d9488, #ccfbf1)
  * Pure Cloud White (#ffffff)
  * Strawberry Coral (#f43f5e)
- Strict Anti-AI-Slop: Hand-crafted charm, no AI voices, authentic Minshawi recitation, real parent voice.
- Typography: Authentic Quranic Amiri for Quranic verses, Cairo / Tajawal (weights 700, 800, 900) for UI. Full RTL.`,

      `=== SCREEN 1: WINDING GOLDEN ROADMAP & HERO MILESTONE ===
Platform: Mobile Portrait (9:16)
Art Style: Vibrant sunny morning meadow with radiant sky and rolling green hills.
Landscape Elements:
- Left Horizon: Mosque with graceful emerald turquoise dome and minaret.
- Right Foreground: Shady leafy green tree where Omar rests.
- Golden Cobblestone Road: Winding upward carrying Surah milestones:
  * Milestone 1 (Bottom): Surah An-Nas (Completed ✓ with green star).
  * Milestone 2 (Active): Surah Al-Falaq (Glowing golden stop 🌟 where Omar stands holding his Quran).
  * Milestone 3: Surah Al-Ikhlas (Locked treasure chest awaiting 🔒🎁).
  * Milestone 4: Surah Al-Masad (Locked stop 🔒).
- Wooden Signboard at Bottom: Cute rustic sign carved: "كل يوم آية جديدة ❤️".
Header HUD:
- Top Right: "رِحْلة ⭐" logo with rank "مستكشف صغير" and "جزء عم: 1/30".
- Top Left: Parental settings gear ⚙️ 🔒.
Primary Action:
- Emerald/Sky Blue wide pill button: "انطلق في مسار السور 🚀" with gentle pulsing glow.
Zero-Mic Banner:
- Discreet bottom badge: "🛡️ صفر مايكروفون أثناء الترديد (Output Only)".`,

      `=== SCREEN 2: SURAH WINDING PATH PROGRESSION (JUZ' AMMA - 37 SURAHS) ===
Platform: Mobile Portrait (9:16)
Header:
- Greeting: "مسار السور الذهبي 📖 ⭐ إنجازات عمر: 1 سورة مكتملة"
- Navigation: Back button 🔙 and Parental gear ⚙️.
Content Grid / Road Progression:
- Vertical ascending milestone cards along the winding garden path:
  1. Surah An-Nas: 6 verses, completed badge, golden star ⭐.
  2. Surah Al-Falaq: 5 verses, active glowing card with "ابدأ الآن 🌟" badge and Omar avatar preview.
  3. Surah Al-Ikhlas: 4 verses, next reward anticipation card with gift icon 🎁.
  4. Surah Al-Masad: 5 verses, locked milestone 🔒.
- Card Styling: Pure cloud white (#ffffff) with delicate sunny borders (#facc15 / #bae6fd).`,

      `=== SCREEN 3: THE GOLDEN HOOK (ANTICIPATED GIFT SELECTION) ===
Platform: Mobile Portrait (9:16)
Concept: The child chooses their desired reward BEFORE reciting. The toy gets locked in a chest.
Header:
- Joyful heading: "اختر هديتك التي ستفتحها بعد تلاوة سورة الفلق! 🎁"
Category Tabs:
- Horizontal scrolling pill tabs: "سيارات سباق 🏎️", "حيوانات الغابة 🦁", "طائرات وصواريخ ✈️", "ألغاز ومكعبات 🧩".
Showcase Card:
- 3D rotating preview of selected toy (Shiny red cartoon racecar with playful eyes).
- Joyful bounce animation on tap with cartoon sound effects.
Treasure Chest Preview:
- In front of the toy, a rich handcrafted wooden treasure chest with brass bands and a smiling golden padlock: 📦🔒.
Primary CTA:
- Pulsing golden CTA button: "ضع الهدية في الصندوق وابدأ! 🔒✨".
- Animation upon click: Toy leaps into chest, lid slams shut with a cartoon "CLACK", padlock snaps shut.`,

      `=== SCREEN 4: PLAY SETTINGS, PARENT VOICE & PARENTAL GATE ===
Platform: Mobile Floating Modal (Overlaid on sunny garden backdrop)
Visual: Soft white cloud card (#ffffff) with Omar the hero sitting cutely on the top edge.
Parental Security Gate:
- Random math question: "8 + 5 = [ 13 ] ✓" to prevent toddler accidental tampering.
Settings Controls:
1. Child Avatar & Photo: Choice of boy (Omar), girl (Maryam), or (+) upload child's real face photo blended on canvas and stored in IndexedDB.
2. Parent's Voice Recorder: Microphone button for parent to record their real encouragement voice ("عاش يا بطل يا عمر! أنا فخور بيك يا حبيبي") saved as Blob in IndexedDB.
3. Verse Repetitions: Tactile circular buttons [ 1 | 2 | 3 | 4 | 5 ].
4. Auto-Play Toggle: Continuous recitation switch without touching the screen.
CTA:
- Golden "حفظ التعديلات وإغلاق ✓" button returning to Screen 1 or Screen 2.`,

      `=== SCREEN 5: ACTIVE RECITATION (SURAH AL-FALAQ & SHEIKH AL-MINSHAWI) ===
Platform: Mobile Portrait (9:16)
CRITICAL: ZERO visible child buttons on screen! Zero microphone prompts!
Setting: Sunny garden under the big leafy green tree on the right.
Hero: Omar stands under the tree holding his green Quran.
Top HUD:
- Surah title: "سُورَةُ الفَلَقِ" (5 verses).
- 5 Verse Progress Pearls: (1) lit in golden yellow (#facc15), (2), (3), (4), (5).
- Completely invisible top-corner double-tap area for parent safe exit.
Central Luxury Verse Card:
- Pure cloud white card with authentic bold Quranic text in Amiri font:
  "﴿ قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ ﴾"
- Recitation mode toggles: [ 🌿 الشيخ والأطفال (المصحف المعلم) ] and [ 🌊 الشيخ فقط ].
Foreground:
- Closed golden treasure chest resting on the grass, trembling and emitting tiny sparkle particles with each verse.
Parent Interaction:
- Single invisible tap anywhere on screen instantly pauses or repeats the current verse (Audio Peek-a-boo).`,

      `=== SCREEN 6: CELEBRATION, TREASURE UNBOXING & PARENT VOICE CHEERING ===
Platform: Mobile Portrait (9:16)
Atmosphere: Pure ecstatic joy, sunlight beams, and colorful confetti rain!
Visual Effects:
- Radiant sunburst beams radiating from center.
- Chest lid flies open: 📦🔓✨ with golden fireworks.
- The child's chosen toy (Red racecar) bursts out, revving its engine and racing across the meadow grass!
Parent Voice Cheering Launch:
- Instant playback of the real recorded parent's voice:
  "عاش يا بطل يا عُمر! أنا فخور بيك يا حبيبي ومبارك حفظ سورة الفلق!"
Actions:
- "العب بالهدية في الحديقة 🎮" (Interactively drives the toy across screen).
- "سورة جديدة وهدية جديدة 🚀" (Primary CTA returning to Screen 2 to unlock Surah Al-Ikhlas).
- "إعادة تلاوة سورة الفلق 🔁" (Repeats same Surah to consolidate memorization).`
    ];

    // Current State Variables
    let currentSelectedScreen = 1;
    let activeStitchTabIndex = 0;

    // Pan & Zoom Engine State
    let isPanning = false;
    let startX = 0, startY = 0;
    let panX = 0, panY = 0;
    let scale = 1.0;
    let initialTouchDist = null;

    // DOM Elements Cache
    let svgContainer, diagramSvg, diagramViewport;

    // Initialize application on DOM ready
    document.addEventListener("DOMContentLoaded", () => {
      svgContainer = document.getElementById("svgContainer");
      diagramSvg = document.getElementById("appDiagramSvg");
      diagramViewport = document.getElementById("diagramViewport");

      initPanZoomEngine();
      renderInspector(1);
      updateStitchPromptDisplay();
    });

    // ==========================================
    // 1. GENUINE PAN & ZOOM ENGINE
    // ==========================================
    function initPanZoomEngine() {
      if (!svgContainer || !diagramViewport) return;

      // Mouse drag handlers
      svgContainer.addEventListener("mousedown", (e) => {
        // If clicked on an interactive button or text, avoid initiating pan
        if (e.target.closest(".diagram-btn-pill") || e.target.closest("button")) return;
        isPanning = true;
        startX = e.clientX - panX;
        startY = e.clientY - panY;
        svgContainer.style.cursor = "grabbing";
      });

      window.addEventListener("mousemove", (e) => {
        if (!isPanning) return;
        panX = e.clientX - startX;
        panY = e.clientY - startY;
        applyViewportTransform();
      });

      window.addEventListener("mouseup", () => {
        if (isPanning) {
          isPanning = false;
          svgContainer.style.cursor = "grab";
        }
      });

      // Mouse Wheel Zoom centered on cursor
      svgContainer.addEventListener("wheel", (e) => {
        e.preventDefault();
        const rect = svgContainer.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        const zoomFactor = e.deltaY < 0 ? 1.12 : 0.89;
        const newScale = Math.min(Math.max(scale * zoomFactor, 0.45), 3.0);

        // Focal point formula
        panX = mouseX - (mouseX - panX) * (newScale / scale);
        panY = mouseY - (mouseY - panY) * (newScale / scale);
        scale = newScale;

        applyViewportTransform();
      }, { passive: false });

      // Touch Drag & Pinch Zoom for mobile / tablets
      svgContainer.addEventListener("touchstart", (e) => {
        if (e.touches.length === 1) {
          isPanning = true;
          startX = e.touches[0].clientX - panX;
          startY = e.touches[0].clientY - panY;
        } else if (e.touches.length === 2) {
          isPanning = false;
          initialTouchDist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
        }
      }, { passive: true });

      svgContainer.addEventListener("touchmove", (e) => {
        if (e.touches.length === 1 && isPanning) {
          panX = e.touches[0].clientX - startX;
          panY = e.touches[0].clientY - startY;
          applyViewportTransform();
        } else if (e.touches.length === 2 && initialTouchDist) {
          const dist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
          const factor = dist / initialTouchDist;
          scale = Math.min(Math.max(scale * factor, 0.45), 3.0);
          initialTouchDist = dist;
          applyViewportTransform();
        }
      }, { passive: true });

      svgContainer.addEventListener("touchend", () => {
        isPanning = false;
        initialTouchDist = null;
      });
    }

    function applyViewportTransform() {
      if (!diagramViewport) return;
      diagramViewport.setAttribute("transform", `translate(${panX}, ${panY}) scale(${scale})`);
    }

    function zoomDiagram(factor) {
      playChime('click');
      scale = Math.min(Math.max(scale * factor, 0.45), 3.0);
      applyViewportTransform();
    }

    function resetDiagramZoom() {
      playChime('click');
      scale = 1.0;
      panX = 0;
      panY = 0;
      applyViewportTransform();
      showToast("تمت إعادة ضبط موضع المخطط ⟲");
    }

    function fitDiagramToScreen() {
      playChime('click');
      const rect = svgContainer.getBoundingClientRect();
      const scaleX = rect.width / 1350;
      const scaleY = rect.height / 780;
      scale = Math.min(scaleX, scaleY) * 0.95;
      panX = (rect.width - 1350 * scale) / 2;
      panY = (rect.height - 780 * scale) / 2;
      applyViewportTransform();
      showToast("تمت ملاءمة المخطط على الشاشة ⛶");
    }

    // ==========================================
    // 2. VIEW SWITCHING
    // ==========================================
    function switchView(viewId, btnElement) {
      playChime('click');
      document.querySelectorAll(".view-panel").forEach(panel => {
        panel.classList.remove("active");
      });
      document.querySelectorAll(".nav-tab-btn").forEach(btn => {
        btn.classList.remove("active");
      });

      const target = document.getElementById(viewId);
      if (target) target.classList.add("active");
      if (btnElement) btnElement.classList.add("active");
    }

    // ==========================================
    // 3. DIAGRAM & INSPECTOR SELECTION
    // ==========================================
    function selectScreenNode(screenId) {
      currentSelectedScreen = screenId;
      playChime('click');

      // Update Node Highlight in SVG
      document.querySelectorAll(".diagram-node").forEach(node => {
        node.classList.remove("selected");
        node.classList.remove("target-highlight");
      });
      const nodeEl = document.getElementById(`node-screen${screenId}`);
      if (nodeEl) nodeEl.classList.add("selected");

      // Clear button active pills
      document.querySelectorAll(".diagram-btn-pill").forEach(pill => {
        pill.classList.remove("active-btn");
      });

      // Highlight links associated with this screen
      highlightScreenLinks(screenId);

      // Render Inspector details
      renderInspector(screenId);
    }

    function highlightScreenLinks(screenId) {
      document.querySelectorAll(".link-path").forEach(path => {
        path.classList.remove("active-link");
      });

      const screenLinks = {
        1: ["link-s1-s2", "link-s1-s4"],
        2: ["link-s2-s3", "link-s2-s4", "link-s2-s1"],
        3: ["link-s3-s5", "link-s3-s2"],
        4: ["link-s4-s1", "link-s4-s2"],
        5: ["link-s5-s6", "link-s5-s2"],
        6: ["link-s6-s2", "link-s6-s5"]
      };

      const links = screenLinks[screenId] || [];
      links.forEach(lid => {
        const pathEl = document.getElementById(lid);
        if (pathEl) pathEl.classList.add("active-link");
      });
    }

    // Trigger button from either SVG diagram or inspector
    function triggerButtonFromDiagram(btnId, sourceScreen, targetScreen, actionCode, linkId) {
      playChime('click');
      currentSelectedScreen = sourceScreen;

      // Select source screen node
      selectScreenNode(sourceScreen);

      // Highlight the specific link path
      document.querySelectorAll(".link-path").forEach(p => p.classList.remove("active-link"));
      if (linkId) {
        const linkEl = document.getElementById(linkId);
        if (linkEl) {
          linkEl.classList.add("active-link");
        }
      }

      // Highlight target node
      if (targetScreen) {
        const targetNode = document.getElementById(`node-screen${targetScreen}`);
        if (targetNode) {
          targetNode.classList.add("target-highlight");
          setTimeout(() => targetNode.classList.remove("target-highlight"), 2500);
        }
      }

      // Highlight clicked pill in inspector
      document.querySelectorAll(".btn-inspector-card").forEach(c => c.classList.remove("active-inspected"));
      const insCard = document.getElementById(`inspect-card-${btnId}`);
      if (insCard) {
        insCard.classList.add("active-inspected");
        insCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      showToast(`🎯 تفعيل: [${btnId}] ➔ ${targetScreen ? 'الوجهة: شاشة ' + targetScreen : 'تحديث الحالة'} | ${actionCode}`);
    }

    function renderInspector(screenId) {
      const data = SCREENS_DATA[screenId];
      if (!data) return;

      document.getElementById("inspectTitle").innerHTML = `<span>📱</span> ${data.title}`;
      document.getElementById("inspectBadge").textContent = data.badge;

      let buttonsHtml = "";
      data.buttons.forEach(btn => {
        const isParent = btn.name.includes("الوالد") || btn.name.includes("بوابة") || btn.name.includes("خفية");
        const hasDest = !!btn.targetScreen;
        buttonsHtml += `
          <div class="btn-inspector-card ${isParent ? 'parent-btn' : 'child-btn'}" id="inspect-card-${btn.id}" onclick="triggerButtonFromDiagram('${btn.id}', ${screenId}, ${btn.targetScreen || 'null'}, '${btn.action}', '${btn.linkId || ''}')">
            <div class="btn-card-top">
              <span class="btn-title">${btn.name}</span>
              <span class="btn-dest-tag">${btn.type}</span>
            </div>
            <div class="btn-desc">${btn.desc}</div>
            <div class="btn-action-code">
              <span>الوجهة: <strong>${btn.dest}</strong> &bull; <code>${btn.action}</code></span>
              ${hasDest ? `<button class="jump-to-dest-btn" onclick="event.stopPropagation(); selectScreenNode(${btn.targetScreen})">انتقل للشاشة ${btn.targetScreen} ➔</button>` : ''}
            </div>
          </div>
        `;
      });

      const html = `
        <div class="screen-meta-badge">
          <span class="meta-tag core">${data.code}</span>
          <span class="meta-tag child">${data.persona}</span>
          <span class="meta-tag parent">${data.micStatus}</span>
        </div>

        <div class="detail-card">
          <h4>🎯 الغرض المعماري والتربوي للشاشة</h4>
          <p>${data.purpose}</p>
        </div>

        <div>
          <h4 style="font-size: 0.92rem; font-weight: 800; margin-bottom: 10px; display: flex; align-items: center; justify-content: space-between;">
            <span>🔘 الأزرار والتفاعلات (${data.buttons.length})</span>
            <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: normal;">انقر لاختبار مسار الزر</span>
          </h4>
          <div class="buttons-list-group">
            ${buttonsHtml}
          </div>
        </div>

        <div style="margin-top: 10px;">
          <button class="mock-btn secondary" style="width: 100%; font-size: 0.8rem; padding: 8px;" onclick="scrollToMockCard('mock-s${screenId}')">
            📱 معاينة هذه الشاشة في محاكي الهواتف
          </button>
        </div>
      `;

      document.getElementById("inspectContent").innerHTML = html;
    }

    // ==========================================
    // 4. FLOW FILTERING & SEARCH
    // ==========================================
    function filterDiagramFlow(flowType, btnElement) {
      playChime('click');
      document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
      btnElement.classList.add("active");

      const paths = document.querySelectorAll(".link-path");
      paths.forEach(p => {
        p.style.opacity = "1";
        p.classList.remove("active-link");
      });

      if (flowType === "child") {
        paths.forEach(p => {
          if (!p.classList.contains("child-flow")) p.style.opacity = "0.15";
          else p.classList.add("active-link");
        });
        showToast("عرض رحلة الطفل الأساسية (1 ➔ 2 ➔ 3 ➔ 5 ➔ 6)");
      } else if (flowType === "parent") {
        paths.forEach(p => {
          if (!p.classList.contains("parent-flow")) p.style.opacity = "0.15";
          else p.classList.add("active-link");
        });
        showToast("عرض تدفقات بوابة الوالدين والتحكم الهادئ");
      } else if (flowType === "reward") {
        paths.forEach(p => {
          if (!p.classList.contains("reward-flow")) p.style.opacity = "0.15";
          else p.classList.add("active-link");
        });
        showToast("عرض حلقة المكافأة والهدية المرتقبة (The Golden Hook)");
      } else {
        showToast("عرض كافة المسارات والروابط");
      }
    }

    function handleDiagramSearch(query) {
      query = query.trim().toLowerCase();
      if (!query) {
        document.querySelectorAll(".diagram-node").forEach(n => n.style.opacity = "1");
        return;
      }
      for (let i = 1; i <= 6; i++) {
        const node = document.getElementById(`node-screen${i}`);
        const data = SCREENS_DATA[i];
        const match = data.title.toLowerCase().includes(query) ||
                      data.purpose.toLowerCase().includes(query) ||
                      data.buttons.some(b => b.name.toLowerCase().includes(query) || b.dest.toLowerCase().includes(query));
        if (node) {
          node.style.opacity = match ? "1" : "0.2";
          if (match && !document.querySelector(".diagram-node.selected")) {
            selectScreenNode(i);
          }
        }
      }
    }

    function handleMatrixSearch(query) {
      query = query.trim().toLowerCase();
      const rows = document.querySelectorAll("#matrixTable tbody tr");
      rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(query) ? "" : "none";
      });
    }

    // ==========================================
    // 5. WIREFRAME SIMULATOR NAVIGATION
    // ==========================================
    function scrollToMockCard(cardId) {
      switchView('wireframes-view', document.querySelectorAll(".nav-tab-btn")[1]);
      const card = document.getElementById(cardId);
      if (card) {
        card.scrollIntoView({ behavior: "smooth", block: "center" });
        card.classList.add("phone-highlight-pulse");
        setTimeout(() => card.classList.remove("phone-highlight-pulse"), 1600);
      }
    }

    function navigateToScreenMock(screenId, actionLabel, triggerBtnId) {
      playChime('start');
      showToast(`⚡ تنقل: ${actionLabel} ➔ الشاشة ${screenId}`);

      // Highlight step in Journey Bar
      for (let i = 1; i <= 6; i++) {
        const step = document.getElementById(`journeyStep${i}`);
        if (step) {
          if (i === screenId) step.classList.add("active");
          else step.classList.remove("active");
        }
      }

      // Scroll to phone card
      const targetCard = document.getElementById(`mock-s${screenId}`);
      if (targetCard) {
        targetCard.scrollIntoView({ behavior: "smooth", block: "center" });
        targetCard.classList.add("phone-highlight-pulse");
        setTimeout(() => targetCard.classList.remove("phone-highlight-pulse"), 1600);
      }

      // Update diagram selection in background
      selectScreenNode(screenId);
    }

    function setPhoneHero(gender) {
      playChime('click');
      const emoji = document.getElementById("phone1AvatarEmoji");
      const name = document.getElementById("phone1AvatarName");
      if (gender === "boy") {
        emoji.textContent = "👦";
        name.textContent = "البطل عُمَر";
        showToast("تم اختيار شخصية البطل: عُمَر 👦");
      } else {
        emoji.textContent = "👧";
        name.textContent = "البطلة مَرْيَم";
        showToast("تم اختيار شخصية البطلة: مَرْيَم 👧");
      }
    }

    // ==========================================
    // 6. SCREEN 5 AUDIO PEEK-A-BOO SIMULATOR
    // ==========================================
    let isSheikhTurn = true;
    let currentVerseNumber = 1;

    function simulateParentInvisibleTap() {
      playChime('click');
      isSheikhTurn = !isSheikhTurn;

      const avatar = document.getElementById("simAvatarGraphic");
      const badge = document.getElementById("simAvatarStatusBadge");
      const title = document.getElementById("simWaveTitle");
      const sub = document.getElementById("simWaveSubtext");

      if (!isSheikhTurn) {
        // Child's turn (Sheikh silent)
        avatar.textContent = "😃";
        avatar.style.transform = "scale(1.15)";
        badge.innerHTML = "✨ دورك يا عمر! ردد الآية لبابا وماما في الغرفة";
        badge.style.borderColor = "#f59e0b";
        badge.style.color = "#b45309";
        title.textContent = "وقفة الصمت المحسوبة للترديد (لعبة الصوت الغائب)";
        sub.textContent = "الطفل يقرأ لوالديه في الغرفة بدون مايكروفون";
        showToast("🌟 وقفة الترديد: الطفل يقرأ لوالديه في الغرفة (Zero-Mic)");
      } else {
        // Sheikh recitation state
        avatar.textContent = "👦";
        avatar.style.transform = "scale(1.0)";
        badge.innerHTML = "🎙️ الشيخ المنشاوي يتلو الآية...";
        badge.style.borderColor = "#10b981";
        badge.style.color = "#065f46";
        title.textContent = "بث التلاوة لفضيلة الشيخ المنشاوي المعلم";
        sub.textContent = "👆 اضغط هنا لمحاكاة لمسة الوالد الخفية في أي مكان";
        showToast("🎙️ الشيخ المنشاوي يتلو الآية المرجعية بخشوع");

        // Advance pearls
        currentVerseNumber = (currentVerseNumber % 4) + 1;
        updatePearls(currentVerseNumber);
      }
    }

    function updatePearls(num) {
      for (let i = 1; i <= 4; i++) {
        const p = document.getElementById(`pearl${i}`);
        if (p) {
          p.textContent = i <= num ? "🟢" : "⚪";
        }
      }
    }

    function simulateSurahCompletion() {
      playChime('celebrate');
      showToast("🏆 اكتمال تلاوة سورة الإخلاص! انتقال تلقائي للاحتفال 🎉");
      setTimeout(() => {
        navigateToScreenMock(6, 'اكتمال السورة ➔ الاحتفال', 'btn-s5-auto');
      }, 700);
    }

    function triggerToyPlayAnimation() {
      playChime('start');
      const toy = document.getElementById("unboxedToy");
      if (toy) {
        toy.style.transform = "translateX(-80px) rotate(-15deg) scale(1.3)";
        setTimeout(() => {
          toy.style.transform = "translateX(80px) rotate(15deg) scale(1.3)";
        }, 300);
        setTimeout(() => {
          toy.style.transform = "translateX(0) rotate(0deg) scale(1)";
        }, 700);
      }
      showToast("🏎️ اللعبة تنطلق وتمرح مع الأفاتار في الحديقة القرآنية!");
    }

    // ==========================================
    // 7. GOOGLE STITCH PROMPT STUDIO
    // ==========================================
    function openStitchModal() {
      playChime('click');
      document.getElementById("stitchModal").classList.add("active");
    }

    function closeStitchModal(e) {
      if (!e || e.target === document.getElementById("stitchModal")) {
        document.getElementById("stitchModal").classList.remove("active");
      }
    }

    function switchStitchTab(index, btnElement) {
      playChime('click');
      activeStitchTabIndex = index;
      document.querySelectorAll(".stitch-tab-btn").forEach(b => b.classList.remove("active"));
      if (btnElement) btnElement.classList.add("active");
      updateStitchPromptDisplay();
    }

    function updateStitchPromptDisplay() {
      const display = document.getElementById("stitchPromptText");
      if (display) {
        display.textContent = STITCH_PROMPTS[activeStitchTabIndex];
      }
    }

    function copyCurrentStitchPrompt() {
      playChime('click');
      const text = STITCH_PROMPTS[activeStitchTabIndex];
      navigator.clipboard.writeText(text).then(() => {
        showToast("📋 تم نسخ برومبت الشاشة المحددة لـ Google Stitch!");
      }).catch(() => {
        showToast("تم تحديد النص للنسخ");
      });
    }

    function copyAllStitchPrompts() {
      playChime('start');
      const allText = STITCH_PROMPTS.join("\\n\\n" + "=".repeat(60) + "\\n\\n");
      navigator.clipboard.writeText(allText).then(() => {
        showToast("📑 تم نسخ كامل برومبتات مشروع رِحْلة لـ Google Stitch!");
      }).catch(() => {
        showToast("تم تحديد النص للنسخ");
      });
    }

    // ==========================================
    // 8. THEME & TOAST
    // ==========================================
    function toggleDarkMode() {
      playChime('click');
      document.body.classList.toggle("dark-mode");
      const isDark = document.body.classList.contains("dark-mode");
      document.getElementById("themeIcon").textContent = isDark ? "☀️" : "🌙";
      showToast(isDark ? "تم تفعيل الوضع الليلي 🌙" : "تم تفعيل الوضع النهاري ☀️");
    }

    function showToast(msg) {
      const box = document.getElementById("toastBox");
      if (!box) return;
      const toast = document.createElement("div");
      toast.className = "toast-msg";
      toast.innerHTML = `<span>🌟</span> <span>${msg}</span>`;
      box.appendChild(toast);
      setTimeout(() => {
        toast.style.opacity = "0";
        toast.style.transform = "translateX(100%)";
        toast.style.transition = "all 0.3s";
        setTimeout(() => toast.remove(), 300);
      }, 3500);
    }
  </script>
</body>
</html>
""")
    return "".join(parts)

if __name__ == "__main__":
    target_file = r"d:\quraan project\app_flow_diagram.html"
    print(f"Generating {target_file}...")
    content = get_html_content()
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[SUCCESS] Generated {target_file} (length: {len(content)} chars)")
