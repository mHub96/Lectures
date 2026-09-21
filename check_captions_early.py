import sys
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

doc = pymupdf.open('Youmans and Winn Ventricular Tumors.pdf')

for pno in [2, 3, 4, 5, 6, 7, 8]:
    page = doc[pno]
    print(f"\n--- Page {pno+1} ---")
    blocks = page.get_text("blocks")
    for b in blocks:
        txt = b[4].strip().replace('\n', ' ')
        if "Figure 170." in txt:
            print(f"  {txt[:120]}")

