import sys
sys.stdout.reconfigure(encoding='utf-8')
import pymupdf

doc = pymupdf.open('Youmans and Winn Ventricular Tumors.pdf')

crops = {
    # 1. Page 3: Fig 170.1 dCTA (top 3 panels A, B, C)
    # Images are at y=72 to 196, caption is at y=200.3
    "fig_170_1_dcta.png": (2, pymupdf.Rect(90, 70, 540, 198)),

    # 2. Page 3: Fig 170.2 Fornix (right side panels A & B)
    # Images at x=326 to 566, y=237 to 606. Caption is below at y=609.8. Text column on left is x<310.
    "fig_170_2_fornix.png": (2, pymupdf.Rect(320, 235, 568, 608)),

    # 3. Page 4: Fig 170.3 Frontal horn cuts
    # Images at y=282 to 466. Caption is below at y=478.1.
    "fig_170_3_frontal_horn.png": (3, pymupdf.Rect(44, 280, 552, 468)),

    # 4. Page 4: Fig 170.4 Venous angle (Panel A)
    # Image at x=225 to 407, y=531 to 746. Caption is on left (x<240).
    "fig_170_4_venous_angle.png": (3, pymupdf.Rect(220, 530, 407, 747)),

    # 5. Page 4: Fig 170.5 Tela choroidea & ICVs (Panel B)
    # Image at x=408 to 560, y=531 to 746. Caption is above at y=470-519.
    "fig_170_5_tela_choroidea.png": (3, pymupdf.Rect(406, 530, 560, 747)),

    # 6. Page 5: Fig 170.6 Cross sections (left column A & B)
    # Image at x=66.7 to 218.4, y=72.2 to 670.4. Caption is at y=674.6.
    "fig_170_6_cross_sections.png": (4, pymupdf.Rect(60, 70, 225, 672)),

    # 7. Page 6: Fig 170.7 Third ventricle sagittal & roof layers (A & B)
    # Images at y=72 to 226. Caption is at y=230.3.
    "fig_170_7_third_ventricle.png": (5, pymupdf.Rect(60, 70, 535, 228)),

    # 8. Page 7: Fig 170.8 Fourth ventricle floor & roof (A, B, C, D, E)
    # Images at y=72 to 554. Caption is at y=558.8.
    "fig_170_8_fourth_ventricle_floor.png": (6, pymupdf.Rect(80, 70, 550, 556)),

    # 9. Page 8: Fig 170.9 PICA segments
    # Images at y=72 to 417. Caption is at y=421.4.
    "fig_170_9_pica_segments.png": (7, pymupdf.Rect(65, 70, 285, 419)),

    # 10. Page 9: Fig 170.10 Surgical corridors matrix
    # Diagram at y=72 to 318. Caption is at y=330.9.
    "fig_170_10_surgical_approaches.png": (8, pymupdf.Rect(135, 70, 465, 322)),

    # 11. Page 13: Fig 170.11 Subependymoma case
    # Scans at y=413 to 714. Caption is at y=718.4.
    "fig_170_11_subependymoma_case.png": (12, pymupdf.Rect(95, 410, 535, 716)),

    # 12. Page 15: Fig 170.12 Third ventricle approaches
    # Diagrams at y=72 to 277. Caption is at y=281.1.
    "fig_170_12_third_ventricle_approaches.png": (14, pymupdf.Rect(110, 70, 515, 279)),

    # 13. Page 18: Fig 170.13 Endonasal prolactinoma case
    # Scans at y=72 to 351. Caption is at y=355.1.
    "fig_170_13_endonasal_case.png": (17, pymupdf.Rect(80, 70, 515, 353)),

    # 14. Page 18: Fig 170.14 Cranio-orbital macroadenoma case
    # Scans at y=388 to 651. Caption is at y=655.8.
    "fig_170_14_cranioorbital_case.png": (17, pymupdf.Rect(80, 385, 515, 653)),

    # 15. Page 20: Fig 170.15 Transfrontal transforaminal colloid cyst case
    # Scans at y=72 to 393. Caption is at y=397.4.
    "fig_170_15_transfrontal_case.png": (19, pymupdf.Rect(80, 70, 515, 395)),

    # 16. Page 21: Fig 170.16 Hydrocephalus CT & colloid cyst resection
    # Scans at y=72 to 342. Caption is at y=346.5.
    "fig_170_16_hydrocephalus_ct.png": (20, pymupdf.Rect(72, 70, 556, 344)),

    # 17. Page 21: Fig 170.17 Interhemispheric transchoroidal metastasis case
    # Scans at y=442 to 709. Caption is at y=713.1.
    "fig_170_17_transchoroidal_case.png": (20, pymupdf.Rect(95, 440, 535, 711)),

    # 18. Page 24: Fig 170.18 ETV & supracerebellar infratentorial tumor case
    # Scans at y=72 to 362. Caption is at y=366.3.
    "fig_170_18_etv_case.png": (23, pymupdf.Rect(80, 70, 515, 364)),

    # 19. Page 25: Fig 170.19 Cranio-orbitozygomatic (COZ) craniopharyngioma case
    # Scans at y=72 to 338. Caption is at y=342.8.
    "fig_170_19_coz_case.png": (24, pymupdf.Rect(95, 70, 532, 340)),

    # 20. Page 26: Fig 170.20 Telovelar 4th ventricle ependymoma resection case
    # Scans & operative photos at y=72 to 327. Caption is at y=331.6.
    "fig_170_20_telovelar_ependymoma_case.png": (25, pymupdf.Rect(80, 70, 515, 329))
}

print(f"Verifying text exclusion in all {len(crops)} crops...")
for fname, (pno, rect) in crops.items():
    page = doc[pno]
    text_inside = page.get_text("text", clip=rect).strip()
    # Check if there is any 'Figure 170' in text_inside
    has_fig_label = "Figure 170." in text_inside or "Fig. 170." in text_inside
    lines = [line.strip() for line in text_inside.split('\n') if len(line.strip()) > 0]
    print(f"[{fname}] Text lines: {len(lines)}, Has caption header: {has_fig_label}")
    if has_fig_label:
        print(f"  WARNING: Caption header found in {fname}!")

