import os, sys
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

doc = pymupdf.open('Youmans and Winn Ventricular Tumors.pdf')
out_dir = 'enhanced_figures'
os.makedirs(out_dir, exist_ok=True)

crops = {
    # 1. Page 3: Fig 170.1 dCTA (top 3 panels A, B, C)
    "fig_170_1_dcta.png": (2, pymupdf.Rect(90, 70, 540, 198)),

    # 2. Page 3: Fig 170.2 Fornix (right side panels A & B)
    "fig_170_2_fornix.png": (2, pymupdf.Rect(320, 235, 568, 608)),

    # 3. Page 4: Fig 170.3 Frontal horn cuts (Panels A & B)
    "fig_170_3_frontal_horn.png": (3, pymupdf.Rect(44, 280, 552, 468)),

    # 4. Page 4: Fig 170.4 Venous angle (Panel A: Caudate, Septal & Thalamostriate Veins)
    "fig_170_4_venous_angle.png": (3, pymupdf.Rect(220, 530, 407, 747)),

    # 5. Page 4: Fig 170.5 Tela choroidea & ICVs (Panel B: Velum Interpositum & ICVs)
    "fig_170_5_tela_choroidea.png": (3, pymupdf.Rect(406, 530, 560, 747)),

    # 6. Page 5: Fig 170.6 Cross sections (Panels A & B)
    "fig_170_6_cross_sections.png": (4, pymupdf.Rect(60, 70, 225, 672)),

    # 7. Page 6: Fig 170.7 Third ventricle sagittal & roof layers (Panels A & B)
    "fig_170_7_third_ventricle.png": (5, pymupdf.Rect(60, 70, 535, 228)),

    # 8. Page 7: Fig 170.8 Fourth ventricle floor & roof (Panels A, B, C, D, E)
    "fig_170_8_fourth_ventricle_floor.png": (6, pymupdf.Rect(80, 70, 550, 556)),

    # 9. Page 8: Fig 170.9 PICA segments (Panels A & B)
    "fig_170_9_pica_segments.png": (7, pymupdf.Rect(65, 70, 285, 419)),

    # 10. Page 9: Fig 170.10 Surgical corridors matrix
    "fig_170_10_surgical_approaches.png": (8, pymupdf.Rect(135, 70, 465, 322)),

    # 11. Page 13: Fig 170.11 Subependymoma case (Scans A–F)
    "fig_170_11_subependymoma_case.png": (12, pymupdf.Rect(95, 410, 535, 716)),

    # 12. Page 15: Fig 170.12 Third ventricle approaches (Panels A & B)
    "fig_170_12_third_ventricle_approaches.png": (14, pymupdf.Rect(110, 70, 515, 279)),

    # 13. Page 18: Fig 170.13 Endonasal prolactinoma case (Scans A–F)
    "fig_170_13_endonasal_case.png": (17, pymupdf.Rect(80, 70, 515, 353)),

    # 14. Page 18: Fig 170.14 Cranio-orbital macroadenoma case (Scans A–F)
    "fig_170_14_cranioorbital_case.png": (17, pymupdf.Rect(80, 385, 515, 653)),

    # 15. Page 20: Fig 170.15 Transfrontal transforaminal colloid cyst case (Scans A–F)
    "fig_170_15_transfrontal_case.png": (19, pymupdf.Rect(80, 70, 515, 395)),

    # 16. Page 21: Fig 170.16 Hydrocephalus CT & colloid cyst resection (Scans A–H)
    "fig_170_16_hydrocephalus_ct.png": (20, pymupdf.Rect(72, 70, 556, 344)),

    # 17. Page 21: Fig 170.17 Interhemispheric transchoroidal metastasis case (Scans A–F)
    "fig_170_17_transchoroidal_case.png": (20, pymupdf.Rect(95, 440, 535, 711)),

    # 18. Page 24: Fig 170.18 ETV & supracerebellar infratentorial tumor case (Scans A–F)
    "fig_170_18_etv_case.png": (23, pymupdf.Rect(80, 70, 515, 364)),

    # 19. Page 25: Fig 170.19 Cranio-orbitozygomatic (COZ) craniopharyngioma case (Scans A–F)
    "fig_170_19_coz_case.png": (24, pymupdf.Rect(95, 70, 532, 340)),

    # 20. Page 26: Fig 170.20 Telovelar 4th ventricle ependymoma resection case (Scans & Views A–F)
    "fig_170_20_telovelar_ependymoma_case.png": (25, pymupdf.Rect(80, 70, 515, 329))
}

print(f"Extracting {len(crops)} clean 300 DPI figures (strictly images + callouts, zero body/caption text)...")
for fname, (pno, rect) in crops.items():
    page = doc[pno]
    pix = page.get_pixmap(dpi=300, clip=rect)
    out_path = os.path.join(out_dir, fname)
    pix.save(out_path)
    print(f"✓ Cleanly extracted {fname}: {pix.width}x{pix.height} ({os.path.getsize(out_path)//1024} KB)")

print("All 20 clean figures extracted successfully!")

