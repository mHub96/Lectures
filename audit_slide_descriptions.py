import sys
sys.stdout.reconfigure(encoding='utf-8')

from deck1_data import DECK1_SLIDES
from deck2_data import DECK2_SLIDES

print("=================== DECK 1 AUDIT ===================")
for idx, s in enumerate(DECK1_SLIDES):
    img = s.get('img_path', '')
    cap_title = s.get('caption_title', '')
    cap_body = s.get('caption_body', '')
    print(f"Slide {idx+1:02d}: [{s['type']}] {s['title'][:40]}...")
    print(f"   IMG: {img}")
    print(f"   CAP_TITLE: {cap_title}")
    print(f"   CAP_BODY:  {cap_body[:90]}...\n")

print("\n=================== DECK 2 AUDIT ===================")
for idx, s in enumerate(DECK2_SLIDES):
    img = s.get('img_path', '')
    cap_title = s.get('caption_title', '')
    cap_body = s.get('caption_body', '')
    print(f"Slide {idx+1:02d}: [{s['type']}] {s['title'][:40]}...")
    print(f"   IMG: {img}")
    print(f"   CAP_TITLE: {cap_title}")
    print(f"   CAP_BODY:  {cap_body[:90]}...\n")

