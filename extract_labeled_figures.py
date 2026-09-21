import os, sys
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

doc = pymupdf.open('Youmans and Winn Ventricular Tumors.pdf')
os.makedirs('enhanced_figures', exist_ok=True)

# Define exact figure crops (page 0-indexed, x0, y0, x1, y1) with label margins
fig_crops = {
    # Page 3 (doc[2])
    'fig_170_1_dcta.png': (2, pymupdf.Rect(40, 70, 570, 315)),
    'fig_170_2_fornix.png': (2, pymupdf.Rect(40, 310, 570, 605)),
    
    # Page 4 (doc[3])
    'fig_170_3_frontal_horn.png': (3, pymupdf.Rect(290, 275, 560, 480)),
    'fig_170_4_venous_angle.png': (3, pymupdf.Rect(40, 460, 305, 755)),
    'fig_170_5_tela_choroidea.png': (3, pymupdf.Rect(300, 470, 560, 755)),
    
    # Page 5 (doc[4])
    'fig_170_6_cross_sections.png': (4, pymupdf.Rect(40, 65, 235, 680)),
    
    # Page 6 (doc[5])
    'fig_170_7_third_ventricle.png': (5, pymupdf.Rect(40, 65, 560, 240)),
    
    # Page 7 (doc[6])
    'fig_170_8_fourth_ventricle_floor.png': (6, pymupdf.Rect(40, 65, 565, 560)),
    
    # Page 8 (doc[7])
    'fig_170_9_pica_segments.png': (7, pymupdf.Rect(40, 65, 300, 430)),
    
    # Page 9 (doc[8])
    'fig_170_10_surgical_approaches.png': (8, pymupdf.Rect(110, 65, 490, 335)),
    
    # Page 13 (doc[12])
    'fig_170_11_subependymoma_case.png': (12, pymupdf.Rect(80, 400, 550, 725)),
    
    # Page 15 (doc[14])
    'fig_170_12_third_ventricle_approaches.png': (14, pymupdf.Rect(80, 65, 540, 290)),
    
    # Page 18 (doc[17])
    'fig_170_13_endonasal_case.png': (17, pymupdf.Rect(60, 65, 530, 350)),
    'fig_170_14_cranioorbital_case.png': (17, pymupdf.Rect(60, 370, 530, 660)),
    
    # Page 20 (doc[19])
    'fig_170_15_transfrontal_case.png': (19, pymupdf.Rect(60, 65, 530, 405)),
    
    # Page 21 (doc[20])
    'fig_170_16_hydrocephalus_ct.png': (20, pymupdf.Rect(60, 65, 540, 370)),
    'fig_170_17_transchoroidal_case.png': (20, pymupdf.Rect(60, 370, 555, 715)),
    
    # Page 24 (doc[23])
    'fig_170_18_etv_case.png': (23, pymupdf.Rect(60, 65, 530, 375)),
    
    # Page 25 (doc[24])
    'fig_170_19_coz_case.png': (24, pymupdf.Rect(60, 65, 540, 350)),
    
    # Page 26 (doc[25])
    'fig_170_20_telovelar_ependymoma_case.png': (25, pymupdf.Rect(60, 65, 530, 340))
}

print(f"Rendering {len(fig_crops)} complete figures with all labels and arrows at 300 DPI...")
for fname, (pno, rect) in fig_crops.items():
    page = doc[pno]
    # Render at 300 DPI (approx 4.16x zoom over 72 DPI)
    pix = page.get_pixmap(dpi=300, clip=rect)
    out_path = os.path.join('enhanced_figures', fname)
    pix.save(out_path)
    print(f"✓ Saved {fname}: {pix.width}x{pix.height} ({os.path.getsize(out_path)//1024} KB)")

print("All enhanced labeled figures rendered successfully!")

