# deck2_data.py - Data for Ventricular Tumors Part 2: Third & Fourth Ventricles, Approaches & Pathology

DECK2_SLIDES = [
    # Slide 1: Title
    {
        "type": "title",
        "badge": "YOUMANS & WINN COMPREHENSIVE MASTERCLASS • PART 2",
        "title": "Third & Fourth Ventricles:\nApproaches & Histopathology",
        "subtitle": "Transchoroidal corridors, telovelar microsurgery, and specific tumor biological classification.",
        "img_path": "assets_images/third_ventricle.jpg",
        "credits": [
            "Source: Youmans & Winn Neurological Surgery (Chapter 170: Ventricular Tumors)",
            "Curriculum: Third & Fourth Ventricular Corridors, Pineal Region & Telovelar Microsurgery",
            "Pathology: WHO CNS Classification, Molecular Stratification & Surgical Resection Outcomes"
        ]
    },
    # Slide 2: Surgical Topography
    {
        "type": "content",
        "badge": "SURGICAL TOPOGRAPHY • THIRD VENTRICLE",
        "title": "Third Ventricular Core Boundaries",
        "subtitle": "Midline cleft nestled between bilateral thalami and hypothalami, connecting anterior and posterior CSF pathways.",
        "cards": [
            ("Lateral Walls & Hypothalamic Sulcus", "Formed by medial surfaces of bilateral thalami superiorly and hypothalami inferiorly; demarcated by hypothalamic sulcus."),
            ("Massa Intermedia (Interthalamic Adhesion)", "Traverses ventricular cavity connecting bilateral thalami in 75% of individuals; may be divided safely if obstructing view."),
            ("Ventral Floor & Recesses", "Extends from optic chiasm anteriorly through infundibular recess, tuber cinereum, mamillary bodies, and posterior perforated substance."),
            ("Anterior & Posterior Limits", "Anterior: Lamina terminalis and anterior commissure; Posterior: Pineal recess, posterior commissure, and aqueduct of Sylvius.")
        ],
        "img_path": "enhanced_figures/fig_170_7_third_ventricle.png",
        "caption_title": "FIG 170.7: MIDSAGITTAL THIRD VENTRICLE & SURROUNDING ROOF",
        "caption_body": "Enlarged sagittal view from Chapter 170 showing third ventricle boundaries, recesses, floor structures, and aqueduct of Sylvius."
    },
    # Slide 3: Diencephalic Anatomy
    {
        "type": "content",
        "badge": "DIENCEPHALIC ANATOMY • ROOF ARCHITECTURE",
        "title": "The Five Layers of the Third Ventricle Roof",
        "subtitle": "The surgical gateway into the third ventricle consists of five distinct micro-anatomical layers.",
        "cards": [
            ("Layer 1: Body of the Fornix", "Paired forniceal bodies united in the midline raphe, forming the superior structural arch of the roof."),
            ("Layer 2: Superior Leaf of Tela Choroidea", "Dorsal pial membrane adhering intimately to the inferior surface of the fornices and hippocampal commissure."),
            ("Layer 3: Velum Interpositum Space", "Vascular space containing paired internal cerebral veins (ICVs) and medial posterior choroidal arteries (MPChA)."),
            ("Layer 4 & 5: Inferior Leaf & Choroid Plexus", "Layer 4: Ventral pial membrane forming ventricular ceiling; Layer 5: Paired choroid plexus ribbons hanging into third ventricle.")
        ],
        "img_path": "enhanced_figures/fig_170_7_third_ventricle.png",
        "caption_title": "FIG 170.7: THE FIVE ROOF LAYERS & VELUM INTERPOSITUM",
        "caption_body": "Global sagittal view from Chapter 170 illustrating the 5-layer stratification of the third ventricular roof and velum interpositum."
    },
    # Slide 4: Vascular Topography
    {
        "type": "content",
        "badge": "VASCULAR TOPOGRAPHY • VELUM INTERPOSITUM",
        "title": "Velum Interpositum Vascular Complex",
        "subtitle": "Critical neurovascular bundle traversing the roof of the third ventricle.",
        "cards": [
            ("Internal Cerebral Veins (ICVs)", "Paired veins course side-by-side beneath fornices in anterior roof, diverging posterolaterally around pineal recess before uniting."),
            ("Great Cerebral Vein of Galen Union", "ICVs join basal veins of Rosenthal beneath splenium of corpus callosum to form the vein of Galen in quadrigeminal cistern."),
            ("Medial Posterior Choroidal Arteries (MPChA)", "Course anteriorly within velum interpositum, giving fine perforating feeders to third ventricle choroid and pineal body."),
            ("Surgical Hazard: ICV Spasm or Thrombosis", "Excessive traction on roof layers causes ICV thrombosis, leading to fatal bilateral thalamic infarction and coma.")
        ],
        "img_path": "enhanced_figures/fig_170_5_tela_choroidea.png",
        "caption_title": "FIG 170.5: INTERNAL CEREBRAL VEINS IN ROOF & TELA CHOROIDEA",
        "caption_body": "Chapter 170 dissection with lateral ventricle body opened, displaying ICVs and MPChA traversing the velum interpositum."
    },
    # Slide 5: Operative Corridors
    {
        "type": "content",
        "badge": "OPERATIVE CORRIDORS • TRANSFORAMINAL",
        "title": "Transforaminal Route & Foraminoplasty",
        "subtitle": "Natural orifice entry through the foramen of Monro into the anterior and middle third ventricle.",
        "cards": [
            ("Natural Orifice Access", "Enters third ventricle without dividing neural tissue; ideal for colloid cysts and small tumors presenting with hydrocephalus."),
            ("Foraminoplasty Technique", "Enlarges constricted foramen of Monro by coagulating and transecting the anterior septal vein proximal to venous angle."),
            ("Posterior Extension (Tenia Fornicis)", "Extending incision posteriorly along choroidal fissure (tenia fornicis) expands working aperture up to 1.5 cm without forniceal traction."),
            ("Limitations", "Working trajectory is confined to anterior and middle third ventricle; poor visualization of posterior third and pineal region.")
        ],
        "img_path": "enhanced_figures/fig_170_12_third_ventricle_approaches.png",
        "caption_title": "FIG 170.12: THIRD VENTRICLE APPROACHES (TRANSFORAMINAL & TRANSCHOROIDAL)",
        "caption_body": "Chapter 170 diagram of transforaminal corridor via anterior transcallosal approach, showing entry through foramen of Monro."
    },
    # Slide 6: Operative Corridors
    {
        "type": "content",
        "badge": "OPERATIVE CORRIDORS • TRANSCHOROIDAL",
        "title": "Transchoroidal Approach (Wen Technique)",
        "subtitle": "Incision through the choroidal fissure between fornix and choroid plexus provides wide atraumatic access.",
        "cards": [
            ("Tenia Fornicis Incision", "Sharp incision along the tenia fornicis (medial attachment of choroid plexus to fornix), sweeping choroid plexus laterally."),
            ("Internal Cerebral Vein Splitting", "Dissection carried between the paired ICVs within the velum interpositum, entering the roof of the third ventricle."),
            ("Forniceal Preservation Advantage", "Avoids any direct traction or manipulation of the anterior forniceal columns, significantly reducing risk of postoperative amnesia."),
            ("Wide Coronal Exposure", "Provides expansive visualization of anterior, middle, and posterior third ventricular cavity through a single lateral corridor.")
        ],
        "img_path": "enhanced_figures/fig_170_12_third_ventricle_approaches.png",
        "caption_title": "FIG 170.12: TRANSCHOROIDAL CORRIDOR & CHOROIDAL FISSURE OPENING",
        "caption_body": "Chapter 170 schematic of transchoroidal dissection opening tenia fornicis to reach third ventricle beneath forniceal body."
    },
    # Slide 7: Operative Comparison
    {
        "type": "content",
        "badge": "OPERATIVE COMPARISON • CHOROIDAL ROUTES",
        "title": "Subchoroidal vs. Transchoroidal Corridors",
        "subtitle": "Anatomical nuances between entering medial vs. lateral to the choroid plexus ribbon.",
        "cards": [
            ("Transchoroidal (Tenia Fornicis)", "Entered medial to choroid plexus; mobilizes plexus laterally with thalamus; provides wider exposure of contralateral third ventricle."),
            ("Subchoroidal (Tenia Choroidea)", "Entered lateral to choroid plexus along stria terminalis/thalamus; keeps fornix and plexus medially; provides direct ipsilateral floor view."),
            ("Neurovascular Risk Profile", "Subchoroidal route runs closer to thalamostriate vein and thalamus; transchoroidal route runs closer to forniceal body and ICVs."),
            ("Selection Rationale", "Transchoroidal is favored for midline or contralateral third ventricular masses; subchoroidal for lesions with prominent lateral thalamic extension.")
        ],
        "img_path": "enhanced_figures/fig_170_17_transchoroidal_case.png",
        "caption_title": "FIG 170.17: INTERHEMISPHERIC TRANSCHOROIDAL CASE OUTCOME",
        "caption_body": "Pre- and postoperative neuroimaging from Chapter 170 demonstrating complete resection of a third ventricular mass via transchoroidal route."
    },
    # Slide 8: Operative Corridors
    {
        "type": "content",
        "badge": "OPERATIVE CORRIDORS • INTERFORNICEAL",
        "title": "The Interforniceal Approach (Busch)",
        "subtitle": "Direct midline entry dividing the raphe between bilateral forniceal bodies.",
        "cards": [
            ("Midline Raphe Division", "Incision placed strictly in midline between paired bodies of fornix beneath the septum pellucidum."),
            ("Direct Symmetrical Exposure", "Provides direct, orthogonal visualization into the center of the third ventricle; excellent for giant colloid cysts and hypothalamic hamartomas."),
            ("Risk of Severe Memory Loss", "Excessive posterior dissection (>1.5 cm) or bilateral lateral retraction causes irreversible damage to hippocampal commissure and forniceal tracts."),
            ("Current Surgical Consensus", "Largely superseded by transchoroidal approach due to significantly lower risk of bilateral limbic memory impairment.")
        ],
        "img_path": "enhanced_figures/fig_170_2_fornix.png",
        "caption_title": "FIG 170.2: BILATERAL FORNIX BODY & COMMISSURAL ANATOMY",
        "caption_body": "Anatomy of paired forniceal bodies in relation to third ventricle roof, emphasizing the narrow margin of safety during interforniceal entry."
    },
    # Slide 9: Anterior Routes
    {
        "type": "content",
        "badge": "ANTERIOR ROUTES • SKULL BASE",
        "title": "Subfrontal & Cranio-Orbital Corridors",
        "subtitle": "Anterior cranial base approaches targeting suprasellar tumors extending into the anterior third ventricle.",
        "cards": [
            ("Subfrontal Trans-Lamina Terminalis", "Unilateral or bifrontal craniotomy; optic chiasm and ACom complex visualized; lamina terminalis opened to enter anterior floor."),
            ("Cranio-Orbital (Frontotemporal-Orbital)", "Orbital osteotomy lowers approach angle by 10–15°, minimizing frontal lobe retraction and improving superior visualization."),
            ("Indications", "Craniopharyngiomas, pituitary macroadenomas, tuberculum sellae meningiomas, and optic pathway gliomas invading third ventricle."),
            ("Hypothalamic Preservation", "Critical to preserve anterior communicating artery perforators supplying the optic chiasm, hypothalamus, and lamina terminalis.")
        ],
        "img_path": "enhanced_figures/fig_170_14_cranioorbital_case.png",
        "caption_title": "FIG 170.14: CRANIO-ORBITAL RESECTION CASE",
        "caption_body": "Chapter 170 case illustration of cranio-orbital subfrontal approach for resection of a large retrochiasmatic suprasellar lesion."
    },
    # Slide 10: Skull Base Endoscopy
    {
        "type": "content",
        "badge": "SKULL BASE ENDOSCOPY • ENDONASAL",
        "title": "Expanded Endoscopic Endonasal (EEA)",
        "subtitle": "Transsphenoidal, transtuberculum, and transplanum routes into the anterior and ventral third ventricle.",
        "cards": [
            ("Transtuberculum / Transplanum Corridor", "Removal of planum sphenoidale and tuberculum sellae; provides direct ventral access without brain retraction."),
            ("Direct In-Line Ventral Visualization", "Direct line of sight to retrochiasmatic space, optic chiasm undersurface, pituitary stalk, and third ventricular floor."),
            ("Vascular Considerations", "Must identify and protect internal carotid arteries laterally and anterior communicating artery complex superiorly."),
            ("Vascularized Nasoseptal Flap (Hadad-Bassagasteguy)", "Essential for skull base reconstruction to prevent high-flow postoperative CSF fistulas and bacterial meningitis.")
        ],
        "img_path": "enhanced_figures/fig_170_13_endonasal_case.png",
        "caption_title": "FIG 170.13: EXPANDED ENDONASAL TRANSCLIVAL / TRANSSPHENIDAL CASE",
        "caption_body": "Chapter 170 endoscopic endonasal transsphenoidal resection of a giant third ventricular adenoma with pituitary stalk preservation."
    },
    # Slide 11: Decision Matrix
    {
        "type": "content",
        "badge": "DECISION MATRIX • THIRD VENTRICLE",
        "title": "Third Ventricular Approach Selection",
        "subtitle": "Algorithm stratifying corridor selection based on tumor origin, growth axis, and foramen of Monro patency.",
        "cards": [
            ("Roof / Foramen of Monro Lesions (Colloid Cyst)", "Transcallosal Transforaminal or Transchoroidal approach; highly direct with low morbidity."),
            ("Intraventricular with Ventriculomegaly", "Transfrontal Transcortical approach into lateral ventricle then transforaminal into third ventricle."),
            ("Retrochiasmatic / Suprasellar Origin (Craniopharyngioma)", "Expanded Endoscopic Endonasal (EEA) or Subfrontal/Cranio-orbital approach."),
            ("Posterior Third / Pineal Region Tumors", "Infratentorial Supracerebellar (Krause) or Occipital Transtentorial (Jamieson/Poppen) approach.")
        ],
        "img_path": "enhanced_figures/fig_170_15_transfrontal_case.png",
        "caption_title": "FIG 170.15: TRANSFRONTAL TRANSFORAMINAL CASE CORRIDOR",
        "caption_body": "Pre- and postoperative MRI from Chapter 170 demonstrating complete removal of a third ventricular mass via transfrontal transforaminal corridor."
    },
    # Slide 12: Pineal Region
    {
        "type": "content",
        "badge": "PINEAL REGION • QUADRIGEMINAL CISTERN",
        "title": "Pineal & Quadrigeminal Relationships",
        "subtitle": "Anatomical crossroads bordered by splenium, quadrigeminal plate, culmen of cerebellum, and the Galenic venous confluence.",
        "cards": [
            ("Anterior & Inferior Boundaries", "Anterior: Third ventricle posterior wall and habenular commissure; Inferior: Superior and inferior colliculi (tectal plate)."),
            ("Superior & Posterior Boundaries", "Superior: Splenium of corpus callosum; Posterior: Culmen of cerebellar vermis and straight sinus."),
            ("Neurovascular Convergence", "Enclosed by the Great Vein of Galen, basal veins of Rosenthal, internal cerebral veins, and trochlear nerves (CN IV)."),
            ("Surgical Challenges", "Deep narrow working corridors; high density of critical deep veins; high sensitivity of tectal plate to surgical manipulation.")
        ],
        "img_path": "assets_images/pineal_gland_wiki.jpg",
        "caption_title": "PINEAL GLAND & DORSAL MIDBRAIN ANATOMY",
        "caption_body": "Midsagittal dissection highlighting pineal gland, quadrigeminal cistern, and venous relations beneath the splenium."
    },
    # Slide 13: Posterior Corridors
    {
        "type": "content",
        "badge": "POSTERIOR CORRIDORS • SUPRACEREBELLAR",
        "title": "Supracerebellar Infratentorial (Krause)",
        "subtitle": "The standard suboccipital infratentorial corridor accessing the pineal region and posterior third ventricle.",
        "cards": [
            ("Patient Positioning Options", "Sitting (optimal gravity drainage and venous decompression, but risk of air embolism) or Concorde / Prone Concorde position."),
            ("Suboccipital Infratentorial Trajectory", "Follows superior surface of cerebellar culmen beneath tentorium into quadrigeminal cistern; entirely below deep veins."),
            ("Arachnoid & Bridging Vein Division", "Release of supracerebellar bridging veins allows cerebellum to relax downward, opening natural corridor to pineal tumor."),
            ("Deep Vein Topography", "Tumor is approached ventral to the vein of Galen and internal cerebral veins, protecting these vessels from traction.")
        ],
        "img_path": "enhanced_figures/fig_170_10_surgical_approaches.png",
        "caption_title": "FIG 170.10: SUPRACEREBELLAR INFRATENTORIAL TRAJECTORY",
        "caption_body": "Chapter 170 schematic illustrating the infratentorial trajectory following the cerebellar surface to the posterior third ventricle."
    },
    # Slide 14: Approach Selection
    {
        "type": "content",
        "badge": "APPROACH SELECTION • TENTORIAL ANGLE",
        "title": "The Torcular-to-Pineal Line Rule",
        "subtitle": "The slope of the tentorium cerebelli dictates selection between supracerebellar and occipital transtentorial routes.",
        "cards": [
            ("Torcular-to-Pineal Line Concept", "Straight line drawn on sagittal MRI from torcular Herophili to pineal gland determines approach trajectory clearance."),
            ("Flat / Shallow Tentorium (<45°)", "Favors Infratentorial Supracerebellar Approach; provides generous trajectory over cerebellar culmen into posterior third ventricle."),
            ("Steep / High-Slope Tentorium (>45°)", "Infratentorial view is obstructed by tentorial steepness; favors Occipital Transtentorial Approach to reach superior tumor pole."),
            ("Tumor Projection Vector", "Tumors extending superiorly into velum interpositum favor occipital transtentorial; lesions extending into fourth ventricle favor supracerebellar.")
        ],
        "img_path": "assets_images/fourth_ventricle.jpg",
        "caption_title": "TENTORIAL SLOPE & INFRATENTORIAL SPACE",
        "caption_body": "Sagittal neuroanatomy demonstrating the relationship between the straight sinus, tentorial angle, and cerebellar culmen."
    },
    # Slide 15: Posterior Corridors
    {
        "type": "content",
        "badge": "POSTERIOR CORRIDORS • TRANSTENTORIAL",
        "title": "Occipital Transtentorial Route (Jamieson)",
        "subtitle": "Supratentorial paramedian occipital approach with tentorial incision for superiorly projecting pineal lesions.",
        "cards": [
            ("Patient Positioning & Craniotomy", "Prone or modified three-quarters prone; right occipital craniotomy extending to superior sagittal and transverse sinuses."),
            ("Occipital Lobe Retraction", "Medial occipital lobe gently retracted laterally; bridging veins to straight sinus divided if necessary."),
            ("Tentorial Incision (Tentoriotomy)", "Tentorium incised parallel to straight sinus (1–1.5 cm lateral), exposing dorsal midbrain, pineal region, and ambient cistern."),
            ("Key Advantage", "Provides superior-to-inferior visualization of tumors extending above internal cerebral veins into the splenium or velum interpositum.")
        ],
        "img_path": "enhanced_figures/fig_170_10_surgical_approaches.png",
        "caption_title": "FIG 170.10: OCCIPITAL TRANSTENTORIAL ROUTE",
        "caption_body": "Chapter 170 surgical approach schematic demonstrating the supratentorial corridor across the incised tentorium."
    },
    # Slide 16: Fourth Ventricle
    {
        "type": "content",
        "badge": "FOURTH VENTRICLE • RHOMBOID FOSSA",
        "title": "Rhomboid Fossa Floor Anatomy",
        "subtitle": "The delicate floor of the fourth ventricle houses critical cranial nerve nuclei and autonomic centers.",
        "cards": [
            ("Median Sulcus & Sulcus Limitans", "Median sulcus divides floor into halves; Sulcus limitans separates medial motor trigones from lateral sensory vestibular areas."),
            ("Facial Colliculus (Motor Genu)", "Prominence in lower pontine floor formed by facial nerve (CN VII) fibers looping over abducens nucleus (CN VI); must NEVER be touched."),
            ("Striae Medullares & Acoustic Tubercle", "Transverse acoustic fibers dividing pontine and medullary halves of floor; key anatomical orientation landmark."),
            ("Hypoglossal & Vagal Trigones", "Inferior medullary floor triangles: Hypoglossal trigone (CN XII) medially, Vagal trigone (CN X autonomic centers) laterally.")
        ],
        "img_path": "enhanced_figures/fig_170_8_fourth_ventricle_floor.png",
        "caption_title": "FIG 170.8A: FOURTH VENTRICULAR FLOOR (RHOMBOID FOSSA)",
        "caption_body": "Chapter 170 dorsal dissection of fourth ventricular floor detailing facial colliculus, striae medullares, and hypoglossal/vagal trigones."
    },
    # Slide 17: Fourth Ventricle
    {
        "type": "content",
        "badge": "FOURTH VENTRICLE • TENT-LIKE ROOF",
        "title": "Tent-Like Roof Segments",
        "subtitle": "Anatomical division into superior velar, fastigial, and inferior velo-tonsillar compartments.",
        "cards": [
            ("Superior (Cranial) Roof Segment", "Formed by superior cerebellar peduncles (brachia conjunctiva) and superior medullary velum; projects to the fastigium apex."),
            ("The Fastigium (Tentorial Apex)", "Sharp angular junction of cranial and caudal roof segments, projecting deeply into cerebellar vermis."),
            ("Inferior (Caudal) Roof Segment", "Formed by inferior medullary velum, tela choroidea, and paired tonsils of the cerebellum."),
            ("Foramina of Luschka & Magendie", "Lateral apertures (Luschka) at cerebellopontine angles; Midline aperture (Magendie) draining into cisterna magna.")
        ],
        "img_path": "enhanced_figures/fig_170_8_fourth_ventricle_floor.png",
        "caption_title": "FIG 170.8: FOURTH VENTRICLE ROOF & VELAR ARCHITECTURE",
        "caption_body": "Dorsal view from Chapter 170 showing the fastigial apex, inferior medullary velum, and tela choroidea roof architecture."
    },
    # Slide 18: Vascular Topography
    {
        "type": "content",
        "badge": "VASCULAR TOPOGRAPHY • PICA SEGMENTS",
        "title": "Five Segments of the PICA",
        "subtitle": "The posterior inferior cerebellar artery (PICA) has the most complex course of any intracranial artery.",
        "cards": [
            ("1. Anterior Medullary Segment", "Originates from vertebral artery; courses along anterior medulla past hypoglossal nerve rootlets."),
            ("2. Lateral Medullary Segment", "Runs along lateral medulla, passing glossopharyngeal, vagus, and accessory (CN IX, X, XI) rootlets."),
            ("3. Tonsillomedullary Segment", "Loops inferiorly around cerebellar tonsil (infratonsillar loop) toward foramen magnum."),
            ("4. Telovelomedullary Segment", "Ascends along inferior medullary velum into fourth ventricle roof (supratonsillar loop) to supply choroid plexus."),
            ("5. Cortical Branches", "Bifurcates into vermian and hemispheric branches supplying inferior vermis and cerebellar cortex.")
        ],
        "img_path": "enhanced_figures/fig_170_9_pica_segments.png",
        "caption_title": "FIG 170.9: PICA ANATOMIC SEGMENTS & TELOVELAR VASCULAR RELATIONS",
        "caption_body": "Lateral neurovascular dissection from Chapter 170 showing the complex loops of PICA in relation to medulla, tonsils, and roof."
    },
    # Slide 19: Operative Technique
    {
        "type": "content",
        "badge": "OPERATIVE TECHNIQUE • TELOVELAR",
        "title": "Telovelar Approach (Matsushima)",
        "subtitle": "The modern standard corridor to fourth ventricular tumors utilizing natural anatomical clefts.",
        "cards": [
            ("Suboccipital Craniotomy & Cisterna Magna Opening", "Suboccipital midline exposure; arachnoid of cisterna magna opened widely to release CSF and decompress posterior fossa."),
            ("Uvulotonsillar Space Mobilization", "Gentle lateral elevation of cerebellar tonsils away from the uvula and medulla without resecting or splitting neural tissue."),
            ("Tela Choroidea & Inferior Velum Incision", "Opening the transparent tela choroidea and inferior medullary velum provides direct panoramic access to fourth ventricle."),
            ("Full Floor & Apex Visualization", "Exposes from foramen of Magendie inferiorly to the fastigium and aqueduct superiorly through bilateral telovelar opening.")
        ],
        "img_path": "enhanced_figures/fig_170_20_telovelar_ependymoma_case.png",
        "caption_title": "FIG 170.20: TELOVELAR CORRIDOR & OPERATIVE VIEWS",
        "caption_body": "Operative view from Chapter 170 showing telovelar entry, tonsillar mobilization, and tumor dissection in the fourth ventricle."
    },
    # Slide 20: Operative Comparison
    {
        "type": "content",
        "badge": "OPERATIVE COMPARISON • POSTERIOR FOSSA",
        "title": "Telovelar vs. Transvermian Approach",
        "subtitle": "Overcoming the historical morbidity of vermian split through anatomical corridor development.",
        "cards": [
            ("Historical Transvermian Approach", "Splits the inferior cerebellar vermis (nodule, uvula) to reach fourth ventricle roof; damages fastigial and dentate efferents."),
            ("Cerebellar Mutism Syndrome (CMS)", "Dividing inferior vermis causes postoperative transient or permanent mutism, emotional lability, and profound ataxia (seen in up to 25% of children)."),
            ("Telovelar Approach (Vermis-Sparing)", "Obtains equivalent or superior exposure exclusively through natural clefts (tela choroidea / velum) without dividing any vermis."),
            ("Surgical Consensus", "The transvermian approach is now largely obsolete; telovelar entry is the standard of care for fourth ventricular neoplasms.")
        ],
        "img_path": "enhanced_figures/fig_170_20_telovelar_ependymoma_case.png",
        "caption_title": "FIG 170.20: INFERIOR VERMIAN PRESERVATION IN TELOVELAR APPROACH",
        "caption_body": "Post-resection inspection confirming anatomical preservation of the vermis and bilateral tonsils following telovelar dissection."
    },
    # Slide 21: Floor Safety
    {
        "type": "content",
        "badge": "FLOOR SAFETY • NUCLEAR PRECAUTIONS",
        "title": "Fourth Ventricle Floor Precautions",
        "subtitle": "Rigid microsurgical rules to prevent fatal autonomic and cranial nerve dysfunction.",
        "cards": [
            ("Pia-Ependyma Dissection Plane", "Dissect strictly within the tumor-ependyma pseudocapsule; never pull or avulse tumor nodules adherent to rhomboid fossa floor."),
            ("Subtotal Resection Over Infiltrated Floor", "If ependymoma or glioma directly invades the floor nuclei, leave a thin residual cuff; complete resection causes fatal apnea or vegetative state."),
            ("Safe Entry Zones into Brainstem", "Suprafacial and infrafacial triangles permit limited entry into deep intrinsic pontine lesions, avoiding CN VI/VII nuclei."),
            ("Floor Retraction Avoidance", "Never place cottonoids or blade retractors directly against the floor; use gentle irrigation and soft suction on tumor capsule only.")
        ],
        "img_path": "enhanced_figures/fig_170_8_fourth_ventricle_floor.png",
        "caption_title": "FIG 170.8: RHOMBOID FOSSA NUCLEAR DANGER ZONES & ENTRY PRECAUTIONS",
        "caption_body": "Rhomboid fossa landmarks from Chapter 170 highlighting facial colliculus, striae medullares, and nuclear danger zones."
    },
    # Slide 22: Histopathology Spectrum
    {
        "type": "content",
        "badge": "HISTOPATHOLOGY SPECTRUM • WHO GRADING",
        "title": "WHO Grading of Ventricular Neoplasms",
        "subtitle": "Modern CNS tumor classification incorporates histological morphology and integrated molecular diagnostics.",
        "cards": [
            ("WHO Grade I (Benign / Indolent)", "Subependymoma, Pilocytic Astrocytoma, Choroid Plexus Papilloma, Intraventricular Meningioma; cured by gross total resection."),
            ("WHO Grade II (Intermediate / Recurrence Risk)", "Central Neurocytoma, Classic Ependymoma, Atypical Choroid Plexus Papilloma; require vigilant long-term surveillance."),
            ("WHO Grade III (Malignant Neoplasms)", "Anaplastic Ependymoma, Choroid Plexus Carcinoma; high propensity for leptomeningeal CSF seeding; mandate adjuvant chemoradiation."),
            ("Integrated Molecular Classification", "DNA methylation profiling and genetic alterations (e.g., ZFTA-RELA, YAP1, PFA/PFB) supersede traditional histology for prognosis.")
        ],
        "img_path": "assets_images/ependymoma.jpg",
        "caption_title": "WHO VENTRICULAR HISTOPATHOLOGY SPECTRUM",
        "caption_body": "Microscopic spectrum of neuroepithelial ventricular neoplasms demonstrating characteristic cellular architecture and rosettes."
    },
    # Slide 23: Tumor Pathology
    {
        "type": "content",
        "badge": "TUMOR PATHOLOGY • EPENDYMOMA",
        "title": "Ependymoma: Biology & Morphology",
        "subtitle": "Glial neoplasm arising from radial glia / ependymal lining cells of the ventricular system.",
        "cards": [
            ("Perivascular Pseudorosettes", "Pathognomonic hallmark: Tumor cell processes radiating toward central blood vessels, creating an anuclear perivascular fibrillary cuff."),
            ("True Ependymal Rosettes", "Tumor cells arranged radially around a central lumen lined by microvilli and cilia; diagnostic but less commonly encountered."),
            ("Immunohistochemistry Profile", "Strongly positive for GFAP (in perivascular processes), Vimentin, S100, and characteristic dot-like or ring-like EMA perinuclear positivity."),
            ("Surgical Objective", "Gross total resection is the single most powerful prognostic factor for event-free and overall survival across all age groups.")
        ],
        "img_path": "assets_images/ependymoma.jpg",
        "caption_title": "EPENDYMOMA: PERIVASCULAR PSEUDOROSETTES",
        "caption_body": "High-power H&E histology displaying classic perivascular pseudorosettes with dense radiating fibrillary glial processes around central capillaries."
    },
    # Slide 24: Molecular Subgroups
    {
        "type": "content",
        "badge": "MOLECULAR SUBGROUPS • EPENDYMOMA",
        "title": "Ependymoma: Molecular Stratification",
        "subtitle": "Current WHO classification divides ependymomas into distinct anatomical, epigenetic, and oncogenic subgroups.",
        "cards": [
            ("Posterior Fossa Group A (PF-EPN-A)", "Infants and young children; H3K27me3 global loss of trimethylation; aggressive course; high recurrence and seeding rates."),
            ("Posterior Fossa Group B (PF-EPN-B)", "Older children and adults; retained H3K27me3; indolent clinical course; high rate of cure following gross total resection."),
            ("Supratentorial ZFTA (RELA) Fusion", "ZFTA-RELA gene fusion activates oncogenic NF-κB pathway; frequent cystic/solid presentation with poor outcome if subtotal."),
            ("Supratentorial YAP1 Fusion", "Young children; YAP1-MAMLD1 gene fusions; favorable prognosis following complete surgical resection.")
        ],
        "img_path": "enhanced_figures/fig_170_20_telovelar_ependymoma_case.png",
        "caption_title": "FIG 170.20: FOURTH VENTRICULAR EPENDYMOMA MRI & RESECTION",
        "caption_body": "Chapter 170 case showing gross total resection of a fourth ventricular ependymoma with re-established CSF pathways."
    },
    # Slide 25: Tumor Pathology
    {
        "type": "content",
        "badge": "TUMOR PATHOLOGY • SUBEPENDYMOMA",
        "title": "Subependymoma (WHO Grade I)",
        "subtitle": "Benign, slow-growing ependymal neoplasm typically discovered incidentally in older adults.",
        "cards": [
            ("Histopathological Hallmark", "Nodular clusters of uniform, isomorphic nuclei embedded within an abundant dense fibrillary glial background with microcystic degeneration."),
            ("Common Locations", "Fourth ventricle (50–60%) and frontal horns / septum pellucidum near the foramen of Monro (30–40%)."),
            ("Radiological Features", "Well-circumscribed, lobular, non-enhancing or minimally enhancing mass on T1 post-contrast MRI; low T2/FLAIR edema."),
            ("Prognosis & Management", "Surgical cure achieved via gross total resection; asymptomatic incidental lesions can be safely observed with serial imaging.")
        ],
        "img_path": "assets_images/subependymoma.jpg",
        "caption_title": "SUBEPENDYMOMA: CLUSTERED NUCLEI & GLIA",
        "caption_body": "Histology of subependymoma displaying islands of uniform round nuclei set in a dense, acellular fibrillary matrix with microcysts."
    },
    # Slide 26: Tumor Pathology
    {
        "type": "content",
        "badge": "TUMOR PATHOLOGY • NEUROCYTOMA",
        "title": "Central Neurocytoma (WHO Grade II)",
        "subtitle": "Neuronal intraventricular neoplasm typically presenting in young adults (20–40 years of age).",
        "cards": [
            ("Classic Location & Septal Attachment", "Arises almost exclusively in anterior lateral ventricle attached to septum pellucidum near foramen of Monro."),
            ("Histology: 'Fried-Egg' Appearance", "Uniform round cells with clear perinuclear halos and delicate chromatin; easily misdiagnosed as oligodendroglioma or ependymoma."),
            ("Immunohistochemical Differentiation", "Diffusely and strongly positive for Synaptophysin, NeuN, and MAP2; GFAP is negative in tumor cells (only positive in reactive astrocytes)."),
            ("MIB-1 / Ki-67 Proliferation Index", "Ki-67 <2% indicates classic indolent course; Ki-67 >3% ('Atypical Central Neurocytoma') portends higher recurrence risk requiring adjuvant radiation.")
        ],
        "img_path": "assets_images/central_neurocytoma.jpg",
        "caption_title": "CENTRAL NEUROCYTOMA: MRI & FRIED-EGG CELLS",
        "caption_body": "Axial MR image showing characteristic bubbly, heterogeneous intraventricular mass at foramen of Monro with septal attachment."
    },
    # Slide 27: Pediatric Gliomas
    {
        "type": "content",
        "badge": "PEDIATRIC GLIOMAS • PILOCYTIC ASTROCYTOMA",
        "title": "Pilocytic Astrocytoma (WHO Grade I)",
        "subtitle": "The most common pediatric brain tumor; frequently presents in cerebellum, optic pathway, and ventricular walls.",
        "cards": [
            ("Biphasic Histological Pattern", "Alternating compact piloid areas (elongated bipolar astrocytes) and loose, microcystic, hypocellular regions."),
            ("Rosenthal Fibers & EGBs", "Eosinophilic corkscrew-shaped protein aggregates (Rosenthal fibers) in astrocytic processes and eosinophilic granular bodies (EGBs)."),
            ("Molecular Driver: BRAF Alteration", "KIAA1549-BRAF gene duplication/fusion in >70% of cases, constitutively activating MAPK/ERK signaling pathway."),
            ("Surgical Strategy & Outcome", "Gross total resection is curative (>95% 10-year survival); BRAF/MEK inhibitors (e.g., trametinib) effective in unresectable lesions.")
        ],
        "img_path": "assets_images/pilocytic_astrocytoma.jpg",
        "caption_title": "PILOCYTIC ASTROCYTOMA: ROSENTHAL FIBERS",
        "caption_body": "Microscopic smear showing brightly eosinophilic, refractile Rosenthal fibers embedded within elongated, hair-like piloid glial processes."
    },
    # Slide 28: Choroid Neoplasms
    {
        "type": "content",
        "badge": "CHOROID NEOPLASMS • PLEXUS PAPILLOMA",
        "title": "Choroid Papilloma vs. Carcinoma",
        "subtitle": "Epithelial tumors arising from the secretory epithelium of the choroid plexus.",
        "cards": [
            ("Choroid Plexus Papilloma (WHO Grade I)", "Benign papillary fronds lined by single layer of cuboidal epithelium surrounding delicate fibrovascular cores; 'cauliflower' gross appearance."),
            ("Choroid Plexus Carcinoma (WHO Grade III)", "Malignant, destructive tumor; frank parenchymal invasion, mitotic figures (>5/10 HPF), nuclear pleomorphism, necrosis; TP53 mutations common."),
            ("Age & Anatomical Distribution", "Children: Lateral ventricle atrium (glomus); Adults: Fourth ventricle floor/roof and cerebellopontine angle."),
            ("CSF Hyperproduction & Hydrocephalus", "Causes severe communicating hydrocephalus via active CSF hypersecretion as well as mechanical pathway obstruction.")
        ],
        "img_path": "assets_images/choroid_papilloma.jpg",
        "caption_title": "CHOROID PLEXUS PAPILLOMA MACRO/MICRO",
        "caption_body": "Characteristic papillary architecture consisting of finger-like projections lined by uniform epithelial cells around vascular fibrovascular stalks."
    },
    # Slide 29: Atrial Neoplasms
    {
        "type": "content",
        "badge": "ATRIAL NEOPLASMS • MENINGIOMA",
        "title": "Intraventricular Meningioma Tenets",
        "subtitle": "Arise from arachnoid cap cells of the stroma of the tela choroidea, typically residing in the atrium (trigone).",
        "cards": [
            ("Female Predilection & Age", "Account for 1–2% of all intracranial meningiomas; strong female preponderance (3:1 ratio); peak incidence 4th–6th decades."),
            ("Histology: Whorls & Psammoma Bodies", "Syncytial or transitional morphology featuring concentric cellular whorls and laminating calcifications ('psammoma bodies')."),
            ("Massive Arterial Parasitization", "Fed aggressively by anterior choroidal artery and lateral posterior choroidal arteries; late intense homogeneous contrast enhancement on MRI."),
            ("Operative Devitalisation Principle", "Preoperative DSA embolization or early microscopic ligation of choroidal arterial pedicles is mandatory before attempting mobilization.")
        ],
        "img_path": "assets_images/meningioma.jpg",
        "caption_title": "INTRAVENTRICULAR MENINGIOMA: PSAMMOMA BODIES",
        "caption_body": "Radiological and histological presentation displaying sharp circumscription, intense enhancement, and calcified psammoma whorls."
    },
    # Slide 30: Congenital Inclusions
    {
        "type": "content",
        "badge": "CONGENITAL INCLUSIONS • EPIDERMOID",
        "title": "Epidermoid Cysts: 'Pearly Tumors'",
        "subtitle": "Congenital inclusion cysts resulting from entrapped ectodermal tissue during neural tube closure.",
        "cards": [
            ("Gross Appearance ('Pearly Tumor')", "Glistening, iridescent pearly white capsule filled with desquamated keratin flakes and waxy cholesterol crystals."),
            ("Creeping Insinuating Growth Pattern", "Grow slowly by linear accretion; insinuate between cranial nerves, basilar artery branches, and ventricular recesses without displacing them."),
            ("Pathognomonic MRI Signal: DWI Restriction", "Iso-to-hypointense on T1, hyperintense on T2 (mimics CSF), but crucially shows marked bright RESTRICTED DIFFUSION on DWI / ADC maps."),
            ("Surgical Goal: Capsule vs. Nerve Safety", "Evacuate keratin contents gently; avoid aggressive traction on capsule tightly adherent to basilar perforators or brainstem.")
        ],
        "img_path": "assets_images/epidermoid_cyst.jpg",
        "caption_title": "EPIDERMOID CYST: DWI RESTRICTION & PEARL CAPSULE",
        "caption_body": "High-resolution specimen showing the classic stratified squamous epithelial lining and iridescent keratin flakes characteristic of epidermoid cyst."
    },
    # Slide 31: Congenital Inclusions
    {
        "type": "content",
        "badge": "CONGENITAL INCLUSIONS • DERMOID",
        "title": "Dermoid Cysts & Rupture Sequelae",
        "subtitle": "Complex ectodermal inclusion cysts containing dermal appendages (hair follicles, sebaceous glands).",
        "cards": [
            ("Dermal Appendages & Lipid Content", "Contain stratified squamous lining along with hair shafts, sweat glands, and sebaceous elements producing thick, oily, lipid-rich contents."),
            ("Neuroimaging Characteristics", "Markedly hypodense on CT (<0 Hounsfield Units, fat density); bright hyperintense on T1 MRI without contrast enhancement."),
            ("Catastrophic Spontaneous Rupture", "Spontaneous or iatrogenic rupture releases lipid droplets into ventricular CSF and subarachnoid spaces, causing severe chemical meningitis."),
            ("Rupture Management", "Aggressive intraoperative saline irrigation to wash out spilled lipid; systemic corticosteroids to suppress chemical arachnoiditis.")
        ],
        "img_path": "assets_images/davinci_ventricles.jpg",
        "caption_title": "INTRACRANIAL DERMOID CYST ARCHITECTURE",
        "caption_body": "Anatomical mapping of inclusion cyst topography in midline ventricles and cisterns showing characteristic multilocular lipid architecture."
    },
    # Slide 32: Masterclass Summary
    {
        "type": "summary",
        "badge": "YOUMANS & WINN MASTERCLASS SUMMARY",
        "title": "Mastery of Ventricular Surgery",
        "subtitle": "Synthesized operative tenets for the successful management of ventricular and periventricular neoplasms.",
        "cards": [
            ("1. Natural Corridors Over Corticectomy", "Prioritize interhemispheric transchoroidal and telovelar corridors; avoid destructive transcortical incisions and vermian splitting."),
            ("2. Deep Venous System Inviolability", "The internal cerebral veins, basal vein of Rosenthal, and vein of Galen cannot be sacrificed; always preserve collateral venous channels."),
            ("3. Adhere to Safe Entry Zones", "In fourth ventricular tumors, respect the facial colliculus, striae medullares, and hypoglossal/vagal trigones; never pull on adherent floor tumor."),
            ("4. Integrated Molecular Resection Strategy", "Tailor surgical aggressiveness to molecular biology: gross total resection for ependymoma/central neurocytoma; biopsy for germinoma/lymphoma.")
        ],
        "img_path": "enhanced_figures/fig_170_10_surgical_approaches.png",
        "caption_title": "FIG 170.10: COMPREHENSIVE VENTRICULAR SURGICAL CORRIDORS",
        "caption_body": "Master schematic from Youmans & Winn Chapter 170 summarizing safe anatomical entry points and microsurgical corridors."
    },
    # Slide 33: Cartoonish Thank You & Discussion (User Requested)
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
