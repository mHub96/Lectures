import os, time
import subprocess

# We can create small HTML wrappers or pass hash/params to jump to slides
# Or we can write a tiny script that modifies index.html or loads with hash:
# Let's see if index.html supports location.hash or a param!
# Let's add support for ?slide=N in index.html, or jump via JS!

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add URL parameter support to index.html if not already present:
if "URLSearchParams" not in content:
    old_init = "// Initialize first slide on load\n    renderSlide('forward');"
    new_init = """// URL param support for direct slide jump
    const urlParams = new URLSearchParams(window.location.search);
    const slideParam = urlParams.get('slide');
    if (slideParam) {
      const targetIdx = parseInt(slideParam, 10) - 1;
      if (targetIdx >= 0 && targetIdx < SLIDES_DATA.length) {
        currentIndex = targetIdx;
      }
    }
    const stepParam = urlParams.get('step');
    if (stepParam === 'all') {
      currentStep = 999;
    }
    const quizParam = urlParams.get('quiz');
    if (quizParam === 'open') {
      setTimeout(() => toggleQuiz(), 200);
    }
    const zoomParam = urlParams.get('zoom');
    if (zoomParam) {
      setTimeout(() => openLightbox(zoomParam, '300 DPI High-Resolution Microanatomy Inspection'), 250);
    }
    renderSlide('forward');"""
    content = content.replace(old_init, new_init)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    with open("interactive_lecture.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Added URL param support to index.html and interactive_lecture.html")

# Now capture screenshots using chrome headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
tests = [
    ("web_slide2.png", "file:///C:/Users/GHOST/Desktop/Lecture project/index.html?slide=2&step=all"),
    ("web_slide16.png", "file:///C:/Users/GHOST/Desktop/Lecture project/index.html?slide=16&step=all"),
    ("web_slide33_part1_thankyou.png", "file:///C:/Users/GHOST/Desktop/Lecture project/index.html?slide=33&step=all"),
    ("web_slide66_part2_thankyou.png", "file:///C:/Users/GHOST/Desktop/Lecture project/index.html?slide=66&step=all"),
    ("web_quiz.png", "file:///C:/Users/GHOST/Desktop/Lecture project/index.html?quiz=open"),
    ("web_zoom_lightbox.png", "file:///C:/Users/GHOST/Desktop/Lecture project/index.html?zoom=enhanced_figures/fig_170_8_fourth_ventricle_floor.png")
]

for out_name, url in tests:
    out_path = os.path.abspath(out_name)
    cmd = [
        chrome_path,
        "--headless=new",
        f"--screenshot={out_path}",
        "--window-size=1920,1080",
        "--disable-gpu",
        url
    ]
    print(f"Capturing {out_name}...")
    subprocess.run(cmd, check=True)
    print(f"Captured {out_name} successfully!")

