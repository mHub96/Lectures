import sys
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

doc = pymupdf.open('Youmans and Winn Ventricular Tumors.pdf')

figures_data = []

for pno in range(len(doc)):
    page = doc[pno]
    blocks = page.get_text("blocks")
    for b in blocks:
        txt = b[4].strip()
        if "Figure 170." in txt or "Fig. 170." in txt or "FIG. 170." in txt:
            # Clean text
            clean_txt = " ".join(txt.split())
            figures_data.append({
                "page": pno + 1,
                "bbox": (round(b[0], 1), round(b[1], 1), round(b[2], 1), round(b[3], 1)),
                "text": clean_txt
            })

print(f"Found {len(figures_data)} figure captions in Chapter 170:")
for f in figures_data:
    print(f"\n[Page {f['page']} @ {f['bbox']}]")
    print(f['text'])

