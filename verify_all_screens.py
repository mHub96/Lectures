import os, sys, time, subprocess
sys.stdout.reconfigure(encoding='utf-8')

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cwd = os.path.abspath(".")

tests = [
    # 1. Slide with clean figure
    ("test_web_slide16.png", f"file:///{cwd}/index.html?slide=16&step=all", (1920, 1080), 1.0),
    # 2. Lightbox 300 DPI Zoom
    ("test_web_lightbox.png", f"file:///{cwd}/index.html?zoom=enhanced_figures/fig_170_8_fourth_ventricle_floor.png", (1920, 1080), 1.0),
    # 3. Quiz Lobby (QR Code + Room Code)
    ("test_quiz_lobby.png", f"file:///{cwd}/index.html?quiz=lobby", (1920, 1080), 1.2),
    # 4. Quiz Active Question (60s timer + respondents)
    ("test_quiz_question.png", f"file:///{cwd}/index.html?quiz=start", (1920, 1080), 1.5),
    # 4b. Quiz Reveal (votes breakdown, correct answer, rationale, 5s countdown)
    ("test_quiz_reveal.png", f"file:///{cwd}/index.html?quiz=reveal", (1920, 1080), 1.5),
    # 5. Quiz Podium (1st, 2nd, 3rd + leaderboard)
    ("test_quiz_podium.png", f"file:///{cwd}/index.html?quiz=podium", (1920, 1080), 1.5),
    # 6. Mobile Player - Registration Screen
    ("test_mobile_join.png", f"file:///{cwd}/quiz_player.html", (500, 920), 1.0),
    # 7. Mobile Player - 4-Button Question Screen (A, B, C, D only)
    ("test_mobile_question.png", f"file:///{cwd}/quiz_player.html?preview=question", (500, 920), 1.0),
    # 8. Mobile Player - Instant Feedback Screen
    ("test_mobile_reveal.png", f"file:///{cwd}/quiz_player.html?preview=reveal", (500, 920), 1.0),
    # 9. Mobile Player - Final Results / Podium
    ("test_mobile_podium.png", f"file:///{cwd}/quiz_player.html?preview=podium", (500, 920), 1.0),
]

print(f"Running {len(tests)} automated visual verification captures via Chrome...")
for out_file, url, (w, h), wait_s in tests:
    out_path = os.path.join(cwd, out_file)
    cmd = [
        chrome_path,
        "--headless=new",
        f"--window-size={w},{h}",
        f"--screenshot={out_path}",
        "--hide-scrollbars",
        "--disable-gpu",
        "--no-sandbox",
        url
    ]
    # Give a moment if needed
    time.sleep(0.5)
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
        print(f"  ✓ {out_file}: {os.path.getsize(out_path):,} bytes captured from {url.split('/')[-1]}")
    else:
        print(f"  ✗ {out_file} failed! stderr: {res.stderr}")

print("All visual verification tests completed!")
