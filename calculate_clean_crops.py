import sys
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

doc = pymupdf.open('Youmans and Winn Ventricular Tumors.pdf')

pages = [
    (2, "Fig 170.1 & Fig 170.2"),
    (3, "Fig 170.3, Fig 170.4, Fig 170.5"),
    (4, "Fig 170.6"),
    (5, "Fig 170.7"),
    (6, "Fig 170.8"),
    (7, "Fig 170.9"),
    (8, "Fig 170.10"),
    (12, "Fig 170.11"),
    (14, "Fig 170.12"),
    (17, "Fig 170.13 & Fig 170.14"),
    (19, "Fig 170.15"),
    (20, "Fig 170.16 & Fig 170.17"),
    (23, "Fig 170.18"),
    (24, "Fig 170.19"),
    (25, "Fig 170.20")
]

for pno, desc in pages:
    page = doc[pno]
    print(f"\n=================== PAGE {pno+1} ({desc}) ===================")
    
    # 1. Images
    images = page.get_images()
    for img in images:
        for r in page.get_image_rects(img[0]):
            print(f"  IMAGE: ({r.x0:.1f}, {r.y0:.1f}, {r.x1:.1f}, {r.y1:.1f})")
            
    # 2. Text blocks
    blocks = page.get_text("blocks")
    for b in blocks:
        txt = b[4].strip().replace('\n', ' ')
        if "Figure 170." in txt or "Fig. 170." in txt:
            print(f"  CAPTION BLOCK: ({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}) -> {txt[:70]}...")

