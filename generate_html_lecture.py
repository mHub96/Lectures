import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

from deck1_data import DECK1_SLIDES
from deck2_data import DECK2_SLIDES

# Combine all slides into a unified list of 66 slides
ALL_SLIDES = []
for idx, s in enumerate(DECK1_SLIDES):
    slide_copy = dict(s)
    slide_copy['global_id'] = idx + 1
    slide_copy['part'] = 1
    slide_copy['slide_in_part'] = idx + 1
    slide_copy['part_title'] = "Part 1: Lateral Ventricles & Approaches"
    ALL_SLIDES.append(slide_copy)

for idx, s in enumerate(DECK2_SLIDES):
    slide_copy = dict(s)
    slide_copy['global_id'] = len(DECK1_SLIDES) + idx + 1
    slide_copy['part'] = 2
    slide_copy['slide_in_part'] = idx + 1
    slide_copy['part_title'] = "Part 2: Tumors of the Brain Ventricles"
    ALL_SLIDES.append(slide_copy)

slides_json = json.dumps(ALL_SLIDES, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ventricular Tumors Masterclass • Lecture Hall Presentation & Interactive Curriculum</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Standalone QR Code & MQTT Libraries (Self-Contained Offline + Online) -->
  <script src="qrcode.min.js"></script>
  <script src="mqtt.min.js"></script>

  <style>
    :root {{
      --bg-base: #0b1120;
      --bg-surface: #131d31;
      --bg-card: #1c2a45;
      --bg-card-hover: #233557;
      --border-subtle: #243552;
      --border-focus: #38bdf8;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent-primary: #38bdf8;
      --accent-primary-hover: #7dd3fc;
      --accent-glow: rgba(56, 189, 248, 0.25);
      --navy-deep: #030712;
      --emerald: #10b981;
      --amber: #f59e0b;
      --rose: #ef4444;
      --purple: #a855f7;
      --gold: #fbbf24;
      --silver: #cbd5e1;
      --bronze: #d97706;
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.4);
      --shadow-md: 0 4px 10px rgba(0, 0, 0, 0.5);
      --shadow-xl: 0 20px 30px rgba(0, 0, 0, 0.7);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-xl: 22px;
      --transition-fast: 0.16s ease;
      --transition-normal: 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    [data-theme="light"] {{
      --bg-base: #f1f5f9;
      --bg-surface: #ffffff;
      --bg-card: #f8fafc;
      --bg-card-hover: #f1f5f9;
      --border-subtle: #cbd5e1;
      --border-focus: #0284c7;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #64748b;
      --accent-primary: #0284c7;
      --accent-primary-hover: #0369a1;
      --accent-glow: rgba(2, 132, 199, 0.18);
      --navy-deep: #0f1e36;
      --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.08);
      --shadow-md: 0 4px 6px -1px rgba(15, 23, 42, 0.1);
      --shadow-xl: 0 20px 25px -5px rgba(15, 23, 42, 0.12);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-base);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      transition: background-color var(--transition-normal), color var(--transition-normal);
      user-select: none;
    }}

    /* Top Navigation Header */
    header.lecture-header {{
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      height: 60px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: var(--shadow-sm);
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #ffffff;
      font-weight: 800;
      font-size: 0.8rem;
      padding: 5px 12px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.06em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.35);
    }}

    .lecture-title-text {{
      display: flex;
      flex-direction: column;
    }}

    .lecture-title-text span:first-child {{
      font-weight: 700;
      font-size: 0.95rem;
      letter-spacing: -0.01em;
      color: var(--text-main);
    }}

    .lecture-subtitle-text {{
      font-size: 0.72rem;
      color: var(--text-muted);
      font-weight: 500;
    }}

    .header-center {{
      display: flex;
      align-items: center;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      padding: 4px;
      border-radius: 999px;
    }}

    .part-pill {{
      border: none;
      background: transparent;
      color: var(--text-muted);
      padding: 5px 14px;
      font-size: 0.82rem;
      font-weight: 600;
      border-radius: 999px;
      cursor: pointer;
      transition: all var(--transition-fast);
    }}

    .part-pill:hover {{
      color: var(--text-main);
    }}

    .part-pill.active {{
      background: var(--accent-primary);
      color: #030712;
      box-shadow: 0 2px 8px rgba(56, 189, 248, 0.4);
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .btn-icon {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      width: 36px;
      height: 36px;
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all var(--transition-fast);
      position: relative;
    }}

    .btn-icon:hover {{
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    .btn-icon.active-mode {{
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    .btn-icon.btn-quiz-highlight {{
      background: linear-gradient(135deg, rgba(2, 132, 199, 0.25), rgba(16, 185, 129, 0.25));
      border-color: var(--accent-primary);
      color: #38bdf8;
    }}

    /* Progress strip */
    .progress-strip {{
      height: 4px;
      background: var(--bg-card);
      width: 100%;
      position: relative;
    }}

    .progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, #0284c7, #38bdf8, #10b981);
      width: 0%;
      transition: width 0.3s ease;
    }}

    /* Main Presentation Canvas */
    main.presentation-stage {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.25rem 2rem;
      position: relative;
    }}

    .slide-aspect-box {{
      width: 100%;
      max-width: 1550px;
      aspect-ratio: 16 / 9;
      max-height: calc(100vh - 145px);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-xl);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all var(--transition-normal);
    }}

    .slide-content-container {{
      width: 100%;
      height: 100%;
      padding: 2.25rem 2.75rem;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
    }}

    /* Animations for slides */
    .slide-forward {{
      animation: slideInForward 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    .slide-backward {{
      animation: slideInBackward 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    @keyframes slideInForward {{
      from {{ opacity: 0; transform: translateX(35px) scale(0.98); }}
      to {{ opacity: 1; transform: translateX(0) scale(1); }}
    }}

    @keyframes slideInBackward {{
      from {{ opacity: 0; transform: translateX(-35px) scale(0.98); }}
      to {{ opacity: 1; transform: translateX(0) scale(1); }}
    }}

    /* Step-by-step element reveal */
    .step-hidden {{
      opacity: 0 !important;
      transform: translateY(16px) !important;
      pointer-events: none !important;
      visibility: hidden !important;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .step-active {{
      opacity: 1 !important;
      transform: translateY(0) !important;
      pointer-events: auto !important;
      visibility: visible !important;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* ---- VARIED SLIDE ANIMATION STYLES ---- */
    @keyframes slideInFadeScale {{
      from {{ opacity: 0; transform: scale(0.96); }}
      to   {{ opacity: 1; transform: scale(1); }}
    }}
    @keyframes slideInBottom {{
      from {{ opacity: 0; transform: translateY(30px); }}
      to   {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes slideInTop {{
      from {{ opacity: 0; transform: translateY(-30px); }}
      to   {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes slideInLeft {{
      from {{ opacity: 0; transform: translateX(-35px); }}
      to   {{ opacity: 1; transform: translateX(0); }}
    }}
    @keyframes slideInRight {{
      from {{ opacity: 0; transform: translateX(35px); }}
      to   {{ opacity: 1; transform: translateX(0); }}
    }}
    @keyframes slideFlip {{
      from {{ opacity: 0; transform: rotateY(12deg) scale(0.97); }}
      to   {{ opacity: 1; transform: rotateY(0deg) scale(1); }}
    }}
    .anim-fade-scale  {{ animation: slideInFadeScale 0.38s cubic-bezier(0.16,1,0.3,1) forwards; }}
    .anim-from-bottom {{ animation: slideInBottom    0.38s cubic-bezier(0.16,1,0.3,1) forwards; }}
    .anim-from-top    {{ animation: slideInTop       0.38s cubic-bezier(0.16,1,0.3,1) forwards; }}
    .anim-from-left   {{ animation: slideInLeft      0.38s cubic-bezier(0.16,1,0.3,1) forwards; }}
    .anim-from-right  {{ animation: slideInRight     0.38s cubic-bezier(0.16,1,0.3,1) forwards; }}
    .anim-flip        {{ animation: slideFlip        0.42s cubic-bezier(0.16,1,0.3,1) forwards; }}

    /* ---- EDIT MODE STYLES ---- */
    .btn-edit-mode.edit-active {{
      background: rgba(245, 158, 11, 0.22) !important;
      border-color: var(--amber) !important;
      color: var(--amber) !important;
    }}

    body.edit-mode-active .slide-aspect-box {{
      outline: 3px dashed var(--amber) !important;
      outline-offset: 3px;
    }}
    body.edit-mode-active [contenteditable] {{
      outline: 1px dashed rgba(245,158,11,0.5) !important;
      border-radius: 4px;
      cursor: text !important;
    }}
    body.edit-mode-active [contenteditable]:focus {{
      outline: 2px solid var(--amber) !important;
      background: rgba(245,158,11,0.07) !important;
    }}

    /* Edit toolbar that appears on image hover in edit mode */
    body.edit-mode-active .image-edit-overlay {{
      display: flex !important;
    }}
    .image-edit-overlay {{
      display: none;
      position: absolute;
      top: 8px;
      right: 8px;
      gap: 5px;
      z-index: 10;
      flex-wrap: wrap;
    }}
    .img-edit-btn {{
      background: rgba(15,23,42,0.88);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(255,255,255,0.2);
      color: #fff;
      padding: 4px 9px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }}
    .img-edit-btn:hover {{ background: var(--amber); color: #000; }}
    .img-edit-btn.danger:hover {{ background: var(--rose); }}

    /* Edit Mode Banner */
    .edit-mode-banner {{
      display: none;
      position: fixed;
      top: 64px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 200;
      background: rgba(245,158,11,0.95);
      color: #030712;
      padding: 5px 18px;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      box-shadow: 0 4px 16px rgba(245,158,11,0.5);
      pointer-events: none;
    }}
    body.edit-mode-active .edit-mode-banner {{ display: block; }}

    /* ---- QUIZ EDITOR STYLES ---- */
    .quiz-editor-modal {{
      position: fixed;
      inset: 0;
      background: rgba(3,7,18,0.85);
      backdrop-filter: blur(10px);
      z-index: 300;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }}
    .quiz-editor-modal.active {{
      opacity: 1;
      pointer-events: auto;
    }}
    .quiz-editor-box {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      width: 92vw;
      max-width: 880px;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: var(--shadow-xl);
      animation: modalPop 0.25s cubic-bezier(0.16,1,0.3,1);
    }}
    .quiz-editor-header {{
      padding: 1.1rem 1.75rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-card);
    }}
    .quiz-editor-body {{
      flex: 1;
      overflow-y: auto;
      padding: 1.5rem 2rem;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }}
    .qe-question-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      position: relative;
    }}
    .qe-q-num {{
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--accent-primary);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }}
    .qe-field-label {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 0.25rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .qe-input, .qe-textarea {{
      width: 100%;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 0.6rem 0.9rem;
      color: var(--text-main);
      font-family: inherit;
      font-size: 0.88rem;
      outline: none;
      transition: border-color 0.15s;
    }}
    .qe-input:focus, .qe-textarea:focus {{
      border-color: var(--accent-primary);
      box-shadow: 0 0 0 2px rgba(56,189,248,0.15);
    }}
    .qe-textarea {{ resize: vertical; min-height: 60px; }}
    .qe-options-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
    }}
    .qe-option-row {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .qe-opt-letter {{
      width: 28px;
      height: 28px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.78rem;
      font-weight: 900;
      color: #fff;
      flex-shrink: 0;
    }}
    .qe-opt-letter.let-a {{ background: #ef4444; }}
    .qe-opt-letter.let-b {{ background: #0284c7; }}
    .qe-opt-letter.let-c {{ background: #f59e0b; }}
    .qe-opt-letter.let-d {{ background: #10b981; }}
    .qe-correct-radio {{
      width: 18px;
      height: 18px;
      cursor: pointer;
      accent-color: var(--emerald);
      flex-shrink: 0;
    }}
    .qe-delete-btn {{
      position: absolute;
      top: 0.75rem;
      right: 0.75rem;
      background: rgba(239,68,68,0.12);
      border: 1px solid rgba(239,68,68,0.3);
      color: #f87171;
      width: 28px;
      height: 28px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 0.88rem;
      transition: all 0.15s;
    }}
    .qe-delete-btn:hover {{ background: rgba(239,68,68,0.25); }}
    .qe-add-btn {{
      align-self: flex-start;
      background: rgba(16,185,129,0.12);
      border: 1px dashed rgba(16,185,129,0.4);
      color: var(--emerald);
      padding: 0.65rem 1.25rem;
      border-radius: var(--radius-md);
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .qe-add-btn:hover {{ background: rgba(16,185,129,0.22); }}
    .qe-editor-footer {{
      padding: 1rem 1.75rem;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      gap: 0.75rem;
      justify-content: flex-end;
      background: var(--bg-card);
    }}

    /* Image Add button in edit mode */
    .img-add-zone {{
      border: 2px dashed var(--amber);
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100px;
      cursor: pointer;
      color: var(--amber);
      font-weight: 700;
      font-size: 0.88rem;
      gap: 8px;
      transition: background 0.15s;
    }}
    .img-add-zone:hover {{ background: rgba(245,158,11,0.1); }}


    /* Slide Header Area */
    .slide-header {{
      margin-bottom: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }}

    .slide-category-badge {{
      display: inline-flex;
      align-items: center;
      align-self: flex-start;
      gap: 6px;
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: var(--radius-sm);
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: var(--accent-primary);
    }}

    .slide-category-badge.badge-emerald {{
      background: rgba(16, 185, 129, 0.15);
      border-color: rgba(16, 185, 129, 0.35);
      color: var(--emerald);
    }}

    .slide-category-badge.badge-purple {{
      background: rgba(168, 85, 247, 0.15);
      border-color: rgba(168, 85, 247, 0.35);
      color: var(--purple);
    }}

    .slide-title {{
      font-size: 1.95rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.18;
      color: var(--text-main);
    }}

    .slide-subtitle {{
      font-size: 0.96rem;
      color: var(--text-muted);
      font-weight: 500;
    }}

    /* ---- NEW IMAGE-CENTERED LAYOUT ---- */
    .slide-body-image-centered {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      min-height: 0;
      overflow: hidden;
    }}

    /* Central Hero Stage for 1 or more images */
    .slide-image-hero {{
      flex: 1.35;
      display: flex;
      gap: 1.15rem;
      min-height: 0;
      position: relative;
      justify-content: center;
      align-items: stretch;
    }}

    .slide-image-hero .image-panel {{
      flex: 1;
      max-width: 900px;
      display: flex;
      flex-direction: column;
      min-height: 0;
      position: relative;
    }}

    .slide-image-hero .image-panel.multi-img {{
      max-width: 48%;
    }}

    .slide-image-hero .image-viewport {{
      flex: 1;
      background: #020617;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      cursor: zoom-in;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.45);
      transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
    }}

    .slide-image-hero .image-viewport:hover {{
      border-color: var(--accent-primary);
      box-shadow: 0 6px 24px var(--accent-glow);
    }}

    .slide-image-hero .image-viewport img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.25s ease;
    }}

    .slide-image-hero .caption-card {{
      margin-top: 0.35rem;
      padding: 0.4rem 0.8rem;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .slide-image-hero .caption-title {{
      font-size: 0.74rem;
      font-weight: 800;
      color: var(--accent-primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .slide-image-hero .caption-text {{
      font-size: 0.76rem;
      color: var(--text-muted);
      line-height: 1.35;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* Commentary cards strip below the central figure */
    .slide-cards-strip {{
      flex: 0.95;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 0.65rem;
      min-height: 0;
      overflow-y: auto;
      padding-right: 0.25rem;
    }}

    .slide-body-no-image {{
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.85rem;
      min-height: 0;
      overflow-y: auto;
    }}

    /* Two Column Body Grid */
    .slide-body-grid {{
      flex: 1;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 2.25rem;
      min-height: 0;
    }}

    .cards-column {{
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      justify-content: center;
      overflow-y: auto;
      padding-right: 0.5rem;
    }}

    .lecture-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-left: 4px solid var(--accent-primary);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      box-shadow: var(--shadow-sm);
      transition: transform var(--transition-fast), border-color var(--transition-fast), box-shadow var(--transition-fast);
    }}

    .lecture-card:hover {{
      transform: translateX(4px);
      border-color: var(--accent-primary);
      box-shadow: var(--shadow-md);
    }}

    .lecture-card.card-emerald {{
      border-left-color: var(--emerald);
    }}

    .lecture-card.card-purple {{
      border-left-color: var(--purple);
    }}

    .card-heading {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.3rem;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .card-text {{
      font-size: 0.86rem;
      line-height: 1.48;
      color: var(--text-muted);
    }}

    /* Image Display Panel */
    .image-panel {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      height: 100%;
      min-height: 0;
    }}

    .image-viewport {{
      flex: 1;
      background: #020617;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      cursor: zoom-in;
      box-shadow: var(--shadow-md);
    }}

    .image-viewport img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.25s ease;
    }}

    .image-viewport:hover img {{
      transform: scale(1.025);
    }}

    .zoom-hint-badge {{
      position: absolute;
      bottom: 10px;
      right: 10px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      padding: 4px 10px;
      border-radius: 999px;
      font-size: 0.72rem;
      font-weight: 700;
      backdrop-filter: blur(4px);
      pointer-events: none;
      display: flex;
      align-items: center;
      gap: 5px;
    }}

    .caption-card {{
      margin-top: 0.65rem;
      padding: 0.65rem 0.85rem;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
    }}

    .caption-title {{
      font-size: 0.76rem;
      font-weight: 800;
      color: var(--accent-primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.2rem;
    }}

    .caption-text {{
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.4;
    }}

    /* Title Slide Special Styles */
    .title-slide-container {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 2.5rem;
      height: 100%;
      align-items: center;
    }}

    .title-left {{
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    .title-left .slide-title {{
      font-size: 2.75rem;
      margin: 0.75rem 0 0.5rem;
      line-height: 1.12;
    }}

    .title-left .slide-subtitle {{
      font-size: 1.15rem;
      margin-bottom: 1.75rem;
    }}

    .credits-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.25rem;
    }}

    .credits-heading {{
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--accent-primary);
      letter-spacing: 0.08em;
      margin-bottom: 0.5rem;
    }}

    .credits-list {{
      list-style: none;
    }}

    .credits-list li {{
      font-size: 0.84rem;
      color: var(--text-muted);
      margin-bottom: 0.25rem;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .credits-list li::before {{
      content: "•";
      color: var(--accent-primary);
      font-weight: bold;
    }}

    /* Controls Bottom Bar */
    footer.controls-footer {{
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      height: 65px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.75rem;
      position: sticky;
      bottom: 0;
      z-index: 50;
      box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.2);
    }}

    .controls-help-text {{
      display: flex;
      align-items: center;
      gap: 1.25rem;
      font-size: 0.78rem;
      color: var(--text-dim);
    }}

    .key-badge {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 2px 7px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 600;
    }}

    .nav-buttons-cluster {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .btn-nav {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 0.55rem 1.15rem;
      border-radius: var(--radius-sm);
      font-size: 0.86rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all var(--transition-fast);
    }}

    .btn-nav:hover:not(:disabled) {{
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    .btn-nav.primary {{
      background: var(--accent-primary);
      border-color: var(--accent-primary);
      color: #030712;
      box-shadow: 0 2px 10px rgba(56, 189, 248, 0.35);
    }}

    .btn-nav.primary:hover:not(:disabled) {{
      background: var(--accent-primary-hover);
      transform: translateY(-1px);
    }}

    .btn-nav:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}

    .slide-counter-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-main);
      padding: 0 0.5rem;
    }}

    .step-indicator-pill {{
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--accent-primary);
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
    }}

    /* Drawer Modal (Curriculum Overview) */
    .drawer-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(8px);
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity var(--transition-normal);
      padding: 1.5rem;
    }}

    .drawer-overlay.active {{
      opacity: 1;
      pointer-events: auto;
    }}

    .drawer-modal {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-xl);
      width: 95vw;
      max-width: 1440px;
      height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      animation: modalPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .drawer-header {{
      padding: 1.25rem 2rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      background: rgba(15, 23, 42, 0.95);
      flex-wrap: wrap;
    }}

    .drawer-header-left {{
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }}

    .drawer-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .drawer-filter-pills {{
      display: flex;
      gap: 0.5rem;
      background: rgba(2, 6, 23, 0.6);
      padding: 0.25rem;
      border-radius: var(--radius-full);
      border: 1px solid var(--border-subtle);
    }}

    .drawer-pill-btn {{
      padding: 0.4rem 1rem;
      font-size: 0.78rem;
      font-weight: 700;
      border-radius: var(--radius-full);
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      transition: all var(--transition-fast);
    }}

    .drawer-pill-btn:hover {{
      color: var(--text-main);
    }}

    .drawer-pill-btn.active {{
      background: var(--accent-primary);
      color: #020617;
      box-shadow: 0 2px 8px rgba(56, 189, 248, 0.4);
    }}

    .drawer-header-right {{
      display: flex;
      align-items: center;
      gap: 1rem;
      flex: 1;
      max-width: 480px;
      justify-content: flex-end;
    }}

    .drawer-search-input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 0.55rem 1rem;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.88rem;
      outline: none;
      transition: border-color var(--transition-fast);
    }}

    .drawer-search-input:focus {{
      border-color: var(--accent-primary);
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }}

    .drawer-grid {{
      flex: 1;
      min-height: 0;
      overflow-y: auto;
      padding: 1.75rem 2rem;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      grid-auto-rows: 250px;
      gap: 1.5rem;
    }}

    .drawer-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      overflow: hidden;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      height: 250px;
      min-height: 250px;
      transition: all var(--transition-fast);
      position: relative;
    }}

    .drawer-card:hover {{
      transform: translateY(-4px);
      border-color: var(--accent-primary);
      box-shadow: 0 12px 24px -6px rgba(0, 0, 0, 0.5), 0 0 0 1px var(--accent-primary);
    }}

    .drawer-card.active-slide {{
      border: 2px solid var(--accent-primary);
      box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    }}

    .drawer-card-thumb {{
      height: 155px;
      min-height: 155px;
      flex-shrink: 0;
      background: #020617;
      overflow: hidden;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .drawer-card-thumb img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }}

    .drawer-card:hover .drawer-card-thumb img {{
      transform: scale(1.05);
    }}

    .drawer-badge-slide {{
      position: absolute;
      top: 10px;
      left: 10px;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--accent-primary);
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      letter-spacing: 0.04em;
    }}

    .drawer-badge-part {{
      position: absolute;
      top: 10px;
      right: 10px;
      background: rgba(30, 41, 59, 0.88);
      backdrop-filter: blur(6px);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #cbd5e1;
      font-size: 0.7rem;
      font-weight: 700;
      padding: 0.25rem 0.55rem;
      border-radius: 6px;
    }}

    .drawer-card-body {{
      padding: 0.8rem 1rem;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      background: var(--bg-card);
      overflow: hidden;
    }}

    .drawer-card-title {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.35;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .drawer-card-sub {{
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-top: 0.3rem;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* ULTRA-CLEAR HIGH-POWER LIGHTBOX ZOOM MODAL */
    .lightbox-modal {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(3, 7, 18, 0.96);
      backdrop-filter: blur(12px);
      z-index: 200;
      display: flex;
      flex-direction: column;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease;
    }}

    .lightbox-modal.active {{
      opacity: 1;
      pointer-events: auto;
    }}

    .lightbox-toolbar {{
      height: 60px;
      background: rgba(15, 23, 42, 0.9);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 2rem;
      z-index: 210;
    }}

    .lightbox-tool-group {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .lightbox-btn {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all var(--transition-fast);
    }}

    .lightbox-btn:hover {{
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    .zoom-level-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent-primary);
      background: rgba(56, 189, 248, 0.15);
      padding: 4px 10px;
      border-radius: 999px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}

    .lightbox-viewport {{
      flex: 1;
      overflow: hidden;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: grab;
    }}

    .lightbox-viewport.is-dragging {{
      cursor: grabbing;
    }}

    .lightbox-img-wrapper {{
      transform-origin: center center;
      will-change: transform;
      user-select: none;
    }}

    .lightbox-img-wrapper img {{
      max-width: 90vw;
      max-height: 80vh;
      object-fit: contain;
      border-radius: 4px;
      box-shadow: 0 0 50px rgba(0, 0, 0, 0.9);
      pointer-events: none;
    }}

    .lightbox-footer {{
      padding: 0.85rem 2rem;
      background: rgba(15, 23, 42, 0.9);
      border-top: 1px solid var(--border-subtle);
      text-align: center;
      color: var(--text-muted);
      font-size: 0.92rem;
      font-weight: 600;
      box-shadow: var(--shadow-md);
      z-index: 210;
    }}

    /* ==========================================================================
       LIVE AUDIENCE INTERACTIVE QUIZ ARENA (HOST SCREEN)
       ========================================================================== */
    .quiz-drawer-modal {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-xl);
      width: 96vw;
      max-width: 1180px;
      max-height: 92vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      animation: modalPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .quiz-header-bar {{
      padding: 1rem 1.75rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-card);
    }}

    .quiz-header-left {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .quiz-badge-live {{
      background: linear-gradient(135deg, #ef4444, #dc2626);
      color: #fff;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.08em;
      display: flex;
      align-items: center;
      gap: 5px;
      animation: pulseLive 1.5s infinite;
    }}

    @keyframes pulseLive {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.85; transform: scale(0.98); }}
    }}

    .room-code-badge {{
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: var(--accent-primary);
      padding: 4px 12px;
      border-radius: 999px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 0.05em;
    }}

    .quiz-header-right {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .quiz-mode-pill-group {{
      display: flex;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      padding: 3px;
      border-radius: 999px;
    }}

    .quiz-mode-btn {{
      border: none;
      background: transparent;
      color: var(--text-muted);
      padding: 4px 12px;
      font-size: 0.78rem;
      font-weight: 700;
      border-radius: 999px;
      cursor: pointer;
      transition: all var(--transition-fast);
    }}

    .quiz-mode-btn.active {{
      background: var(--accent-primary);
      color: #030712;
    }}

    /* Main Arena Viewport */
    .quiz-arena-viewport {{
      flex: 1;
      overflow-y: auto;
      padding: 1.75rem 2.25rem;
      display: flex;
      flex-direction: column;
    }}

    /* LOBBY SCREEN */
    .lobby-grid {{
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 2.5rem;
      align-items: start;
    }}

    .qr-card-container {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      text-align: center;
      box-shadow: var(--shadow-md);
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .qr-box {{
      width: 210px;
      height: 210px;
      background: #ffffff;
      padding: 10px;
      border-radius: 14px;
      margin-bottom: 1.25rem;
      box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .qr-box img, .qr-box canvas {{
      width: 100% !important;
      height: 100% !important;
    }}

    .qr-instruction-title {{
      font-size: 1.05rem;
      font-weight: 800;
      margin-bottom: 0.35rem;
      color: var(--text-main);
    }}

    .qr-instruction-desc {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 1.15rem;
    }}

    .join-link-box {{
      width: 100%;
      background: var(--bg-surface);
      border: 1px dashed var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 0.6rem 0.85rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.76rem;
      color: var(--accent-primary);
      margin-bottom: 0.85rem;
      word-break: break-all;
    }}

    .lobby-action-row {{
      display: flex;
      gap: 0.5rem;
      width: 100%;
    }}

    .btn-secondary-sm {{
      flex: 1;
      padding: 0.55rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      color: var(--text-main);
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      transition: all var(--transition-fast);
    }}

    .btn-secondary-sm:hover {{
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    /* Participants Column */
    .participants-column {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}

    .roster-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      padding: 1rem 1.35rem;
      border-radius: var(--radius-md);
    }}

    .roster-count-badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--emerald);
    }}

    .participants-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
      gap: 0.85rem;
      max-height: 380px;
      overflow-y: auto;
      padding-right: 0.5rem;
    }}

    .participant-chip {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 0.75rem 1rem;
      display: flex;
      align-items: center;
      gap: 0.75rem;
      animation: chipJoin 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      transition: border-color 0.2s;
    }}

    .participant-chip:hover {{
      border-color: var(--accent-primary);
    }}

    @keyframes chipJoin {{
      from {{ transform: scale(0.85); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}

    .chip-avatar {{
      font-size: 1.5rem;
    }}

    .chip-name {{
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--text-main);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .empty-roster-msg {{
      grid-column: 1 / -1;
      padding: 3rem 1.5rem;
      text-align: center;
      color: var(--text-muted);
      border: 2px dashed var(--border-subtle);
      border-radius: var(--radius-md);
    }}

    /* Start Button & Controls */
    .lobby-controls-strip {{
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-top: 0.5rem;
    }}

    .btn-start-arena {{
      flex: 1.4;
      background: linear-gradient(135deg, #10b981, #059669);
      border: none;
      color: #ffffff;
      padding: 1.1rem;
      border-radius: var(--radius-md);
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: 0.02em;
      cursor: pointer;
      box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: all var(--transition-fast);
    }}

    .btn-start-arena:hover:not(:disabled) {{
      transform: translateY(-2px);
      box-shadow: 0 6px 25px rgba(16, 185, 129, 0.55);
    }}

    .btn-start-arena:disabled {{
      opacity: 0.5;
      cursor: not-allowed;
    }}

    .btn-sim-bots {{
      flex: 1;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 1.1rem;
      border-radius: var(--radius-md);
      font-size: 0.92rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all var(--transition-fast);
    }}

    .btn-sim-bots:hover {{
      background: var(--bg-card-hover);
      border-color: var(--purple);
      color: var(--purple);
    }}

    /* ==========================================================================
       QUESTION & REVEAL ACTIVE SCREEN (HOST)
       ========================================================================== */
    .arena-status-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      padding: 1rem 1.5rem;
      border-radius: var(--radius-md);
      margin-bottom: 1.5rem;
    }}

    .arena-q-index {{
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--accent-primary);
    }}

    .arena-timer-pill {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--gold);
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.35);
      padding: 4px 18px;
      border-radius: 999px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .arena-timer-pill.urgent {{
      color: var(--rose);
      background: rgba(239, 68, 68, 0.2);
      border-color: var(--rose);
      animation: pulseUrgent 0.8s infinite;
    }}

    @keyframes pulseUrgent {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.05); }}
    }}

    .respondent-tracker {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .resp-bar-wrap {{
      width: 140px;
      height: 10px;
      background: var(--bg-surface);
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid var(--border-subtle);
    }}

    .resp-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #0284c7, #10b981);
      width: 0%;
      transition: width 0.3s ease;
    }}

    .resp-text {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    /* Main Question Card */
    .arena-question-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.75rem 2rem;
      margin-bottom: 1.5rem;
    }}

    .arena-question-prompt {{
      font-size: 1.35rem;
      font-weight: 800;
      line-height: 1.4;
      color: var(--text-main);
      margin-bottom: 1.5rem;
    }}

    /* 4 Option Rows */
    .arena-options-container {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
    }}

    .arena-option-card {{
      background: var(--bg-surface);
      border: 2px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.15rem 1.35rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      position: relative;
      overflow: hidden;
      transition: all 0.25s ease;
    }}

    .arena-option-card.correct {{
      border-color: var(--emerald) !important;
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), var(--bg-surface)) !important;
      box-shadow: 0 0 20px rgba(16, 185, 129, 0.3);
    }}

    .arena-option-card.dimmed {{
      opacity: 0.55;
    }}

    .arena-opt-top {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .arena-opt-letter {{
      width: 36px;
      height: 36px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.1rem;
      font-weight: 900;
      color: #fff;
      flex-shrink: 0;
    }}

    .arena-opt-letter.let-a {{ background: #ef4444; }}
    .arena-opt-letter.let-b {{ background: #0284c7; }}
    .arena-opt-letter.let-c {{ background: #f59e0b; }}
    .arena-opt-letter.let-d {{ background: #10b981; }}

    .arena-opt-text {{
      font-size: 1.02rem;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.35;
      flex: 1;
    }}

    .arena-correct-tag {{
      background: var(--emerald);
      color: #030712;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      letter-spacing: 0.05em;
    }}

    /* Vote distribution bar */
    .vote-bar-wrap {{
      width: 100%;
      height: 8px;
      background: var(--bg-card);
      border-radius: 999px;
      overflow: hidden;
      margin-top: 0.35rem;
    }}

    .vote-bar-fill {{
      height: 100%;
      background: var(--accent-primary);
      width: 0%;
      transition: width 0.5s ease;
    }}

    .vote-stats-label {{
      display: flex;
      justify-content: space-between;
      font-size: 0.78rem;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-muted);
      font-weight: 700;
    }}

    /* Rationale box */
    .arena-rationale-box {{
      background: var(--bg-surface);
      border-left: 5px solid var(--accent-primary);
      border-radius: var(--radius-sm);
      padding: 1.15rem 1.35rem;
      margin-top: 1.25rem;
      line-height: 1.5;
      font-size: 0.95rem;
      color: var(--text-muted);
      animation: fadeIn 0.4s ease;
    }}

    .arena-rationale-box strong {{
      color: var(--text-main);
    }}

    /* Reveal Bottom Transition Bar (5s countdown with pause button) */
    .reveal-transition-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      padding: 0.85rem 1.5rem;
      border-radius: var(--radius-md);
      margin-top: 1rem;
    }}

    .countdown-pill {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--accent-primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .reveal-actions {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    /* ==========================================================================
       PODIUM & FINAL LEADERBOARD SCREEN
       ========================================================================== */
    .podium-arena-container {{
      display: flex;
      flex-direction: column;
      gap: 2rem;
      padding: 1rem 0;
    }}

    .podium-title-box {{
      text-align: center;
    }}

    .podium-title-box h2 {{
      font-size: 2.2rem;
      font-weight: 900;
      letter-spacing: -0.02em;
      margin-bottom: 0.35rem;
    }}

    /* 3D Olympic Podium Steps */
    .olympic-podium {{
      display: flex;
      align-items: flex-end;
      justify-content: center;
      gap: 1.5rem;
      margin: 1.5rem 0 2rem;
      height: 280px;
    }}

    .podium-col {{
      width: 190px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-end;
    }}

    .podium-user-card {{
      margin-bottom: 0.75rem;
      text-align: center;
      animation: dropUser 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    @keyframes dropUser {{
      from {{ transform: translateY(-30px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    .podium-avatar {{
      font-size: 2.4rem;
      margin-bottom: 0.2rem;
    }}

    .podium-name {{
      font-size: 1rem;
      font-weight: 800;
      color: var(--text-main);
      max-width: 180px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}

    .podium-score {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--accent-primary);
    }}

    .podium-block {{
      width: 100%;
      border-radius: 16px 16px 0 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      padding-top: 1rem;
      color: #030712;
      font-weight: 900;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      position: relative;
    }}

    .podium-block.first {{
      height: 180px;
      background: linear-gradient(180deg, #fcd34d, #f59e0b);
      border: 2px solid #fbbf24;
    }}

    .podium-block.second {{
      height: 130px;
      background: linear-gradient(180deg, #e2e8f0, #94a3b8);
      border: 2px solid #cbd5e1;
    }}

    .podium-block.third {{
      height: 95px;
      background: linear-gradient(180deg, #fba973, #d97706);
      border: 2px solid #ea580c;
    }}

    .podium-rank-num {{
      font-size: 2.4rem;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 900;
      line-height: 1;
    }}

    .podium-medal-icon {{
      font-size: 1.5rem;
      margin-top: 0.2rem;
    }}

    /* Leaderboard Table */
    .leaderboard-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      overflow: hidden;
    }}

    .leaderboard-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }}

    .leaderboard-table th {{
      padding: 0.75rem 1rem;
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .leaderboard-table td {{
      padding: 0.85rem 1rem;
      font-size: 0.92rem;
      font-weight: 600;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .leaderboard-table tr:hover td {{
      background: var(--bg-card-hover);
    }}

    .rank-cell {{
      font-family: 'JetBrains Mono', monospace;
      font-weight: 800;
      width: 60px;
    }}

    .rank-1 {{ color: var(--gold); }}
    .rank-2 {{ color: var(--silver); }}
    .rank-3 {{ color: var(--bronze); }}


    /* ==========================================================================
       TRUE FULLSCREEN HALL PRESENTATION MODE (100vw x 100vh EDGE-TO-EDGE)
       ========================================================================== */
    :fullscreen .lecture-header,
    :-webkit-full-screen .lecture-header,
    body.is-fullscreen .lecture-header,
    :fullscreen .controls-footer,
    :-webkit-full-screen .controls-footer,
    body.is-fullscreen .controls-footer {{
      display: none !important;
    }}

    :fullscreen .progress-strip,
    :-webkit-full-screen .progress-strip,
    body.is-fullscreen .progress-strip {{
      position: fixed !important;
      top: 0 !important;
      left: 0 !important;
      width: 100vw !important;
      height: 3px !important;
      z-index: 999 !important;
      background: transparent !important;
    }}

    :fullscreen main.presentation-stage,
    :-webkit-full-screen main.presentation-stage,
    body.is-fullscreen main.presentation-stage {{
      padding: 0 !important;
      margin: 0 !important;
      width: 100vw !important;
      height: 100vh !important;
      max-width: 100vw !important;
      max-height: 100vh !important;
      overflow: hidden !important;
      background: var(--bg-base) !important;
    }}

    :fullscreen .slide-aspect-box,
    :-webkit-full-screen .slide-aspect-box,
    body.is-fullscreen .slide-aspect-box {{
      width: 100vw !important;
      height: 100vh !important;
      max-width: 100vw !important;
      max-height: 100vh !important;
      aspect-ratio: auto !important;
      border: none !important;
      border-radius: 0 !important;
      box-shadow: none !important;
      margin: 0 !important;
      background: var(--bg-surface) !important;
    }}

    :fullscreen .slide-content-container,
    :-webkit-full-screen .slide-content-container,
    body.is-fullscreen .slide-content-container {{
      width: 100vw !important;
      height: 100vh !important;
      padding: clamp(1.25rem, 2.2vh, 2.75rem) clamp(2.5rem, 4vw, 5.5rem) clamp(2.5rem, 4vh, 4.5rem) !important;
      box-sizing: border-box !important;
      display: flex !important;
      flex-direction: column !important;
    }}

    :fullscreen .slide-header,
    :-webkit-full-screen .slide-header,
    body.is-fullscreen .slide-header {{
      margin-bottom: clamp(1rem, 2vh, 1.8rem) !important;
    }}

    :fullscreen .slide-title,
    :-webkit-full-screen .slide-title,
    body.is-fullscreen .slide-title {{
      font-size: clamp(2.2rem, 3.4vw, 4rem) !important;
      line-height: 1.15 !important;
    }}

    :fullscreen .slide-subtitle,
    :-webkit-full-screen .slide-subtitle,
    body.is-fullscreen .slide-subtitle {{
      font-size: clamp(1.1rem, 1.4vw, 1.6rem) !important;
    }}

    :fullscreen .slide-category-badge,
    :-webkit-full-screen .slide-category-badge,
    body.is-fullscreen .slide-category-badge {{
      font-size: clamp(0.85rem, 1vw, 1.15rem) !important;
      padding: 6px 14px !important;
    }}

    :fullscreen .slide-body-grid,
    :-webkit-full-screen .slide-body-grid,
    body.is-fullscreen .slide-body-grid {{
      grid-template-columns: 1.1fr 0.9fr !important;
      gap: clamp(2rem, 3.5vw, 4.5rem) !important;
      flex: 1 !important;
      min-height: 0 !important;
    }}

    :fullscreen .slide-body-image-centered,
    :-webkit-full-screen .slide-body-image-centered,
    body.is-fullscreen .slide-body-image-centered {{
      flex: 1 !important;
      gap: clamp(0.75rem, 1.5vh, 1.6rem) !important;
      overflow: hidden !important;
    }}

    :fullscreen .slide-image-hero,
    :-webkit-full-screen .slide-image-hero,
    body.is-fullscreen .slide-image-hero {{
      flex: 1.65 !important;
      gap: clamp(1rem, 2vw, 2.5rem) !important;
    }}

    :fullscreen .slide-image-hero .caption-card,
    :-webkit-full-screen .slide-image-hero .caption-card,
    body.is-fullscreen .slide-image-hero .caption-card {{
      padding: clamp(0.5rem, 1vh, 0.9rem) clamp(0.75rem, 1.2vw, 1.5rem) !important;
    }}

    :fullscreen .slide-image-hero .caption-title,
    :-webkit-full-screen .slide-image-hero .caption-title,
    body.is-fullscreen .slide-image-hero .caption-title {{
      font-size: clamp(0.85rem, 1.1vw, 1.3rem) !important;
    }}

    :fullscreen .slide-image-hero .caption-text,
    :-webkit-full-screen .slide-image-hero .caption-text,
    body.is-fullscreen .slide-image-hero .caption-text {{
      font-size: clamp(0.85rem, 1.0vw, 1.15rem) !important;
      white-space: normal !important;
    }}

    :fullscreen .slide-cards-strip,
    :-webkit-full-screen .slide-cards-strip,
    body.is-fullscreen .slide-cards-strip {{
      flex: 0.95 !important;
      gap: clamp(0.65rem, 1.2vw, 1.25rem) !important;
    }}

    :fullscreen .slide-cards-strip .lecture-card,
    :-webkit-full-screen .slide-cards-strip .lecture-card,
    body.is-fullscreen .slide-cards-strip .lecture-card {{
      padding: clamp(0.8rem, 1.4vh, 1.4rem) clamp(1rem, 1.5vw, 1.8rem) !important;
      border-radius: var(--radius-lg) !important;
      border-left-width: 5px !important;
    }}

    :fullscreen .slide-cards-strip .card-heading,
    :-webkit-full-screen .slide-cards-strip .card-heading,
    body.is-fullscreen .slide-cards-strip .card-heading {{
      font-size: clamp(1rem, 1.3vw, 1.5rem) !important;
      margin-bottom: 0.35rem !important;
    }}

    :fullscreen .slide-cards-strip .card-text,
    :-webkit-full-screen .slide-cards-strip .card-text,
    body.is-fullscreen .slide-cards-strip .card-text {{
      font-size: clamp(0.9rem, 1.1vw, 1.3rem) !important;
      line-height: 1.5 !important;
    }}

    :fullscreen .slide-body-no-image,
    :-webkit-full-screen .slide-body-no-image,
    body.is-fullscreen .slide-body-no-image {{
      gap: clamp(0.85rem, 1.6vh, 1.5rem) !important;
    }}
    /* Title slides in Fullscreen */
    :fullscreen .title-slide-container,
    :-webkit-full-screen .title-slide-container,
    body.is-fullscreen .title-slide-container {{
      gap: clamp(2.5rem, 4.5vw, 5.5rem) !important;
      height: 100% !important;
    }}

    :fullscreen .title-left .slide-title,
    :-webkit-full-screen .title-left .slide-title,
    body.is-fullscreen .title-left .slide-title {{
      font-size: clamp(3rem, 4.8vw, 5.2rem) !important;
      line-height: 1.12 !important;
    }}

    :fullscreen .title-left .slide-subtitle,
    :-webkit-full-screen .title-left .slide-subtitle,
    body.is-fullscreen .title-left .slide-subtitle {{
      font-size: clamp(1.35rem, 1.8vw, 2.2rem) !important;
      margin-bottom: clamp(1.5rem, 2.5vh, 2.5rem) !important;
    }}

    :fullscreen .credits-box,
    :-webkit-full-screen .credits-box,
    body.is-fullscreen .credits-box {{
      padding: clamp(1.25rem, 2vh, 2.25rem) clamp(1.5rem, 2vw, 2.5rem) !important;
      border-radius: var(--radius-lg) !important;
    }}

    :fullscreen .credits-heading,
    :-webkit-full-screen .credits-heading,
    body.is-fullscreen .credits-heading {{
      font-size: clamp(0.9rem, 1.1vw, 1.25rem) !important;
      margin-bottom: 0.75rem !important;
    }}

    :fullscreen .credits-list li,
    :-webkit-full-screen .credits-list li,
    body.is-fullscreen .credits-list li {{
      font-size: clamp(1.05rem, 1.25vw, 1.45rem) !important;
      margin-bottom: 0.45rem !important;
    }}

    /* Sleek Floating Fullscreen Presentation HUD (Auto-Hiding) */
    .fullscreen-hud {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(0);
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.18);
      border-radius: 999px;
      padding: 6px 16px;
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 1000;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.55);
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.35s ease, transform 0.35s ease;
    }}

    :fullscreen .fullscreen-hud,
    :-webkit-full-screen .fullscreen-hud,
    body.is-fullscreen .fullscreen-hud {{
      pointer-events: auto;
      opacity: 1;
    }}

    .fullscreen-hud.hud-hidden {{
      opacity: 0.08 !important;
      transform: translateX(-50%) translateY(10px) !important;
    }}

    .fullscreen-hud:hover,
    .fullscreen-hud:focus-within {{
      opacity: 1 !important;
      transform: translateX(-50%) translateY(0) !important;
    }}

    .hud-btn {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 5px 12px;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all var(--transition-fast);
    }}

    .hud-btn.primary {{
      background: var(--accent-primary);
      border-color: var(--accent-primary);
      color: #030712;
    }}

    .hud-btn:hover:not(:disabled) {{
      transform: translateY(-1px);
    }}

    .hud-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}

    .hud-counter {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      font-weight: 800;
      color: #fff;
      padding: 0 4px;
    }}

    .hud-divider {{
      width: 1px;
      height: 20px;
      background: rgba(255, 255, 255, 0.2);
    }}

    .hud-step-pill {{
      background: rgba(56, 189, 248, 0.18);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: var(--accent-primary);
      padding: 3px 10px;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
    }}

    .hud-icon-btn {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all var(--transition-fast);
    }}

    .hud-icon-btn:hover {{
      background: rgba(255, 255, 255, 0.2);
      color: var(--accent-primary);
    }}

    .hud-icon-btn.exit-fs:hover {{
      background: rgba(239, 68, 68, 0.25);
      color: #f87171;
      border-color: rgba(239, 68, 68, 0.5);
    }}


    .btn-exit-quiz {{
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.45);
      color: #f87171;
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all var(--transition-fast);
      margin-right: 6px;
    }}

    .btn-exit-quiz:hover {{
      background: rgba(239, 68, 68, 0.28);
      border-color: #f87171;
      transform: translateY(-1px);
      box-shadow: 0 2px 8px rgba(239, 68, 68, 0.35);
    }}

    /* Responsive */
    @media (max-width: 1100px) {{
      .slide-body-grid {{
        grid-template-columns: 1fr;
      }}
      .slide-aspect-box {{
        height: auto;
        min-height: 85vh;
        overflow-y: auto;
      }}
      .image-panel {{
        min-height: 380px;
      }}
      .lobby-grid {{
        grid-template-columns: 1fr;
      }}
      .arena-options-container {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body data-theme="dark">

  <!-- Header -->
  <header class="lecture-header">
    <div class="header-left">
      <div class="logo-badge">
        <span>YOUMANS & WINN</span>
      </div>
      <div class="lecture-title-text">
        <span>Ventricular Tumors Masterclass</span>
        <span class="lecture-subtitle-text">Chapter 170 • High-Yield Neurosurgical Interactive Curriculum</span>
      </div>
    </div>

    <div class="header-center">
      <button class="part-pill active" id="pillAll" onclick="setFilter('all')">All Slides (80)</button>
      <button class="part-pill" id="pillPart1" onclick="setFilter('part1')">Part 1: Lateral (33)</button>
      <button class="part-pill" id="pillPart2" onclick="setFilter('part2')">Part 2: Ventricular Tumors (47)</button>
    </div>

    <div class="header-right">
      <button class="btn-icon active-mode" id="btnStepMode" title="Toggle Click-by-Click Element Reveal (Press B)" onclick="toggleStepMode()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 17 18 12 13 7"/><polyline points="6 17 11 12 6 7"/></svg>
      </button>
      <button class="btn-icon" title="Slide Overview & Grid (Press O)" onclick="toggleDrawer()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
      </button>
      <button class="btn-icon btn-quiz-highlight" title="Interactive Live Audience Quiz (Press Q)" onclick="toggleQuiz()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
      </button>
      <button class="btn-icon btn-edit-mode" id="btnEditMode" title="Edit Mode: Edit Slide Text &amp; Images (Press E)" onclick="toggleEditMode()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
      </button>
      <button class="btn-icon" title="Toggle Light/Dark Theme (Press T)" onclick="toggleTheme()">
        <svg id="themeIcon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      </button>
      <button class="btn-icon" title="Fullscreen Hall Mode (Press F)" onclick="toggleFullscreen()">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>
      </button>
    </div>
  </header>

  <!-- Progress bar -->
  <div class="progress-strip">
    <div class="progress-fill" id="progressBar"></div>
  </div>

  <!-- Main Presentation Stage -->
  <main class="presentation-stage">
    <div class="slide-aspect-box" id="slideBox" onclick="handleSlideBoxClick(event)">
      <!-- Dynamic slide content renders here -->
    </div>
  </main>

  <!-- Sleek Floating Presentation HUD (Auto-Hiding in Fullscreen) -->
  <div id="fullscreenHud" class="fullscreen-hud">
    <button class="hud-btn" id="fsBtnPrev" onclick="navigateStepOrSlide(-1)" title="Previous (Left Arrow)">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
    </button>
    <span class="hud-counter" id="fsSlideCounter">Slide 1 / 80</span>
    <button class="hud-btn primary" id="fsBtnNext" onclick="navigateStepOrSlide(1)" title="Next Point (Space or Right Arrow)">
      <span id="fsNextLabel">Next</span>
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
    </button>
    <div class="hud-divider"></div>
    <span class="hud-step-pill" id="fsStepBadge">Build: Ready</span>
    <button class="hud-icon-btn" onclick="toggleDrawer()" title="Slide Overview & Index (O)">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
    </button>
    <button class="hud-icon-btn" onclick="toggleQuiz()" title="Live Quiz Arena (Q)">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
    </button>
    <button class="hud-icon-btn exit-fs" onclick="toggleFullscreen()" title="Exit Fullscreen (Esc or F)">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
  </div>


  <!-- Bottom Navigation & Controls -->
  <footer class="controls-footer">
    <div class="controls-help-text">
      <span><span class="key-badge">Click / Space / →</span> Reveal & Advance</span>
      <span><span class="key-badge">←</span> Back</span>
      <span><span class="key-badge">B</span> Build Mode</span>
      <span><span class="key-badge">F</span> Fullscreen</span>
      <span><span class="key-badge">O</span> Index</span>
      <span><span class="key-badge">Q</span> Live Quiz</span>
    </div>

    <div class="nav-buttons-cluster">
      <button class="btn-nav" id="btnPrev" onclick="navigateStepOrSlide(-1)">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
        <span>Previous</span>
      </button>

      <div class="step-indicator-pill" id="stepIndicator">Build: Ready</div>
      <span class="slide-counter-badge" id="slideCounter">Slide 1 / 80</span>

      <button class="btn-nav primary" id="btnNext" onclick="navigateStepOrSlide(1)">
        <span id="nextBtnLabel">Next Point</span>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
      </button>
    </div>
  </footer>

  <!-- Slide Overview Grid Drawer -->
  <div class="drawer-overlay" id="drawerOverlay" onclick="if(event.target===this) toggleDrawer()">
    <div class="drawer-modal">
      <div class="drawer-header">
        <div class="drawer-header-left">
          <h2 class="drawer-title">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent-primary)" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
            Slide Overview &amp; Visual Index
          </h2>
          <div class="drawer-filter-pills">
            <button class="drawer-pill-btn active" id="drawerPillAll" onclick="setDrawerFilter('all', this)">All (80)</button>
            <button class="drawer-pill-btn" id="drawerPill1" onclick="setDrawerFilter('1', this)">Part 1 (33)</button>
            <button class="drawer-pill-btn" id="drawerPill2" onclick="setDrawerFilter('2', this)">Part 2 (47)</button>
          </div>
        </div>
        <div class="drawer-header-right">
          <input type="text" class="drawer-search-input" id="drawerSearch" placeholder="Search anatomy, corridor, pathology, figure..." oninput="filterDrawerSlides()">
          <button class="btn-icon" title="Close Overview (Esc)" onclick="toggleDrawer()">✕</button>
        </div>
      </div>
      <div class="drawer-grid" id="drawerGrid">
        <!-- Rendered by JS -->
      </div>
    </div>
  </div>

  <!-- ULTRA-CLEAR HIGH-POWER LIGHTBOX ZOOM MODAL -->
  <div class="lightbox-modal" id="lightboxModal" onclick="if(event.target===this) toggleLightbox()">
    <div class="lightbox-toolbar">
      <div class="lightbox-tool-group">
        <button class="lightbox-btn" onclick="adjustZoom(0.35)">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
          <span>Zoom In (+)</span>
        </button>
        <button class="lightbox-btn" onclick="adjustZoom(-0.35)">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
          <span>Zoom Out (-)</span>
        </button>
        <button class="lightbox-btn" onclick="setZoomLevel(1)">100%</button>
        <button class="lightbox-btn" onclick="setZoomLevel(2)">200% (Labels & Arrows)</button>
        <button class="lightbox-btn" onclick="setZoomLevel(3)">300% (Ultra-Detail)</button>
        <button class="lightbox-btn" onclick="resetZoom()">Fit</button>
      </div>
      <div class="lightbox-tool-group">
        <span class="zoom-level-badge" id="zoomLevelBadge">Zoom: 100%</span>
        <button class="lightbox-btn" onclick="toggleLightbox()">✕ Close (Esc)</button>
      </div>
    </div>

    <div class="lightbox-viewport" id="lightboxViewport" onmousedown="startDrag(event)" onwheel="handleWheelZoom(event)">
      <div class="lightbox-img-wrapper" id="lightboxWrapper">
        <img id="lightboxImg" src="" alt="Zoomed view">
      </div>
    </div>

    <div class="lightbox-footer" id="lightboxCap"></div>
  </div>

  <!-- LIVE AUDIENCE INTERACTIVE QUIZ ARENA MODAL -->
  <div class="drawer-overlay" id="quizOverlay" onclick="if(event.target===this) toggleQuiz()">
    <div class="quiz-drawer-modal">
      <div class="quiz-header-bar">
        <div class="quiz-header-left">
          <span class="quiz-badge-live">● LIVE AUDIENCE ARENA</span>
          <span class="room-code-badge" id="arenaRoomBadge">ROOM: VENTRICLE</span>
          <span style="font-size: 0.8rem; color: var(--text-muted); display: flex; align-items: center; gap: 5px;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: var(--emerald);" id="arenaConnDot"></span>
            <span id="arenaConnLabel">Broker Ready</span>
          </span>
        </div>

        <div class="quiz-header-right">
          <div class="quiz-mode-pill-group">
            <button class="quiz-mode-btn active" id="btnModeLive" onclick="setQuizArenaMode('live')">Live Audience Mode</button>
            <button class="quiz-mode-btn" id="btnModeSolo" onclick="setQuizArenaMode('solo')">Solo Board Mode</button>
          </div>
          <button class="btn-secondary-sm" onclick="openQuizEditor()" style="flex:initial; padding:6px 14px; font-size:0.8rem; font-weight:700; margin-right:6px;" title="Edit Questions, Choices &amp; Explanations">✏️ Edit Questions</button>
          <button class="btn-exit-quiz" id="btnExitQuizAdmin" onclick="adminExitQuiz()" title="Exit Quiz & End Session for All">🛑 Exit Quiz</button>
          <button class="btn-icon" onclick="toggleQuiz()" title="Close Quiz View">✕</button>
        </div>
      </div>

      <div class="quiz-arena-viewport" id="quizArenaBody">
        <!-- Rendered dynamically by Quiz Engine: Lobby, Question, Reveal, or Podium -->
      </div>
    </div>
  </div>

  <!-- Edit Mode Banner -->
  <div class="edit-mode-banner" id="editModeBanner">✏️ EDIT MODE ACTIVE — Click any text to edit • Click an image to manage it</div>

  <!-- Hidden file input for image upload -->
  <input type="file" id="imgUploadInput" accept="image/*" style="display:none" onchange="handleImageUpload(event)">

  <!-- QUIZ EDITOR MODAL -->
  <div class="quiz-editor-modal" id="quizEditorModal" onclick="if(event.target===this) closeQuizEditor()">
    <div class="quiz-editor-box">
      <div class="quiz-editor-header">
        <div style="display:flex;align-items:center;gap:0.75rem;">
          <span style="font-size:1.15rem;font-weight:800;">📝 Quiz Question Editor</span>
          <span style="font-size:0.78rem;color:var(--text-muted);">Changes saved to browser storage automatically</span>
        </div>
        <div style="display:flex;gap:0.5rem;">
          <button class="btn-nav primary" onclick="saveQuizEdits()" style="padding:6px 14px;font-size:0.82rem;">💾 Save &amp; Apply</button>
          <button class="btn-icon" onclick="closeQuizEditor()">✕</button>
        </div>
      </div>
      <div class="quiz-editor-body" id="quizEditorBody">
        <!-- rendered by JS -->
      </div>
      <div class="qe-editor-footer">
        <button class="qe-add-btn" onclick="addNewQuestion()">➕ Add Question</button>
        <button class="btn-nav" onclick="resetQuizToDefaults()">↺ Reset to Defaults</button>
      </div>
    </div>
  </div>


    <script>
    const SLIDES_DATA = {slides_json};

    let currentIndex = 0;
    let currentFilter = 'all'; // 'all', 'part1', 'part2'
    let filteredIndices = SLIDES_DATA.map((_, i) => i);
    
    // Manual Click-by-Click Element Reveal State
    let stepModeEnabled = true;
    let currentStep = 0;
    let totalStepsForSlide = 0;

    function setFilter(filter) {{
      currentFilter = filter;
      document.querySelectorAll('.part-pill').forEach(p => p.classList.remove('active'));
      
      if (filter === 'all') {{
        document.getElementById('pillAll').classList.add('active');
        filteredIndices = SLIDES_DATA.map((_, i) => i);
      }} else if (filter === 'part1') {{
        document.getElementById('pillPart1').classList.add('active');
        filteredIndices = SLIDES_DATA.map((s, i) => s.part === 1 ? i : -1).filter(i => i !== -1);
      }} else if (filter === 'part2') {{
        document.getElementById('pillPart2').classList.add('active');
        filteredIndices = SLIDES_DATA.map((s, i) => s.part === 2 ? i : -1).filter(i => i !== -1);
      }}

      currentIndex = filteredIndices[0];
      currentStep = 0;
      renderSlide('forward');
      renderDrawerGrid();
    }}

    function toggleStepMode() {{
      stepModeEnabled = !stepModeEnabled;
      const btn = document.getElementById('btnStepMode');
      btn.classList.toggle('active-mode', stepModeEnabled);
      renderSlide('none');
    }}

    function navigateStepOrSlide(direction) {{
      if (!stepModeEnabled) {{
        navigateSlide(direction);
        return;
      }}

      if (direction > 0) {{
        if (currentStep < totalStepsForSlide) {{
          currentStep++;
          applyStepVisibility();
        }} else {{
          navigateSlide(1);
        }}
      }} else {{
        if (currentStep > 0) {{
          currentStep--;
          applyStepVisibility();
        }} else {{
          navigateSlide(-1, 'end');
        }}
      }}
    }}

    function navigateSlide(delta, targetStep = 'start') {{
      const pos = filteredIndices.indexOf(currentIndex);
      const nextPos = pos + delta;
      if (nextPos >= 0 && nextPos < filteredIndices.length) {{
        const direction = delta > 0 ? 'forward' : 'backward';
        currentIndex = filteredIndices[nextPos];
        currentStep = (targetStep === 'end') ? 999 : 0;
        renderSlide(direction);
      }}
    }}

    function handleSlideBoxClick(e) {{
      if (e.target.closest('.image-viewport') || e.target.closest('button')) return;
      navigateStepOrSlide(1);
    }}

    function applyStepVisibility() {{
      const stepElements = document.querySelectorAll('[data-step-order]');
      totalStepsForSlide = stepElements.length;

      if (!stepModeEnabled) {{
        stepElements.forEach(el => {{
          el.classList.remove('step-hidden');
          el.classList.add('step-active');
        }});
        document.getElementById('stepIndicator').textContent = "Build: All Visible";
        document.getElementById('nextBtnLabel').textContent = "Next Slide";
        return;
      }}

      if (currentStep > totalStepsForSlide) currentStep = totalStepsForSlide;

      stepElements.forEach(el => {{
        const order = parseInt(el.getAttribute('data-step-order'), 10);
        if (order <= currentStep) {{
          el.classList.remove('step-hidden');
          el.classList.add('step-active');
        }} else {{
          el.classList.add('step-hidden');
          el.classList.remove('step-active');
        }}
      }});

      const indicator = document.getElementById('stepIndicator');
      const nextLabel = document.getElementById('nextBtnLabel');
      const fsStep = document.getElementById('fsStepBadge');
      const fsNextLabel = document.getElementById('fsNextLabel');

      if (totalStepsForSlide === 0) {{
        indicator.textContent = "Title View";
        nextLabel.textContent = "Next Slide";
      }} else if (currentStep < totalStepsForSlide) {{
        indicator.textContent = `Point ${{currentStep}} / ${{totalStepsForSlide}}`;
        nextLabel.textContent = (currentStep === totalStepsForSlide - 1) ? "Reveal Image" : "Next Point";
      }} else {{
        indicator.textContent = "Slide Complete ✓";
        nextLabel.textContent = "Next Slide";
      }}
      if (fsStep) fsStep.textContent = indicator.textContent;
      if (fsNextLabel) fsNextLabel.textContent = (nextLabel.textContent === 'Next Point') ? 'Next' : nextLabel.textContent;
    }}

        // --- Varied animation styles cycling across slides ---
    const SLIDE_ANIM_STYLES = [
      'anim-fade-scale', 'anim-from-bottom', 'anim-from-right',
      'anim-from-left', 'anim-from-top', 'anim-flip'
    ];

    // Card palette rotation for visual variety across 80 slides
    const CARD_PALETTES = [
      {{ badgeClass: '', cardClass: '' }},
      {{ badgeClass: 'badge-emerald', cardClass: 'card-emerald' }},
      {{ badgeClass: 'badge-purple', cardClass: 'card-purple' }},
      {{ badgeClass: '', cardClass: '' }},
      {{ badgeClass: 'badge-emerald', cardClass: 'card-emerald' }},
      {{ badgeClass: 'badge-purple', cardClass: 'card-purple' }}
    ];

    function getSlideAnimClass(index, direction) {{
      if (direction === 'none') return '';
      const base = SLIDE_ANIM_STYLES[index % SLIDE_ANIM_STYLES.length];
      if (direction === 'backward') {{
        const mirror = {{
          'anim-from-right': 'anim-from-left',
          'anim-from-left': 'anim-from-right',
          'anim-from-bottom': 'anim-from-top',
          'anim-from-top': 'anim-from-bottom'
        }};
        return mirror[base] || base;
      }}
      return base;
    }}

    function makeImagePanelHtml(imgPath, captionTitle, captionBody, colorStyle, isMulti, imgIndex = 0) {{
      if (!imgPath) return '';
      const editOverlay = `
        <div class="image-edit-overlay">
          <button class="img-edit-btn" onclick="editImageReplace(this, '${{imgPath}}', ${{imgIndex}})" title="Replace image">🔄 Replace</button>
          <button class="img-edit-btn" onclick="editImageAdd(this)" title="Add another image">➕ Add</button>
          <button class="img-edit-btn danger" onclick="editImageRemove(this, ${{imgIndex}})" title="Remove image">🗑 Remove</button>
        </div>`;

      return `
        <div class="image-panel${{isMulti ? ' multi-img' : ''}}" style="position:relative; min-height:0;">
          <div class="image-viewport" onclick="handleImgClick(event, '${{imgPath}}', '${{captionTitle}}: ${{captionBody}}')">
            <img src="${{imgPath}}" alt="${{captionTitle}}" onerror="this.style.opacity=0.3">
            <div class="zoom-hint-badge">🔍 Zoom Ultra-Res (300 DPI)</div>
            ${{editOverlay}}
          </div>
          <div class="caption-card">
            <div class="caption-title" style="${{colorStyle}}" contenteditable="false" data-edit-key="caption_title" data-img-idx="${{imgIndex}}">${{captionTitle}}</div>
            <div class="caption-text" contenteditable="false" data-edit-key="caption_body" data-img-idx="${{imgIndex}}">${{captionBody}}</div>
          </div>
        </div>`;
    }}

    function handleImgClick(e, src, caption) {{
      if (document.body.classList.contains('edit-mode-active')) return;
      if (e.target.closest('.image-edit-overlay')) return;
      openLightbox(src, caption);
    }}

    function formatTitle(t) {{
      if (!t) return '';
      return t.split(String.fromCharCode(10)).join('<br>');
    }}

    function formatTitle(t) {{
      if (!t) return '';
      return t.split(String.fromCharCode(10)).join('<br>');
    }}

    function renderSlide(direction = 'forward') {{
      const slide = getEffectiveSlide(currentIndex);
      const box = document.getElementById('slideBox');
      const pos = filteredIndices.indexOf(currentIndex);

      document.getElementById('slideCounter').textContent = `Slide ${{pos + 1}} / ${{filteredIndices.length}}`;
      document.getElementById('btnPrev').disabled = (pos === 0 && currentStep === 0);
      document.getElementById('btnNext').disabled = (pos === filteredIndices.length - 1 && currentStep >= totalStepsForSlide);

      const fsCounter = document.getElementById('fsSlideCounter');
      if (fsCounter) fsCounter.textContent = `Slide ${{pos + 1}} / ${{filteredIndices.length}}`;
      const fsPrev = document.getElementById('fsBtnPrev');
      if (fsPrev) fsPrev.disabled = (pos === 0 && currentStep === 0);
      const fsNext = document.getElementById('fsBtnNext');
      if (fsNext) fsNext.disabled = (pos === filteredIndices.length - 1 && currentStep >= totalStepsForSlide);

      const pct = ((pos + 1) / filteredIndices.length) * 100;
      document.getElementById('progressBar').style.width = pct + '%';

      const animClass = getSlideAnimClass(currentIndex, direction);
      const palette = CARD_PALETTES[currentIndex % CARD_PALETTES.length];

      if (slide.type === 'title') {{
        const creditsHtml = (slide.credits || []).map(c => `<li contenteditable="false">${{c}}</li>`).join('');
        const imgHtml = makeImagePanelHtml(
          slide.img_path,
          '3D VENTRICULAR PROJECTION',
          'High-resolution reconstruction of cerebral ventricular cavities from Youmans & Winn.',
          '',
          false,
          0
        );

        box.innerHTML = `
          <div class="slide-content-container ${{animClass}}">
            <div class="title-slide-container">
              <div class="title-left">
                <div class="slide-category-badge" contenteditable="false" data-edit-key="badge">${{slide.badge}}</div>
                <h1 class="slide-title" contenteditable="false" data-edit-key="title">${{formatTitle(slide.title)}}</h1>
                <p class="slide-subtitle" contenteditable="false" data-edit-key="subtitle">${{slide.subtitle}}</p>
                <div class="credits-box">
                  <div class="credits-heading">REFERENCE TEXT &amp; CURRICULUM</div>
                  <ul class="credits-list">${{creditsHtml}}</ul>
                </div>
              </div>
              ${{imgHtml}}
            </div>
          </div>
        `;
      }} else {{
        const isSummary = (slide.type === 'summary');
        const isThankYou = (slide.type === 'thankyou');
        const cards = slide.cards || [];
        const hasImage = !!slide.img_path;

        let badgeClass = '', cardClass = '', colorStyle = '';
        if (isSummary) {{
          badgeClass = 'badge-emerald'; cardClass = 'card-emerald'; colorStyle = 'color: var(--emerald);';
        }} else if (isThankYou) {{
          badgeClass = 'badge-purple thankyou-badge'; cardClass = 'card-purple'; colorStyle = 'color: var(--purple);';
        }} else {{
          badgeClass = palette.badgeClass; cardClass = palette.cardClass; colorStyle = '';
        }}

        // Commentary cards with step order (reveal step-by-step)
        const cardsHtml = cards.map((c, i) => `
          <div class="lecture-card ${{cardClass}}" data-step-order="${{i + 1}}">
            <div class="card-heading" contenteditable="false" data-card-idx="${{i}}" data-edit-key="card_title">
              <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:currentColor;opacity:0.8;flex-shrink:0;"></span>
              ${{c[0]}}
            </div>
            <div class="card-text" contenteditable="false" data-card-idx="${{i}}" data-edit-key="card_body">${{c[1]}}</div>
          </div>
        `).join('');

        const extra_images = slide.extra_images || [];
        const isMulti = extra_images.length > 0;
        let allImgHtml = '';

        if (hasImage) {{
          allImgHtml += makeImagePanelHtml(slide.img_path, slide.caption_title || '', slide.caption_body || '', colorStyle, isMulti, 0);
        }}
        extra_images.forEach((ei, eidx) => {{
          allImgHtml += makeImagePanelHtml(ei.path, ei.caption_title || 'ADDITIONAL FIGURE', ei.caption_body || '', colorStyle, true, eidx + 1);
        }});

        const addImgBtnHtml = `<div class="img-add-zone" onclick="editImageAddNew(${{currentIndex}})" style="display:none;" id="addImgZone_${{currentIndex}}">➕ Add Image to Slide</div>`;

        if (hasImage || isMulti) {{
          // IMAGE IS THE CENTER OF ATTENTION, DETAILS COME AFTER AS COMMENTS
          box.innerHTML = `
            <div class="slide-content-container ${{animClass}}">
              <div class="slide-header">
                <div class="slide-category-badge ${{badgeClass}}" contenteditable="false" data-edit-key="badge">${{slide.badge}}</div>
                <h2 class="slide-title" contenteditable="false" data-edit-key="title">${{formatTitle(slide.title)}}</h2>
                <p class="slide-subtitle" contenteditable="false" data-edit-key="subtitle">${{slide.subtitle}}</p>
              </div>
              <div class="slide-body-image-centered">
                <div class="slide-image-hero">
                  ${{allImgHtml}}
                  ${{addImgBtnHtml}}
                </div>
                <div class="slide-cards-strip">
                  ${{cardsHtml}}
                </div>
              </div>
            </div>
          `;
        }} else {{
          // NO IMAGE SLIDE: Cards take center stage in clean balanced layout
          box.innerHTML = `
            <div class="slide-content-container ${{animClass}}">
              <div class="slide-header">
                <div class="slide-category-badge ${{badgeClass}}" contenteditable="false" data-edit-key="badge">${{slide.badge}}</div>
                <h2 class="slide-title" contenteditable="false" data-edit-key="title">${{formatTitle(slide.title)}}</h2>
                <p class="slide-subtitle" contenteditable="false" data-edit-key="subtitle">${{slide.subtitle}}</p>
              </div>
              <div class="slide-body-no-image">
                ${{cardsHtml}}
              </div>
              ${{addImgBtnHtml}}
            </div>
          `;
        }}
      }}

      if (document.body.classList.contains('edit-mode-active')) {{
        const addZone = document.getElementById('addImgZone_' + currentIndex);
        if (addZone) addZone.style.display = 'flex';
      }}

      applyEditModeToSlide();
      applyStepVisibility();
    }}
    // Drawer Functions
    let currentDrawerPart = 'all';

    function setDrawerFilter(part, btn) {{
      currentDrawerPart = part;
      document.querySelectorAll('.drawer-pill-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      filterDrawerSlides();
    }}

    function toggleDrawer() {{
      const overlay = document.getElementById('drawerOverlay');
      overlay.classList.toggle('active');
      if (overlay.classList.contains('active')) {{
        renderDrawerGrid();
        document.getElementById('drawerSearch').focus();
      }}
    }}

    function renderDrawerGrid(filterText = '') {{
      const grid = document.getElementById('drawerGrid');
      const query = filterText.toLowerCase();

      grid.innerHTML = SLIDES_DATA.map((s, idx) => {{
        if (currentDrawerPart !== 'all' && String(s.part) !== String(currentDrawerPart)) return '';

        const matches = s.title.toLowerCase().includes(query) || 
                        s.subtitle.toLowerCase().includes(query) ||
                        s.badge.toLowerCase().includes(query) ||
                        (s.caption_body && s.caption_body.toLowerCase().includes(query));
        if (!matches) return '';

        const isActive = (idx === currentIndex);
        const safeTitle = s.title.replace(/"/g, '&quot;').replace(/\\n/g, ' ');
        const subtitleText = s.subtitle || s.badge || '';
        return `
          <div class="drawer-card ${{isActive ? 'active-slide' : ''}}" onclick="jumpToSlide(${{idx}})" title="Slide ${{idx + 1}}: ${{safeTitle}}">
            <div class="drawer-card-thumb">
              <img src="${{s.img_path}}" alt="${{safeTitle}}" loading="lazy">
              <span class="drawer-badge-slide">SLIDE ${{idx + 1}}</span>
              <span class="drawer-badge-part">PART ${{s.part}}</span>
            </div>
            <div class="drawer-card-body">
              <div class="drawer-card-title">${{safeTitle}}</div>
              <div class="drawer-card-sub">${{subtitleText}}</div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function filterDrawerSlides() {{
      const query = document.getElementById('drawerSearch').value;
      renderDrawerGrid(query);
    }}

    function jumpToSlide(idx) {{
      currentIndex = idx;
      currentStep = 0;
      toggleDrawer();
      renderSlide('forward');
    }}

    // ULTRA-CLEAR HIGH-POWER LIGHTBOX ZOOM IMPLEMENTATION
    let zoomScale = 1;
    let panX = 0;
    let panY = 0;
    let isDragging = false;
    let startMouseX = 0;
    let startMouseY = 0;

        // Touch Pinch-to-Zoom & Pan Support for Touchscreens
    let touchStartDist = 0;
    let touchStartScale = 1;
    let touchPanStartX = 0;
    let touchPanStartY = 0;

    function initLightboxTouch() {{
      const vp = document.getElementById('lightboxViewport');
      if (!vp) return;

      vp.addEventListener('touchstart', (e) => {{
        if (e.touches.length === 2) {{
          touchStartDist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
          touchStartScale = zoomScale;
        }} else if (e.touches.length === 1) {{
          touchPanStartX = e.touches[0].clientX - panX;
          touchPanStartY = e.touches[0].clientY - panY;
        }}
      }}, {{ passive: false }});

      vp.addEventListener('touchmove', (e) => {{
        if (e.touches.length === 2 && touchStartDist > 0) {{
          e.preventDefault();
          const dist = Math.hypot(
            e.touches[0].clientX - e.touches[1].clientX,
            e.touches[0].clientY - e.touches[1].clientY
          );
          const factor = dist / touchStartDist;
          zoomScale = Math.max(0.6, Math.min(5, touchStartScale * factor));
          updateTransform();
        }} else if (e.touches.length === 1 && zoomScale > 1) {{
          e.preventDefault();
          panX = e.touches[0].clientX - touchPanStartX;
          panY = e.touches[0].clientY - touchPanStartY;
          updateTransform();
        }}
      }}, {{ passive: false }});

      vp.addEventListener('touchend', () => {{
        touchStartDist = 0;
      }});
    }}

    function openLightbox(src, caption) {{
      initLightboxTouch();
      const modal = document.getElementById('lightboxModal');
      document.getElementById('lightboxImg').src = src;
      document.getElementById('lightboxCap').textContent = caption;
      resetZoom();
      modal.classList.add('active');
    }}

    function toggleLightbox() {{
      const modal = document.getElementById('lightboxModal');
      modal.classList.remove('active');
      resetZoom();
    }}

    function updateTransform() {{
      const wrapper = document.getElementById('lightboxWrapper');
      wrapper.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{zoomScale}})`;
      document.getElementById('zoomLevelBadge').textContent = `Zoom: ${{Math.round(zoomScale * 100)}}%`;
    }}

    function adjustZoom(delta) {{
      zoomScale = Math.max(0.6, Math.min(5, zoomScale + delta));
      updateTransform();
    }}

    function setZoomLevel(level) {{
      zoomScale = level;
      panX = 0;
      panY = 0;
      updateTransform();
    }}

    function resetZoom() {{
      zoomScale = 1;
      panX = 0;
      panY = 0;
      updateTransform();
    }}

    function handleWheelZoom(e) {{
      e.preventDefault();
      const delta = e.deltaY > 0 ? -0.2 : 0.2;
      adjustZoom(delta);
    }}

    function startDrag(e) {{
      if (e.target.tagName === 'BUTTON') return;
      isDragging = true;
      startMouseX = e.clientX - panX;
      startMouseY = e.clientY - panY;
      const vp = document.getElementById('lightboxViewport');
      vp.classList.add('is-dragging');

      window.addEventListener('mousemove', onDragMove);
      window.addEventListener('mouseup', onDragEnd);
    }}

    function onDragMove(e) {{
      if (!isDragging) return;
      panX = e.clientX - startMouseX;
      panY = e.clientY - startMouseY;
      updateTransform();
    }}

    function onDragEnd() {{
      isDragging = false;
      const vp = document.getElementById('lightboxViewport');
      vp.classList.remove('is-dragging');
      window.removeEventListener('mousemove', onDragMove);
      window.removeEventListener('mouseup', onDragEnd);
    }}

    function toggleTheme() {{
      const current = document.body.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.body.setAttribute('data-theme', next);
    }}

    function toggleFullscreen() {{
      const isCurrentlyFs = !!(document.fullscreenElement || document.webkitFullscreenElement || document.body.classList.contains('is-fullscreen-forced'));
      if (!isCurrentlyFs) {{
        const el = document.documentElement;
        if (el.requestFullscreen) {{
          el.requestFullscreen().catch(err => {{
            console.warn('Native requestFullscreen blocked, using CSS hall fullscreen:', err);
            document.body.classList.add('is-fullscreen-forced');
            updateFullscreenState();
          }});
        }} else if (el.webkitRequestFullscreen) {{
          el.webkitRequestFullscreen();
        }} else {{
          document.body.classList.add('is-fullscreen-forced');
          updateFullscreenState();
        }}
      }} else {{
        document.body.classList.remove('is-fullscreen-forced');
        if (document.exitFullscreen && document.fullscreenElement) {{
          document.exitFullscreen().catch(err => console.log(err));
        }} else if (document.webkitExitFullscreen && document.webkitFullscreenElement) {{
          document.webkitExitFullscreen();
        }}
        updateFullscreenState();
      }}
    }}

    function updateFullscreenState() {{
      const isFs = !!(document.fullscreenElement || document.webkitFullscreenElement || document.body.classList.contains('is-fullscreen-forced'));
      document.body.classList.toggle('is-fullscreen', isFs);
      const hud = document.getElementById('fullscreenHud');
      if (hud) {{
        hud.classList.remove('hud-hidden');
        if (isFs) resetHudTimer();
      }}
    }}

    document.addEventListener('fullscreenchange', updateFullscreenState);
    document.addEventListener('webkitfullscreenchange', updateFullscreenState);

    let hudHideTimeout = null;
    function resetHudTimer() {{
      const hud = document.getElementById('fullscreenHud');
      if (!hud) return;
      hud.classList.remove('hud-hidden');
      clearTimeout(hudHideTimeout);
      if (document.body.classList.contains('is-fullscreen') || document.fullscreenElement) {{
        hudHideTimeout = setTimeout(() => {{
          hud.classList.add('hud-hidden');
        }}, 2500);
      }}
    }}
    window.addEventListener('mousemove', resetHudTimer);
    window.addEventListener('touchstart', resetHudTimer);

    // ==========================================================================
    // 10 HIGH-YIELD NEUROSURGICAL BOARD EXAMINATION QUESTIONS
    // ==========================================================================
    const QUIZ_QUESTIONS = [
      {{
        q: "What anatomical landmark reliably identifies the posterior margin of the foramen of Monro?",
        options: [
          "The stria terminalis crossing the pulvinar",
          "The venous angle formed by anterior septal and thalamostriate veins",
          "The anterior choroidal artery entry point",
          "The massa intermedia of the thalamus"
        ],
        answer: 1,
        explanation: "In normal anatomy, the venous angle (junction of anterior septal and thalamostriate veins) lies within 5.5 mm of the posterior margin of the foramen of Monro and safeguards the internal cerebral veins."
      }},
      {{
        q: "Which specific roof layer of the third ventricle harbors the paired internal cerebral veins (ICVs)?",
        options: [
          "Layer 1: Midline raphe of the forniceal bodies",
          "Layer 2: Superior leaf of the tela choroidea",
          "Layer 3: Velum interpositum space",
          "Layer 5: Inferior choroid plexus ribbons"
        ],
        answer: 2,
        explanation: "The velum interpositum (Layer 3) is a vascular space enclosed between the superior and inferior pial leaves of the tela choroidea, containing the ICVs and medial posterior choroidal arteries."
      }},
      {{
        q: "In the transchoroidal approach (Wen technique) to the third ventricle, where is the micro-incision placed?",
        options: [
          "Directly through the anterior forniceal column",
          "Along the tenia fornicis (medial attachment of choroid plexus to fornix)",
          "Transcortically through the superior parietal lobule",
          "Across the rostrum of the corpus callosum"
        ],
        answer: 1,
        explanation: "The transchoroidal approach enters via the tenia fornicis, sweeping the choroid plexus laterally and avoiding direct traction or trauma to the forniceal columns, preventing severe amnesia."
      }},
      {{
        q: "Why is the telovelar approach preferred over the traditional transvermian approach for fourth ventricular tumors?",
        options: [
          "It completely avoids splitting the inferior cerebellar vermis, preventing post-operative cerebellar mutism syndrome",
          "It does not require opening the cisterna magna",
          "It permits routine sacrifice of the PICA artery",
          "It enables supratentorial visualization of the splenium"
        ],
        answer: 0,
        explanation: "The telovelar approach mobilizes cerebellar tonsils and incises the inferior medullary velum and tela choroidea, fully sparing the vermian nodule and dentate pathways, eliminating postoperative cerebellar mutism."
      }},
      {{
        q: "Which cranial nerve nucleus prominence on the rhomboid fossa floor must NEVER be manipulated or coagulated?",
        options: [
          "Facial colliculus (facial motor genu wrapping around abducens CN VI nucleus)",
          "Hypoglossal trigone",
          "Vagal trigone",
          "Area postrema"
        ],
        answer: 0,
        explanation: "The facial colliculus in the lower pontine floor contains CN VII motor fibers looping over the CN VI nucleus. Direct manipulation causes irreversible abducens palsy and facial diplegia."
      }},
      {{
        q: "Which pathognomonic histological hallmark is characteristic of ependymoma (WHO Grade II/III)?",
        options: [
          "Rosenthal fibers and eosinophilic granular bodies",
          "Perivascular pseudorosettes with radiating anuclear fibrillary cuffs",
          "Psammoma bodies with concentric syncytial whorls",
          "Perinuclear clear halos producing a 'fried-egg' appearance"
        ],
        answer: 1,
        explanation: "Perivascular pseudorosettes (tumor cell processes radiating toward central capillaries, leaving an anuclear fibrillary cuff) represent the diagnostic hallmark of ependymomas."
      }},
      {{
        q: "In posterior fossa ependymoma molecular stratification, which group carries a poor prognosis and loss of H3K27me3?",
        options: [
          "Posterior Fossa Group A (PF-EPN-A)",
          "Posterior Fossa Group B (PF-EPN-B)",
          "Supratentorial YAP1 fusion",
          "Subependymoma (WHO Grade I)"
        ],
        answer: 0,
        explanation: "PF-EPN-A ependymomas occur predominantly in infants/young children, display global loss of H3K27me3 histone trimethylation, and carry high recurrence and dissemination rates."
      }},
      {{
        q: "Central neurocytoma (WHO Grade II) is strongly differentiated from oligodendroglioma by which marker?",
        options: [
          "IDH1 R132H mutation positivity",
          "Diffusely and strongly positive for Synaptophysin and NeuN",
          "GFAP strong diffuse cytoplasmic reactivity in all tumor cells",
          "Cytokeratin AE1/AE3 positivity"
        ],
        answer: 1,
        explanation: "Central neurocytoma cells are uniform round cells that mimic oligodendroglioma ('fried egg'), but are strongly and diffusely positive for neuronal markers Synaptophysin and NeuN."
      }},
      {{
        q: "On magnetic resonance imaging, which sequence definitively differentiates an epidermoid cyst from an arachnoid cyst?",
        options: [
          "T1-weighted post-gadolinium enhancement",
          "T2-weighted spin-echo sequence",
          "Diffusion-Weighted Imaging (DWI) showing marked restricted diffusion",
          "Magnetic resonance angiography (MRA) arterial phase"
        ],
        answer: 2,
        explanation: "Epidermoid cysts show marked hyperintensity on DWI with low ADC values (restricted diffusion due to dense keratin flakes), whereas arachnoid cysts follow free CSF signal and do not restrict."
      }},
      {{
        q: "Which segment of the PICA artery courses along the inferior medullary velum into the fourth ventricle roof?",
        options: [
          "Anterior medullary segment",
          "Lateral medullary segment",
          "Tonsillomedullary segment",
          "Telovelomedullary segment (giving rise to the supratonsillar loop)"
        ],
        answer: 3,
        explanation: "The telovelomedullary segment of PICA ascends along the tela choroidea and inferior medullary velum, creating the supratonsillar loop before branching into the vermian and hemispheric cortical arteries."
      }}
    ];

    // ==========================================================================
    // INTERACTIVE LIVE AUDIENCE QUIZ ENGINE (HOST BACKBONE)
    // ==========================================================================
    const QUIZ_STORAGE_KEY = 'ventricular_tumors_quiz_results_v2';
    const ROOM_ID = 'VENTRICLE';
    const MQTT_FALLBACKS = [
      'wss://test.mosquitto.org:8081',
      'wss://broker.hivemq.com:8884/mqtt',
      'wss://broker.emqx.io:8084/mqtt'
    ];
    let currentBrokerIdx = 0;
    const MQTT_BROKER = MQTT_FALLBACKS[0];
    const TOPIC = `neurosurg/ventricular-quiz/${{ROOM_ID}}`;

    let quizArenaMode = 'live'; // 'live' or 'solo'
    let hostState = 'LOBBY'; // 'LOBBY', 'LOCKED', 'QUESTION', 'REVEAL', 'PODIUM'
    let currentQIdx = 0;
    let questionTimerVal = 60;
    let questionTimerInterval = null;
    let revealTimerVal = 5;
    let revealTimerInterval = null;
    let isRevealTimerPaused = false;

    // Registered Participants: {{ id: {{ name, avatar, score: 0, answers: {{}}, isBot: false }} }}
    let participants = {{}};
    let botSimulationTimers = [];

    let hostMqttClient = null;
    let hostBroadcastChannel = null;

    // Solo Mode State
    let soloAnswers = {{}};
    let soloScore = 0;

    function getPlayerUrl() {{
      if (window.location.protocol === 'file:') {{
        return 'https://mhub96.github.io/Lectures/quiz_player.html?room=' + ROOM_ID;
      }}
      const loc = window.location;
      let base = loc.href.split('?')[0].split('#')[0];
      if (base.endsWith('/index.html') || base.endsWith('/interactive_lecture.html')) {{
        base = base.replace(/\\/index\\.html$/, '/quiz_player.html').replace(/\\/interactive_lecture\\.html$/, '/quiz_player.html');
      }} else if (base.endsWith('/')) {{
        base += 'quiz_player.html';
      }} else if (!base.endsWith('.html')) {{
        base += '/quiz_player.html';
      }} else {{
        base = base.substring(0, base.lastIndexOf('/') + 1) + 'quiz_player.html';
      }}
      return base + '?room=' + ROOM_ID;
    }}

    function initHostSync() {{
      // 1. BroadcastChannel API for 0ms local tabs
      try {{
        if (window.BroadcastChannel) {{
          hostBroadcastChannel = new BroadcastChannel(`ventricular_quiz_${{ROOM_ID}}`);
          hostBroadcastChannel.onmessage = (e) => {{
            handleHostIncomingMessage(e.data);
          }};
        }}
      }} catch(err) {{
        console.log('BroadcastChannel not supported:', err);
      }}

      // 2. LocalStorage storage event fallback
      window.addEventListener('storage', (e) => {{
        if (e.key === `vq_msg_to_host_${{ROOM_ID}}` && e.newValue) {{
          try {{ handleHostIncomingMessage(JSON.parse(e.newValue)); }} catch(err){{}}
        }}
      }});

      // 3. Resilient MQTT connection with broker failover
      connectHostMqtt();
    }}

    function connectHostMqtt() {{
      const brokerUrl = MQTT_FALLBACKS[currentBrokerIdx];
      try {{
        const hostId = `vqh_${{Math.random().toString(16).substring(2, 8)}}`;
        hostMqttClient = mqtt.connect(brokerUrl, {{
          clientId: hostId,
          clean: true,
          connectTimeout: 6000,
          reconnectPeriod: 3000
        }});

        hostMqttClient.on('connect', () => {{
          updateArenaConnectionStatus(true, 'Broker Online');
          hostMqttClient.subscribe(TOPIC, {{ qos: 1 }});
          broadcastHostSync();
        }});

        hostMqttClient.on('message', (topic, message) => {{
          try {{
            const data = JSON.parse(message.toString());
            handleHostIncomingMessage(data);
          }} catch(e){{}}
        }});

        hostMqttClient.on('offline', () => {{
          updateArenaConnectionStatus(false, 'Broker Reconnecting');
        }});

        hostMqttClient.on('error', (err) => {{
          console.warn(`Host broker ${{brokerUrl}} error:`, err);
          if (!hostMqttClient.connected && currentBrokerIdx < MQTT_FALLBACKS.length - 1) {{
            currentBrokerIdx++;
            try {{ hostMqttClient.end(true); }} catch(e){{}}
            setTimeout(connectHostMqtt, 1000);
          }}
        }});
      }} catch(err) {{
        console.warn('Host MQTT init error:', err);
      }}
    }}

    function updateArenaConnectionStatus(online, label) {{
      const dot = document.getElementById('arenaConnDot');
      const text = document.getElementById('arenaConnLabel');
      if (dot && text) {{
        dot.style.background = online ? 'var(--emerald)' : 'var(--rose)';
        text.textContent = label;
      }}
    }}

    function broadcastToPlayers(payload) {{
      const msg = {{ ...payload, sender: 'HOST', timestamp: Date.now() }};
      if (hostBroadcastChannel) {{
        try {{ hostBroadcastChannel.postMessage(msg); }} catch(e){{}}
      }}
      try {{
        localStorage.setItem(`vq_msg_to_player_${{ROOM_ID}}`, JSON.stringify(msg));
      }} catch(e){{}}
      if (hostMqttClient && hostMqttClient.connected) {{
        try {{
          hostMqttClient.publish(TOPIC, JSON.stringify(msg));
        }} catch(e){{}}
      }}
    }}

    function broadcastHostSync() {{
      const ranks = calculateRanks();
      broadcastToPlayers({{
        type: 'HOST_SYNC',
        state: hostState,
        questionIndex: currentQIdx,
        totalQuestions: getActiveQuestions().length,
        timeRemaining: questionTimerVal,
        correctAnswer: (hostState === 'REVEAL' || hostState === 'PODIUM') ? getShuffledQuestion(currentQIdx).answer : null,
        ranks: ranks,
        participantCount: Object.keys(participants).length
      }});
    }}

    function handleHostIncomingMessage(msg) {{
      if (!msg || !msg.type || msg.sender === 'HOST') return;

      // ATTENDEE WITHDRAWAL / LOGOUT BEFORE EXAM
      if (msg.type === 'PLAYER_LEAVE') {{
        if (participants[msg.playerId]) {{
          delete participants[msg.playerId];
          if (document.getElementById('quizOverlay').classList.contains('active') && hostState === 'LOBBY') {{
            renderLobbyScreen();
          }}
          broadcastHostSync();
        }}
        return;
      }}

      // ATTENDEE WITHDRAWAL AFTER EXAM START
      if (msg.type === 'PLAYER_WITHDRAW') {{
        if (participants[msg.playerId]) {{
          participants[msg.playerId].withdrawn = true;
          updateRespondentBar();
          if (haveAllParticipantsAnswered()) {{
            revealQuestionResult();
          }}
        }}
        return;
      }}

      if (msg.type === 'PLAYER_JOIN_REQUEST' || (msg.type === 'PLAYER_PING' && hostState === 'LOBBY')) {{
        // REGISTRATION LOCK CHECK:
        if (hostState !== 'LOBBY' && !participants[msg.playerId]) {{
          broadcastToPlayers({{
            type: 'HOST_PLAYER_REJECTED',
            targetPlayerId: msg.playerId,
            reason: 'REGISTRATION_LOCKED'
          }});
          return;
        }}

        // Accept user or update name
        let updated = false;
        if (!participants[msg.playerId]) {{
          participants[msg.playerId] = {{
            id: msg.playerId,
            name: msg.name || 'Anonymous Surgeon',
            avatar: msg.avatar || '🧠',
            score: 0,
            answers: {{}},
            isBot: false
          }};
          updated = true;
        }} else if (msg.name && participants[msg.playerId].name !== msg.name) {{
          participants[msg.playerId].name = msg.name;
          updated = true;
        }}

        if (updated && document.getElementById('quizOverlay').classList.contains('active') && hostState === 'LOBBY') {{
          renderLobbyScreen();
        }}

        // ALWAYS acknowledge join requests so player knows they are registered!
        broadcastToPlayers({{
          type: 'HOST_PLAYER_ACCEPTED',
          targetPlayerId: msg.playerId
        }});
        broadcastHostSync();
      }} else if (msg.type === 'PLAYER_PING') {{
        if (participants[msg.playerId]) {{
          broadcastHostSync();
        }}
      }} else if (msg.type === 'PLAYER_SUBMIT_ANSWER') {{
        if (hostState !== 'QUESTION') return;
        if (msg.questionIndex === currentQIdx && participants[msg.playerId]) {{
          participants[msg.playerId].answers[currentQIdx] = {{
            choice: msg.choice,
            timeRemaining: msg.timeRemaining || 0
          }};

          updateRespondentBar();

          // Check if all registered participants have answered!
          if (haveAllParticipantsAnswered()) {{
            revealQuestionResult();
          }}
        }}
      }}
    }}

    function haveAllParticipantsAnswered() {{
      const list = Object.values(participants).filter(p => !p.withdrawn);
      if (list.length === 0) return false;
      return list.every(p => p.answers[currentQIdx] !== undefined);
    }}

    function getSubmittedCount() {{
      return Object.values(participants).filter(p => !p.withdrawn && p.answers[currentQIdx] !== undefined).length;
    }}

    function updateRespondentBar() {{
      const count = getSubmittedCount();
      const activeList = Object.values(participants).filter(p => !p.withdrawn);
      const total = activeList.length;
      const pct = total > 0 ? (count / total) * 100 : 0;
      
      const countEl = document.getElementById('arenaRespCount');
      const barEl = document.getElementById('arenaRespBar');
      if (countEl) countEl.textContent = `${{count}} / ${{total}} Answered`;
      if (barEl) barEl.style.width = `${{pct}}%`;
    }}

    function adminExitQuiz() {{
      const isRunning = (hostState === 'QUESTION' || hostState === 'REVEAL');
      const confirmMsg = isRunning
        ? 'Are you sure you want to STOP the exam? All attendee devices will receive their results and be exited.'
        : 'Are you sure you want to exit the live quiz session?';

      if (!confirm(confirmMsg)) return;

      // 1. Broadcast QUIZ_ENDED to all attendee devices
      const ranks = calculateRanks();
      broadcastToPlayers({{
        type: 'HOST_QUIZ_ENDED',
        ranks: ranks,
        questionIndex: currentQIdx,
        totalQuestions: getActiveQuestions().length,
        reason: 'ADMIN_STOPPED'
      }});

      // 2. Clear all timers
      clearInterval(questionTimerInterval);
      clearInterval(revealTimerInterval);
      clearBotTimers();

      // 3. Reset host state back to LOBBY
      hostState = 'LOBBY';
      participants = {{}};

      // 4. Close quiz overlay
      toggleQuiz();
    }}

    function calculateRanks() {{
      const list = Object.values(participants);
      list.sort((a, b) => b.score - a.score);
      const ranks = {{}};
      list.forEach((p, idx) => {{
        ranks[p.id] = {{ score: p.score, rank: idx + 1, name: p.name, avatar: p.avatar }};
      }});
      return ranks;
    }}

    function toggleQuiz() {{
      const overlay = document.getElementById('quizOverlay');
      overlay.classList.toggle('active');
      if (overlay.classList.contains('active')) {{
        if (!hostMqttClient && !hostBroadcastChannel) {{
          initHostSync();
        }}
        renderCurrentArenaScreen();
      }}
    }}

    function setQuizArenaMode(mode) {{
      quizArenaMode = mode;
      document.getElementById('btnModeLive').classList.toggle('active', mode === 'live');
      document.getElementById('btnModeSolo').classList.toggle('active', mode === 'solo');
      renderCurrentArenaScreen();
    }}

    function renderCurrentArenaScreen() {{
      if (quizArenaMode === 'solo') {{
        renderSoloScreen();
        return;
      }}

      if (hostState === 'LOBBY') {{
        renderLobbyScreen();
      }} else if (hostState === 'QUESTION') {{
        renderQuestionScreen();
      }} else if (hostState === 'REVEAL') {{
        renderRevealScreen();
      }} else if (hostState === 'PODIUM') {{
        renderPodiumScreen();
      }}
    }}

    // -------------------------------------------------------------
    // LOBBY RENDERING & SIMULATION BOT LOGIC
    // -------------------------------------------------------------
    function renderLobbyScreen() {{
      const body = document.getElementById('quizArenaBody');
      const playerUrl = getPlayerUrl();
      const pList = Object.values(participants);

      body.innerHTML = `
        <div class="lobby-grid">
          <div class="qr-card-container">
            <div class="qr-box" id="arenaQrCode">
              <!-- QR Code Render Target -->
            </div>
            <div class="qr-instruction-title">Scan on Mobile to Join</div>
            <div class="qr-instruction-desc">
              Point your smartphone camera at the QR code to open your audience controller. No apps or sign-ups required.
            </div>
            <div class="join-link-box" id="playerUrlDisplay">${{playerUrl}}</div>
            <div class="lobby-action-row">
              <button class="btn-secondary-sm" onclick="copyPlayerUrl()">📋 Copy Link</button>
              <button class="btn-secondary-sm" onclick="openPlayerTab()">📱 Open Player Tab</button>
            </div>
          </div>

          <div class="participants-column">
            <div class="roster-header">
              <div>
                <div style="font-size: 0.8rem; font-weight: 800; color: var(--text-muted); text-transform: uppercase;">LOBBY REGISTRATION</div>
                <div style="font-size: 1.25rem; font-weight: 800; color: var(--text-main);">Audience Roster</div>
              </div>
              <div class="roster-count-badge" id="rosterCounter">${{pList.length}} Registered</div>
            </div>

            <div class="participants-grid" id="rosterGrid">
              ${{pList.length === 0 ? `
                <div class="empty-roster-msg">
                  <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">📱</div>
                  <div style="font-weight: 700; font-size: 1.05rem;">Waiting for attendees to scan & join...</div>
                  <div style="font-size: 0.85rem; margin-top: 0.35rem; color: var(--text-dim);">
                    Participants will appear here in real time as they enter their names.
                  </div>
                </div>
              ` : pList.map(p => `
                <div class="participant-chip">
                  <span class="chip-avatar">${{p.avatar}}</span>
                  <span class="chip-name">${{p.name}}</span>
                </div>
              `).join('')}}
            </div>

            <div class="lobby-controls-strip">
              <button class="btn-start-arena" id="btnStartArena" onclick="startLiveQuiz()" ${{pList.length === 0 ? '' : ''}}>
                <span>▶ START QUIZ (Lock Registration)</span>
              </button>
              <button class="btn-sim-bots" onclick="simulateAttendees()">
                <span>🤖 Simulate 5 Attendees</span>
              </button>
            </div>
          </div>
        </div>
      `;

      // Render crisp QR code using local qrcode.min.js
      setTimeout(() => {{
        const qrEl = document.getElementById('arenaQrCode');
        if (qrEl) {{
          qrEl.innerHTML = '';
          try {{
            if (typeof QRCode !== 'undefined') {{
              new QRCode(qrEl, {{
                text: playerUrl,
                width: 190,
                height: 190,
                colorDark: '#0b1120',
                colorLight: '#ffffff',
                correctLevel: QRCode.CorrectLevel.M
              }});
            }} else {{
              // Fallback image tag
              qrEl.innerHTML = `<img src="https://api.qrserver.com/v1/create-qr-code/?size=190x190&data=${{encodeURIComponent(playerUrl)}}" alt="QR Code">`;
            }}
          }} catch(e) {{
            qrEl.innerHTML = `<img src="https://api.qrserver.com/v1/create-qr-code/?size=190x190&data=${{encodeURIComponent(playerUrl)}}" alt="QR Code">`;
          }}
        }}
      }}, 50);
    }}

    function copyPlayerUrl() {{
      const url = getPlayerUrl();
      navigator.clipboard.writeText(url).then(() => {{
        alert('Player URL copied to clipboard: ' + url);
      }}).catch(() => {{
        prompt('Copy Player URL:', url);
      }});
    }}

    function openPlayerTab() {{
      window.open(getPlayerUrl(), '_blank');
    }}

    // Simulate Attendees Helper
    function simulateAttendees() {{
      const bots = [
        {{ name: 'Dr. Harvey Cushing', avatar: '🎩', accuracy: 0.95 }},
        {{ name: 'Dr. Walter Dandy', avatar: '🔬', accuracy: 0.90 }},
        {{ name: 'Dr. Gazi Yasargil', avatar: '👁️', accuracy: 0.92 }},
        {{ name: 'Dr. Albert Rhoton', avatar: '🧠', accuracy: 0.98 }},
        {{ name: 'Dr. Hung Tzeng Wen', avatar: '⚡', accuracy: 0.88 }}
      ];

      bots.forEach((b, i) => {{
        const botId = `bot_${{i + 1}}`;
        participants[botId] = {{
          id: botId,
          name: b.name,
          avatar: b.avatar,
          score: 0,
          answers: {{}},
          accuracy: b.accuracy,
          isBot: true
        }};
      }});

      broadcastHostSync();
      renderLobbyScreen();
    }}

    function startLiveQuiz() {{
      buildShuffledQuestions();
      // If 0 participants, automatically add simulation attendees for immediate smooth presentation
      if (Object.keys(participants).length === 0) {{
        simulateAttendees();
      }}

      // LOCK REGISTRATION
      hostState = 'QUESTION';
      currentQIdx = 0;
      startQuestionRound(0);
    }}

    // -------------------------------------------------------------
    // QUESTION ROUND LOGIC (60s Timer + Auto-Reveal)
    // -------------------------------------------------------------
    function startQuestionRound(qIdx) {{
      hostState = 'QUESTION';
      currentQIdx = qIdx;
      questionTimerVal = 60;
      clearInterval(questionTimerInterval);
      clearInterval(revealTimerInterval);
      clearBotTimers();

      renderQuestionScreen();
      broadcastHostSync();

      // Schedule simulated bot answers with realistic randomized delays (2s to 12s)
      scheduleBotAnswers(qIdx);

      questionTimerInterval = setInterval(() => {{
        questionTimerVal--;
        updateQuestionTimerUI();

        if (questionTimerVal <= 0) {{
          clearInterval(questionTimerInterval);
          revealQuestionResult();
        }}
      }}, 1000);
    }}

    function scheduleBotAnswers(qIdx) {{
      const correctAns = getShuffledQuestion(qIdx).answer;
      Object.values(participants).forEach(p => {{
        if (p.isBot) {{
          // Bot randomized answer delay
          const delayMs = Math.floor(Math.random() * 8000) + 2000;
          const timerId = setTimeout(() => {{
            if (hostState === 'QUESTION' && currentQIdx === qIdx) {{
              const isCorrect = Math.random() < (p.accuracy || 0.9);
              let choice = correctAns;
              if (!isCorrect) {{
                const wrongs = [0, 1, 2, 3].filter(c => c !== correctAns);
                choice = wrongs[Math.floor(Math.random() * wrongs.length)];
              }}
              p.answers[qIdx] = {{
                choice: choice,
                timeRemaining: questionTimerVal
              }};
              updateRespondentBar();
              if (haveAllParticipantsAnswered()) {{
                revealQuestionResult();
              }}
            }}
          }}, delayMs);
          botSimulationTimers.push(timerId);
        }}
      }});
    }}

    function clearBotTimers() {{
      botSimulationTimers.forEach(id => clearTimeout(id));
      botSimulationTimers = [];
    }}

    function updateQuestionTimerUI() {{
      const timerEl = document.getElementById('arenaQuestionTimer');
      if (timerEl) {{
        timerEl.textContent = `⏱ ${{questionTimerVal}}s`;
        if (questionTimerVal <= 10) {{
          timerEl.classList.add('urgent');
        }} else {{
          timerEl.classList.remove('urgent');
        }}
      }}
    }}

    function renderQuestionScreen() {{
      const body = document.getElementById('quizArenaBody');
      const item = getShuffledQuestion(currentQIdx);
      const count = getSubmittedCount();
      const total = Object.keys(participants).length;
      const pct = total > 0 ? (count / total) * 100 : 0;
      const letters = ['A', 'B', 'C', 'D'];

      body.innerHTML = `
        <div class="arena-status-bar">
          <div class="arena-q-index">Question ${{currentQIdx + 1}} of ${{QUIZ_QUESTIONS.length}}</div>
          <div class="arena-timer-pill ${{questionTimerVal <= 10 ? 'urgent' : ''}}" id="arenaQuestionTimer">
            ⏱ ${{questionTimerVal}}s
          </div>
          <div class="respondent-tracker">
            <div class="resp-bar-wrap">
              <div class="resp-bar-fill" id="arenaRespBar" style="width: ${{pct}}%;"></div>
            </div>
            <div class="resp-text" id="arenaRespCount">${{count}} / ${{total}} Answered</div>
          </div>
          <button class="btn-secondary-sm" onclick="revealQuestionResult()" style="flex: none; padding: 6px 14px; font-weight: 800;">
            Reveal Answers Now ⏭
          </button>
          <button class="btn-exit-quiz" onclick="adminExitQuiz()" style="flex: none;" title="Stop Quiz for All Attendees">
            🛑 Exit Quiz
          </button>
        </div>

        <div class="arena-question-card">
          <div class="arena-question-prompt">
            ${{currentQIdx + 1}}. ${{item.q}}
          </div>

          <div class="arena-options-container">
            ${{item.options.map((opt, oIdx) => `
              <div class="arena-option-card">
                <div class="arena-opt-top">
                  <div class="arena-opt-letter let-${{letters[oIdx].toLowerCase()}}">${{letters[oIdx]}}</div>
                  <div class="arena-opt-text">${{opt}}</div>
                </div>
              </div>
            `).join('')}}
          </div>
        </div>
      `;
    }}

    // -------------------------------------------------------------
    // REVEAL LOGIC (5s Countdown with Pause/Resume)
    // -------------------------------------------------------------
    function revealQuestionResult() {{
      clearInterval(questionTimerInterval);
      clearBotTimers();
      hostState = 'REVEAL';

      // Grade participants and calculate scores
      const correctAns = getShuffledQuestion(currentQIdx).answer;
      Object.values(participants).forEach(p => {{
        const resp = p.answers[currentQIdx];
        if (resp && resp.choice === correctAns) {{
          // 100 points base + time bonus up to 20 pts
          const speedBonus = Math.round((resp.timeRemaining / 60) * 20);
          p.score += (100 + speedBonus);
        }}
      }});

      // Count votes per choice
      const voteCounts = [0, 0, 0, 0];
      Object.values(participants).forEach(p => {{
        const resp = p.answers[currentQIdx];
        if (resp && resp.choice !== undefined) {{
          voteCounts[resp.choice]++;
        }}
      }});

      renderRevealScreen(voteCounts);
      broadcastHostSync();

      // Start 5-second countdown to next question
      revealTimerVal = 5;
      isRevealTimerPaused = false;
      clearInterval(revealTimerInterval);

      revealTimerInterval = setInterval(() => {{
        if (!isRevealTimerPaused) {{
          revealTimerVal--;
          updateRevealTimerUI();
          if (revealTimerVal <= 0) {{
            clearInterval(revealTimerInterval);
            advanceToNextQuestion();
          }}
        }}
      }}, 1000);
    }}

    function togglePauseRevealTimer() {{
      isRevealTimerPaused = !isRevealTimerPaused;
      const btn = document.getElementById('btnPauseReveal');
      if (btn) {{
        btn.textContent = isRevealTimerPaused ? '▶ Resume Countdown' : '⏸ Pause Countdown';
      }}
    }}

    function updateRevealTimerUI() {{
      const el = document.getElementById('revealTimerCount');
      if (el) {{
        el.textContent = `${{revealTimerVal}}s`;
      }}
    }}

    function advanceToNextQuestion() {{
      clearInterval(revealTimerInterval);
      if (currentQIdx < getActiveQuestions().length - 1) {{
        startQuestionRound(currentQIdx + 1);
      }} else {{
        showGrandPodium();
      }}
    }}

    function renderRevealScreen(voteCounts) {{
      const body = document.getElementById('quizArenaBody');
      const item = getShuffledQuestion(currentQIdx);
      const letters = ['A', 'B', 'C', 'D'];
      const totalVotes = Object.values(participants).length;

      // If voteCounts not passed, calculate from state
      if (!voteCounts) {{
        voteCounts = [0, 0, 0, 0];
        Object.values(participants).forEach(p => {{
          const resp = p.answers[currentQIdx];
          if (resp && resp.choice !== undefined) {{
            voteCounts[resp.choice]++;
          }}
        }});
      }}

      body.innerHTML = `
        <div class="arena-status-bar">
          <div class="arena-q-index">Question ${{currentQIdx + 1}} Results</div>
          <div class="countdown-pill">
            <span>Next Question in: <strong id="revealTimerCount">${{revealTimerVal}}s</strong></span>
          </div>
          <div class="reveal-actions">
            <button class="btn-secondary-sm" id="btnPauseReveal" onclick="togglePauseRevealTimer()">
              ${{isRevealTimerPaused ? '▶ Resume Countdown' : '⏸ Pause Countdown'}}
            </button>
            <button class="btn-nav primary" onclick="advanceToNextQuestion()" style="padding: 6px 14px;">
              ${{currentQIdx < QUIZ_QUESTIONS.length - 1 ? 'Next Question ⏭' : 'View Final Podium 🏆'}}
            </button>
            <button class="btn-exit-quiz" onclick="adminExitQuiz()" style="margin-left: 6px;" title="Stop Quiz for All Attendees">
              🛑 Exit Quiz
            </button>
          </div>
        </div>

        <div class="arena-question-card">
          <div class="arena-question-prompt">
            ${{currentQIdx + 1}}. ${{item.q}}
          </div>

          <div class="arena-options-container">
            ${{item.options.map((opt, oIdx) => {{
              const isCorrect = (oIdx === item.answer);
              const votes = voteCounts[oIdx] || 0;
              const pct = totalVotes > 0 ? Math.round((votes / totalVotes) * 100) : 0;

              return `
                <div class="arena-option-card ${{isCorrect ? 'correct' : 'dimmed'}}">
                  <div class="arena-opt-top">
                    <div class="arena-opt-letter let-${{letters[oIdx].toLowerCase()}}">${{letters[oIdx]}}</div>
                    <div class="arena-opt-text">${{opt}}</div>
                    ${{isCorrect ? '<span class="arena-correct-tag">✓ CORRECT</span>' : ''}}
                  </div>
                  <div class="vote-bar-wrap">
                    <div class="vote-bar-fill" style="width: ${{pct}}%; background: ${{isCorrect ? 'var(--emerald)' : 'var(--accent-primary)'}};"></div>
                  </div>
                  <div class="vote-stats-label">
                    <span>${{votes}} Votes</span>
                    <span>${{pct}}%</span>
                  </div>
                </div>
              `;
            }}).join('')}}
          </div>

          <div class="arena-rationale-box">
            <strong>Anatomical Rationale (Youmans & Winn Chapter 170):</strong><br>
            ${{item.explanation}}
          </div>
        </div>
      `;
    }}

    // -------------------------------------------------------------
    // GRAND PODIUM & PERSISTENT LEADERBOARD SCREEN
    // -------------------------------------------------------------
    function showGrandPodium() {{
      clearInterval(questionTimerInterval);
      clearInterval(revealTimerInterval);
      clearBotTimers();
      hostState = 'PODIUM';

      const list = Object.values(participants);
      list.sort((a, b) => b.score - a.score);

      // Save to localStorage history
      saveRoundHistory(list);
      broadcastHostSync();
      renderPodiumScreen(list);
    }}

    function saveRoundHistory(rankedList) {{
      try {{
        const history = JSON.parse(localStorage.getItem(QUIZ_STORAGE_KEY) || '[]');
        history.unshift({{
          date: new Date().toISOString(),
          participantsCount: rankedList.length,
          topScorer: rankedList[0] ? rankedList[0].name : 'N/A',
          topScore: rankedList[0] ? rankedList[0].score : 0,
          leaderboard: rankedList.map((p, idx) => ({{
            rank: idx + 1,
            name: p.name,
            score: p.score
          }}))
        }});
        // Keep last 10 rounds
        if (history.length > 10) history.pop();
        localStorage.setItem(QUIZ_STORAGE_KEY, JSON.stringify(history));
      }} catch(e){{}}
    }}

    function renderPodiumScreen(rankedList) {{
      if (!rankedList) {{
        rankedList = Object.values(participants);
        rankedList.sort((a, b) => b.score - a.score);
      }}

      const body = document.getElementById('quizArenaBody');
      const first = rankedList[0] || {{ name: 'Winner', avatar: '🏆', score: 0 }};
      const second = rankedList[1] || {{ name: '2nd Place', avatar: '🥈', score: 0 }};
      const third = rankedList[2] || {{ name: '3rd Place', avatar: '🥉', score: 0 }};

      body.innerHTML = `
        <div class="podium-arena-container">
          <div class="podium-title-box">
            <h2>🏆 Neurosurgical Board Examination Podium</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem;">
              Masterclass Chapter 170 Certified Results • Persistence Enabled
            </p>
          </div>

          <div class="olympic-podium">
            <!-- 2nd Place -->
            <div class="podium-col">
              <div class="podium-user-card">
                <div class="podium-avatar">${{second.avatar}}</div>
                <div class="podium-name">${{second.name}}</div>
                <div class="podium-score">${{second.score}} pts</div>
              </div>
              <div class="podium-block second">
                <span class="podium-rank-num">2</span>
                <span class="podium-medal-icon">🥈</span>
              </div>
            </div>

            <!-- 1st Place -->
            <div class="podium-col">
              <div class="podium-user-card">
                <div class="podium-avatar">${{first.avatar}}</div>
                <div class="podium-name">${{first.name}}</div>
                <div class="podium-score">${{first.score}} pts</div>
              </div>
              <div class="podium-block first">
                <span class="podium-rank-num">1</span>
                <span class="podium-medal-icon">🥇</span>
              </div>
            </div>

            <!-- 3rd Place -->
            <div class="podium-col">
              <div class="podium-user-card">
                <div class="podium-avatar">${{third.avatar}}</div>
                <div class="podium-name">${{third.name}}</div>
                <div class="podium-score">${{third.score}} pts</div>
              </div>
              <div class="podium-block third">
                <span class="podium-rank-num">3</span>
                <span class="podium-medal-icon">🥉</span>
              </div>
            </div>
          </div>

          <div class="leaderboard-card">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
              <h3 style="font-size: 1.1rem; font-weight: 800;">Complete Participant Leaderboard (${{rankedList.length}})</h3>
              <div style="display: flex; gap: 0.5rem;">
                <button class="btn-secondary-sm" onclick="downloadLeaderboardCSV()">📥 Export CSV</button>
                <button class="btn-nav primary" onclick="restartArenaSession()" style="padding: 6px 14px;">🔄 Start New Round</button>
              </div>
            </div>

            <table class="leaderboard-table">
              <thead>
                <tr>
                  <th class="rank-cell">Rank</th>
                  <th>Participant</th>
                  <th>Total Score</th>
                  <th>Accuracy</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                ${{rankedList.map((p, idx) => {{
                  const correctCount = Object.keys(p.answers).filter(qI => p.answers[qI].choice === QUIZ_QUESTIONS[qI].answer).length;
                  const acc = QUIZ_QUESTIONS.length > 0 ? Math.round((correctCount / QUIZ_QUESTIONS.length) * 100) : 0;
                  const rankClass = idx === 0 ? 'rank-1' : (idx === 1 ? 'rank-2' : (idx === 2 ? 'rank-3' : ''));

                  return `
                    <tr>
                      <td class="rank-cell ${{rankClass}}">#${{idx + 1}}</td>
                      <td style="display: flex; align-items: center; gap: 8px;">
                        <span>${{p.avatar}}</span>
                        <strong style="color: var(--text-main);">${{p.name}}</strong>
                      </td>
                      <td style="font-family: 'JetBrains Mono', monospace; font-weight: 800; color: var(--accent-primary);">${{p.score}}</td>
                      <td style="font-family: 'JetBrains Mono', monospace;">${{acc}}% (${{correctCount}}/${{QUIZ_QUESTIONS.length}})</td>
                      <td>
                        <span style="font-size: 0.78rem; font-weight: 700; color: ${{acc >= 70 ? 'var(--emerald)' : 'var(--amber)'}};">
                          ${{acc >= 70 ? '✓ Board Certified' : 'Review Suggested'}}
                        </span>
                      </td>
                    </tr>
                  `;
                }}).join('')}}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }}

    function downloadLeaderboardCSV() {{
      const list = Object.values(participants);
      list.sort((a, b) => b.score - a.score);

      let csv = 'Rank,Name,Score,CorrectAnswers,TotalQuestions,Date\\n';
      const dateStr = new Date().toISOString();
      list.forEach((p, idx) => {{
        const correctCount = Object.keys(p.answers).filter(qI => p.answers[qI].choice === getShuffledQuestion(parseInt(qI)).answer).length;
        csv += `${{idx + 1}},"${{p.name}}",${{p.score}},${{correctCount}},${{QUIZ_QUESTIONS.length}},"${{dateStr}}"\\n`;
      }});

      const blob = new Blob([csv], {{ type: 'text/csv' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `ventricular_quiz_results_${{new Date().toISOString().slice(0, 10)}}.csv`;
      a.click();
    }}

    function restartArenaSession() {{
      buildShuffledQuestions();
      hostState = 'LOBBY';
      participants = {{}};
      currentQIdx = 0;
      broadcastHostSync();
      renderLobbyScreen();
    }}

    // -------------------------------------------------------------
    // SOLO BOARD PRACTICE MODE
    // -------------------------------------------------------------
    function renderSoloScreen() {{
      const body = document.getElementById('quizArenaBody');
      const answeredCount = Object.keys(soloAnswers).length;
      const totalCount = getActiveQuestions().length;
      const isComplete = (answeredCount === totalCount);

      let scoreHtml = '';
      if (isComplete || answeredCount > 0) {{
        const pct = Math.round((soloScore / totalCount) * 100);
        scoreHtml = `
          <div class="arena-status-bar" style="margin-bottom: 1.5rem;">
            <div>
              <div style="font-size: 0.75rem; font-weight: 800; color: var(--text-muted); text-transform: uppercase;">SOLO BOARD SCORE</div>
              <div style="font-size: 1.6rem; font-weight: 800; color: var(--accent-primary); font-family: 'JetBrains Mono', monospace;">
                ${{soloScore}} / ${{totalCount}} <span style="font-size: 1rem; color: var(--text-muted);">(${{pct}}%)</span>
              </div>
            </div>
            <div>
              <button class="btn-secondary-sm" onclick="restartSoloQuiz()">🔄 Restart Solo Practice</button>
            </div>
          </div>
        `;
      }}

      const _soloQs = getActiveQuestions(); body.innerHTML = scoreHtml + _soloQs.map((item, qIdx) => {{
        const userAnswer = soloAnswers[qIdx];
        const isAnswered = (userAnswer !== undefined);

        return `
          <div class="arena-question-card" style="margin-bottom: 1.25rem;">
            <div style="font-weight: 800; font-size: 1.05rem; margin-bottom: 0.85rem;">
              ${{qIdx + 1}}. ${{item.q}}
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.5rem;">
              ${{item.options.map((opt, oIdx) => {{
                let style = 'padding: 0.75rem 1rem; border-radius: 8px; border: 1px solid var(--border-subtle); background: var(--bg-surface); color: var(--text-main); font-weight: 600; text-align: left; cursor: pointer; display: flex; justify-content: space-between;';
                if (isAnswered) {{
                  if (oIdx === item.answer) {{
                    style += ' border-color: var(--emerald); background: rgba(16, 185, 129, 0.15); color: var(--emerald); font-weight: 800;';
                  }} else if (oIdx === userAnswer) {{
                    style += ' border-color: var(--rose); background: rgba(239, 68, 68, 0.15); color: var(--rose);';
                  }}
                }}
                return `
                  <button style="${{style}}" ${{isAnswered ? 'disabled' : ''}} onclick="answerSoloQuestion(${{qIdx}}, ${{oIdx}})">
                    <span>${{opt}}</span>
                    ${{isAnswered && oIdx === item.answer ? '<span>✓ Correct</span>' : (isAnswered && oIdx === userAnswer ? '<span>✗ Your Choice</span>' : '')}}
                  </button>
                `;
              }}).join('')}}
            </div>
            ${{isAnswered ? `
              <div class="arena-rationale-box">
                <strong>Anatomical Rationale:</strong> ${{item.explanation}}
              </div>
            ` : ''}}
          </div>
        `;
      }}).join('');
    }}

    function answerSoloQuestion(qIdx, optIdx) {{
      if (soloAnswers[qIdx] !== undefined) return;
      soloAnswers[qIdx] = optIdx;
      if (optIdx === getShuffledQuestion(qIdx).answer) {{
        soloScore++;
      }}
      renderSoloScreen();
    }}

    function restartSoloQuiz() {{
      buildShuffledQuestions();
      soloAnswers = {{}};
      soloScore = 0;
      renderSoloScreen();
    }}


    // ==========================================================================
    // EDIT MODE: Inline text editing + image management + localStorage
    // ==========================================================================
    const EDIT_STORAGE_KEY = 'ventricular_lecture_slide_edits_v1';
    let slideEdits = {{}}; // {{ [globalId]: {{ badge, title, subtitle, caption_title, caption_body, img_path, extra_images, cards[] }} }}

    function loadSlideEdits() {{
      try {{
        const stored = localStorage.getItem(EDIT_STORAGE_KEY);
        if (stored) slideEdits = JSON.parse(stored);
      }} catch(e) {{ slideEdits = {{}}; }}
    }}
    loadSlideEdits();

    function saveSlideEdits() {{
      try {{ localStorage.setItem(EDIT_STORAGE_KEY, JSON.stringify(slideEdits)); }} catch(e) {{}}
    }}

    function getEffectiveSlide(idx) {{
      const base = SLIDES_DATA[idx];
      const edits = slideEdits[base.global_id];
      if (!edits) return base;
      return Object.assign({{}}, base, edits);
    }}

    let editModeActive = false;
    function toggleEditMode() {{
      editModeActive = !editModeActive;
      document.body.classList.toggle('edit-mode-active', editModeActive);
      const btn = document.getElementById('btnEditMode');
      btn.classList.toggle('edit-active', editModeActive);
      renderSlide('none');
    }}

    function applyEditModeToSlide() {{
      if (!editModeActive) return;
      // Make text elements contenteditable
      document.querySelectorAll('[data-edit-key]').forEach(el => {{
        el.contentEditable = 'true';
        el.addEventListener('blur', onEditFieldBlur, {{ once: true }});
      }});
      // Show add-image zones
      document.querySelectorAll('.img-add-zone').forEach(el => el.style.display = 'flex');
    }}

    function onEditFieldBlur(e) {{
      const el = e.target;
      const key = el.getAttribute('data-edit-key');
      const cardIdx = el.getAttribute('data-card-idx');
      const slide = SLIDES_DATA[currentIndex];
      const gid = slide.global_id;
      if (!slideEdits[gid]) slideEdits[gid] = {{}};

      const rawText = el.innerText.trim();

      if (cardIdx !== null) {{
        // Editing a card
        if (!slideEdits[gid].cards) {{
          const effective = getEffectiveSlide(currentIndex);
          slideEdits[gid].cards = effective.cards ? effective.cards.map(c => [c[0], c[1]]) : [];
        }}
        const ci = parseInt(cardIdx);
        if (!slideEdits[gid].cards[ci]) slideEdits[gid].cards[ci] = ['',''];
        if (key === 'card_title') slideEdits[gid].cards[ci][0] = rawText;
        if (key === 'card_body')  slideEdits[gid].cards[ci][1] = rawText;
      }} else {{
        slideEdits[gid][key] = rawText;
      }}
      saveSlideEdits();
    }}

    // --- Image management ---
    let _pendingImgAction = null; // {{ action: 'replace'|'add', imgPath: str, slideIdx: int }}

    function editImageReplace(btn, currentPath) {{
      if (!editModeActive) return;
      _pendingImgAction = {{ action: 'replace', imgPath: currentPath, slideIdx: currentIndex }};
      document.getElementById('imgUploadInput').click();
    }}

    function editImageAdd(btn) {{
      if (!editModeActive) return;
      _pendingImgAction = {{ action: 'add', slideIdx: currentIndex }};
      document.getElementById('imgUploadInput').click();
    }}

    function editImageAddNew(idx) {{
      if (!editModeActive) return;
      _pendingImgAction = {{ action: 'add', slideIdx: idx }};
      document.getElementById('imgUploadInput').click();
    }}

    function editImageRemove(btn) {{
      if (!editModeActive) return;
      const panel = btn.closest('.image-panel');
      const img = panel && panel.querySelector('img');
      if (!img) return;
      const removedSrc = img.src.replace(window.location.origin + '/', '').replace(window.location.origin, '');
      const slide = SLIDES_DATA[currentIndex];
      const gid = slide.global_id;
      if (!slideEdits[gid]) slideEdits[gid] = {{}};
      const effective = getEffectiveSlide(currentIndex);
      // If removing primary image
      if (removedSrc === effective.img_path || img.src.endsWith(effective.img_path)) {{
        if (effective.extra_images && effective.extra_images.length > 0) {{
          // Promote first extra to primary
          const promoted = effective.extra_images[0];
          slideEdits[gid].img_path = promoted.path;
          slideEdits[gid].caption_title = promoted.caption_title;
          slideEdits[gid].caption_body = promoted.caption_body;
          slideEdits[gid].extra_images = effective.extra_images.slice(1);
        }} else {{
          slideEdits[gid].img_path = '';
        }}
      }} else {{
        // Removing an extra image
        const extras = (effective.extra_images || []).filter(ei => !img.src.endsWith(ei.path));
        slideEdits[gid].extra_images = extras;
      }}
      saveSlideEdits();
      renderSlide('none');
    }}

    function handleImageUpload(e) {{
      const file = e.target.files[0];
      if (!file || !_pendingImgAction) return;
      const reader = new FileReader();
      reader.onload = function(ev) {{
        const dataUrl = ev.target.result;
        const action = _pendingImgAction;
        const slide = SLIDES_DATA[action.slideIdx];
        const gid = slide.global_id;
        if (!slideEdits[gid]) slideEdits[gid] = {{}};
        const effective = getEffectiveSlide(action.slideIdx);

        if (action.action === 'replace') {{
          slideEdits[gid].img_path = dataUrl;
        }} else if (action.action === 'add') {{
          const extras = (effective.extra_images || []).slice();
          extras.push({{ path: dataUrl, caption_title: 'ADDITIONAL IMAGE', caption_body: 'Uploaded image.' }});
          slideEdits[gid].extra_images = extras;
        }}
        saveSlideEdits();
        _pendingImgAction = null;
        renderSlide('none');
      }};
      reader.readAsDataURL(file);
      e.target.value = '';
    }}

    // ==========================================================================
    // QUIZ EDITOR: Add/Remove/Edit questions, choices, explanations + answer shuffle
    // ==========================================================================
    const QUIZ_EDIT_KEY = 'ventricular_quiz_custom_questions_v2';
    let editableQuestions = null; // null = use QUIZ_QUESTIONS; array = custom set

    function loadQuizEdits() {{
      try {{
        const stored = localStorage.getItem(QUIZ_EDIT_KEY);
        if (stored) editableQuestions = JSON.parse(stored);
      }} catch(e) {{ editableQuestions = null; }}
    }}
    loadQuizEdits();

    function getActiveQuestions() {{
      return editableQuestions !== null ? editableQuestions : QUIZ_QUESTIONS;
    }}

    // Override QUIZ_QUESTIONS references in quiz engine to use getActiveQuestions()
    // (done dynamically via the functions below)

    function openQuizEditor() {{
      // Deep clone current questions for editing
      const qs = getActiveQuestions().map(q => ({{
        q: q.q,
        options: q.options.slice(),
        answer: q.answer,
        explanation: q.explanation
      }}));
      renderQuizEditor(qs);
      document.getElementById('quizEditorModal').classList.add('active');
    }}

    function closeQuizEditor() {{
      document.getElementById('quizEditorModal').classList.remove('active');
    }}

    function renderQuizEditor(qs) {{
      const body = document.getElementById('quizEditorBody');
      const letters = ['A','B','C','D'];
      const letClasses = ['let-a','let-b','let-c','let-d'];
      body.innerHTML = qs.map((q, qi) => `
        <div class="qe-question-card" id="qeCard_${{qi}}">
          <div class="qe-q-num">Question ${{qi + 1}}</div>
          <button class="qe-delete-btn" onclick="deleteQeQuestion(${{qi}})" title="Delete question">✕</button>
          <div>
            <div class="qe-field-label">Question Text</div>
            <textarea class="qe-textarea" id="qeQ_${{qi}}">${{q.q}}</textarea>
          </div>
          <div>
            <div class="qe-field-label">Answer Choices (select correct one)</div>
            <div class="qe-options-grid">
              ${{q.options.map((opt, oi) => `
                <div class="qe-option-row">
                  <div class="qe-opt-letter ${{letClasses[oi]}}">${{letters[oi]}}</div>
                  <input class="qe-input" type="text" id="qeOpt_${{qi}}_${{oi}}" value="${{opt.replace(/"/g,'&quot;')}}" style="flex:1;">
                  <input type="radio" class="qe-correct-radio" name="correct_${{qi}}" value="${{oi}}" ${{q.answer === oi ? 'checked' : ''}} id="qeCorr_${{qi}}_${{oi}}" title="Mark as correct">
                  <label for="qeCorr_${{qi}}_${{oi}}" style="font-size:0.72rem;color:var(--emerald);font-weight:700;cursor:pointer;">✓</label>
                </div>
              `).join('')}}
            </div>
          </div>
          <div>
            <div class="qe-field-label">Explanation / Rationale</div>
            <textarea class="qe-textarea" id="qeExp_${{qi}}">${{q.explanation}}</textarea>
          </div>
        </div>
      `).join('');
      // Store count for save
      body.setAttribute('data-q-count', qs.length);
    }}

    function deleteQeQuestion(qi) {{
      const body = document.getElementById('quizEditorBody');
      const card = document.getElementById('qeCard_' + qi);
      if (card) card.remove();
      // Re-number remaining
      const remaining = body.querySelectorAll('.qe-question-card');
      remaining.forEach((c, i) => {{
        c.id = 'qeCard_' + i;
        const num = c.querySelector('.qe-q-num');
        if (num) num.textContent = 'Question ' + (i+1);
      }});
      body.setAttribute('data-q-count', remaining.length);
    }}

    function addNewQuestion() {{
      const body = document.getElementById('quizEditorBody');
      const count = parseInt(body.getAttribute('data-q-count') || '0');
      const qi = count;
      const letters = ['A','B','C','D'];
      const letClasses = ['let-a','let-b','let-c','let-d'];
      const newCard = document.createElement('div');
      newCard.className = 'qe-question-card';
      newCard.id = 'qeCard_' + qi;
      newCard.innerHTML = `
        <div class="qe-q-num">Question ${{qi + 1}}</div>
        <button class="qe-delete-btn" onclick="deleteQeQuestion(${{qi}})" title="Delete question">✕</button>
        <div>
          <div class="qe-field-label">Question Text</div>
          <textarea class="qe-textarea" id="qeQ_${{qi}}" placeholder="Enter question text..."></textarea>
        </div>
        <div>
          <div class="qe-field-label">Answer Choices (select correct one)</div>
          <div class="qe-options-grid">
            ${{[0,1,2,3].map(oi => `
              <div class="qe-option-row">
                <div class="qe-opt-letter ${{letClasses[oi]}}">${{letters[oi]}}</div>
                <input class="qe-input" type="text" id="qeOpt_${{qi}}_${{oi}}" placeholder="Option ${{letters[oi]}}..." style="flex:1;">
                <input type="radio" class="qe-correct-radio" name="correct_${{qi}}" value="${{oi}}" ${{oi===0?'checked':''}} id="qeCorr_${{qi}}_${{oi}}">
                <label for="qeCorr_${{qi}}_${{oi}}" style="font-size:0.72rem;color:var(--emerald);font-weight:700;cursor:pointer;">✓</label>
              </div>
            `).join('')}}
          </div>
        </div>
        <div>
          <div class="qe-field-label">Explanation / Rationale</div>
          <textarea class="qe-textarea" id="qeExp_${{qi}}" placeholder="Explain the correct answer..."></textarea>
        </div>
      `;
      body.appendChild(newCard);
      body.setAttribute('data-q-count', qi + 1);
      newCard.scrollIntoView({{ behavior: 'smooth' }});
    }}

    function saveQuizEdits() {{
      const body = document.getElementById('quizEditorBody');
      const count = parseInt(body.getAttribute('data-q-count') || '0');
      const saved = [];
      for (let qi = 0; qi < 200; qi++) {{
        const card = document.getElementById('qeCard_' + qi);
        if (!card) continue;
        const qText = (document.getElementById('qeQ_' + qi) || {{}}).value || '';
        const opts = [0,1,2,3].map(oi => (document.getElementById('qeOpt_' + qi + '_' + oi) || {{}}).value || '');
        const corrRadio = body.querySelector('input[name="correct_' + qi + '"]:checked');
        const ans = corrRadio ? parseInt(corrRadio.value) : 0;
        const exp = (document.getElementById('qeExp_' + qi) || {{}}).value || '';
        if (qText.trim()) {{
          saved.push({{ q: qText.trim(), options: opts, answer: ans, explanation: exp.trim() }});
        }}
      }}
      editableQuestions = saved.length > 0 ? saved : null;
      try {{
        if (editableQuestions) localStorage.setItem(QUIZ_EDIT_KEY, JSON.stringify(editableQuestions));
        else localStorage.removeItem(QUIZ_EDIT_KEY);
      }} catch(e) {{}}
      closeQuizEditor();
      // Notify
      const banner = document.createElement('div');
      banner.style.cssText = 'position:fixed;top:80px;left:50%;transform:translateX(-50%);z-index:9999;background:var(--emerald);color:#030712;padding:8px 22px;border-radius:999px;font-weight:800;font-size:0.85rem;box-shadow:0 4px 16px rgba(16,185,129,0.5);';
      banner.textContent = '✓ Quiz questions saved! ' + (editableQuestions ? editableQuestions.length : QUIZ_QUESTIONS.length) + ' questions active.';
      document.body.appendChild(banner);
      setTimeout(() => banner.remove(), 2800);
    }}

    function resetQuizToDefaults() {{
      if (!confirm('Reset all quiz questions to the original defaults?')) return;
      editableQuestions = null;
      localStorage.removeItem(QUIZ_EDIT_KEY);
      closeQuizEditor();
    }}

    // --- Answer Shuffling ---
    // We patch the quiz engine to shuffle answer choices on each quiz start.
    // shuffledQuestionMaps stores: {{ questionIdx: {{ shuffledOptions: [], correctShuffledIdx: int }} }}
    let shuffledQuestionMaps = [];

    function buildShuffledQuestions() {{
      const qs = getActiveQuestions();
      shuffledQuestionMaps = qs.map(q => {{
        // Create index array and shuffle it
        const indices = [0,1,2,3].slice(0, q.options.length);
        // Fisher-Yates shuffle
        for (let i = indices.length - 1; i > 0; i--) {{
          const j = Math.floor(Math.random() * (i + 1));
          [indices[i], indices[j]] = [indices[j], indices[i]];
        }}
        const shuffledOptions = indices.map(i => q.options[i]);
        const correctShuffledIdx = indices.indexOf(q.answer);
        return {{ shuffledOptions, correctShuffledIdx, originalAnswer: q.answer }};
      }});
    }}

    function getShuffledQuestion(qIdx) {{
      const base = getActiveQuestions()[qIdx];
      if (!shuffledQuestionMaps[qIdx]) return base;
      const map = shuffledQuestionMaps[qIdx];
      return {{
        q: base.q,
        options: map.shuffledOptions,
        answer: map.correctShuffledIdx,
        explanation: base.explanation
      }};
    }}

    // Keyboard shortcut: E = toggle Edit Mode
    // (Added to existing keydown handler below)

    // Master Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {{
      if (document.getElementById('drawerOverlay').classList.contains('active')) {{
        if (e.key === 'Escape') toggleDrawer();
        return;
      }}
      if (document.getElementById('lightboxModal').classList.contains('active')) {{
        if (e.key === 'Escape') toggleLightbox();
        if (e.key === '+' || e.key === '=') adjustZoom(0.35);
        if (e.key === '-' || e.key === '_') adjustZoom(-0.35);
        if (e.key === '0') resetZoom();
        return;
      }}
      if (document.getElementById('quizOverlay').classList.contains('active')) {{
        if (e.key === 'Escape') toggleQuiz();
        return;
      }}

      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown' || e.key === 'Enter') {{
        e.preventDefault();
        navigateStepOrSlide(1);
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        navigateStepOrSlide(-1);
      }} else if (e.key.toLowerCase() === 'b') {{
        toggleStepMode();
      }} else if (e.key.toLowerCase() === 'f') {{
        toggleFullscreen();
      }} else if (e.key.toLowerCase() === 'o') {{
        toggleDrawer();
      }} else if (e.key.toLowerCase() === 'q') {{
        toggleQuiz();
      }} else if (e.key.toLowerCase() === 't') {{
        toggleTheme();
      }}
    }});

    // URL param support for direct slide jump, quiz states, and lightbox zoom
    const urlParams = new URLSearchParams(window.location.search);
    const fsParam = urlParams.get('fullscreen');
    if (fsParam === 'true' || fsParam === '1') {{
      document.body.classList.add('is-fullscreen');
      document.body.classList.add('is-fullscreen-forced');
    }}
    const slideParam = urlParams.get('slide');
    if (slideParam) {{
      const targetIdx = parseInt(slideParam, 10) - 1;
      if (targetIdx >= 0 && targetIdx < SLIDES_DATA.length) {{
        currentIndex = targetIdx;
      }}
    }}
    const stepParam = urlParams.get('step');
    if (stepParam === 'all') {{
      currentStep = 999;
    }}
    const editParam = urlParams.get('edit');
    if (editParam === 'true' || editParam === '1') {{
      toggleEditMode();
    }}
    const quizParam = urlParams.get('quiz');
    if (quizParam === 'edit') {{
      toggleQuiz();
      openQuizEditor();
    }} else if (quizParam === 'open' || quizParam === 'lobby') {{
      toggleQuiz();
    }} else if (quizParam === 'start') {{
      toggleQuiz();
      simulateAttendees();
      startLiveQuiz();
    }} else if (quizParam === 'reveal') {{
      toggleQuiz();
      simulateAttendees();
      startLiveQuiz();
      revealQuestionResult();
    }} else if (quizParam === 'podium') {{
      toggleQuiz();
      simulateAttendees();
      showGrandPodium();
    }}
    const zoomParam = urlParams.get('zoom');
    if (zoomParam) {{
      openLightbox(zoomParam, '300 DPI High-Resolution Microanatomy Inspection');
    }}
    const drawerParam = urlParams.get('drawer');
    if (drawerParam) {{
      toggleDrawer();
      if (drawerParam === 'part1' || drawerParam === '1') {{
        setDrawerFilter('1', document.getElementById('drawerPill1'));
      }} else if (drawerParam === 'part2' || drawerParam === '2') {{
        setDrawerFilter('2', document.getElementById('drawerPill2'));
      }}
    }}

    // Initialize first slide on load
    renderSlide('forward');
  </script>

</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('interactive_lecture.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# Copy this generator script to generate_html_lecture.py
import shutil
shutil.copyfile('build_html_lecture_arena.py', 'generate_html_lecture.py')

print(f"Master interactive lecture web application generated successfully!")
print(f"Total slides: {len(ALL_SLIDES)} (Part 1: {len(DECK1_SLIDES)}, Part 2: {len(DECK2_SLIDES)})")
print(f"Files written: index.html ({len(html_content)//1024} KB) and interactive_lecture.html")
