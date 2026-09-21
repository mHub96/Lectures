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
    slide_copy['part_title'] = "Part 2: Third & Fourth Ventricles, Approaches & Pathology"
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
      width: 100%;
      max-width: 1250px;
      height: 85vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      animation: modalPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    @keyframes modalPop {{
      from {{ transform: scale(0.95); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}

    .drawer-header {{
      padding: 1.25rem 1.75rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
    }}

    .drawer-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text-main);
    }}

    .drawer-search-input {{
      flex: 1;
      max-width: 400px;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 0.55rem 1rem;
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.88rem;
      outline: none;
    }}

    .drawer-search-input:focus {{
      border-color: var(--accent-primary);
    }}

    .drawer-grid {{
      flex: 1;
      overflow-y: auto;
      padding: 1.75rem;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1.25rem;
    }}

    .drawer-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      transition: transform var(--transition-fast), border-color var(--transition-fast);
    }}

    .drawer-card:hover {{
      transform: translateY(-3px);
      border-color: var(--accent-primary);
    }}

    .drawer-card.active-slide {{
      border: 2px solid var(--accent-primary);
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.3);
    }}

    .drawer-card-thumb {{
      height: 140px;
      background: #020617;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .drawer-card-thumb img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
    }}

    .drawer-card-meta {{
      padding: 0.75rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--accent-primary);
      border-bottom: 1px solid var(--border-subtle);
    }}

    .drawer-card-title {{
      padding: 0.75rem 1rem;
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.35;
      flex: 1;
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
      <button class="part-pill active" id="pillAll" onclick="setFilter('all')">All Slides (66)</button>
      <button class="part-pill" id="pillPart1" onclick="setFilter('part1')">Part 1: Lateral (33)</button>
      <button class="part-pill" id="pillPart2" onclick="setFilter('part2')">Part 2: 3rd & 4th (33)</button>
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
      <span class="slide-counter-badge" id="slideCounter">Slide 1 / 66</span>

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
        <h2 class="drawer-title">Masterclass Curriculum Index (66 Slides)</h2>
        <input type="text" class="drawer-search-input" id="drawerSearch" placeholder="Search anatomy, corridor, pathology, figure..." oninput="filterDrawerSlides()">
        <button class="btn-icon" onclick="toggleDrawer()">✕</button>
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
          <button class="btn-icon" onclick="toggleQuiz()">✕</button>
        </div>
      </div>

      <div class="quiz-arena-viewport" id="quizArenaBody">
        <!-- Rendered dynamically by Quiz Engine: Lobby, Question, Reveal, or Podium -->
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
    }}

    function renderSlide(direction = 'forward') {{
      const slide = SLIDES_DATA[currentIndex];
      const box = document.getElementById('slideBox');
      const pos = filteredIndices.indexOf(currentIndex);

      document.getElementById('slideCounter').textContent = `Slide ${{pos + 1}} / ${{filteredIndices.length}}`;
      document.getElementById('btnPrev').disabled = (pos === 0 && currentStep === 0);
      document.getElementById('btnNext').disabled = (pos === filteredIndices.length - 1 && currentStep >= totalStepsForSlide);

      const pct = ((pos + 1) / filteredIndices.length) * 100;
      document.getElementById('progressBar').style.width = pct + '%';

      const animClass = direction === 'forward' ? 'slide-forward' : (direction === 'backward' ? 'slide-backward' : '');

      if (slide.type === 'title') {{
        const creditsHtml = (slide.credits || []).map(c => `<li>${{c}}</li>`).join('');
        box.innerHTML = `
          <div class="slide-content-container ${{animClass}}">
            <div class="title-slide-container">
              <div class="title-left">
                <div class="slide-category-badge">${{slide.badge}}</div>
                <h1 class="slide-title">${{slide.title.replace(/\\n/g, '<br>')}}</h1>
                <p class="slide-subtitle">${{slide.subtitle}}</p>
                <div class="credits-box">
                  <div class="credits-heading">REFERENCE TEXT & CURRICULUM</div>
                  <ul class="credits-list">
                    ${{creditsHtml}}
                  </ul>
                </div>
              </div>
              <div class="image-panel" data-step-order="1">
                <div class="image-viewport" onclick="openLightbox('${{slide.img_path}}', '${{slide.title.replace(/\\n/g, ' ')}}')">
                  <img src="${{slide.img_path}}" alt="${{slide.title}}">
                  <div class="zoom-hint-badge">🔍 Zoom Ultra-Res (300 DPI)</div>
                </div>
                <div class="caption-card">
                  <div class="caption-title">3D VENTRICULAR PROJECTION</div>
                  <div class="caption-text">High-resolution reconstruction of cerebral ventricular cavities from Youmans & Winn.</div>
                </div>
              </div>
            </div>
          </div>
        `;
      }} else {{
        const isSummary = (slide.type === 'summary');
        const isThankYou = (slide.type === 'thankyou');
        const cards = slide.cards || [];
        
        let badgeClass = '';
        let cardClass = '';
        if (isSummary) {{
          badgeClass = 'badge-emerald';
          cardClass = 'card-emerald';
        }} else if (isThankYou) {{
          badgeClass = 'badge-purple thankyou-badge';
          cardClass = 'card-purple';
        }}

        const cardsHtml = cards.map((c, i) => `
          <div class="lecture-card ${{cardClass}}" data-step-order="${{i + 1}}">
            <div class="card-heading">
              <span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:currentColor;opacity:0.8;"></span>
              ${{c[0]}}
            </div>
            <div class="card-text">${{c[1]}}</div>
          </div>
        `).join('');

        const imgStepOrder = cards.length + 1;

        box.innerHTML = `
          <div class="slide-content-container ${{animClass}}">
            <div class="slide-header">
              <div class="slide-category-badge ${{badgeClass}}">${{slide.badge}}</div>
              <h2 class="slide-title">${{slide.title.replace(/\\n/g, '<br>')}}</h2>
              <p class="slide-subtitle">${{slide.subtitle}}</p>
            </div>
            <div class="slide-body-grid">
              <div class="cards-column">
                ${{cardsHtml}}
              </div>
              <div class="image-panel" data-step-order="${{imgStepOrder}}">
                <div class="image-viewport" onclick="openLightbox('${{slide.img_path}}', '${{slide.caption_title}}: ${{slide.caption_body}}')">
                  <img src="${{slide.img_path}}" alt="${{slide.title}}">
                  <div class="zoom-hint-badge">🔍 Zoom Ultra-Res (300 DPI)</div>
                </div>
                <div class="caption-card">
                  <div class="caption-title" style="${{isSummary ? 'color: var(--emerald);' : (isThankYou ? 'color: var(--purple);' : '')}}">${{slide.caption_title}}</div>
                  <div class="caption-text">${{slide.caption_body}}</div>
                </div>
              </div>
            </div>
          </div>
        `;
      }}

      applyStepVisibility();
    }}

    // Drawer Functions
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
        const matches = s.title.toLowerCase().includes(query) || 
                        s.subtitle.toLowerCase().includes(query) ||
                        s.badge.toLowerCase().includes(query) ||
                        (s.caption_body && s.caption_body.toLowerCase().includes(query));
        if (!matches) return '';

        const isActive = (idx === currentIndex);
        return `
          <div class="drawer-card ${{isActive ? 'active-slide' : ''}}" onclick="jumpToSlide(${{idx}})">
            <div class="drawer-card-thumb">
              <img src="${{s.img_path}}" alt="${{s.title}}" loading="lazy">
            </div>
            <div class="drawer-card-meta">
              <span>SLIDE ${{idx + 1}}</span>
              <span>PART ${{s.part}}</span>
            </div>
            <div class="drawer-card-title">${{s.title.replace(/\\n/g, ' ')}}</div>
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

    function openLightbox(src, caption) {{
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
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => console.log(err));
      }} else {{
        document.exitFullscreen().catch(err => console.log(err));
      }}
    }}

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
    const MQTT_BROKER = 'wss://broker.emqx.io:8084/mqtt';
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

      // 3. MQTT over WebSockets
      try {{
        const hostId = `vqh_${{Math.random().toString(16).substring(2, 8)}}`;
        hostMqttClient = mqtt.connect(MQTT_BROKER, {{
          clientId: hostId,
          clean: true,
          connectTimeout: 5000,
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
          updateArenaConnectionStatus(false, 'Broker Offline');
        }});

        hostMqttClient.on('error', () => {{
          updateArenaConnectionStatus(false, 'Local Sync Mode');
        }});
      }} catch(err) {{
        console.warn('MQTT init failed, falling back to Local Tab Broadcast:', err);
        updateArenaConnectionStatus(true, 'Local Sync Mode');
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
        totalQuestions: QUIZ_QUESTIONS.length,
        timeRemaining: questionTimerVal,
        correctAnswer: (hostState === 'REVEAL' || hostState === 'PODIUM') ? QUIZ_QUESTIONS[currentQIdx].answer : null,
        ranks: ranks,
        participantCount: Object.keys(participants).length
      }});
    }}

    function handleHostIncomingMessage(msg) {{
      if (!msg || !msg.type || msg.sender === 'HOST') return;

      if (msg.type === 'PLAYER_JOIN_REQUEST') {{
        // REGISTRATION LOCK CHECK:
        if (hostState !== 'LOBBY') {{
          // Registration is locked!
          broadcastToPlayers({{
            type: 'HOST_PLAYER_REJECTED',
            targetPlayerId: msg.playerId,
            reason: 'REGISTRATION_LOCKED'
          }});
          return;
        }}

        // Accept user
        if (!participants[msg.playerId]) {{
          participants[msg.playerId] = {{
            id: msg.playerId,
            name: msg.name || 'Anonymous Surgeon',
            avatar: msg.avatar || '🧠',
            score: 0,
            answers: {{}},
            isBot: false
          }};
          broadcastToPlayers({{
            type: 'HOST_PLAYER_ACCEPTED',
            targetPlayerId: msg.playerId
          }});
          broadcastHostSync();
          if (document.getElementById('quizOverlay').classList.contains('active') && hostState === 'LOBBY') {{
            renderLobbyScreen();
          }}
        }}
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
      const list = Object.values(participants);
      if (list.length === 0) return false;
      return list.every(p => p.answers[currentQIdx] !== undefined);
    }}

    function getSubmittedCount() {{
      return Object.values(participants).filter(p => p.answers[currentQIdx] !== undefined).length;
    }}

    function updateRespondentBar() {{
      const count = getSubmittedCount();
      const total = Object.keys(participants).length;
      const pct = total > 0 ? (count / total) * 100 : 0;
      
      const countEl = document.getElementById('arenaRespCount');
      const barEl = document.getElementById('arenaRespBar');
      if (countEl) countEl.textContent = `${{count}} / ${{total}} Answered`;
      if (barEl) barEl.style.width = `${{pct}}%`;
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
      const correctAns = QUIZ_QUESTIONS[qIdx].answer;
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
      const item = QUIZ_QUESTIONS[currentQIdx];
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
      const correctAns = QUIZ_QUESTIONS[currentQIdx].answer;
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
      if (currentQIdx < QUIZ_QUESTIONS.length - 1) {{
        startQuestionRound(currentQIdx + 1);
      }} else {{
        showGrandPodium();
      }}
    }}

    function renderRevealScreen(voteCounts) {{
      const body = document.getElementById('quizArenaBody');
      const item = QUIZ_QUESTIONS[currentQIdx];
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
        const correctCount = Object.keys(p.answers).filter(qI => p.answers[qI].choice === QUIZ_QUESTIONS[qI].answer).length;
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
      const totalCount = QUIZ_QUESTIONS.length;
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

      body.innerHTML = scoreHtml + QUIZ_QUESTIONS.map((item, qIdx) => {{
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
      if (optIdx === QUIZ_QUESTIONS[qIdx].answer) {{
        soloScore++;
      }}
      renderSoloScreen();
    }}

    function restartSoloQuiz() {{
      soloAnswers = {{}};
      soloScore = 0;
      renderSoloScreen();
    }}

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
    const quizParam = urlParams.get('quiz');
    if (quizParam === 'open' || quizParam === 'lobby') {{
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
print(f"Total slides: {len(ALL_SLIDES)} (Part 1: 33, Part 2: 33)")
print(f"Files written: index.html ({len(html_content)//1024} KB) and interactive_lecture.html")
