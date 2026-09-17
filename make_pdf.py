import os
import subprocess
import sys

html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>وثيقة مشروع نُور - بطل رحلتك القرآنية</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4 portrait;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  body {
    margin: 0;
    padding: 0;
    font-family: 'Cairo', 'Tajawal', sans-serif;
    background-color: #03150f;
    color: #e2e8f0;
    direction: rtl;
    text-align: right;
  }
  
  .page {
    width: 210mm;
    height: 297mm;
    position: relative;
    page-break-after: always;
    page-break-inside: avoid;
    padding: 16mm 18mm;
    background: radial-gradient(circle at 80% 20%, #083827 0%, #041f15 50%, #02110c 100%);
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  /* Page Border Frame */
  .page::before {
    content: "";
    position: absolute;
    top: 8mm;
    bottom: 8mm;
    left: 8mm;
    right: 8mm;
    border: 1.5px solid rgba(245, 158, 11, 0.25);
    border-radius: 12px;
    pointer-events: none;
  }
  .page::after {
    content: "";
    position: absolute;
    top: 10mm;
    bottom: 10mm;
    left: 10mm;
    right: 10mm;
    border: 0.5px dashed rgba(245, 158, 11, 0.15);
    border-radius: 9px;
    pointer-events: none;
  }

  /* Corner Ornaments */
  .corner-ornament {
    position: absolute;
    width: 28px;
    height: 28px;
    border: 2px solid #f59e0b;
    pointer-events: none;
  }
  .co-tl { top: 9mm; left: 9mm; border-right: 0; border-bottom: 0; border-top-left-radius: 6px; }
  .co-tr { top: 9mm; right: 9mm; border-left: 0; border-bottom: 0; border-top-right-radius: 6px; }
  .co-bl { bottom: 9mm; left: 9mm; border-right: 0; border-top: 0; border-bottom-left-radius: 6px; }
  .co-br { bottom: 9mm; right: 9mm; border-left: 0; border-top: 0; border-bottom-right-radius: 6px; }

  /* Headers and Badges */
  .doc-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(245, 158, 11, 0.2);
    padding-bottom: 8px;
    margin-bottom: 14px;
  }
  .doc-header .brand {
    font-size: 15px;
    font-weight: 800;
    color: #fbbf24;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .doc-header .doc-id {
    font-size: 10px;
    background: rgba(245, 158, 11, 0.1);
    color: #fcd34d;
    padding: 3px 10px;
    border-radius: 20px;
    border: 1px solid rgba(245, 158, 11, 0.3);
    letter-spacing: 0.5px;
  }

  .page-footer {
    margin-top: auto;
    border-top: 1px solid rgba(245, 158, 11, 0.2);
    padding-top: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10px;
    color: #94a3b8;
  }

  /* Typography */
  h1, h2, h3, h4 {
    margin: 0;
    color: #ffffff;
  }
  .page-title {
    font-size: 20px;
    font-weight: 800;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
  }
  .page-title span.badge {
    font-size: 11px;
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #041b14;
    font-weight: 800;
    padding: 3px 10px;
    border-radius: 12px;
  }

  /* Cards & Grid */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
  }
  .grid-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
  }

  .card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 12px 14px;
    position: relative;
  }
  .card.gold-border {
    border-color: rgba(245, 158, 11, 0.35);
    background: rgba(245, 158, 11, 0.03);
  }
  .card.emerald-border {
    border-color: rgba(16, 185, 129, 0.35);
    background: rgba(16, 185, 129, 0.03);
  }
  .card.danger-border {
    border-color: rgba(239, 68, 68, 0.35);
    background: rgba(239, 68, 68, 0.03);
  }

  .card-title {
    font-size: 13px;
    font-weight: 800;
    color: #fbbf24;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .card p {
    font-size: 11px;
    line-height: 1.65;
    color: #cbd5e1;
    margin: 0;
  }

  /* Table styling */
  table.matrix-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 10px;
    margin-top: 6px;
  }
  table.matrix-table th {
    background: rgba(245, 158, 11, 0.15);
    color: #fcd34d;
    padding: 6px 8px;
    text-align: right;
    border-bottom: 1.5px solid rgba(245, 158, 11, 0.3);
    font-weight: 700;
  }
  table.matrix-table td {
    padding: 6px 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    color: #e2e8f0;
    vertical-align: middle;
  }
  table.matrix-table tr:nth-child(even) td {
    background: rgba(255, 255, 255, 0.02);
  }
  .code-tag {
    font-family: monospace;
    font-size: 9.5px;
    background: rgba(16, 185, 129, 0.15);
    color: #34d399;
    padding: 2px 6px;
    border-radius: 4px;
    border: 0.5px solid rgba(16, 185, 129, 0.3);
  }
  .dest-tag {
    background: rgba(245, 158, 11, 0.15);
    color: #fbbf24;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
  }

  /* Timeline / Stages */
  .timeline-container {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin: 10px 0;
  }
  .timeline-step {
    display: flex;
    gap: 12px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 10px 12px;
    align-items: center;
  }
  .timeline-step .num {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #041b14;
    font-weight: 900;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    flex-shrink: 0;
  }
  .timeline-step .content h4 {
    font-size: 12px;
    color: #fbbf24;
    margin-bottom: 2px;
  }
  .timeline-step .content p {
    font-size: 10.5px;
    color: #cbd5e1;
    margin: 0;
    line-height: 1.45;
  }

  /* COVER PAGE STYLES */
  .cover-page {
    justify-content: center;
    align-items: center;
    text-align: center;
    background: radial-gradient(circle at 50% 30%, #0d4a34 0%, #04241a 45%, #01110b 90%);
  }
  .cover-emblem {
    width: 110px;
    height: 110px;
    margin-bottom: 20px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .crescent-svg {
    width: 100px;
    height: 100px;
    filter: drop-shadow(0 0 25px rgba(245, 158, 11, 0.6));
  }
  .cover-title {
    font-size: 44px;
    font-weight: 900;
    color: #ffffff;
    letter-spacing: -0.5px;
    margin-bottom: 8px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.6);
  }
  .cover-title span {
    color: #fbbf24;
    background: linear-gradient(to right, #fcd34d, #f59e0b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .cover-subtitle {
    font-size: 18px;
    font-weight: 700;
    color: #34d399;
    margin-bottom: 16px;
  }
  .cover-desc {
    font-size: 12.5px;
    color: #94a3b8;
    max-width: 520px;
    line-height: 1.8;
    margin-bottom: 30px;
  }
  .cover-badges {
    display: flex;
    gap: 10px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 35px;
  }
  .c-badge {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(245, 158, 11, 0.3);
    padding: 6px 14px;
    border-radius: 30px;
    font-size: 11px;
    color: #fcd34d;
    font-weight: 700;
  }
  .c-badge.special {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(16, 185, 129, 0.2));
    border-color: #10b981;
    color: #6ee7b7;
  }
  .cover-meta-box {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 14px 24px;
    display: flex;
    gap: 30px;
    font-size: 11px;
    color: #cbd5e1;
  }
  .meta-item {
    display: flex;
    flex-direction: column;
    gap: 3px;
  }
  .meta-item strong {
    color: #fbbf24;
    font-size: 10px;
    text-transform: uppercase;
  }
</style>
</head>
<body>

<!-- ========================================================================= -->
<!-- PAGE 1: COVER PAGE                                                        -->
<!-- ========================================================================= -->
<div class="page cover-page">
  <div class="corner-ornament co-tl"></div>
  <div class="corner-ornament co-tr"></div>
  <div class="corner-ornament co-bl"></div>
  <div class="corner-ornament co-br"></div>

  <div class="cover-emblem">
    <svg class="crescent-svg" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="45" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.4"/>
      <path d="M50 15C30.67 15 15 30.67 15 50C15 69.33 30.67 85 50 85C42 77 37 64.5 37 50C37 35.5 42 23 50 15Z" fill="url(#goldGrad)"/>
      <polygon points="62,28 65,37 74,37 67,43 70,52 62,46 54,52 57,43 50,37 59,37" fill="#fef3c7"/>
      <defs>
        <linearGradient id="goldGrad" x1="15" y1="15" x2="60" y2="85" gradientUnits="userSpaceOnUse">
          <stop stop-color="#fbbf24"/>
          <stop offset="1" stop-color="#d97706"/>
        </linearGradient>
      </defs>
    </svg>
  </div>

  <div class="cover-title">مشروع <span>«نُـور»</span></div>
  <div class="cover-subtitle">بطل رحلتك القرآنية — الوثيقة المعمارية والفكرية الشاملة</div>
  
  <p class="cover-desc">
    دليل التصميم المعتمد لتطبيق تحفيظ جزء عم للأطفال (3-5 سنوات)، القائم على ميكانيكية 
    <strong>"لعبة الصوت الغائب"</strong> وميثاق <strong>"صفر مايكروفون"</strong>، في طقس عائلي دافئ 
    يتحول فيه الطفل إلى بطل مغامرته القرآنية مع فضيلة الشيخ المنشاوي المعلم.
  </p>

  <div class="cover-badges">
    <div class="c-badge">الفئة المستهدفة: 3 إلى 5 سنوات</div>
    <div class="c-badge">جزء عمّ كاملاً (37 سورة)</div>
    <div class="c-badge special">ميثاق: صفر مايكروفون (100% خصوصية)</div>
    <div class="c-badge">المصحف المعلم (المنشاوي)</div>
    <div class="c-badge">معتمد طبقاً لـ ECC 2.2.0</div>
  </div>

  <div class="cover-meta-box">
    <div class="meta-item">
      <strong>حالة الوثيقة</strong>
      <span>الإصدار 3.0 النهائي المعتمد</span>
    </div>
    <div class="meta-item">
      <strong>البطل المُلهم</strong>
      <span>البطل الصغير "عُمَر" (3 سنوات)</span>
    </div>
    <div class="meta-item">
      <strong>جاهزية التنفيذ</strong>
      <span>مُهيأ لمنصة Google Stitch</span>
    </div>
    <div class="meta-item">
      <strong>فريق التطوير</strong>
      <span>شراكة ستوديو الأنيميشن</span>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- PAGE 2: CORE PHILOSOPHY & ZERO-MIC COVENANT                               -->
<!-- ========================================================================= -->
<div class="page">
  <div class="corner-ornament co-tl"></div>
  <div class="corner-ornament co-tr"></div>
  <div class="corner-ornament co-bl"></div>
  <div class="corner-ornament co-br"></div>

  <div class="doc-header">
    <div class="brand">مشروع نُور <span>✦</span> الفلسفة والميثاق التربوي</div>
    <div class="doc-id">SECTION 01 / 04</div>
  </div>

  <div class="page-title">
    الفلسفة الجوهرية وميثاق «صفر مايكروفون»
    <span class="badge">سيكولوجية سن 3-5 سنوات</span>
  </div>

  <!-- Comparison Cards -->
  <div class="grid-2" style="margin-bottom: 12px;">
    <div class="card danger-border">
      <div class="card-title" style="color: #f87171;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>
        التطبيقات التقليدية (ما استبعدناه تماماً)
      </div>
      <p>
        • <strong>التشتيت بالألعاب الجانبية:</strong> ألعاب فراشات وقطارات وجسور تصرف الطفل عن روح القرآن.<br>
        • <strong>إحباط التعرف الصوتي (STT):</strong> تخطئة الطفل لعدم اكتمال مخارج حروفه الطفولية.<br>
        • <strong>العزلة الرقمية:</strong> ترك الطفل بمفرده أمام الشاشة كأداة تسلية رخيصة.<br>
        • <strong>انتهاك الخصوصية:</strong> تسجيل أصوات الأطفال ورفعها على قواعد بيانات خارجية.
      </p>
    </div>

    <div class="card emerald-border">
      <div class="card-title" style="color: #34d399;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        فلسفة مشروع «نُور» (النموذج الفريد)
      </div>
      <p>
        • <strong>القرآن هو الجائزة والنور:</strong> لا ألعاب مصطنعة، التلاوة ذاتها هي مصدر البهجة والضياء.<br>
        • <strong>الطقس العائلي التشاركي:</strong> الأب أو الأم يجلسان مع الطفل ويحتضنانه ويشجعانه.<br>
        • <strong>الترديد الواقعي الحر:</strong> الطفل يقرأ لوالديه في الغرفة دون أي رقابة برمجية.<br>
        • <strong>بطل الرواية:</strong> شخصية كرتونية باستايل ستوديو احترافي تجعل الطفل بطل رحلته.
      </p>
    </div>
  </div>

  <!-- 3 Pillar Cards -->
  <div class="grid-3" style="margin-bottom: 12px;">
    <div class="card gold-border">
      <div class="card-title">
        <span>🛡️</span> ميثاق صفر مايكروفون
      </div>
      <p>
        التطبيق <strong>إخراج فقط (Output-Only)</strong>. لا يطلب إذن الميكروفون نهائياً، ولا يسجل أي صوت. الطفل يقرأ لأبيه وأمه في العالم الحقيقي، مما يحميه من أي إحباط تقني ويضمن خصوصية عائلية مطلقة 100%.
      </p>
    </div>

    <div class="card gold-border">
      <div class="card-title">
        <span>🎁</span> الخطاف الذهبي (الهدية)
      </div>
      <p>
        قبل بدء السورة، يختار الطفل لعبته المحبوبة (سيارات، طائرات، ديناصورات للأولاد، وألعاب مبهجة للبنات). توضع في <strong>صندوق كنز مغلق</strong> أمام الأفاتار، ليظل متحمساً لإنهاء السورة لرؤية الصندوق ينفتح!
      </p>
    </div>

    <div class="card gold-border">
      <div class="card-title">
        <span>🔒</span> بوابة الأمان الحسابية
      </div>
      <p>
        شاشة الطفل خالية 100% من أي أزرار أو خروج عرضي. إعدادات التكرار واختيار السور محمية بمسألة حسابية مخصصة للوالد (مثلاً: 7 + 8 = ؟) لمنع عبث الطفل بالخيارات أثناء الجلسة.
      </p>
    </div>
  </div>

  <!-- Bottom Visual Callout -->
  <div class="card" style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.08), rgba(245, 158, 11, 0.08)); border: 1px solid rgba(245, 158, 11, 0.3);">
    <div style="font-size: 12px; font-weight: 800; color: #fbbf24; margin-bottom: 4px;">
      💡 سر النجاح مع سن 3 سنوات: "التشويق المسبق ولغة الجسد"
    </div>
    <p style="font-size: 10.5px; line-height: 1.6;">
      طفل الـ 3 سنوات قادر على الاستماع لقصة لمدة 3 ساعات، ولكنه قد يمل من القرآن في دقيقة واحدة إذا فُرض عليه بأسلوب جاف. تحويل السورة إلى مهمة استكشافية يكون فيها الطفل هو البطل ومعه صندوق الهدية المغلق، يجعله يأتي بنفسه لوالديه قائلاً: <em>"يلا يا بابا نحفظ شوية؟!"</em>.
    </p>
  </div>

  <div class="page-footer">
    <span>مشروع نُور — بطل رحلتك القرآنية</span>
    <span>وثيقة التصميم المعماري الشامل</span>
    <span>صفحة 2 من 5</span>
  </div>
</div>

<!-- ========================================================================= -->
<!-- PAGE 3: AUDIO PEEK-A-BOO & QURANIC PEDAGOGY                               -->
<!-- ========================================================================= -->
<div class="page">
  <div class="corner-ornament co-tl"></div>
  <div class="corner-ornament co-tr"></div>
  <div class="corner-ornament co-bl"></div>
  <div class="corner-ornament co-br"></div>

  <div class="doc-header">
    <div class="brand">مشروع نُور <span>✦</span> المنهجية القرآنية</div>
    <div class="doc-id">SECTION 02 / 04</div>
  </div>

  <div class="page-title">
    ميكانيكا «لعبة الصوت الغائب» والترديد
    <span class="badge">المصحف المعلم — المنشاوي</span>
  </div>

  <div class="timeline-container">
    <div class="timeline-step">
      <div class="num">1</div>
      <div class="content">
        <h4>المرحلة الأولى: الاستماع الكامل وتلقي النغمة (Full Recitation)</h4>
        <p>الشيخ المنشاوي يتلو الآية كاملة وتردد خلفه أصوات الأطفال في التسجيل. الأفاتار في حالة <strong>"الاستماع الخاشع"</strong> (مغمض العينين ومبتسم بهدوء)، ليتشرب الطفل النغمة السماوية في أذنه دون أي ضغط.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="num">2</div>
      <div class="content">
        <h4>المرحلة الثانية: الصوت الغائب — الكلمة الأخيرة (Missing Last Word)</h4>
        <p>الشيخ يقرأ: <em>"قل أعوذ برب..."</em> ثم يسكت الصوت لفترة زمنية مدروسة. الأفاتار يلتفت للطفل مبتسماً ويشير بيده: <em>"دورك يا بطل!"</em>، والطفل يكمل في الغرفة: <strong>"الفلق"</strong> لوالده بحماس.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="num">3</div>
      <div class="content">
        <h4>المرحلة الثالثة: الصوت الغائب — نصف الآية (Missing Half Verse)</h4>
        <p>الشيخ يقرأ أول كلمتين فقط ويسكت الصوت تلقائياً. الطفل يكمل نصف الآية الثاني بصوته. صندوق الكنز يهتز بخفة وتنطلق منه ومضات بريق ذهبية تشجيعاً لاقتراب الفتح.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="num">4</div>
      <div class="content">
        <h4>المرحلة الرابعة: البطل الصغير المستقل (Little Hero Full Verse)</h4>
        <p>الشيخ يسكت تماماً، الأفاتار يشجع الطفل بكلتا يديه، والطفل يقرأ الآية كاملة لوالديه. عند انتهاء الآية يضيء مؤشر التقدم بنجمة ذهبية، وتنتقل الجلسة بسلاسة وتلقائية للآية التالية.</p>
      </div>
    </div>
  </div>

  <!-- Linking Mechanic & Parent Gestures -->
  <div class="grid-2" style="margin-top: 6px;">
    <div class="card emerald-border">
      <div class="card-title">
        <span>🔗</span> ميكانيكية الربط التراكمي (Verse Linking)
      </div>
      <p>
        أكبر مشكلة تواجه الطفل هي التوقف بين الآيات. يتيح التطبيق للأهل تحديد <strong>"عدد آيات الربط"</strong>؛ فعند الوصول للآية 3 مثلاً، يقرأ الشيخ الآيتين 2 و 3 معاً لترسيخ الروابط التلقائية في ذاكرة الطفل.
      </p>
    </div>

    <div class="card gold-border">
      <div class="card-title">
        <span>👆</span> التحكم السري الخفي للوالدين
      </div>
      <p>
        شاشة الطفل خالية تماماً من الأزرار؛ لكن يمكن للوالد الجالس بجواره <strong>لمس أي مكان فارغ بالشاشة</strong> لإيقاف التلاوة مؤقتاً لتقبيل الطفل، أو النقر المزدوج في الزاوية العلوية للخروج الآمن لقائمة السور.
      </p>
    </div>
  </div>

  <div class="page-footer">
    <span>مشروع نُور — بطل رحلتك القرآنية</span>
    <span>وثيقة التصميم المعماري الشامل</span>
    <span>صفحة 3 من 5</span>
  </div>
</div>

<!-- ========================================================================= -->
<!-- PAGE 4: SCREENS & INTERACTIVE BUTTONS MATRIX                              -->
<!-- ========================================================================= -->
<div class="page">
  <div class="corner-ornament co-tl"></div>
  <div class="corner-ornament co-tr"></div>
  <div class="corner-ornament co-bl"></div>
  <div class="corner-ornament co-br"></div>

  <div class="doc-header">
    <div class="brand">مشروع نُور <span>✦</span> خريطة الشاشات والتدفق</div>
    <div class="doc-id">SECTION 03 / 04</div>
  </div>

  <div class="page-title">
    خريطة الشاشات الست والأزرار التفاعلية
    <span class="badge">State Machine & Routing Matrix</span>
  </div>

  <table class="matrix-table">
    <thead>
      <tr>
        <th style="width: 18%;">الشاشة</th>
        <th style="width: 25%;">الزر / العنصر التفاعلي</th>
        <th style="width: 20%;">نوع الحدث</th>
        <th style="width: 37%;">الوجهة والأثر المعماري</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3"><strong>1. الشاشة الرئيسية</strong><br><span style="font-size:8.5px; color:#94a3b8;">اختيار البطل والاسم</span></td>
        <td><span class="code-tag">BTN_HERO_SELECT</span> اختيار ولد / بنت</td>
        <td>Click</td>
        <td>تبديل مظهر الأفاتار الكرتوني المختار</td>
      </tr>
      <tr>
        <td><span class="code-tag">BTN_START_JOURNEY</span> "ابدأ رحلتك"</td>
        <td>Click (CTA)</td>
        <td><span class="dest-tag">انتقال للشاشة 2: اختيار السورة</span></td>
      </tr>
      <tr>
        <td><span class="code-tag">BTN_PARENT_GATE</span> قفل الأهل 🔒</td>
        <td>Click</td>
        <td><span class="dest-tag">فتح الشاشة 4: بوابة الأمان الحسابية</span></td>
      </tr>

      <tr>
        <td rowspan="3"><strong>2. اختيار السورة</strong><br><span style="font-size:8.5px; color:#94a3b8;">جزء عمّ (37 سورة)</span></td>
        <td><span class="code-tag">CARD_SURAH[1..37]</span> بطاقة السورة</td>
        <td>Click</td>
        <td>تحديد السورة و<span class="dest-tag">انتقال للشاشة 3: اختيار الهدية</span></td>
      </tr>
      <tr>
        <td><span class="code-tag">BTN_BACK_HOME</span> زر العودة 🔙</td>
        <td>Click</td>
        <td><span class="dest-tag">رجوع للشاشة 1: الرئيسية</span></td>
      </tr>
      <tr>
        <td><span class="code-tag">BTN_PARENT_SETTINGS</span> ترس الضبط ⚙️</td>
        <td>Click</td>
        <td><span class="dest-tag">فتح الشاشة 4: بوابة الأمان الحسابية</span></td>
      </tr>

      <tr>
        <td rowspan="2"><strong>3. اختيار الهدية</strong><br><span style="font-size:8.5px; color:#94a3b8;">الخطاف الذهبي</span></td>
        <td><span class="code-tag">CARD_TOY[id]</span> سيارة، طيارة، ديناصور</td>
        <td>Click</td>
        <td>دوران اللعبة وتشغيل نغمة ترقب لطيفة</td>
      </tr>
      <tr>
        <td><span class="code-tag">BTN_LOCK_GIFT</span> "اقفل الصندوق وابدأ"</td>
        <td>Click (CTA)</td>
        <td>إغلاق الصندوق و<span class="dest-tag">انتقال للشاشة 5: الترديد النشط</span></td>
      </tr>

      <tr>
        <td rowspan="3"><strong>4. بوابة الأهل</strong><br><span style="font-size:8.5px; color:#94a3b8;">نافذة محمية بحساب</span></td>
        <td><span class="code-tag">MATH_INPUT</span> حل مسألة 8 + 6 = ؟</td>
        <td>Numeric Input</td>
        <td>التحقق من هوية الوالد لفتح الخيارات</td>
      </tr>
      <tr>
        <td><span class="code-tag">REPETITION_SELECT</span> 1x, 2x, 3x, 5x</td>
        <td>Selector</td>
        <td>ضبط عدد تكرارات الآية بصوت الشيخ</td>
      </tr>
      <tr>
        <td><span class="code-tag">BTN_SAVE_CLOSE</span> حفظ وإغلاق ✕</td>
        <td>Click</td>
        <td>حفظ الإعدادات و<span class="dest-tag">العودة للشاشة السابقة</span></td>
      </tr>

      <tr>
        <td rowspan="2"><strong>5. الترديد النشط</strong><br><span style="font-size:8.5px; color:#94a3b8;">شاشة هادئة مع المنشاوي</span></td>
        <td><span class="code-tag">GESTURE_TAP_SCREEN</span> لمس أي مكان</td>
        <td>Secret Parent Tap</td>
        <td>إيقاف مؤقت أو إعادة الآية الحالية دون إرباك</td>
      </tr>
      <tr>
        <td><span class="code-tag">AUTO_SURAH_DONE</span> ختام آخر آية</td>
        <td>Auto System Event</td>
        <td>تكبير احتفالي و<span class="dest-tag">انتقال تلقائي للشاشة 6: الاحتفال</span></td>
      </tr>

      <tr>
        <td rowspan="2"><strong>6. شاشة الاحتفال</strong><br><span style="font-size:8.5px; color:#94a3b8;">فتح صندوق الكنز</span></td>
        <td><span class="code-tag">BTN_NEXT_SURAH</span> "سورة وهدية جديدة"</td>
        <td>Click (CTA)</td>
        <td>تثبيت النجمة و<span class="dest-tag">انتقال للشاشة 2: اختيار السورة</span></td>
      </tr>
      <tr>
        <td><span class="code-tag">BTN_REPEAT_SURAH</span> "إعادة السورة" 🔁</td>
        <td>Click</td>
        <td><span class="dest-tag">انتقال للشاشة 5 لنفس السورة</span> لتثبيت الحفظ</td>
      </tr>
    </tbody>
  </table>

  <div class="page-footer">
    <span>مشروع نُور — بطل رحلتك القرآنية</span>
    <span>وثيقة التصميم المعماري الشامل</span>
    <span>صفحة 4 من 5</span>
  </div>
</div>

<!-- ========================================================================= -->
<!-- PAGE 5: DESIGN SYSTEM & GOOGLE STITCH READINESS                           -->
<!-- ========================================================================= -->
<div class="page">
  <div class="corner-ornament co-tl"></div>
  <div class="corner-ornament co-tr"></div>
  <div class="corner-ornament co-bl"></div>
  <div class="corner-ornament co-br"></div>

  <div class="doc-header">
    <div class="brand">مشروع نُور <span>✦</span> الهوية والتنفيذ الفني</div>
    <div class="doc-id">SECTION 04 / 04</div>
  </div>

  <div class="page-title">
    الهوية البصرية وتجهيز منصة Google Stitch
    <span class="badge">Design Tokens & Implementation</span>
  </div>

  <!-- Color Palette Swatches -->
  <div style="margin-bottom: 12px;">
    <div style="font-size: 11px; font-weight: 800; color: #fbbf24; margin-bottom: 6px;">مصفوفة الرموز اللونية (Color Tokens Palette):</div>
    <div class="grid-4">
      <div class="card" style="background: #064e3b; border-color: #10b981; text-align: center; padding: 8px;">
        <div style="font-weight: 800; font-size: 11px; color: #6ee7b7;">الزمردي القرآني</div>
        <div style="font-size: 9.5px; color: #a7f3d0; font-family: monospace;">#064e3b</div>
        <div style="font-size: 8.5px; color: #cbd5e1; margin-top: 3px;">الحدائق والصفاء</div>
      </div>
      <div class="card" style="background: #78350f; border-color: #f59e0b; text-align: center; padding: 8px;">
        <div style="font-weight: 800; font-size: 11px; color: #fcd34d;">الذهب الملكي</div>
        <div style="font-size: 9.5px; color: #fef3c7; font-family: monospace;">#f59e0b</div>
        <div style="font-size: 8.5px; color: #cbd5e1; margin-top: 3px;">صندوق الكنز والنجوم</div>
      </div>
      <div class="card" style="background: #065f46; border-color: #34d399; text-align: center; padding: 8px;">
        <div style="font-weight: 800; font-size: 11px; color: #a7f3d0;">الأخضر النعناعي</div>
        <div style="font-size: 9.5px; color: #d1fae5; font-family: monospace;">#10b981</div>
        <div style="font-size: 8.5px; color: #cbd5e1; margin-top: 3px;">أزرار الإجراء (CTA)</div>
      </div>
      <div class="card" style="background: #0f172a; border-color: #475569; text-align: center; padding: 8px;">
        <div style="font-weight: 800; font-size: 11px; color: #cbd5e1;">الليل السكيني</div>
        <div style="font-size: 9.5px; color: #94a3b8; font-family: monospace;">#03150f</div>
        <div style="font-size: 8.5px; color: #cbd5e1; margin-top: 3px;">الخلفيات الحاضنة</div>
      </div>
    </div>
  </div>

  <!-- Typography & Assets -->
  <div class="grid-2" style="margin-bottom: 12px;">
    <div class="card gold-border">
      <div class="card-title">
        <span>🖋️</span> الخطوط والتايبوغرافي
      </div>
      <p>
        • <strong>عناوين السور والآيات:</strong> خط النسخ القرآني (Amiri / Naskh) لضمان وقار النص الشريف.<br>
        • <strong>واجهات الأزرار والتفاعل:</strong> خط (Cairo / Tajawal) بأوزان 700 و 800 عريضة تناسب يد الطفل وعين الوالدين، مع مراعاة التباعد الحركي الكبير لسهولة اللمس.
      </p>
    </div>

    <div class="card emerald-border">
      <div class="card-title">
        <span>🎬</span> أسلوب الأنيميشن (Animation Style)
      </div>
      <p>
        • <strong>المستوى البصري:</strong> رسوم ستوديو أنيميشن دافئة تشبه أفلام الرسوم المتحركة العالمية.<br>
        • <strong>لغة الجسد التعبيرية:</strong> الأفاتار يتنفس بهدوء، يحرك رأسه مع نغمة الشيخ، ويصفق بفرح حقيقي عند انتهاء السورة دون حركات سريعة مزعجة.
      </p>
    </div>
  </div>

  <!-- Google Stitch Integration Ready -->
  <div class="card" style="background: rgba(245, 158, 11, 0.04); border: 1.5px dashed rgba(245, 158, 11, 0.4); padding: 14px;">
    <div style="font-size: 12.5px; font-weight: 800; color: #fbbf24; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
      <span>🚀</span> جاهزية التوليد الفوري عبر Google Stitch MCP
    </div>
    <p style="font-size: 11px; line-height: 1.7; color: #e2e8f0;">
      تم تحويل كافة شاشات التطبيق الست وأزرارها إلى برومبتات هيكلية متقدمة مهيأة للحقن المباشر في أداة <strong>Google Stitch</strong>. يمكنك الآن استدعاء أداة Stitch MCP لتوليد الشاشات التفاعلية بنقرة واحدة، مستندين إلى هذا الدليل وميثاق التصميم <code>DESIGN.md</code> المعتمد في المشروع.
    </p>
  </div>

  <!-- Dedication Box -->
  <div style="margin-top: 10px; text-align: center; font-size: 11px; color: #94a3b8; font-style: italic;">
    "نسأل الله تعالى أن يجعل هذا العمل نوراً يملأ قلوب أطفالنا بحب القرآن الكريم وحلاوة حفظه، وأن يبارك في البطل الصغير عمر ووالديه."
  </div>

  <div class="page-footer">
    <span>مشروع نُور — بطل رحلتك القرآنية</span>
    <span>وثيقة التصميم المعماري الشامل</span>
    <span>صفحة 5 من 5</span>
  </div>
</div>

</body>
</html>
"""

html_path = "d:/quraan project/noor_master_concept.html"
pdf_path = "d:/quraan project/noor_master_concept.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[OK] HTML written to: {html_path}")

# Check browser
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

browser_path = chrome_path if os.path.exists(chrome_path) else edge_path

cmd = [
    browser_path,
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={os.path.abspath(pdf_path)}",
    "--no-pdf-header-footer",
    os.path.abspath(html_path)
]

result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode == 0 and os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"[SUCCESS] PDF generated successfully: {pdf_path} ({size_kb:.1f} KB)")
else:
    print(f"[ERROR] PDF generation failed: {result.stderr}")
