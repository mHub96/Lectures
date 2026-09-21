# Ventricular Tumors: Microsurgical Anatomy, Approaches & Pathology
### Youmans & Winn Neurological Surgery (Chapter 170) Masterclass

An interactive neurosurgical curriculum, dual-deck PowerPoint masterclass, and live audience board examination platform covering the surgical corridors, microsurgical anatomy, and pathology of the ventricular system.

---

## 🌟 Masterclass Highlights

1. **Dual-Deck Animated PowerPoint Presentations**:
   - `Ventricular Tumors_(Part 1).pptx` (33 Slides): Lateral Ventricles (Frontal Horn, Body, Atrium, Occipital & Temporal Horns), Venous Landmarks, and Lateral Approaches (Transcallosal, Transcortical, Transchoroidal).
   - `Ventricular Tumors_(Part 2).pptx` (33 Slides): Third & Fourth Ventricles, Pineal Region, Telovelar Corridor, Rhomboid Fossa Floor Landmarks, WHO Histopathology & Molecular Classification.
   - Built with click-by-click manual build animations and 300 DPI high-resolution neuroanatomical figures.

2. **Interactive Lecture Hall Web Application (`index.html`)**:
   - **Click-by-Click Element Reveal**: Step-by-step point presentation matching lecture hall delivery.
   - **300 DPI Clean Figure Lightbox**: Zoom up to 300% with pan and mouse-wheel controls to inspect delicate microvascular structures, cranial nerve nuclei, and anatomical leader lines with zero loss of clarity.
   - **100% Clean Figure Crops**: All 20 textbook figures cleanly isolated from *Youmans & Winn* with all 49+ pointer labels and arrows perfectly intact, free of printed textbook body paragraphs or caption headers.
   - **Curriculum Overview Index**: Search and jump to any of the 66 slides instantly.

3. **Live Audience Interactive Quiz Arena**:
   - **Lobby Phase**: Displays a high-contrast QR code on the lecture projector screen. Attendees scan with their smartphone camera to join instantly (no apps or sign-up needed).
   - **Roster & Registration Lock**: Attendees enter their name/handle. The host screen displays registered participants in real time. Pressing **"START QUIZ"** permanently locks registration for the round.
   - **Audience Device Controller (`quiz_player.html` / `player.html`)**: In accordance with lecture hall best practices, audience smartphones display **only 4 giant thumb-friendly choice cards (`[ A ]`, `[ B ]`, `[ C ]`, `[ D ]`)** with distinctive colors and geometry—no question text on phones.
   - **60-Second Countdown & Auto-Advance**: Each question features a 60-second timer and live respondent tracker. When all registered participants submit their answer, the host screen automatically reveals the result immediately.
   - **Audience Vote Distribution & Explanations**: Live animated bars reveal the exact vote breakdown across all 4 options, highlights the correct answer in glowing emerald, and displays the textbook rationale. A 5-second countdown with pause/resume controls transitions to the next question.
   - **Olympic 3D Podium & Leaderboard**: Celebrates the top 3 finishers on an animated gold/silver/bronze podium, followed by a full ranked leaderboard with score persistence (`localStorage`) and CSV export.
   - **Simulation Bot Engine**: Includes a built-in "Simulate 5 Attendees" button for instant testing and standalone demonstration.

---

## 📁 Repository Structure

```
.
├── index.html                  # Master presentation web application & Live Quiz Host
├── interactive_lecture.html    # Standalone mirror of master web application
├── quiz_player.html            # Mobile audience controller (thumb-friendly A, B, C, D)
├── player.html                 # Mobile controller alias / redirect
├── qrcode.min.js               # Embedded client-side QR code generator
├── mqtt.min.js                 # MQTT over WebSockets client for real-time sync
│
├── enhanced_figures/           # 20 clean 300 DPI figures from Youmans & Winn Chapter 170
│   ├── fig_170_1_dcta.png
│   ├── fig_170_4_venous_angle.png
│   ├── fig_170_8_fourth_ventricle_floor.png
│   └── ...
├── assets_images/              # Supplementary intraoperative & histological images
│
├── Ventricular Tumors_(Part 1).pptx  # 33-slide animated Master Deck (Part 1)
├── Ventricular Tumors_(Part 2).pptx  # 33-slide animated Master Deck (Part 2)
│
├── generate_html_lecture.py    # Python generator for the lecture web application
├── clean_figure_extractor.py   # High-resolution vector/raster figure extraction pipeline
└── audit_slide_descriptions.py # Automated auditing script verifying 100% caption alignment
```

---

## 🚀 Getting Started

### Presentation Mode
Open `index.html` in any modern web browser (Chrome, Edge, Safari, Firefox).
- **Advance Slide / Point**: `Space`, `Enter`, `→`, or Click
- **Previous Slide / Point**: `←` or `PageUp`
- **Toggle Build Mode**: Press `B`
- **Toggle Fullscreen Hall Mode**: Press `F`
- **Curriculum Slide Index**: Press `O`
- **Launch Live Audience Quiz Arena**: Press `Q`

### Running the Live Audience Quiz
1. Press `Q` on the host screen to launch the Quiz Arena.
2. Direct attendees to scan the QR code projected on screen, or share the direct link: `quiz_player.html?room=VENTRICLE`.
3. Watch attendee badges appear in the roster. (Click *"Simulate 5 Attendees"* if rehearsing alone).
4. Click **"START QUIZ"** to lock registration and start Question 1!

---

## 📖 Reference Curriculum

- **Textbook**: *Youmans & Winn Neurological Surgery*, 8th Edition.
- **Chapter**: Chapter 170: *Surgical Approaches to Ventricular Tumors*.
- **Authors**: H. Richard Winn, MD (Editor-in-Chief); Chapter Authors & Contributors.
