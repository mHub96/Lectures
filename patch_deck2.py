# patch_deck2.py
with open('deck2_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('extracted_pdf_images/p6_img1_63.jpeg', 'enhanced_figures/fig_170_7_third_ventricle.png'),
    ('FIG 170.7A: MIDSAGITTAL THIRD VENTRICLE', 'FIG 170.7: MIDSAGITTAL THIRD VENTRICLE & SURROUNDING ROOF'),
    ('extracted_pdf_images/p6_img2_68.jpeg', 'enhanced_figures/fig_170_7_third_ventricle.png'),
    ('FIG 170.7B: THE 5 ROOF LAYERS & VELUM INTERPOSITUM', 'FIG 170.7: THE FIVE ROOF LAYERS & VELUM INTERPOSITUM'),
    ('extracted_pdf_images/p4_img3_39.jpeg', 'enhanced_figures/fig_170_5_tela_choroidea.png'),
    ('FIG 170.5: INTERNAL CEREBRAL VEINS IN ROOF', 'FIG 170.5: INTERNAL CEREBRAL VEINS IN ROOF & TELA CHOROIDEA'),
    ('extracted_pdf_images/p15_img1_169.jpeg', 'enhanced_figures/fig_170_12_third_ventricle_approaches.png'),
    ('FIG 170.12A: TRANSFORAMINAL APPROACH', 'FIG 170.12: THIRD VENTRICLE APPROACHES (TRANSFORAMINAL & TRANSCHOROIDAL)'),
    ('extracted_pdf_images/p15_img2_173.jpeg', 'enhanced_figures/fig_170_12_third_ventricle_approaches.png'),
    ('FIG 170.12B: TRANSCHOROIDAL APPROACH (WEN)', 'FIG 170.12: TRANSCHOROIDAL CORRIDOR & CHOROIDAL FISSURE OPENING'),
    ('extracted_pdf_images/p21_img11_220.png', 'enhanced_figures/fig_170_17_transchoroidal_case.png'),
    ('FIG 170.17: INTERHEMISPHERIC TRANSCHOROIDAL', 'FIG 170.17: INTERHEMISPHERIC TRANSCHOROIDAL CASE OUTCOME'),
    ('extracted_pdf_images/p3_img2_20.jpeg', 'enhanced_figures/fig_170_2_fornix.png'),
    ('FIG 170.2: BILATERAL FORNICEAL RAPHE', 'FIG 170.2: BILATERAL FORNIX BODY & COMMISSURAL ANATOMY'),
    ('extracted_pdf_images/p18_img10_190.jpeg', 'enhanced_figures/fig_170_14_cranioorbital_case.png'),
    ('FIG 170.14: CRANIO-ORBITAL RESECTION', 'FIG 170.14: CRANIO-ORBITAL RESECTION CASE'),
    ('extracted_pdf_images/p18_img11_186.jpeg', 'enhanced_figures/fig_170_13_endonasal_case.png'),
    ('FIG 170.13: EXPANDED ENDONASAL EEA', 'FIG 170.13: EXPANDED ENDONASAL TRANSCLIVAL / TRANSSPHENIDAL CASE'),
    ('extracted_pdf_images/p20_img2_203.jpeg', 'enhanced_figures/fig_170_15_transfrontal_case.png'),
    ('FIG 170.15: TRANSFRONTAL TRANSFORAMINAL CASE', 'FIG 170.15: TRANSFRONTAL TRANSFORAMINAL CASE CORRIDOR'),
    ('extracted_pdf_images/p9_img14_122.jpeg', 'enhanced_figures/fig_170_10_surgical_approaches.png'),
    ('extracted_pdf_images/p9_img17_143.jpeg', 'enhanced_figures/fig_170_10_surgical_approaches.png'),
    ('extracted_pdf_images/p7_img1_77.jpeg', 'enhanced_figures/fig_170_8_fourth_ventricle_floor.png'),
    ('extracted_pdf_images/p7_img2_75.jpeg', 'enhanced_figures/fig_170_8_fourth_ventricle_floor.png'),
    ('FIG 170.8B: TENT-LIKE ROOF SEGMENTS', 'FIG 170.8: FOURTH VENTRICLE ROOF & VELAR ARCHITECTURE'),
    ('extracted_pdf_images/p8_img1_85.jpeg', 'enhanced_figures/fig_170_9_pica_segments.png'),
    ('FIG 170.9: PICA FIVE ANATOMIC SEGMENTS', 'FIG 170.9: PICA ANATOMIC SEGMENTS & TELOVELAR VASCULAR RELATIONS'),
    ('extracted_pdf_images/p26_img1_255.jpeg', 'enhanced_figures/fig_170_20_telovelar_ependymoma_case.png'),
    ('FIG 170.20: TELOVELAR ENTRY & RESECTION', 'FIG 170.20: TELOVELAR CORRIDOR & OPERATIVE VIEWS'),
    ('extracted_pdf_images/p26_img2_253.jpeg', 'enhanced_figures/fig_170_20_telovelar_ependymoma_case.png'),
    ('FIG 170.20: PRESERVATION OF INFERIOR VERMIS', 'FIG 170.20: INFERIOR VERMIAN PRESERVATION IN TELOVELAR APPROACH'),
    ('extracted_pdf_images/p7_img4_79.jpeg', 'enhanced_figures/fig_170_8_fourth_ventricle_floor.png'),
    ('FIG 170.8: FLOOR LANDMARKS & PRECAUTIONS', 'FIG 170.8: RHOMBOID FOSSA NUCLEAR DANGER ZONES & ENTRY PRECAUTIONS'),
    ('extracted_pdf_images/p26_img3_258.jpeg', 'enhanced_figures/fig_170_20_telovelar_ependymoma_case.png'),
    ('FIG 170.20: EPENDYMOMA POST-OP MRI', 'FIG 170.20: FOURTH VENTRICULAR EPENDYMOMA MRI & RESECTION'),
    ('extracted_pdf_images/p9_img15_105.jpeg', 'enhanced_figures/fig_170_10_surgical_approaches.png'),
    ('SURGICAL EXCELLENCE IN VENTRICULAR NEURO-ONCOLOGY', 'FIG 170.10: COMPREHENSIVE VENTRICULAR SURGICAL CORRIDORS')
]

for old, new in replacements:
    assert old in content, f'Missing: {old}'
    content = content.replace(old, new)

thank_you_slide = '''    # Slide 33: Cartoonish Thank You & Discussion (User Requested)
    {
        "type": "thankyou",
        "badge": "COMPLETION OF MASTERCLASS • QUESTIONS & ANSWERS",
        "title": "Thank You for Your Engagement!",
        "subtitle": "Mastery of Ventricular Tumors: Microanatomy, Surgical Corridors & Pathology.",
        "cards": [
            ("Masterclass Completed!", "Full mastery achieved across both Part 1 (Lateral Ventricles) and Part 2 (Third & Fourth Ventricles, Surgical Approaches, WHO Pathology)."),
            ("Key Tenets to Remember", "Respect deep veins (ICV, Galen), spare the vermis with telovelar entry, protect rhomboid fossa floor, and tailor resection to tumor histology."),
            ("Interactive Knowledge Quiz", "Test your comprehension with the interactive 10-question masterclass board examination quiz!"),
            ("Open Discussion & Questions", "Floor is now open for clinical questions, surgical case discussions, and technical dissection considerations.")
        ],
        "img_path": "assets_images/part2_thankyou.jpg",
        "caption_title": "ARTISTIC LECTURE ARTWORK: CONGRATULATIONS!",
        "caption_body": "Special educational masterclass illustration: Congratulations on completing the Ventricular Tumors Masterclass!"
    }
]
'''

assert content.strip().endswith(']'), 'Expected list closing bracket'
content = content.rstrip()[:-1].rstrip() + ',\n' + thank_you_slide

with open('deck2_data.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Successfully updated deck2_data.py!')

