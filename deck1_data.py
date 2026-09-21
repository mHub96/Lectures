# deck1_data.py - Data for Ventricular Tumors Part 1: Lateral Ventricles & Approaches

DECK1_SLIDES = [
    # Slide 1: Title
    {
        "type": "title",
        "badge": "YOUMANS & WINN COMPREHENSIVE MASTERCLASS • PART 1",
        "title": "Ventricular Tumors:\nMicrosurgical Anatomy & Lateral Approaches",
        "subtitle": "Surgical corridors, neurovascular orientation, and operative strategies for lateral ventricular pathology.",
        "img_path": "assets_images/ventricular_system_3d.png",
        "credits": [
            "Source: Youmans & Winn Neurological Surgery (Chapter 170: Ventricular Tumors)",
            "Curriculum: Neurosurgical Anatomy, Approaches & Intraoperative Considerations",
            "Target Structures: Lateral Ventricles (Frontal, Body, Atrium, Occipital, Temporal)"
        ]
    },
    # Slide 2: Historical Perspectives
    {
        "type": "content",
        "badge": "HISTORICAL PERSPECTIVES • SURGICAL MILESTONES",
        "title": "Pioneering Milestones in Ventricular Surgery",
        "subtitle": "From ancient ventricular localization to Walter Dandy's revolutionary first lateral ventricular tumor resection.",
        "cards": [
            ("3rd Century BC — Herophilos", "Described the four cerebral ventricles ('four small stomachs') and their communications, establishing the earliest anatomical record."),
            ("1504 — Leonardo da Vinci", "Performed the first cerebral wax cast ventriculography via bovine brain, accurately mapping ventricular geometry for the first time."),
            ("1764 — Cotugno & Magendie", "Defined cerebrospinal fluid (CSF) physiology, proving ventricles are filled with fluid rather than animal spirits ('vital pneuma')."),
            ("1918–1933 — Walter Dandy", "Pioneered air ventriculography, endoscopic choroid plexectomy, and performed the first direct surgical resection of a lateral ventricle ependymoma.")
        ],
        "img_path": "assets_images/walter_dandy.jpg",
        "caption_title": "HISTORICAL FIGURE: WALTER E. DANDY (1886–1946)",
        "caption_body": "Father of modern ventricular surgery, inventor of ventriculography, and pioneer of the transcallosal approach for direct intraventricular tumor resection."
    },
    # Slide 3: Epidemiologic Landscape
    {
        "type": "content",
        "badge": "EPIDEMIOLOGIC LANDSCAPE • CLASSIFICATION",
        "title": "Incidence and Primary vs. Secondary Classification",
        "subtitle": "Pecker schema categorizing neoplasms based on ventricular wall embryological and topographical origin.",
        "cards": [
            ("Overall Incidence (1.6%)", "Ventricular tumors account for approximately 1.6% of all primary intracranial neoplasms in comprehensive neuro-oncology registries."),
            ("Pecker Schema: Primary Lesions", "Originate intrinsically from the ventricular ependymal lining, choroid plexus epithelium, subependymal glia, or tela choroidea."),
            ("Pecker Schema: Secondary Lesions", "Arise in surrounding periventricular deep parenchyma (e.g., thalamus, caudate, septum) and project exophytically into the ventricular cavity."),
            ("Clinical Correlation", "True primary tumors often expand indolently within CSF pathways, presenting late with massive ventriculomegaly.")
        ],
        "img_path": "assets_images/lateral_ventricles.jpg",
        "caption_title": "VENTRICULAR CAVITY & LINING TOPOGRAPHY",
        "caption_body": "Anatomical casting and schematic of ventricular chambers demonstrating the ependymal lining that gives rise to primary neuroepithelial tumors."
    },
    # Slide 4: Clinical Manifestations
    {
        "type": "content",
        "badge": "CLINICAL MANIFESTATIONS • SYMPTOM TRIAD",
        "title": "The Symptom Triad of Ventricular Neoplasms",
        "subtitle": "Three pathophysiological mechanisms dictate clinical presentation: invasion, mass effect, and CSF obstruction.",
        "cards": [
            ("1. Local Neural Tissue Invasion", "Destruction or compression of adjacent critical structures: caudate head, forniceal columns, thalamus, or internal capsule tracts."),
            ("2. Global Parenchymal Mass Effect", "Progressive space-occupying expansion causing hemispheric distortion, subfalcine herniation, progressive headache, and lethargy."),
            ("3. Mechanical CSF Flow Obstruction", "Ball-valve occlusion of the foramen of Monro, third ventricle, or aqueduct of Sylvius causing acute, intermittent, or chronic ventriculomegaly."),
            ("Emergency Presentation", "Acute hydrocephalus can precipitate sudden deterioration, bilateral visual loss from papilledema, or fatal herniation syndromes.")
        ],
        "img_path": "assets_images/hydrocephalus.jpg",
        "caption_title": "OBSTRUCTIVE HYDROCEPHALUS ON NEUROIMAGING",
        "caption_body": "Severe ventriculomegaly secondary to intraventricular pathway obstruction, demonstrating periventricular interstitial CSF seepage / transependymal edema."
    },
    # Slide 5: Demographics
    {
        "type": "content",
        "badge": "DEMOGRAPHICS • AGE PATTERNS",
        "title": "Pediatric vs. Adult Presentation Patterns",
        "subtitle": "Cranial compliance and suture patency profoundly alter presentation between infants and adults.",
        "cards": [
            ("Pediatric Presentation: Calvarial Expansion", "Open sutures and patent fontanelles permit massive ventricular expansion prior to elevated intracranial pressure."),
            ("Pediatric Signs: Fontanelle & Milestones", "Full or bulging anterior fontanelle, sunset sign (forced downward gaze), failure to thrive, and loss of developmental milestones."),
            ("Adult Presentation: Fixed Calvarium", "Rigid cranium results in rapid intracranial hypertension: morning headache, positional nausea, projective vomiting, and papilledema."),
            ("Adult Presentation: Hakim-like Triad", "Chronic low-grade hydrocephalus mimics normal pressure hydrocephalus: progressive gait ataxia, cognitive decline, and urinary urgency.")
        ],
        "img_path": "enhanced_figures/fig_170_16_hydrocephalus_ct.png",
        "caption_title": "FIG 170.16: ACUTE VENTRICULOMEGALY ON CT/MRI",
        "caption_body": "Full labeled neuroimaging from Chapter 170 illustrating acute ventricular dilatation, sulcal effacement, and temporal horn ballooning."
    },
    # Slide 6: Syndromic Patterns
    {
        "type": "content",
        "badge": "SYNDROMIC PATTERNS • MIDBRAIN & TECTUM",
        "title": "Mesencephalic Tectal & Parinaud Syndrome",
        "subtitle": "Compression of dorsal midbrain tectum and sylvian aqueduct produces characteristic neuro-ophthalmic deficits.",
        "cards": [
            ("Parinaud (Dorsal Midbrain) Syndrome", "Classic tetrad: Upward gaze paralysis, convergence-retraction nystagmus on attempted upgaze, light-near pupillary dissociation, and Collier sign."),
            ("Collier's Sign", "Pathological retraction of the upper eyelids caused by posterior commissure disruption ('tucked lids')."),
            ("Aqueductal Stenosis", "Compression of the periaqueductal gray and sylvian aqueduct creates noncommunicating triventricular hydrocephalus."),
            ("Tumor Etiologies", "Pineal parenchymal tumors, germ cell tumors, tectal gliomas, and dorsal third ventricular lesions.")
        ],
        "img_path": "assets_images/parinaud_syndrome.jpg",
        "caption_title": "DORSAL MIDBRAIN & TECTAL TOPOGRAPHY",
        "caption_body": "Anatomical relationship of the pineal gland, superior and inferior colliculi, and the sylvian aqueduct vulnerable to compression."
    },
    # Slide 7: Medical Management
    {
        "type": "content",
        "badge": "MEDICAL MANAGEMENT • NONSURGICAL OPTIONS",
        "title": "Pathologies Responsive to Nonoperative Therapy",
        "subtitle": "Certain histological subtypes achieve cure or durable control via chemotherapy and radiotherapy alone.",
        "cards": [
            ("Pure Germinoma", "Highly radiosensitive and chemosensitive; definitive diagnosis via CSF oncomarkers (AFP normal, β-hCG normal/low) or endoscopic biopsy."),
            ("Primary CNS Lymphoma", "High-dose methotrexate-based immunochemotherapy and whole-brain radiotherapy; surgical resection offers no survival advantage."),
            ("Tectal Glioma (Low-Grade Astrocytoma)", "Indolent course; managed primarily with CSF diversion (endoscopic third ventriculostomy) and serial surveillance MRI."),
            ("Prolactinoma Invading Ventricle", "Exceptional third ventricular giant prolactinomas respond dramatically to dopamine agonist medical therapy (cabergoline).")
        ],
        "img_path": "assets_images/germinoma.jpg",
        "caption_title": "CHEMO- & RADIOSENSITIVE INTRACRANIAL TUMORS",
        "caption_body": "Histological landscape of intracranial germinoma featuring large polygonal tumor cells intermixed with mature reactive T-lymphocytes."
    },
    # Slide 8: Hydrocephalus Strategy
    {
        "type": "content",
        "badge": "HYDROCEPHALUS STRATEGY • CSF DIVERSION",
        "title": "CSF Diversion vs. Direct Tumor Resection",
        "subtitle": "Timing of hydrocephalus treatment remains a fundamental strategic neurosurgical decision.",
        "cards": [
            ("Direct Tumor Resection as Primary Strategy", "Preferred when tumor removal will completely restore physiological CSF pathways without need for permanent hardware."),
            ("Preoperative Endoscopic Third Ventriculostomy (ETV)", "Recommended for pineal region, posterior third, or fourth ventricular tumors causing severe acute hydrocephalus; allows biopsy."),
            ("External Ventricular Drain (EVD)", "Temporary bridge in unstable emergency presentations; placed contralateral to the surgical corridor to prevent ventricular collapse."),
            ("Ventriculoperitoneal Shunt (VPS) Precautions", "Avoid routine upfront shunting; carries risk of peritoneal tumor seeding (especially medulloblastoma/germinoma) and shunt dependency.")
        ],
        "img_path": "enhanced_figures/fig_170_18_etv_case.png",
        "caption_title": "FIG 170.18: ENDOSCOPIC THIRD VENTRICULOSTOMY (ETV)",
        "caption_body": "Full labeled operative endoscopic view from Chapter 170 demonstrating tuber cinereum perforation anterior to basilar artery apex."
    },
    # Slide 9: Diagnostic Imaging
    {
        "type": "content",
        "badge": "DIAGNOSTIC IMAGING • MR SEQUENCES",
        "title": "High-Resolution MR Sequences in Planning",
        "subtitle": "Advanced volumetric, steady-state, and diffusion imaging optimizes corridor selection and minimizes neurological morbidity.",
        "cards": [
            ("CISS / FIESTA (Steady-State Free Precession)", "Submillimeter high-contrast T2 imaging delineates cyst walls, ventricular membranes, basilar artery apex, and ETV floor patency."),
            ("3D-SPACE / CUBE (Volumetric T1 & T2)", "Isotropic 1-mm volumetric sequences for precise intraoperative neuronavigation and multiplanar trajectory modeling."),
            ("DTI Tractography (Diffusion Tensor Imaging)", "Reconstructs corticospinal motor tracts, optic radiations (Meyer loop), and forniceal bundles to navigate cortical incisions safely."),
            ("MR Venography & Arterial MRA", "Defines bridging veins, superior sagittal sinus anatomy, and deep venous drainage displacement (internal cerebral veins).")
        ],
        "img_path": "assets_images/ciss_fiesta_mri.jpg",
        "caption_title": "HIGH-RESOLUTION 3D CISS / FIESTA SEQUENCE",
        "caption_body": "Submillimeter steady-state MR imaging displaying micro-details of intraventricular structures, CSF interfaces, and cranial nerves."
    },
    # Slide 10: Preoperative Angiography
    {
        "type": "content",
        "badge": "PREOPERATIVE ANGIOGRAPHY • VASCULAR MAPPING",
        "title": "Dynamic CTA & Catheter DSA Integration",
        "subtitle": "Discerning arterial feeders and deep venous drainage patterns before incision prevents catastrophic intraoperative hemorrhage.",
        "cards": [
            ("Dynamic CTA (dCTA) Multi-Phase Imaging", "Provides time-resolved arterial, capillary, and venous phases in a single noninvasive acquisition, capturing flow kinetics."),
            ("Catheter Digital Subtraction Angiography (DSA)", "Gold standard for hypervascular tumors (choroid plexus papilloma, hemangioblastoma, meningioma); allows preoperative embolization."),
            ("Early Arterial Pedicle Identification", "Guides corridor selection to target arterial feeders (e.g., anterior or posterior choroidal arteries) early before tumor debulking."),
            ("Deep Venous Outflow Preservation", "Visualizes displacement of the internal cerebral veins, basal vein of Rosenthal, and Vein of Galen to avoid venous infarction.")
        ],
        "img_path": "enhanced_figures/fig_170_1_dcta.png",
        "caption_title": "FIG 170.1: DYNAMIC CTA ARTERIAL & VENOUS PHASES",
        "caption_body": "Complete 300 DPI high-resolution multi-phase dCTA panels from Chapter 170 with labeled arterial, mixed, and venous phases."
    },
    # Slide 11: Venous Topography
    {
        "type": "content",
        "badge": "VENOUS TOPOGRAPHY • CORTICAL DRAINAGE",
        "title": "Critical Superficial Draining Veins",
        "subtitle": "Preservation of cortical bridging veins is the primary constraint of interhemispheric and transcortical approaches.",
        "cards": [
            ("Superior Sagittal Sinus Bridging Veins", "Coronal bridging veins enter the SSS at acute anterior angles; excessive retraction can cause avulsion, thrombosis, and venous infarction."),
            ("Vein of Trolard (Superior Anastomotic)", "Connects middle cerebral system to SSS; injury leads to venous hypertension, hemispheric edema, and hemorrhagic infarction."),
            ("Vein of Labbé (Inferior Anastomotic)", "Drains lateral temporal neocortex into transverse sinus; must be scrupulously protected during subtemporal and transtemporal approaches."),
            ("Preoperative Venous Mapping", "MRV or late venous phase DSA identifies safe interhemispheric entry windows where bridging vein density is lowest.")
        ],
        "img_path": "assets_images/bridging_veins.jpg",
        "caption_title": "DURAL VENOUS SINUSES & BRIDGING VEINS",
        "caption_body": "Anatomical schematic of the superior sagittal sinus and cortical bridging veins demonstrating high vulnerability during interhemispheric retraction."
    },
    # Slide 12: Surgical Anatomy
    {
        "type": "content",
        "badge": "SURGICAL ANATOMY • LATERAL VENTRICLE",
        "title": "The Five Sectors of the Lateral Ventricle",
        "subtitle": "The C-shaped lateral ventricle wraps around diencephalic structures, divided into five distinct operative sectors.",
        "cards": [
            ("1. Frontal (Anterior) Horn", "Extends anterior to foramen of Monro; bounded medially by septum pellucidum and laterally by the head of the caudate nucleus."),
            ("2. Ventricular Body (Cella Media)", "Extends from foramen of Monro to splenium of corpus callosum; roof formed by corpus callosum body, floor by thalamus."),
            ("3. Atrium (Trigone)", "Triangular confluence of body, occipital horn, and temporal horn; harbors the glomus of the choroid plexus."),
            ("4. Occipital (Posterior) Horn", "Projects posteriorly into occipital lobe; bounded medially by forceps major and calcar avis; contains no choroid plexus."),
            ("5. Temporal (Inferior) Horn", "Curves anteriorly and inferiorly into temporal lobe, ending blindly behind the amygdala; contains the hippocampus in its floor.")
        ],
        "img_path": "enhanced_figures/fig_170_6_cross_sections.png",
        "caption_title": "FIG 170.6: LATERAL VENTRICULAR LABELED CROSS SECTIONS",
        "caption_body": "Complete 300 DPI coronal cuts from Chapter 170 with all labels intact: frontal horn, body, occipital horn, atrium, and temporal horn."
    },
    # Slide 13: Commissural Anatomy
    {
        "type": "content",
        "badge": "COMMISSURAL ANATOMY • WHITE MATTER",
        "title": "Corpus Callosum: Anatomic Subdivisions",
        "subtitle": "The principal interhemispheric commissure connecting homologous cerebral cortical regions.",
        "cards": [
            ("Rostrum", "Tapers posteroinferiorly from genu to lamina terminalis; forms anterior floor of frontal horn."),
            ("Genu ('Knee')", "Anterior convexity curving around frontal horns; fibers form forceps minor projecting into frontal poles."),
            ("Body (Trunk)", "Extensive horizontal central portion; roof of lateral ventricular frontal horns and bodies; fibers form radiation of corpus callosum."),
            ("Splenium", "Thick rounded posterior terminus; fibers form forceps major sweeping into occipital lobes; wraps over pineal region and vein of Galen.")
        ],
        "img_path": "assets_images/corpus_callosum.jpg",
        "caption_title": "SAGITTAL CORPUS CALLOSUM SUBDIVISIONS",
        "caption_body": "Midsagittal neuroanatomical section highlighting rostrum, genu, body, and splenium in relation to ventricular cavities."
    },
    # Slide 14: Limbic Architecture
    {
        "type": "content",
        "badge": "LIMBIC ARCHITECTURE • MEMORY CIRCUITS",
        "title": "The Five Segments of the Fornix",
        "subtitle": "Critical limbic arch connecting hippocampus to mamillary bodies; bilaterally vulnerable during ventricular surgery.",
        "cards": [
            ("1. Alveus & Fimbria", "Originates along ventricular surface of hippocampus, coalescing along medial border to form the fimbria."),
            ("2. Crura (Paired Posterior Limbs)", "Ascend beneath the splenium of the corpus callosum, interconnected across midline by the hippocampal commissure (psalterium)."),
            ("3. Body (Corpus Fornicis)", "Runs anteriorly along inferior edge of septum pellucidum, intimately related to roof of third ventricle and superior tela choroidea."),
            ("4. Columns (Columnae Fornicis)", "Arch anteroinferiorly forming the anterior border of the foramen of Monro, descending into hypothalamus to terminate in mamillary bodies.")
        ],
        "img_path": "enhanced_figures/fig_170_2_fornix.png",
        "caption_title": "FIG 170.2: 3D ANATOMY OF THE FORNIX (WITH ALL LABELS)",
        "caption_body": "Ultra-sharp 300 DPI dissection from Chapter 170 showing labeled forniceal columns, body, crus, fimbria, and alveus."
    },
    # Slide 15: Surgical Anatomy
    {
        "type": "content",
        "badge": "SURGICAL ANATOMY • FRONTAL HORN",
        "title": "Frontal Horn Boundaries & Landmarks",
        "subtitle": "The most common surgical entry site for ventricular tumor resection and ventricular drainage.",
        "cards": [
            ("Anterior & Superior Boundaries", "Roof and anterior limit formed by body and genu of corpus callosum; rostrum curves beneath anterior floor."),
            ("Medial Wall", "Septum pellucidum (separating paired frontal horns) and forniceal columns posteriorly."),
            ("Lateral Wall", "Prominent rounded convexity of the head of the caudate nucleus bulging into the ventricular cavity."),
            ("Floor & Foramen of Monro", "Rostrum of corpus callosum anteriorly; opens posteriorly at foramen of Monro into third ventricle.")
        ],
        "img_path": "enhanced_figures/fig_170_3_frontal_horn.png",
        "caption_title": "FIG 170.3: FRONTAL HORN & CAUDATE HEAD (300 DPI)",
        "caption_body": "Axial cut from Chapter 170 showing all labels: caudate head, septum pellucidum, internal capsule genu, and foramen of Monro."
    },
    # Slide 16: Vascular Orientation
    {
        "type": "content",
        "badge": "VASCULAR ORIENTATION • VENOUS LANDMARKS",
        "title": "The Venous Angle Distance Landmark",
        "subtitle": "The critical intraventricular anatomical landmark identifying the posterior margin of the foramen of Monro.",
        "cards": [
            ("Anterior Septal Vein (ASV)", "Courses anteriorly along septum pellucidum, turning posteriorly at foramen of Monro."),
            ("Thalamostriate Vein (TSV)", "Runs anteriorly in striothalamic sulcus between caudate and thalamus, joining ASV at venous angle."),
            ("The Venous Angle Junction", "Union of ASV and TSV marks the exact posterior lip of the foramen of Monro and origin of internal cerebral vein."),
            ("Distance Landmark (5.5 mm)", "In normal anatomy, the venous angle lies within 5.5 mm of the posterior margin of Monro; distortion signifies tumor displacement.")
        ],
        "img_path": "enhanced_figures/fig_170_4_venous_angle.png",
        "caption_title": "FIG 170.4: VENOUS ANGLE & STRIA TERMINALIS (LABELED)",
        "caption_body": "Cranial-to-caudal view from Chapter 170 showing thalamostriate vein, septal vein, choroid plexus, and internal capsule relations."
    },
    # Slide 17: Motor Pathways
    {
        "type": "content",
        "badge": "MOTOR PATHWAYS • INTERNAL CAPSULE",
        "title": "Internal Capsule Genu Spatial Relationship",
        "subtitle": "Directly lateral to the thalamostriate-caudate junction lies the corticobulbar and corticospinal motor pathway.",
        "cards": [
            ("Genu & Anterior Limb Proximity", "The genu of the internal capsule lies immediately adjacent to the striothalamic sulcus and lateral margin of Monro."),
            ("Surgical Margin of Safety", "Over-aggressive coagulation or retraction along the lateral ventricular wall risks catastrophic contralateral hemiparesis or dysarthria."),
            ("Septal Vein Transection Safety", "The anterior septal vein may be safely transected proximal to its venous angle junction; the thalamostriate vein must NEVER be coagulated."),
            ("Stereotactic Guidance", "Preoperative DTI integration ensures lateral corridor retraction vectors remain parallel rather than perpendicular to capsular tracts.")
        ],
        "img_path": "assets_images/internal_capsule.jpg",
        "caption_title": "INTERNAL CAPSULE ANATOMICAL COURSE",
        "caption_body": "Axial white matter dissection displaying anterior limb, genu, and posterior limb of internal capsule hugging the lateral ventricular wall."
    },
    # Slide 18: Surgical Anatomy
    {
        "type": "content",
        "badge": "SURGICAL ANATOMY • CELLA MEDIA",
        "title": "Ventricular Body & Striothalamic Sulcus",
        "subtitle": "The central body of the lateral ventricle extends from foramen of Monro posteriorly to the splenium.",
        "cards": [
            ("Roof & Floor Boundaries", "Roof: Body of corpus callosum; Floor: Dorsal surface of thalamus laterally, fornix medially, separated by choroidal fissure."),
            ("Striothalamic Sulcus (Sulcus Terminalis)", "Groove separating caudate body from dorsal thalamus; carries thalamostriate vein and stria terminalis bundle."),
            ("Choroidal Fissure Entry Point", "Natural cleft between fornix and dorsal thalamus; opening the tenia fornicis provides access to velum interpositum and third ventricle."),
            ("Medial Boundary", "Septum pellucidum anteriorly; posterior body of fornix attached to callosal undersurface posteriorly.")
        ],
        "img_path": "enhanced_figures/fig_170_5_tela_choroidea.png",
        "caption_title": "FIG 170.5: VENTRICULAR BODY & TELA CHOROIDEA (300 DPI)",
        "caption_body": "Complete labeled view from Chapter 170 with tela choroidea opened, displaying internal cerebral veins and MPChA."
    },
    # Slide 19: Atrial Architecture
    {
        "type": "content",
        "badge": "ATRIAL ARCHITECTURE • TRIGONE",
        "title": "Anatomic Elements of the Ventricular Trigone",
        "subtitle": "The triangular confluence where frontal body, occipital horn, and temporal horn meet; common site for meningiomas.",
        "cards": [
            ("Anterior & Medial Boundaries", "Anterior: Pulvinar of thalamus; Medial: Bulb of corpus callosum (forceps major) superiorly, calcar avis inferiorly."),
            ("Lateral Wall & Roof", "Lateral wall and roof formed by fibers of the tapetum of the corpus callosum and optic radiation (sagittal stratum)."),
            ("Floor (Collateral Trigone)", "Prominence formed by the collateral sulcus invaginating into the ventricular cavity."),
            ("Glomus of Choroid Plexus", "Massive confluence of choroid plexus; site of origin for intraventricular meningiomas, choroid papillomas, and vascular lesions.")
        ],
        "img_path": "enhanced_figures/fig_170_6_cross_sections.png",
        "caption_title": "FIG 170.6C: ATRIUM & CHOROID GLOMUS ANATOMY",
        "caption_body": "Coronal section of the ventricular atrium showing tapetum, optic radiations, pulvinar, and glomus of choroid plexus."
    },
    # Slide 20: Surgical Anatomy
    {
        "type": "content",
        "badge": "SURGICAL ANATOMY • OCCIPITAL HORN",
        "title": "The Occipital Horn: Anatomy & Trapping",
        "subtitle": "Highly variable posterior extension into occipital lobe; key landmark for visual pathway preservation.",
        "cards": [
            ("Roof & Lateral Wall", "Formed by tapetum of the corpus callosum sweeping posteroinferiorly, separating cavity from optic radiations."),
            ("Medial Wall Landmarks", "Bulb of the occipital horn (forceps major) superiorly; Calcar avis (produced by deep calcarine fissure) inferiorly."),
            ("Absence of Choroid Plexus", "The occipital horn never contains choroid plexus under normal anatomical conditions."),
            ("Optic Radiation Vulnerability", "Lateral approach trajectories through parieto-occipital neocortex risk homonymous hemianopia; DTI tractography is mandatory.")
        ],
        "img_path": "assets_images/dti_tractography.jpg",
        "caption_title": "DTI TRACTOGRAPHY: OPTIC RADIATIONS",
        "caption_body": "Reconstruction of the geniculocalcarine visual tract (Meyer loop and sagittal stratum) wrapping around the lateral wall of the atrium and occipital horn."
    },
    # Slide 21: Temporal Architecture
    {
        "type": "content",
        "badge": "TEMPORAL ARCHITECTURE • INFERIOR HORN",
        "title": "Temporal Horn Key Relationships",
        "subtitle": "Extends anteroinferiorly around the pulvinar into medial temporal lobe, terminating behind the amygdala.",
        "cards": [
            ("Roof Boundaries", "Formed by tapetum laterally, tail of caudate nucleus, stria terminalis, and retrolenticular internal capsule."),
            ("Floor & Medial Wall", "Hippocampus and fimbria occupy the floor; choroidal fissure sits between fimbria and stria terminalis."),
            ("Anterior Pole & Amygdala", "Temporal horn terminates blindly approximately 2.5 cm behind temporal pole; amygdala forms anterior wall and roof."),
            ("Meyer's Loop Anatomy", "Anterior optic radiation fibers loop over the roof of the temporal horn; anterior temporal resections >3.5 cm cause superior quadrantanopia.")
        ],
        "img_path": "assets_images/choroid_plexus.jpg",
        "caption_title": "TEMPORAL HORN & CHOROID PLEXUS",
        "caption_body": "Anatomical correlation of the inferior choroidal point, choroid plexus attachment, and hippocampal formation in the temporal horn floor."
    },
    # Slide 22: Vascular Supply
    {
        "type": "content",
        "badge": "VASCULAR SUPPLY • ARTERIAL PEDICLES",
        "title": "Arterial Supply to Lateral Ventricles",
        "subtitle": "Choroidal arterial network provides dual supply from both internal carotid and vertebrobasilar systems.",
        "cards": [
            ("Anterior Choroidal Artery (AChA)", "Branch of internal carotid artery; enters temporal horn through inferior choroidal point; supplies choroid plexus of temporal horn and atrium."),
            ("Lateral Posterior Choroidal Artery (LPChA)", "Branch of P2 segment of PCA; courses through choroidal fissure to supply glomus of choroid plexus in the atrium."),
            ("Medial Posterior Choroidal Artery (MPChA)", "Branch of P2 segment of PCA; wraps around midbrain, enters velum interpositum in third ventricle roof, and feeds third ventricle choroid."),
            ("Surgical Principle: Early Devascularization", "Approaching atrial tumors from corridors that access choroidal arteries early significantly reduces blood loss during debulking.")
        ],
        "img_path": "enhanced_figures/fig_170_5_tela_choroidea.png",
        "caption_title": "FIG 170.5: POSTERIOR CHOROIDAL ARTERY BRANCHES",
        "caption_body": "Chapter 170 labeled dissection demonstrating lateral and medial posterior choroidal arteries entering through the choroidal fissure."
    },
    # Slide 23: Deep Drainage
    {
        "type": "content",
        "badge": "DEEP DRAINAGE • GALENIC SYSTEM",
        "title": "Internal Cerebral Veins vs. Basal Vein",
        "subtitle": "Confluence of deep cerebral veins beneath the splenium creates the Galenic drainage complex.",
        "cards": [
            ("Internal Cerebral Veins (ICVs)", "Formed at venous angle by septal and thalamostriate veins; run parallel within velum interpositum in third ventricle roof."),
            ("Basal Vein of Rosenthal (BVR)", "Formed at anterior perforated substance; wraps around cerebral peduncle in ambient cistern; drains into vein of Galen."),
            ("Great Cerebral Vein of Galen", "Short midline trunk formed by union of paired ICVs and BVRs beneath splenium; drains into straight sinus at tentorial apex."),
            ("Surgical Rule: Bilateral ICV Occlusion Fatal", "Occlusion of both ICVs leads to catastrophic bilateral thalamic and basal ganglia hemorrhagic infarction, coma, and death.")
        ],
        "img_path": "enhanced_figures/fig_170_4_venous_angle.png",
        "caption_title": "FIG 170.4: DEEP CEREBRAL VENOUS CONFLUENCE",
        "caption_body": "Venous anatomy from Chapter 170 highlighting bilateral internal cerebral veins converging toward the Vein of Galen beneath the splenium."
    },
    # Slide 24: Operative Technology
    {
        "type": "content",
        "badge": "OPERATIVE TECHNOLOGY • MODERN ADJUNCTS",
        "title": "Modern Intraoperative Surgical Adjuncts",
        "subtitle": "Technological evolution from flat blade retractors to tubular ports, frameless navigation, and high-definition exoscopy.",
        "cards": [
            ("Frameless Neuronavigation & Optical Tracking", "Provides submillimetric accuracy; merges volumetric MRI with DTI tractography to guide incision and trajectory vector."),
            ("Tubular Retractor Systems (Brain Ports)", "Distributes retraction force radially across 360 degrees, minimizing shear stress and focal ischemia along white matter tracts."),
            ("3D Digital Exoscopes & High-Definition Endoscopes", "Provide superior illumination, enhanced focal depth, and ergonomic visualization into deep narrow corridors."),
            ("Ultrasonic Surgical Aspirators (CUSA)", "Permits rapid internal tumor cytoreduction with selective tissue sparing, preserving adjacent delicate ependyma and vessels.")
        ],
        "img_path": "assets_images/craniotomy_wiki.jpg",
        "caption_title": "MODERN INTRAOPERATIVE NEUROSURGICAL SETUP",
        "caption_body": "Integration of frameless stereotactic navigation, micro-instrumentation, and optics during ventricular and deep cranial access."
    },
    # Slide 25: Electrophysiology
    {
        "type": "content",
        "badge": "ELECTROPHYSIOLOGY • NEUROMONITORING",
        "title": "Comprehensive Intraoperative Monitoring",
        "subtitle": "Continuous neurophysiological monitoring provides real-time warning before irreversible neurological injury occurs.",
        "cards": [
            ("Motor Evoked Potentials (MEP)", "Monitors corticospinal tract integrity during retraction near internal capsule and thalamus; >50% amplitude drop warns of ischemia."),
            ("Somatosensory Evoked Potentials (SSEP)", "Evaluates sensory lemniscal pathways through dorsal column-thalamic tracts; sensitive to thalamostriate compromise."),
            ("Visual Evoked Potentials (VEP)", "Used during posterior atrial and occipital approaches to monitor optic radiation and calcarine cortex function."),
            ("Subcortical Direct Electrical Stimulation", "Employed during transfrontal and transcortical approaches to map motor and speech pathways ahead of the surgical corridor.")
        ],
        "img_path": "enhanced_figures/fig_170_10_surgical_approaches.png",
        "caption_title": "FIG 170.10: MULTI-CORRIDOR MONITORING SCHEME",
        "caption_body": "Chapter 170 surgical approach schematic illustrating functional white matter pathways traversed by ventricular corridors."
    },
    # Slide 26: Midline Corridors
    {
        "type": "content",
        "badge": "MIDLINE CORRIDORS • TRANSCALLOSAL",
        "title": "Anterior Interhemispheric Transcallosal",
        "subtitle": "The workhorse approach for tumors of the frontal horn, body of lateral ventricle, and third ventricle.",
        "cards": [
            ("Patient Positioning & Craniotomy", "Supine with head elevated 15–20°; two-thirds of craniotomy anterior to coronal suture, crossing sagittal sinus by 1 cm."),
            ("Interhemispheric Dissection", "Gravity-assisted retraction of right frontal lobe away from falx; identification of callosomarginal and pericallosal arteries."),
            ("Callosotomy Extent (1.5–2.0 cm)", "Performed strictly in midline between pericallosal arteries; anterior to foramen of Monro; limited to ≤2.0 cm to prevent disconnection syndrome."),
            ("Bilateral Ventricular Access", "Fenestration of septum pellucidum provides simultaneous visualization of both lateral ventricles through a single callosotomy.")
        ],
        "img_path": "enhanced_figures/fig_170_11_subependymoma_case.png",
        "caption_title": "FIG 170.11: TRANSCALLOSAL CORRIDOR EXPOSURE",
        "caption_body": "Full labeled operative view from Chapter 170 demonstrating interhemispheric transcallosal entry into the lateral ventricle for tumor resection."
    },
    # Slide 27: Operative Hazards
    {
        "type": "content",
        "badge": "OPERATIVE HAZARDS • RISK REDUCTION",
        "title": "Transcallosal Complications & Avoidance",
        "subtitle": "Key pitfalls of transcallosal surgery and strategies for neurological preservation.",
        "cards": [
            ("Bridging Vein Avulsion & Venous Infarct", "Traction on parasagittal bridging veins can trigger superior sagittal sinus thrombosis; dissect arachnoid bands to mobilize veins."),
            ("Supplementary Motor Area (SMA) Syndrome", "Excessive retraction on medial frontal lobe produces contralateral akinesia and mutism; transient but distressing."),
            ("Callosal Disconnection Syndrome", "Extending callosotomy >2.5 cm or dividing splenium causes alexia without agraphia, tactile anomia, or interhemispheric transfer loss."),
            ("Forniceal Traction & Korsakoff Syndrome", "Bilateral forniceal contusion or ischemia at foramen of Monro causes permanent anterograde amnesia.")
        ],
        "img_path": "enhanced_figures/fig_170_11_subependymoma_case.png",
        "caption_title": "FIG 170.11: RESECTION CAVITY & FORNIX PRESERVATION",
        "caption_body": "Operative view illustrating tumor bed following successful transcallosal resection, confirming anatomic integrity of forniceal columns."
    },
    # Slide 28: Transcortical Corridors
    {
        "type": "content",
        "badge": "TRANSCORTICAL CORRIDORS • TRANSFRONTAL",
        "title": "Transfrontal Corticectomy & Transsulcal",
        "subtitle": "Alternative route to frontal horn and body, especially favored in marked ventriculomegaly or lateral tumor extension.",
        "cards": [
            ("Middle Frontal Gyrus Corticectomy", "Transcortical incision placed in non-eloquent middle frontal gyrus (F2), anterior to motor strip and frontal eye fields."),
            ("Transsulcal Tubular Retractor Approach", "Dissection carried through the depth of the sulcus to enter the ventricle with minimal parenchymal disruption."),
            ("Advantages over Transcallosal", "Direct line of sight to lateral ventricular wall; avoids superior sagittal sinus bridging veins; superior for massively dilated ventricles."),
            ("Disadvantages & Seizure Risk", "Cortical incision carries higher post-operative epileptogenic potential (requires prophylactic anti-seizure medication) and porencephaly.")
        ],
        "img_path": "enhanced_figures/fig_170_15_transfrontal_case.png",
        "caption_title": "FIG 170.15: TRANSFRONTAL TRANSVENTRICULAR ENTRY",
        "caption_body": "Complete labeled operative view from Chapter 170 showing transfrontal entry through the lateral ventricle into the foramen of Monro."
    },
    # Slide 29: Atrial Approaches
    {
        "type": "content",
        "badge": "ATRIAL APPROACHES • PARIETAL ROUTES",
        "title": "Transparietal: Intraparietal Sulcus",
        "subtitle": "Superior parietal lobule and intraparietal sulcal corridors for trigonal and atrial neoplasms.",
        "cards": [
            ("Superior Parietal Lobule (SPL) Corridor", "Incision in non-dominant SPL above intraparietal sulcus; enters roof of atrium; minimizes visual field deficit."),
            ("Intraparietal Sulcus (IPS) Transsulcal Route", "Splits the IPS to enter the atrium; preserves parietal cortex and reduces visual pathway traction."),
            ("Optic Radiation (Sagittal Stratum) Avoidance", "Lateral temporal routes inevitably cross optic radiation; superior parietal approach passes superior to geniculocalcarine fibers."),
            ("Dominant Hemisphere Caution", "In dominant hemisphere, parietal corticectomy carries risk of Gerstmann syndrome (agraphia, acalculia, finger agnosia, left-right disorientation).")
        ],
        "img_path": "enhanced_figures/fig_170_17_transchoroidal_case.png",
        "caption_title": "FIG 170.17: TRANSCHOROIDAL ATRIAL EXPOSURE",
        "caption_body": "Full labeled interhemispheric transchoroidal approach to ventricular atrium from Chapter 170 avoiding neocortical corticectomy."
    },
    # Slide 30: Temporal Corridors
    {
        "type": "content",
        "badge": "TEMPORAL CORRIDORS • SUBTEMPORAL",
        "title": "Transtemporal vs. Subtemporal Routes",
        "subtitle": "Operative corridors targeting temporal horn and inferior atrial tumors.",
        "cards": [
            ("Middle Temporal Gyrus (T2) Transtemporal", "Direct lateral entry into temporal horn; risks language disruption in dominant hemisphere and Meyer loop visual field deficit."),
            ("Inferior Temporal Gyrus (T3) / Sulcal", "Lower trajectory entering floor of temporal horn, reducing optic radiation exposure."),
            ("Subtemporal Approach", "Extradural or intradural elevation of inferior temporal surface; reaches medial temporal structures without traversing neocortex."),
            ("Vein of Labbé Vulnerability", "Subtemporal elevation is strictly constrained by the entry of the vein of Labbé into the transverse sinus; excessive traction risks venous stroke.")
        ],
        "img_path": "enhanced_figures/fig_170_19_coz_case.png",
        "caption_title": "FIG 170.19: CRANIO-ORBITOZYGOMATIC EXPOSURE",
        "caption_body": "Subtemporal and anterolateral corridors from Chapter 170 utilized for deep medial temporal and periventricular exposure."
    },
    # Slide 31: Decision Matrix
    {
        "type": "content",
        "badge": "DECISION MATRIX • SURGICAL SELECTION",
        "title": "Lateral Ventricular Approach Selection",
        "subtitle": "Algorithmic decision framework synthesizing tumor location, ventriculomegaly, vascularity, and hemispheric dominance.",
        "cards": [
            ("Frontal Horn & Body: Normal Ventricles", "Anterior Interhemispheric Transcallosal Approach is favored; provides midline direct access without cortical violation."),
            ("Frontal Horn & Body: Dilated Ventricles / Lateral Extent", "Transcortical (Middle Frontal Gyrus) or transsulcal port approach offers shorter working distance and wide angle of view."),
            ("Atrium (Trigone) Tumors", "Superior Parietal Lobule (SPL) corridor for non-dominant tumors; Interhemispheric Transprecuneal or Transchoroidal for dominant side."),
            ("Temporal Horn Tumors", "Subtemporal route for medial pathology; Transtemporal (T2/T3) for non-dominant lateral tumors with existing visual deficit.")
        ],
        "img_path": "enhanced_figures/fig_170_10_surgical_approaches.png",
        "caption_title": "FIG 170.10: SURGICAL CORRIDOR SUMMARY MATRIX",
        "caption_body": "Chapter 170 master diagram illustrating trajectories of anterior transcallosal, transcortical, and posterior corridors."
    },
    # Slide 32: Summary of Part 1
    {
        "type": "summary",
        "badge": "YOUMANS & WINN MASTERCLASS • PART 1 SUMMARY",
        "title": "Mastery of Lateral Ventricular Corridors",
        "subtitle": "Key anatomical and surgical pearls summarizing Part 1 of the Ventricular Tumors curriculum.",
        "cards": [
            ("Anatomy Dictates Corridors", "Deep familiarity with the 5 sectors of the lateral ventricle and choroidal fissure enables corridor selection tailored to tumor margins."),
            ("Venous Angle as True Compass", "The junction of thalamostriate and septal veins reliably marks foramen of Monro and safeguards internal cerebral veins."),
            ("Tractography Sparing", "Preoperative DTI integration is essential to navigate past internal capsule genu, forniceal columns, and Meyer's loop safely."),
            ("Transition to Part 2", "Part 2 covers the Third & Fourth Ventricles, Infratentorial approaches, and comprehensive WHO Histopathology & Molecular Stratification.")
        ],
        "img_path": "assets_images/ventricular_system_3d.png",
        "caption_title": "3D VENTRICULAR SYSTEM • PROCEED TO PART 2",
        "caption_body": "Comprehensive 3D reconstruction of ventricular cavities linking lateral ventricles to the third and fourth ventricular systems."
    },
    # Slide 33: Cartoonish Thank You & Next Lecture Hint (User Requested)
    {
        "type": "thankyou",
        "badge": "END OF PART 1 • MASTERCLASS LECTURE SERIES",
        "title": "Thank You for Your Attention!",
        "subtitle": "Up Next in Part 2: Third & Fourth Ventricles, Infratentorial Approaches & Histopathology.",
        "cards": [
            ("Masterclass Milestones Completed", "Comprehensive mastery of lateral ventricular sectors, neurovascular landmarks, limbic preservation, and operative corridors."),
            ("What's Coming in Part 2?", "Third ventricle 5-layer roof dissection, transchoroidal (Wen) technique, pineal region, fourth ventricle telovelar approach, and WHO tumor pathology."),
            ("Interactive Review Available", "Use the Knowledge Quiz (top right) to test your clinical retention or explore the Slide Overview drawer."),
            ("Questions & Discussion", "Let's take initial questions on lateral ventricular corridors before advancing to the deep diencephalic system.")
        ],
        "img_path": "assets_images/part1_thankyou.jpg",
        "caption_title": "ARTISTIC LECTURE ARTWORK: SEE YOU IN PART 2!",
        "caption_body": "Special educational masterclass illustration: Up next is Part 2 covering the third and fourth ventricles!"
    }
]
