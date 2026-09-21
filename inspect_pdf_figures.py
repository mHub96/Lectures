import pymupdf

doc = pymupdf.open('Youmans and Winn Ventricular Tumors.pdf')

pages_to_check = [2, 3, 4, 5, 6, 7, 8, 12, 14, 17, 19, 20, 23, 24, 25]

for pno in pages_to_check:
    page = doc[pno]
    print(f"=== PAGE {pno + 1} (index {pno}) ===")
    
    # Get image bboxes on page
    img_list = page.get_images()
    print(f"Images on page: {len(img_list)}")
    for img in img_list:
        xref = img[0]
        rects = page.get_image_rects(xref)
        for r in rects:
            print(f"  Image xref {xref}: rect {r}")
            
    # Get text blocks to see where captions and body text are
    blocks = page.get_text("blocks")
    for b in blocks:
        # b is (x0, y0, x1, y1, text, block_no, block_type)
        txt = b[4].strip().replace('\n', ' ')
        if len(txt) > 0 and ('Figure 170' in txt or 'Fig.' in txt or 'FIG' in txt):
            print(f"  CAPTION BLOCK at ({b[0]:.1f}, {b[1]:.1f}, {b[2]:.1f}, {b[3]:.1f}): {txt[:80]}...")

