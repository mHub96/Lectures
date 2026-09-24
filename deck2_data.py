# deck2_data.py
# Part II: Tumors of the Brain Ventricles
# Neurosurgical Lecture Series — WHO 5th Edition CNS Tumor Classification
# -----------------------------------------------------------------------

DECK2_SLIDES = [

    # =========================================================
    # SLIDE 1 — TITLE
    # =========================================================
    {
        "type": "title",
        "badge": "PART II • VENTRICULAR TUMORS",
        "title": "Tumors of the Brain Ventricles",
        "subtitle": "A comprehensive neurosurgical review of intraventricular neoplasms: classification, diagnosis, surgical approaches, and outcomes.",
        "img_path": "assets_images/ventricular_system_3d.png",
        "credits": [
            "Based on WHO Classification of Tumours of the CNS, 5th Edition (2021)",
            "Youmans & Winn Neurological Surgery, 8th Edition",
            "Lecture Series — Neurological Surgery Department",
        ],
    },

    # =========================================================
    # SLIDE 2 — CLASSIFICATION OVERVIEW
    # =========================================================
    {
        "type": "content",
        "badge": "OVERVIEW • CLASSIFICATION",
        "title": "Classification of Intraventricular Tumors",
        "subtitle": "Ventricular tumors are classified by cell of origin, location, and WHO grade under the 2021 CNS tumor classification.",
        "cards": [
            ("Neuroepithelial Tumors", "Ependymomas (WHO I–III), subependymomas, central neurocytomas, and choroid plexus tumors arise from the ependymal lining or choroid stroma."),
            ("Glial & Neuronal Tumors", "Subependymal giant cell astrocytomas (SEGA, WHO I) arise near the foramen of Monro in tuberous sclerosis; pilocytic astrocytomas may extend into ventricles."),
            ("Meningothelial & Germ Cell Tumors", "Intraventricular meningiomas arise from arachnoid cell rests in the choroid plexus; germinomas and mixed GCTs involve the pineal region and third ventricle."),
            ("Cysts & Developmental Lesions", "Colloid cysts (third ventricle), craniopharyngiomas (sellar/suprasellar with third ventricle involvement), and epidermoid cysts occupy specific ventricular compartments."),
        ],
        "img_path": "assets_images/lateral_ventricles.jpg",
        "caption_title": "VENTRICULAR COMPARTMENTS",
        "caption_body": "The lateral, third, and fourth ventricles each harbor distinct tumor subtypes dictated by their unique cellular lining and anatomical relationships.",
    },

    # =========================================================
    # ── EPENDYMOMA ──
    # =========================================================

    # SLIDE 3 — Ependymoma: Types & Grades
    {
        "type": "content",
        "badge": "EPENDYMOMA • TYPES & GRADES",
        "title": "Ependymoma: Classification and Molecular Subtypes",
        "subtitle": "The 2021 WHO classification integrates histology with molecular profiling to define nine distinct ependymoma entities.",
        "cards": [
            ("Subependymoma (WHO I)", "Benign, slow-growing, well-circumscribed nodules arising in the fourth or lateral ventricle walls; often incidental; clusters of glial cells in a fibrillary matrix."),
            ("Myxopapillary Ependymoma (WHO II)", "Affects the conus medullaris/filum terminale; papillary architecture with myxoid stroma; upgraded to WHO II in 2021 due to risk of dissemination."),
            ("Ependymoma WHO II/III & Molecular Groups", "Posterior fossa: PF-EPN-A (H3 K27me3 loss, infants, worse prognosis) and PF-EPN-B (adults, better prognosis). Supratentorial: ST-YAP1 fusion (children, good prognosis) and ST-RELA/ZFTA fusion (aggressive, NF-κB pathway, WHO III)."),
            ("Anaplastic Ependymoma (WHO III)", "High mitotic index, microvascular proliferation, pseudopalisading necrosis; more common supratentorially in adults; molecular designation now preferred over purely histologic grading."),
        ],
        "img_path": "assets_images/ependymoma.jpg",
        "caption_title": "EPENDYMOMA HISTOLOGY",
        "caption_body": "Classic perivascular pseudorosettes and true ependymal rosettes on H&E. GFAP-positive; EMA dot-like positivity distinguishes ependymoma from other gliomas.",
    },

    # SLIDE 4 — Ependymoma: Signs & Symptoms
    {
        "type": "content",
        "badge": "EPENDYMOMA • SIGNS & SYMPTOMS",
        "title": "Ependymoma: Clinical Presentation",
        "subtitle": "Symptoms depend on tumor location: posterior fossa lesions cause obstructive hydrocephalus, whereas supratentorial lesions present with focal deficits.",
        "cards": [
            ("Raised Intracranial Pressure", "Headache (worse in morning), nausea, vomiting, and papilledema due to CSF outflow obstruction at the fourth ventricle or foramen of Monro; present in >80% of pediatric cases."),
            ("Cerebellar Signs", "Fourth-ventricular ependymomas produce truncal ataxia, nystagmus, and dysmetria from vermian/cerebellar hemisphere compression; head tilt may indicate tonsillar herniation."),
            ("Cranial Nerve Involvement", "Tumor extension through the lateral foramina of Luschka can involve CNs VI, VII, VIII, IX, X causing diplopia, facial palsy, hearing loss, and dysphagia — a hallmark of fourth-ventricle ependymoma."),
            ("Supratentorial Focal Deficits", "Lateral ventricular ependymomas may cause contralateral hemiparesis or hemisensory loss; seizures occur in ~30%; third-ventricular lesions produce memory impairment from fornix compression."),
        ],
        "img_path": "enhanced_figures/fig_170_16_hydrocephalus_ct.png",
        "caption_title": "OBSTRUCTIVE HYDROCEPHALUS",
        "caption_body": "Non-contrast CT demonstrating marked dilation of the lateral and third ventricles caused by a fourth-ventricular ependymoma obstructing the aqueduct of Sylvius.",
    },

    # SLIDE 5 — Ependymoma: Imaging & Investigations
    {
        "type": "content",
        "badge": "EPENDYMOMA • IMAGING & INVESTIGATIONS",
        "title": "Ependymoma: Radiological Features and Workup",
        "subtitle": "MRI with contrast is the modality of choice; whole-spine staging and CSF cytology are mandatory before surgery.",
        "cards": [
            ("MRI Characteristics", "Heterogeneous T1 iso/hypointense, T2 hyperintense mass with mixed solid and cystic components; 'plastic' extension through foramina of Luschka/Magendie on sagittal imaging is pathognomonic for fourth-ventricle ependymoma. Variable gadolinium enhancement."),
            ("CT Features", "Calcifications in 50%; useful for bony erosion assessment; contrast CT shows heterogeneous enhancement; non-contrast CT is first-line for acute presentations with hydrocephalus."),
            ("Whole-Spine MRI & CSF", "Required for all grades given leptomeningeal dissemination risk; CSF cytology and flow cytometry should be obtained; lumbar puncture deferred until after posterior fossa decompression if ICP is elevated."),
            ("Molecular & Pathological Workup", "FISH for ZFTA-RELA/YAP1 fusions; H3 K27me3 immunohistochemistry; DNA methylation profiling for WHO 2021 molecular subgroup assignment; Ki-67 proliferation index; CDKN2A/B deletion status."),
        ],
        "img_path": "assets_images/ciss_fiesta_mri.jpg",
        "caption_title": "CISS/FIESTA MRI SEQUENCE",
        "caption_body": "High-resolution CISS/FIESTA sequences delineate tumor extent within the fourth ventricle and its relationship to the brainstem, cranial nerves, and foramina of Luschka.",
    },

    # SLIDE 6 — Ependymoma: Medical Therapy
    {
        "type": "content",
        "badge": "EPENDYMOMA • MEDICAL THERAPY",
        "title": "Ependymoma: Adjuvant and Systemic Treatment",
        "subtitle": "Radiotherapy remains the primary adjuvant modality; chemotherapy is reserved for young children and recurrent disease.",
        "cards": [
            ("Focal Radiotherapy (Standard of Care)", "Conformal or intensity-modulated RT to the tumor bed (54–59.4 Gy in 30–33 fractions) is standard after gross total resection for WHO II/III; craniospinal irradiation (CSI) reserved for M+ disease."),
            ("Proton Therapy", "Preferred in children <3 years when feasible to reduce neurocognitive sequelae; achieves superior dose conformality, sparing developing hippocampus and cochlea; evidence from COG ACNS0121 supports its use."),
            ("Chemotherapy (Limited Role)", "Carboplatin + vincristine or temozolomide used as bridge therapy in infants <18 months to delay RT; response rates modest (~20–30%); CCNU-based regimens explored for recurrent disease."),
            ("Emerging Targeted Therapies", "ZFTA-RELA fusion tumors: larotrectinib and entrectinib (TRK inhibitors) under investigation; EZH2 inhibitors for H3 K27me3-loss PF-EPN-A; CDK4/6 inhibitors for CDKN2A-deleted tumors; MEK inhibitors for YAP1-fusion tumors."),
        ],
        "img_path": "assets_images/dti_tractography.jpg",
        "caption_title": "DTI TRACTOGRAPHY & RT PLANNING",
        "caption_body": "Diffusion tensor imaging (DTI) tractography integrated into radiotherapy planning to identify corticospinal tract displacement and optimize dose distribution around eloquent structures.",
    },

    # SLIDE 7 — Ependymoma: Surgical Indications & Approaches
    {
        "type": "content",
        "badge": "EPENDYMOMA • SURGERY",
        "title": "Ependymoma: Surgical Strategy and Approaches",
        "subtitle": "Gross total resection (GTR) is the single most important prognostic factor; surgical approach is dictated by tumor location within the ventricular system.",
        "cards": [
            ("Fourth Ventricle — Telovelar Approach", "Preferred for midline fourth-ventricular ependymomas; suboccipital craniotomy with C1 laminectomy; telovelar membrane divided to expose the floor; avoids splitting the vermis; allows access to lateral recesses and foramina of Luschka."),
            ("Supratentorial Lateral Ventricle", "Transcortical (frontal/parietal) or transcallosal-transforaminal approaches for tumors in the body, atrium, or temporal horn; image guidance and ultrasound used intraoperatively; microsurgical dissection with bipolar along feeding choroidal vessels."),
            ("Third Ventricle", "Transcallosal-transforaminal or transchoroidal (Wen) approach for anterior third-ventricle ependymomas; endoscopic biopsy ± resection for small lesions; stereotactic biopsy if eloquent location precludes open surgery."),
            ("Intraoperative Adjuncts", "5-ALA fluorescence may guide resection; intraoperative MRI in select centers; neurophysiological monitoring (BAEP, MEP, facial nerve EMG) mandatory for fourth-ventricular surgery; ultrasonic aspirator (CUSA) for debulking."),
        ],
        "img_path": "enhanced_figures/fig_170_20_telovelar_ependymoma_case.png",
        "caption_title": "TELOVELAR APPROACH — EPENDYMOMA",
        "caption_body": "Intraoperative view of the telovelar approach demonstrating entry into the fourth ventricle through the tela choroidea and inferior medullary velum, exposing a large ependymoma overlying the floor.",
    },

    # SLIDE 8 — Ependymoma: Outcome & Prognosis
    {
        "type": "content",
        "badge": "EPENDYMOMA • OUTCOME & PROGNOSIS",
        "title": "Ependymoma: Survival and Prognostic Factors",
        "subtitle": "Prognosis is highly influenced by extent of resection, molecular subgroup, patient age, and tumor location.",
        "cards": [
            ("Overall Survival by Subgroup", "PF-EPN-B: 5-year OS ~90%; ST-YAP1: excellent, >90% OS with GTR; ST-RELA/ZFTA: 5-year OS ~50–70%; PF-EPN-A: worst posterior fossa subgroup with 5-year OS ~60–70% despite GTR + RT."),
            ("Impact of Extent of Resection", "GTR vs. subtotal resection (STR): 5-year PFS ~60% vs. ~20% respectively; second-look surgery for near-total resection (NTR) may convert to GTR and improve outcomes; extent of resection overrides histologic grade as a prognostic factor."),
            ("Recurrence Patterns", "Local recurrence is most common (>75%); leptomeningeal dissemination in ~10–15% overall, higher in WHO III and M+ disease; median time to recurrence ~2–4 years; re-resection and re-irradiation are options at recurrence."),
            ("Long-term Morbidity", "Posterior fossa syndrome (cerebellar mutism) in 20–30% after fourth-ventricle surgery; endocrine dysfunction after supratentorial RT; neurocognitive decline; sensorineural hearing loss from cisplatin or cochlear RT dose."),
        ],
        "img_path": "enhanced_figures/fig_170_11_subependymoma_case.png",
        "caption_title": "SUBEPENDYMOMA — POST-RESECTION",
        "caption_body": "Post-operative contrast MRI showing gross total resection of a fourth-ventricular subependymoma with no residual enhancement; excellent prognosis with surgery alone for WHO grade I lesions.",
    },

    # SLIDE 9 — Ependymoma: Complications
    {
        "type": "content",
        "badge": "EPENDYMOMA • COMPLICATIONS",
        "title": "Ependymoma: Surgical and Treatment Complications",
        "subtitle": "Complications of ependymoma surgery reflect the intimate relationship of these tumors with the brainstem floor and eloquent structures.",
        "cards": [
            ("Posterior Fossa Syndrome (Cerebellar Mutism)", "Occurs in 20–30% after fourth-ventricular surgery; transient mutism, emotional lability, hypotonia, and ataxia beginning days after surgery; associated with bilateral dentate nucleus manipulation; resolves over weeks to months."),
            ("Cranial Nerve Deficits", "CN VI palsy (diplopia), CN VII paresis (facial weakness), and lower cranial nerve deficits (dysphagia, hoarseness) from dissection along the brainstem floor or lateral recess involvement; permanent deficits in ~10–15%."),
            ("Hydrocephalus", "Persistent hydrocephalus requiring ventriculoperitoneal shunt in 20–40% despite successful resection; pseudomeningocele formation after posterior fossa craniotomy; CSF leak through wound."),
            ("Radiation-Related", "White matter injury, radiation necrosis, endocrinopathy (GH deficiency most common after CSI), secondary malignancies (meningioma, HGG), neurocognitive impairment — particularly in children irradiated before age 3."),
        ],
        "img_path": "assets_images/fourth_ventricle.jpg",
        "caption_title": "FOURTH VENTRICLE ANATOMY",
        "caption_body": "The rhomboid fossa floor contains critical cranial nerve nuclei and long tracts. Safe entry zones (facial colliculus, suprafacial triangle) must be respected to minimize permanent neurological deficits.",
    },

    # =========================================================
    # ── CENTRAL NEUROCYTOMA ──
    # =========================================================

    # SLIDE 10 — Central Neurocytoma: Types & Grades
    {
        "type": "content",
        "badge": "CENTRAL NEUROCYTOMA • OVERVIEW",
        "title": "Central Neurocytoma: Classification and Pathology",
        "subtitle": "Central neurocytoma is a WHO grade II neuronal tumor of the lateral ventricle, typically arising from the septum pellucidum near the foramen of Monro.",
        "cards": [
            ("Definition & WHO Classification", "Central neurocytoma (WHO grade II, 2021) is a well-differentiated neuronal tumor composed of uniform small cells with round nuclei, salt-and-pepper chromatin, and neuropil islands; positive for synaptophysin and NeuN."),
            ("Extraventricular Neurocytoma", "Rare variant occurring outside the ventricular system in cerebral parenchyma, spinal cord, or cerebellum; similar histology but potentially more aggressive behavior; same WHO II designation but higher recurrence risk."),
            ("Atypical Neurocytoma", "Defined by Ki-67 ≥2–3% or MIB-1 LI >2%; higher risk of recurrence; some sources consider WHO II/III spectrum; histology otherwise similar; outcome intermediate between typical and higher-grade tumors."),
            ("Molecular Markers", "No defining molecular alteration currently required for WHO 2021 diagnosis; IDH wild-type; FGFR1 alterations described; 1p/19q intact (distinguishing from oligodendroglioma); synaptophysin and NeuN positivity essential."),
        ],
        "img_path": "assets_images/central_neurocytoma.jpg",
        "caption_title": "CENTRAL NEUROCYTOMA HISTOLOGY",
        "caption_body": "Uniform small round cells with clear halos (oligodendroglioma-like) and neuropil islands on H&E. Diffuse synaptophysin positivity and NeuN nuclear staining confirm neuronal differentiation.",
    },

    # SLIDE 11 — Central Neurocytoma: Signs & Symptoms
    {
        "type": "content",
        "badge": "CENTRAL NEUROCYTOMA • SIGNS & SYMPTOMS",
        "title": "Central Neurocytoma: Clinical Features",
        "subtitle": "Peak incidence in young adults (20–40 years); symptoms arise from obstructive hydrocephalus at the foramen of Monro.",
        "cards": [
            ("Intracranial Hypertension", "Intermittent or progressive headache, nausea, and vomiting from CSF obstruction at the foramen of Monro; papilledema and visual obscurations; rare sudden death from ball-valve obstruction."),
            ("Cognitive and Memory Changes", "Compression of the fornix and septal nuclei produces short-term memory impairment, personality change, and frontal lobe syndrome; Korsakoff-like amnesia in severe cases."),
            ("Visual and Ocular Symptoms", "Bilateral or unilateral visual blurring from papilledema; upward gaze palsy (Parinaud) if posterior third-ventricle involvement; visual field defects from occipital horn expansion."),
            ("Incidental Discovery", "Up to 10–15% discovered incidentally on imaging for unrelated symptoms in young adults; small lesions without significant ventricular dilation may be observed with serial MRI."),
        ],
        "img_path": "enhanced_figures/fig_170_3_frontal_horn.png",
        "caption_title": "FRONTAL HORN & FORAMEN OF MONRO",
        "caption_body": "Axial MRI demonstrating a central neurocytoma attached to the septum pellucidum adjacent to the foramen of Monro, producing asymmetric lateral ventricular dilation on the ipsilateral side.",
    },

    # SLIDE 12 — Central Neurocytoma: Imaging & Investigations
    {
        "type": "content",
        "badge": "CENTRAL NEUROCYTOMA • IMAGING",
        "title": "Central Neurocytoma: Radiological Characteristics",
        "subtitle": "MRI reveals a heterogeneous intraventricular mass with a characteristic 'soap bubble' appearance attached to the septum pellucidum.",
        "cards": [
            ("MRI Appearance", "T1: iso- to hypointense; T2: heterogeneous with multiple cystic foci producing 'bubbly' or 'Swiss cheese' appearance; heterogeneous gadolinium enhancement; flow voids from neovascularity; attached to septum pellucidum or ependyma."),
            ("CT Findings", "Iso- to hyperdense mass on non-contrast CT; punctate calcifications in ~50–70%; homogeneous or heterogeneous enhancement; asymmetric hydrocephalus with enlarged ipsilateral lateral ventricle."),
            ("MR Spectroscopy", "Elevated glycine peak at 3.55 ppm — highly specific for neurocytoma (distinguishes from oligodendroglioma); elevated choline; reduced NAA; alanine peak may be present; useful non-invasive diagnostic adjunct."),
            ("DSA / CTA", "Tumor blush from medial and lateral posterior choroidal artery supply; pre-operative embolization may reduce intraoperative bleeding; venous phase shows relationship to internal cerebral veins and thalamostriate vein."),
        ],
        "img_path": "enhanced_figures/fig_170_1_dcta.png",
        "caption_title": "DCTA — CHOROIDAL ARTERIAL SUPPLY",
        "caption_body": "Digital subtraction CT angiography depicting the medial posterior choroidal artery supply to a lateral ventricular neurocytoma; early venous drainage through the internal cerebral vein system.",
    },

    # SLIDE 13 — Central Neurocytoma: Surgery & Outcomes
    {
        "type": "content",
        "badge": "CENTRAL NEUROCYTOMA • SURGERY & OUTCOMES",
        "title": "Central Neurocytoma: Surgical Management and Prognosis",
        "subtitle": "GTR is curative for typical neurocytoma; subtotal resection combined with radiosurgery achieves excellent local control.",
        "cards": [
            ("Surgical Approach", "Transcallosal-transforaminal approach preferred for foramen of Monro lesions; transcortical approach via frontal cortex for large posterior body lesions; endoscopic resection for small lesions; neuronavigation and intraoperative ultrasound guide safe dissection."),
            ("Radiosurgery (SRS)", "Gamma Knife or CyberKnife for residual/recurrent disease; excellent local control (~90% at 5 years) for lesions <3 cm; marginal dose 12–15 Gy; alternative to fractionated RT for small residuals."),
            ("Prognosis — Typical", "Typical neurocytoma (Ki-67 <2%): 5-year recurrence-free survival ~85% after GTR; 10-year OS >90%; excellent quality of life if forniceal and hypothalamic structures preserved."),
            ("Prognosis — Atypical", "Atypical neurocytoma (Ki-67 ≥2%): higher recurrence rate (~50% at 5 years); adjuvant RT (50–54 Gy) recommended after STR; chemotherapy (temozolomide) explored for multiply recurrent cases."),
        ],
        "img_path": "enhanced_figures/fig_170_17_transchoroidal_case.png",
        "caption_title": "TRANSCHOROIDAL RESECTION",
        "caption_body": "Intraoperative microscopic view of transchoroidal approach to the lateral ventricle; the choroidal fissure has been opened to expose and resect a neurocytoma arising from the septum pellucidum.",
    },

    # =========================================================
    # ── CHOROID PLEXUS TUMORS ──
    # =========================================================

    # SLIDE 14 — Choroid Plexus Tumors: Types & Grades
    {
        "type": "content",
        "badge": "CHOROID PLEXUS TUMORS • TYPES & GRADES",
        "title": "Choroid Plexus Tumors: Classification",
        "subtitle": "Choroid plexus tumors arise from the epithelium of the choroid plexus; classified as papilloma (WHO I), atypical papilloma (WHO II), or carcinoma (WHO III).",
        "cards": [
            ("Choroid Plexus Papilloma — WHO I", "Well-differentiated frond-like papillary growth of columnar cells on fibrovascular cores; strong TTR (transthyretin) expression; 80% of all CPlx tumors; lateral ventricle in children, fourth ventricle in adults; CPC7 (TWIST1) required for WHO 2021 designation."),
            ("Atypical Choroid Plexus Papilloma — WHO II", "Increased mitoses (≥2/10 HPF) without other malignant features; intermediate behavior; 10–20% recurrence rate; complete resection curative in most cases; TP53 mutations beginning to appear."),
            ("Choroid Plexus Carcinoma — WHO III", "Malignant: marked cytological atypia, ≥5 mitoses/10 HPF, necrosis, dense cellularity, loss of papillary architecture, brain invasion; TP53 mutation in 50%; SMARCB1 loss in Li-Fraumeni syndrome; worst prognosis; CSF dissemination common."),
            ("Molecular Alterations (2021)", "CPC: TP53 (50–80%), CDKN2A/B deletion, MYC amplification; SMARCB1/SMARCA4 loss in constitutional tumors; CPP: generally diploid with few alterations; DNA methylation profiling separates groups reliably."),
        ],
        "img_path": "assets_images/choroid_papilloma.jpg",
        "caption_title": "CHOROID PLEXUS PAPILLOMA",
        "caption_body": "Histology of WHO grade I choroid plexus papilloma showing well-ordered columnar epithelium on fibrovascular fronds, resembling normal choroid plexus architecture with minimal atypia.",
    },

    # SLIDE 15 — Choroid Plexus Tumors: Signs, Symptoms & Imaging
    {
        "type": "content",
        "badge": "CHOROID PLEXUS TUMORS • PRESENTATION & IMAGING",
        "title": "Choroid Plexus Tumors: Clinical Presentation and Radiology",
        "subtitle": "Overproduction of CSF by papillomas causes communicating hydrocephalus; carcinomas present with rapidly progressive symptoms and brain invasion.",
        "cards": [
            ("Clinical Presentation", "Infants: rapidly enlarging head circumference, bulging fontanelle, sunset sign, irritability; older children/adults: symptoms of raised ICP (headache, vomiting, papilledema); CPC may present with focal deficits from parenchymal invasion."),
            ("MRI Characteristics", "CPP: T1 iso/hypo, T2 hyperintense cauliflower-like mass with frond-like surface, intense homogeneous enhancement; CPC: heterogeneous, necrotic, invades adjacent brain, perilesional edema, leptomeningeal spread."),
            ("Location by Age", "Children: 80% in lateral ventricle (trigone/atrium); neonates: bilateral tumors possible; adults: more commonly in fourth ventricle or cerebellopontine angle; CPC shows less location specificity."),
            ("Investigations", "MRI brain + spine (CPC mandatory for staging); CSF cytology; lumbar puncture after ICP stabilized; TP53 germline testing for Li-Fraumeni syndrome in CPC patients; serum alpha-fetoprotein and beta-hCG if GCT in differential."),
        ],
        "img_path": "assets_images/choroid_plexus.jpg",
        "caption_title": "CHOROID PLEXUS ANATOMY",
        "caption_body": "The choroid plexus occupies the temporal horn, body, and atrium of the lateral ventricles, the roof of the third ventricle, and the roof of the fourth ventricle — predicting the distribution of choroid plexus tumors.",
    },

    # SLIDE 16 — Choroid Plexus Tumors: Surgery & Outcomes
    {
        "type": "content",
        "badge": "CHOROID PLEXUS TUMORS • SURGERY & OUTCOMES",
        "title": "Choroid Plexus Tumors: Surgical Management and Prognosis",
        "subtitle": "Complete surgical resection is the cornerstone of treatment; vascular control of choroidal supply is critical to managing intraoperative hemorrhage.",
        "cards": [
            ("Surgical Strategy", "Early arterial devascularization of posterior choroidal arteries before tumor delivery; piecemeal resection within the ventricular cavity; transcortical or transcallosal approach depending on location; pre-operative embolization for hypervascular CPC."),
            ("Adjuvant Therapy for CPC", "Adjuvant chemotherapy (cyclophosphamide, carboplatin, vincristine — 'ICE' regimen) followed by RT (CSI 35–36 Gy + boost); young children: chemotherapy-first to delay RT; survival strongly linked to surgical completeness."),
            ("Prognosis — Papilloma", "CPP (WHO I): 5-year OS ~90%; GTR effectively curative; recurrence in <10%; STR requires re-resection; communicating hydrocephalus resolves in most after complete removal without need for VP shunt."),
            ("Prognosis — Carcinoma", "CPC (WHO III): 5-year OS ~30–40% without complete resection; 5-year OS ~70% with GTR + adjuvant therapy; leptomeningeal dissemination at diagnosis (~45%) dramatically worsens prognosis; TP53 mutation associated with poorer outcome."),
        ],
        "img_path": "enhanced_figures/fig_170_15_transfrontal_case.png",
        "caption_title": "TRANSFRONTAL VENTRICULAR APPROACH",
        "caption_body": "Post-operative MRI after transfrontal transcortical approach for trigonal choroid plexus papilloma resection; complete removal with resolution of hydrocephalus and no residual enhancement.",
    },

    # =========================================================
    # ── COLLOID CYST ──
    # =========================================================

    # SLIDE 17 — Colloid Cyst: Overview & Symptoms
    {
        "type": "content",
        "badge": "COLLOID CYST • OVERVIEW & SYMPTOMS",
        "title": "Colloid Cyst of the Third Ventricle",
        "subtitle": "A benign neuroepithelial cyst arising at the roof of the third ventricle that can cause sudden death from acute foramen of Monro obstruction.",
        "cards": [
            ("Pathology & Origin", "Benign mucin-filled cyst lined by simple cuboidal to columnar epithelium; arises from remnant of the paraphysis or endodermal elements at the foramen of Monro; contents vary from watery to gel-like ('motor oil'); NOT a neoplasm per se but surgically managed."),
            ("Intermittent Obstructive Symptoms", "Classic 'positional headache' — sudden severe headache precipitated by neck flexion, Valsalva, or head position change due to transient foramen of Monro obstruction; nausea, vomiting, and visual blurring; symptoms resolve with position change."),
            ("Memory Impairment", "Chronic fornix compression from cyst pressure produces short-term memory deficits, Korsakoff-type amnesia, and personality change; hypothalamic compression causes endocrine dysfunction in large cysts."),
            ("Sudden Death", "Acute complete obstruction of both foramina of Monro causes catastrophic bilateral hydrocephalus; sudden death reported in ~1–2% of patients; risk stratification by cyst size (>1.5 cm), hydrocephalus presence, and symptom pattern guides urgency of intervention."),
        ],
        "img_path": "enhanced_figures/fig_170_7_third_ventricle.png",
        "caption_title": "THIRD VENTRICLE — COLLOID CYST LOCATION",
        "caption_body": "Sagittal MRI demonstrating a colloid cyst occupying the anterior roof of the third ventricle at the foramen of Monro, with resulting bilateral lateral ventricular dilation.",
    },

    # SLIDE 18 — Colloid Cyst: Imaging, Surgery & Outcomes
    {
        "type": "content",
        "badge": "COLLOID CYST • IMAGING, SURGERY & OUTCOMES",
        "title": "Colloid Cyst: Diagnosis, Surgical Options, and Prognosis",
        "subtitle": "Endoscopic or microsurgical resection is curative; approach selection depends on cyst size, consistency, and forniceal anatomy.",
        "cards": [
            ("Imaging Features", "MRI: T1 signal variable — hypointense (watery) to hyperintense (proteinaceous/mucoid); T2 inversely correlates with T1 signal; no enhancement; CT: hyperdense in 2/3 of cases (classic finding); cyst located at foramen of Monro between columns of fornix."),
            ("Endoscopic Resection", "Endoscopic approach via frontal burr hole: best for T2-bright (low-viscosity) cysts; 70–80% complete removal rate; lower morbidity than microsurgery; cyst contents aspirated then wall coagulated; risk of fornix injury during wall removal."),
            ("Microsurgical Transcallosal Approach", "Preferred for T1-hyperintense (thick/viscous) cysts; superior visualization and wall removal rates; callosotomy 1.5–2 cm anterior to coronal suture; forniceal retraction; complete capsule resection to prevent recurrence (~5% vs ~30% with endoscopic)."),
            ("Outcomes & Observation", "Asymptomatic small cysts (<7 mm, no hydrocephalus): annual MRI surveillance acceptable; surgical mortality <1% in experienced hands; memory improvement in 60–70% after relief of forniceal compression; recurrence after complete microsurgical removal <5%."),
        ],
        "img_path": "enhanced_figures/fig_170_18_etv_case.png",
        "caption_title": "ENDOSCOPIC THIRD VENTRICULAR APPROACH",
        "caption_body": "Endoscopic view through the foramen of Monro showing a colloid cyst being aspirated; the fornix columns are visible bilaterally requiring careful retraction to prevent permanent memory deficits.",
    },

    # =========================================================
    # ── SEGA ──
    # =========================================================

    # SLIDE 19 — SEGA: Overview, Symptoms & Imaging
    {
        "type": "content",
        "badge": "SEGA • OVERVIEW & PRESENTATION",
        "title": "Subependymal Giant Cell Astrocytoma (SEGA)",
        "subtitle": "SEGA is a WHO grade I tumor arising in the setting of tuberous sclerosis complex (TSC), characteristically occurring at the foramen of Monro.",
        "cards": [
            ("Pathology & Genetics", "Large gemistocyte-like cells with abundant eosinophilic cytoplasm; mixed glioneuronal differentiation; GFAP and synaptophysin co-expression; caused by biallelic loss of TSC1 (hamartin) or TSC2 (tuberin), leading to mTORC1 pathway hyperactivation."),
            ("Epidemiology & Growth", "Present in 10–15% of TSC patients; grow slowly (≥0.5 cm/year by imaging); highest growth rate in children/adolescents; symptomatic tumors typically >1 cm; annual surveillance MRI from childhood recommended in TSC patients."),
            ("Clinical Presentation", "Hydrocephalus and raised ICP are the primary presentations; seizures (independent of the SEGA, from cortical tubers); cognitive regression; headache; papilledema; incidental in screened TSC patients."),
            ("Imaging Characteristics", "CT: heterogeneously calcified mass at the caudothalamic groove/foramen of Monro; MRI: T1 iso, T2 heterogeneous with blooming calcifications; intense and heterogeneous gadolinium enhancement; serial growth on surveillance imaging is defining criterion."),
        ],
        "img_path": "assets_images/pilocytic_astrocytoma.jpg",
        "caption_title": "SEGA — GIANT CELL MORPHOLOGY",
        "caption_body": "Histology of SEGA showing characteristic large gemistocytic cells with abundant glassy cytoplasm, vesicular nuclei, and prominent nucleoli, admixed with spindle cells; GFAP and synaptophysin positive.",
    },

    # SLIDE 20 — SEGA: Medical Therapy, Surgery & Outcomes
    {
        "type": "content",
        "badge": "SEGA • TREATMENT & OUTCOMES",
        "title": "SEGA: mTOR Inhibitors, Surgery, and Prognosis",
        "subtitle": "Everolimus (mTORC1 inhibitor) is now first-line for many patients; surgery reserved for acute hydrocephalus and everolimus failures.",
        "cards": [
            ("Everolimus (mTOR Inhibitor)", "FDA-approved for SEGA in TSC patients; induces tumor volume reduction in ~50% of patients (≥50% reduction in 35%); taken continuously — discontinuation causes tumor regrowth; also reduces seizure burden and skin lesions; EXIST-1 trial demonstrated efficacy."),
            ("Surgical Resection", "Indicated for: acute obstructive hydrocephalus, everolimus failure, or patient/family preference; transcallosal-transforaminal or endoscopic approach; GTR achievable in >90%; calcified components may require CUSA or ultrasonic fragmentation; VP shunt if GTR not feasible."),
            ("Surgical Outcomes", "GTR: recurrence rare (<5%) but annual MRI surveillance maintained; surgical morbidity primarily from forniceal manipulation (memory, motivation); endocrine dysfunction if hypothalamic manipulation; overall surgical mortality <1%."),
            ("Long-term Surveillance", "Lifelong MRI every 1–3 years after surgical GTR; continued everolimus for residual disease, bilateral tumors, or diffuse TSC burden; multidisciplinary TSC clinic management including nephrology (AML), pulmonology (LAM), and dermatology."),
        ],
        "img_path": "enhanced_figures/fig_170_4_venous_angle.png",
        "caption_title": "FORAMEN OF MONRO & VENOUS ANGLE",
        "caption_body": "The thalamostriate vein meets the internal cerebral vein at the venous angle at the foramen of Monro — a critical landmark during SEGA resection to prevent catastrophic venous infarction.",
    },

    # =========================================================
    # ── INTRAVENTRICULAR MENINGIOMA ──
    # =========================================================

    # SLIDE 21 — Intraventricular Meningioma: Overview & Symptoms
    {
        "type": "content",
        "badge": "INTRAVENTRICULAR MENINGIOMA • OVERVIEW",
        "title": "Intraventricular Meningioma: Classification and Presentation",
        "subtitle": "Rare meningiomas arising from arachnoid cell rests within the choroid plexus stroma, predominantly in the trigone of the lateral ventricle.",
        "cards": [
            ("Epidemiology & Location", "Account for 0.5–3% of all intracranial meningiomas; 80% arise in the trigone (atrium) of the lateral ventricle; left-sided predominance (2:1); more common in women (3:1); middle-aged adults; rare in third or fourth ventricle."),
            ("Histological Subtypes", "Meningothelial (most common intraventricularly), transitional, fibrous, and rarely angiomatous; WHO grade I in >95%; WHO II (atypical) and III (anaplastic) are rare but reported; express EMA and PR (progesterone receptor)."),
            ("Clinical Presentation", "Headache and progressive memory loss from trigonal mass effect on the temporal and occipital horns; contralateral homonymous hemianopia (optic radiation compression); contralateral hemiparesis; raised ICP symptoms when large; seizures less common than cortical meningiomas."),
            ("Imaging Features", "CT: homogeneously hyperdense, calcified in 50%; MRI T1 iso, T2 iso/slight hyper; homogeneous intense enhancement with dural tail absent (no dura attachment); located in trigone without apparent cortical attachment; DDx: CPP, ependymoma, cavernoma."),
        ],
        "img_path": "assets_images/meningioma.jpg",
        "caption_title": "MENINGIOMA HISTOLOGY",
        "caption_body": "Whorls and psammoma bodies are characteristic of meningothelial meningioma. Intraventricular meningiomas share identical histology but arise from choroidal arachnoid rests rather than dural meningothelial cells.",
    },

    # SLIDE 22 — Intraventricular Meningioma: Surgery & Outcomes
    {
        "type": "content",
        "badge": "INTRAVENTRICULAR MENINGIOMA • SURGERY & OUTCOMES",
        "title": "Intraventricular Meningioma: Surgical Approaches and Prognosis",
        "subtitle": "Surgical resection is curative for WHO grade I lesions; approach selection must protect the optic radiations and visual cortex.",
        "cards": [
            ("Surgical Approaches", "Parieto-occipital transcortical (most common): through the superior parietal lobule posterior to the postcentral gyrus; transcallosal posterior interhemispheric; trans-sylvian temporal approach for anterior temporal horn tumors; all require neuronavigation and intraoperative mapping."),
            ("Optic Radiation Preservation", "DTI tractography pre-operatively delineates Meyer's loop and the optic radiations for surgical planning; superior temporal gyrus approaches risk visual field deficits in ~30%; subcortical stimulation mapping of posterior thalamic radiation during awake craniotomy reduces deficit."),
            ("Vascular Control", "Choroidal arterial feeders (anterior and posterior choroidal arteries) must be identified and coagulated early; circumferential dissection from tumor margins inward; avoid avulsion of thalamostriate or internal cerebral veins; pre-operative embolization rarely indicated."),
            ("Prognosis", "GTR (Simpson I–II) for WHO I: <10% recurrence at 10 years; excellent functional outcome if visual fields and motor function preserved; WHO II/III: adjuvant RT recommended; recurrence rates parallel extracranial meningioma of equivalent grade."),
        ],
        "img_path": "assets_images/approach_parietal_wiki.jpg",
        "caption_title": "PARIETO-OCCIPITAL APPROACH",
        "caption_body": "The parieto-occipital transcortical approach provides direct access to the trigone of the lateral ventricle; the incision is placed posterior to the postcentral gyrus to minimize somatosensory deficits.",
    },

    # =========================================================
    # ── CRANIOPHARYNGIOMA ──
    # =========================================================

    # SLIDE 23 — Craniopharyngioma: Types & Grades
    {
        "type": "content",
        "badge": "CRANIOPHARYNGIOMA • TYPES & PATHOLOGY",
        "title": "Craniopharyngioma: Adamantinomatous vs Papillary Types",
        "subtitle": "Craniopharyngioma is a WHO grade I epithelial tumor arising from Rathke's pouch remnants in the sellar/suprasellar region with frequent third ventricle involvement.",
        "cards": [
            ("Adamantinomatous Type (ACP)", "Bimodal age distribution (5–15 years and 45–60 years); 'wet keratin' and cholesterol crystals; calcifications in 90% on CT; CTNNB1 (β-catenin) mutation activating Wnt pathway; whorl-like epithelium with palisading basal layer; cystic with 'motor oil' fluid."),
            ("Papillary Type (PCP)", "Almost exclusively in adults (40–60 years); solid with pseudopapillary squamoid epithelium; rarely calcified; BRAF V600E mutation in nearly 100%; no wet keratin; WHO grade I; responds to BRAF+MEK inhibitor targeted therapy — paradigm-changing."),
            ("Third Ventricle Involvement", "Retrochiasmatic / third-ventricular craniopharyngiomas have the worst prognosis; classified by Kassam and De Vries into intraventricular (65%), extra-arachnoidal/stalk (25%), and infra-diaphragmatic; third-ventricle invasion causes hypothalamic dysfunction."),
            ("Hypothalamic Grading (Muller)", "Grade 0: no hypothalamic contact; Grade 1: contact/distortion without involvement; Grade 2: hypothalamic invasion — associated with hyperphagia, obesity, memory loss, diabetes insipidus, and panhypopituitarism; Grade 2 predicts worst QoL outcomes."),
        ],
        "img_path": "assets_images/craniopharyngioma_wiki.jpg",
        "caption_title": "CRANIOPHARYNGIOMA — ADAMANTINOMATOUS",
        "caption_body": "Adamantinomatous craniopharyngioma showing stellate reticulum, wet keratin (ghost cells), and palisading epithelium; cholesterol crystals and calcifications are hallmarks of this childhood variant.",
    },

    # SLIDE 24 — Craniopharyngioma: Signs & Symptoms
    {
        "type": "content",
        "badge": "CRANIOPHARYNGIOMA • SIGNS & SYMPTOMS",
        "title": "Craniopharyngioma: Clinical Triad and Endocrine Dysfunction",
        "subtitle": "The classic triad of visual disturbance, endocrine dysfunction, and raised ICP defines the clinical presentation of craniopharyngioma.",
        "cards": [
            ("Visual Symptoms", "Bitemporal hemianopia (chiasm compression) is present in 60–80%; visual acuity loss; optic atrophy from chronic compression; papilledema from hydrocephalus; visual recovery possible after early decompression but unlikely with chronic optic atrophy."),
            ("Endocrine Dysfunction", "GH deficiency (most common, 75%); hypothyroidism (TSH deficiency); hypogonadism; ACTH deficiency; diabetes insipidus (DI) in 15–20% pre-operatively, increases to 80–90% post-operatively; hyperphagia and morbid obesity from hypothalamic damage."),
            ("Intracranial Hypertension", "Hydrocephalus in 30–40% from aqueductal compression or third-ventricle obstruction; headache, nausea; papilledema; urgent CSF diversion (EVD/VP shunt) may be needed before definitive surgery."),
            ("Hypothalamic Syndrome", "Weight gain, hypersomnia, temperature dysregulation, behavioral disturbances, and cognitive impairment from hypothalamic involvement; most devastating long-term morbidity — often more disabling than the tumor itself; Muller grade 2 predicts syndrome development."),
        ],
        "img_path": "assets_images/third_ventricle.jpg",
        "caption_title": "THIRD VENTRICLE & HYPOTHALAMUS",
        "caption_body": "Sagittal anatomy of the third ventricle showing the optic chiasm, hypothalamus, pituitary stalk, and mammillary bodies — all structures at risk from craniopharyngioma invasion and surgical manipulation.",
    },

    # SLIDE 25 — Craniopharyngioma: Imaging, Medical Therapy & Surgery
    {
        "type": "content",
        "badge": "CRANIOPHARYNGIOMA • IMAGING, THERAPY & SURGERY",
        "title": "Craniopharyngioma: Radiology, BRAF Inhibitors, and Surgical Approaches",
        "subtitle": "Targeted therapy with BRAF+MEK inhibitors has revolutionized the management of papillary craniopharyngioma; surgical strategy prioritizes hypothalamic preservation.",
        "cards": [
            ("Imaging Characteristics", "ACP: CT shows 'eggshell' calcification; MRI T1 hyperintense cyst (cholesterol/protein), solid enhancing mural nodule, T2 heterogeneous; PCP: predominantly solid, rarely calcified, uniform enhancement; MRI sagittal/coronal for chiasm and stalk anatomy."),
            ("BRAF+MEK Inhibitors (PCP)", "Dabrafenib + trametinib produces dramatic tumor response in BRAF V600E papillary craniopharyngioma (>90% response rate); used neo-adjuvantly to reduce tumor volume before surgery, or as primary therapy for inoperable cases; ongoing trials (NCT04023318)."),
            ("Surgical Approaches", "Transcranial: pterional/frontolateral, interhemispheric-transcallosal for pure third-ventricular tumors; endoscopic endonasal transsphenoidal: excellent for infradiaphragmatic and retrochiasmatic lesions below the chiasm; hypothalamus-sparing philosophy now standard."),
            ("Limited Surgery + RT", "For Muller grade 2 hypothalamic involvement: planned subtotal resection (STR) + adjuvant RT (54–59.4 Gy) yields comparable tumor control to radical resection with significantly better QoL and lower obesity/endocrine morbidity — paradigm shift from radical surgery."),
        ],
        "img_path": "enhanced_figures/fig_170_13_endonasal_case.png",
        "caption_title": "ENDOSCOPIC ENDONASAL APPROACH",
        "caption_body": "Endoscopic endonasal transsphenoidal approach to a retrochiasmatic craniopharyngioma; the optic chiasm is decompressed from below, avoiding the transcranial route and its hypothalamic manipulation risks.",
    },

    # SLIDE 26 — Craniopharyngioma: Outcomes & Complications
    {
        "type": "content",
        "badge": "CRANIOPHARYNGIOMA • OUTCOMES & COMPLICATIONS",
        "title": "Craniopharyngioma: Long-term Prognosis and Complications",
        "subtitle": "Despite WHO grade I designation, craniopharyngioma carries significant long-term morbidity primarily from hypothalamic-pituitary axis dysfunction.",
        "cards": [
            ("Survival Outcomes", "10-year OS: 85–90%; local recurrence is the primary challenge (30–50% at 10 years without adjuvant RT); GTR alone recurrence ~20–30%; STR + RT: recurrence ~15–25%; second-look surgery and SRS options at recurrence."),
            ("Endocrine Complications", "Post-operative panhypopituitarism in 80–100%; permanent DI in 80–90%; mandatory lifelong hormone replacement (GH, thyroid, adrenal, sex hormones, DDAVP); sodium dysregulation (SIADH/DI cycling) in first 1–2 post-operative weeks requires intensive monitoring."),
            ("Hypothalamic Obesity", "Occurs in 50% of patients with hypothalamic involvement; severe, refractory to dietary measures; contributes to cardiovascular morbidity and reduced QoL; GLP-1 agonists (semaglutide, liraglutide) show promise; bariatric surgery in selected cases."),
            ("Neurocognitive & Psychological Impact", "Memory impairment, executive dysfunction, depression, and social isolation common; reduced quality of life scores compared to general population; psychosocial support and neuropsychological rehabilitation essential in multidisciplinary care."),
        ],
        "img_path": "enhanced_figures/fig_170_14_cranioorbital_case.png",
        "caption_title": "CRANIO-ORBITAL APPROACH",
        "caption_body": "The cranio-orbital or orbitozygomatic approach provides a superior panoramic view of the sellar, suprasellar, and anterior third-ventricular compartments for craniopharyngioma resection with reduced brain retraction.",
    },

    # =========================================================
    # ── GERMINOMA / GERM CELL TUMORS ──
    # =========================================================

    # SLIDE 27 — Germinoma: Types & Classification
    {
        "type": "content",
        "badge": "GERM CELL TUMORS • CLASSIFICATION",
        "title": "Intracranial Germ Cell Tumors: Classification and Pathology",
        "subtitle": "Intracranial GCTs are classified by the WHO 2021 using the same schema as gonadal GCTs; germinoma carries the best prognosis among all intracranial GCTs.",
        "cards": [
            ("Germinoma (Pure)", "Most common intracranial GCT (65%); uniform large cells with clear cytoplasm and prominent nucleoli; lymphocytic infiltrate; OCT4, NANOG, c-Kit, and PLAP positive; highly radiosensitive; bifocal germinoma (pineal + suprasellar) is pathognomonic."),
            ("Non-Germinomatous GCTs (NGGCTs)", "Include: embryonal carcinoma, endodermal sinus (yolk sac) tumor, choriocarcinoma, teratoma (mature/immature), and mixed GCTs; AFP elevated in yolk sac tumors; beta-hCG elevated in choriocarcinoma; require multimodal treatment; prognosis varies by component."),
            ("Location & Demographics", "Pineal region (40%): predominantly male; suprasellar/hypothalamus (35%): female preponderance; bifocal (20%); basal ganglia/thalamus (5%); peak incidence 10–14 years; rare in adults; Asian populations have higher incidence (3–4x)."),
            ("Molecular Features (2021)", "KIT/RAS pathway mutations (KIT, KRAS, NRAS); MAPK pathway; isochromosome 12p in some; C11orf95-RELA fusion not applicable; methylation profiling separates GCT subgroups reliably from other pineal region tumors."),
        ],
        "img_path": "assets_images/germinoma.jpg",
        "caption_title": "GERMINOMA HISTOLOGY",
        "caption_body": "Germinoma showing large polygonal tumor cells with clear glycogen-rich cytoplasm and prominent nucleoli, separated by lymphocyte-rich fibrous septa; PLAP, OCT4, and NANOG immunopositivity confirm diagnosis.",
    },

    # SLIDE 28 — Germinoma: Signs & Symptoms
    {
        "type": "content",
        "badge": "GERM CELL TUMORS • SIGNS & SYMPTOMS",
        "title": "Intracranial GCT: Clinical Presentation by Location",
        "subtitle": "Parinaud syndrome (pineal region) and diabetes insipidus (suprasellar) are the hallmark presentations of intracranial germ cell tumors.",
        "cards": [
            ("Parinaud Syndrome (Pineal Region)", "Dorsal midbrain compression produces: upgaze paralysis, convergence-retraction nystagmus, light-near dissociation, and eyelid retraction (Collier's sign); obstructive hydrocephalus from aqueductal compression produces headache, nausea, vomiting; papilledema."),
            ("Suprasellar / Hypothalamic Presentation", "Diabetes insipidus (DI) is often the presenting symptom — polyuria and polydipsia for months to years before diagnosis; growth failure and delayed puberty from GH/gonadotropin deficiency; visual field defects from chiasm compression."),
            ("Bifocal Disease", "Synchronous pineal and suprasellar tumors are virtually pathognomonic for bifocal germinoma; combined endocrine dysfunction (DI + pituitary insufficiency) with Parinaud syndrome; spinal dissemination in ~10% at presentation."),
            ("Raised ICP", "Obstructive hydrocephalus from aqueductal stenosis (pineal) or foramen of Monro obstruction (suprasellar); urgent management with ETV or VP shunt; sudden deterioration from acute hydrocephalus is a neurosurgical emergency."),
        ],
        "img_path": "assets_images/parinaud_syndrome.jpg",
        "caption_title": "PARINAUD SYNDROME",
        "caption_body": "Parinaud or dorsal midbrain syndrome: upgaze palsy, convergence-retraction nystagmus on attempted upgaze, and light-near dissociation from superior colliculus and posterior commissure compression by pineal region masses.",
    },

    # SLIDE 29 — Germinoma: Imaging & Investigations
    {
        "type": "content",
        "badge": "GERM CELL TUMORS • IMAGING & INVESTIGATIONS",
        "title": "Intracranial GCT: Diagnostic Workup",
        "subtitle": "Serum and CSF tumor markers combined with MRI are often sufficient for diagnosis; tissue biopsy is mandatory for NGGCTs and marker-negative cases.",
        "cards": [
            ("Tumor Markers", "Serum and CSF AFP: elevated in yolk sac tumors (>25 ng/mL diagnostic); CSF/serum beta-hCG >50 mIU/mL indicates choriocarcinoma or syncytiotrophoblastic cells; slightly elevated hCG (<50) seen in pure germinoma; normal markers + bifocal lesion = strong presumptive germinoma diagnosis."),
            ("MRI Characteristics", "Germinoma: T1 iso/hypo, T2 iso, avid homogeneous enhancement; engulfs pineal gland ('snowman' sign); pineal calcification displaced to periphery. NGGCT: heterogeneous, fat signal in teratoma, hemorrhage in choriocarcinoma, cystic components."),
            ("CSF Analysis", "Mandatory LP for cytology, AFP, hCG, PLAP; lumbar puncture after ICP stabilized; cytology positive in 10–15%; elevated LDH; staging MRI of entire neuraxis for dissemination; LP may be avoided if elevated ICP."),
            ("ETV + Biopsy Strategy", "Combined endoscopic procedure: ETV for hydrocephalus + simultaneous biopsy via flexible endoscope through foramen of Monro + stereotactic pineal biopsy; allows tissue diagnosis while simultaneously treating hydrocephalus."),
        ],
        "img_path": "assets_images/pineal_gland_wiki.jpg",
        "caption_title": "PINEAL REGION ANATOMY",
        "caption_body": "The pineal gland lies at the posterior commissure above the superior colliculi; displaced or engulfed by germinoma — the 'exploded calcification' sign on CT distinguishes germinoma from pineocytoma.",
    },

    # SLIDE 30 — Germinoma: Treatment & Outcomes
    {
        "type": "content",
        "badge": "GERM CELL TUMORS • TREATMENT & OUTCOMES",
        "title": "Intracranial GCT: Treatment Protocols and Prognosis",
        "subtitle": "Pure germinoma is one of the most curable intracranial tumors with modern combined chemo-radiotherapy protocols; NGGCTs require intensified treatment.",
        "cards": [
            ("Germinoma Treatment Protocol", "Chemotherapy-first (carboplatin + etoposide, 4 cycles) followed by reduced-dose whole-ventricular irradiation (WVI, 24 Gy) + tumor boost (16 Gy) achieves 5-year OS >95%; CSI (30–36 Gy) for M+ disease; eliminates need for GTR in most cases."),
            ("NGGCT Treatment", "Intensive chemotherapy (BEP: bleomycin + etoposide + cisplatin; or ICE) followed by craniospinal irradiation (36 Gy CSI + 54 Gy local boost) ± second-look surgery for residual teratoma ('growing teratoma syndrome'); 5-year OS 60–70%."),
            ("Role of Surgery", "Primarily diagnostic (biopsy); GTR not required for germinoma; surgical resection of residual mature teratoma after chemotherapy (growing teratoma syndrome); ETV for hydrocephalus; occipital transtentorial or infratentorial supracerebellar approach for open biopsy/resection."),
            ("Prognosis", "Pure germinoma: 5-year OS >95%; localized NGGCT: 5-year OS ~70%; disseminated NGGCT: 5-year OS ~50%; mature teratoma with GTR: essentially cured; recurrent germinoma salvageable with high-dose chemotherapy + autologous stem cell rescue."),
        ],
        "img_path": "enhanced_figures/fig_170_19_coz_case.png",
        "caption_title": "OCCIPITAL TRANSTENTORIAL APPROACH",
        "caption_body": "Occipital transtentorial (COZ) approach to the pineal region: the patient is in the sitting or three-quarter prone position; tentorium is retracted to expose the pineal region, vein of Galen, and internal cerebral veins.",
    },

    # =========================================================
    # ── SURGICAL APPROACHES SECTION ──
    # =========================================================

    # SLIDE 31 — Section Header: Surgical Approaches
    {
        "type": "content",
        "badge": "SURGICAL APPROACHES • OVERVIEW",
        "title": "Surgical Approaches to Intraventricular Tumors",
        "subtitle": "Selection of the optimal approach depends on tumor location, size, consistency, vascularity, and proximity to eloquent structures.",
        "cards": [
            ("Transcallosal Approaches", "The transcallosal route provides midline access to the ventricular system through the corpus callosum; avoids cortical incision; preferred for midline and bilateral pathology; variants include transforaminal and transchoroidal extensions."),
            ("Transcortical Approaches", "Direct cortical incision through non-eloquent gyrus; wider working angle for large lateral ventricular tumors; higher seizure risk than transcallosal; preferred for large atrial or temporal horn tumors remote from eloquent cortex."),
            ("Posterior Fossa Approaches", "Telovelar (fourth ventricle) and infratentorial supracerebellar (pineal/posterior third ventricle); suboccipital craniotomies with position-dependent gravity retraction; avoid vermian splitting when possible."),
            ("Endoscopic Approaches", "Endoscopic third ventriculostomy (ETV), biopsy, and colloid cyst aspiration; rigid endoscope via frontal burr hole; flexible endoscopy for bilateral or posterior ventricular pathology; minimally invasive with excellent visualization."),
        ],
        "img_path": "enhanced_figures/fig_170_10_surgical_approaches.png",
        "caption_title": "OVERVIEW OF VENTRICULAR APPROACHES",
        "caption_body": "Schematic demonstrating the principal surgical corridors to the ventricular system: transcallosal, transcortical, telovelar, and endoscopic routes — each optimized for specific locations and pathologies.",
    },

    # SLIDE 32 — Transcallosal-Transforaminal Approach
    {
        "type": "content",
        "badge": "SURGICAL APPROACHES • TRANSCALLOSAL-TRANSFORAMINAL",
        "title": "Transcallosal-Transforaminal Approach",
        "subtitle": "The workhorse approach for anterior third ventricle and foramen of Monro pathology; provides direct access without cortical disruption.",
        "cards": [
            ("Patient Position & Craniotomy", "Supine with 30° head elevation; midline parasagittal craniotomy straddling the coronal suture (2/3 anterior, 1/3 posterior); right-sided approach preferred (non-dominant hemisphere); craniotomy 3–4 cm lateral to midline to allow brain retraction."),
            ("Interhemispheric Dissection", "Dissect along falx in the interhemispheric fissure under microscope with bipolar coagulation of bridging cortical veins if unavoidable; identify the pericallosal arteries bilaterally — retract medially; callosotomy of 1.5–2 cm made in the anterior body."),
            ("Transforaminal Entry", "Identify choroidal fissure and thalamostriate vein (venous angle landmark); enlarged foramen of Monro provides access to anterior third ventricle; choroid plexus retracted; fornix retraction medially provides working corridor; tumor removed via CUSA and suction."),
            ("Closure & Complications", "Watertight dural closure; bone replacement; callosotomy of >2.5 cm risks disconnection syndrome; bilateral forniceal retraction risks permanent amnesia; venous angle injury causes thalamic hemorrhage; post-operative sodium dysregulation from hypothalamic manipulation."),
        ],
        "img_path": "enhanced_figures/fig_170_2_fornix.png",
        "caption_title": "FORNIX & FORAMEN OF MONRO ANATOMY",
        "caption_body": "The columns of the fornix define the anterior boundary of the foramen of Monro; the thalamostriate vein and internal cerebral vein define the posterior boundary — critical landmarks for the transforaminal approach.",
    },

    # SLIDE 33 — Transcallosal-Transchoroidal (Wen) Approach
    {
        "type": "content",
        "badge": "SURGICAL APPROACHES • WEN TRANSCHOROIDAL",
        "title": "Transcallosal-Transchoroidal Approach (Wen Approach)",
        "subtitle": "Extension of the transcallosal approach through the choroidal fissure to access the third ventricle and posterior foramen of Monro without forniceal retraction.",
        "cards": [
            ("Indication & Advantages", "For tumors in the posterior third ventricle, massa intermedia, or extending posterior to the foramen of Monro; avoids direct forniceal retraction by entering the ventricular system through the choroidal fissure; provides wider posterior third-ventricle exposure than pure transforaminal."),
            ("Technical Steps — Choroidal Fissure Opening", "After standard transcallosal entry into lateral ventricle: identify the taenia fornicis (fornix side) and taenia thalami (thalamus side) of the choroidal fissure; open the fissure along the taenia thalami to avoid forniceal injury; internal cerebral veins visible deep."),
            ("Exposure of Third Ventricle", "Tela choroidea divided in the choroidal fissure; the roof of the third ventricle (tela) is opened between the two internal cerebral veins; the roof veins and ICVs must be identified and preserved; posterior third-ventricular tumors accessed from above."),
            ("Risks & Limitations", "ICV or vein of Galen injury causes catastrophic thalamic and deep white matter infarction; bilateral thalamic venous infarction is fatal; memory impairment from bilateral forniceal compression; limited access to very posterior third-ventricular lesions near the pineal recess."),
        ],
        "img_path": "enhanced_figures/fig_170_5_tela_choroidea.png",
        "caption_title": "TELA CHOROIDEA & INTERNAL CEREBRAL VEINS",
        "caption_body": "The tela choroidea forms the roof of the third ventricle between the two internal cerebral veins (ICVs); the Wen transchoroidal approach opens this space to access posterior third-ventricular pathology.",
    },

    # SLIDE 34 — Telovelar Approach (Fourth Ventricle)
    {
        "type": "content",
        "badge": "SURGICAL APPROACHES • TELOVELAR",
        "title": "Telovelar Approach to the Fourth Ventricle",
        "subtitle": "The telovelar approach opens the tela choroidea and inferior medullary velum to access the fourth ventricle without cerebellar vermis splitting.",
        "cards": [
            ("Patient Position & Craniotomy", "Prone or sitting position; midline suboccipital craniotomy from inion to C1 posterior arch (or C1 laminectomy); dura opened in Y-shaped fashion; PICA branches identified and protected in the cisterna magna; cerebellar tonsils retracted laterally."),
            ("Opening the Telovelar Membrane", "The inferior medullary velum (IMV) and tela choroidea are divided along their insertion into the inferior aspect of the cerebellar vermis; bilateral tonsillar retraction and IMV division exposes the entire fourth ventricular floor; foramen of Magendie is the starting point."),
            ("Fourth Ventricle Exposure", "Complete floor visualization including fastigium, facial colliculus, striae medullares, hypoglossal and vagal trigones, and obex; lateral recesses accessible by extending dissection toward foramina of Luschka; PICA choroidal branches supply floor tumors."),
            ("Safe Resection Strategy", "Piecemeal debulking from center outward; avoid direct manipulation of brainstem floor (facial colliculus, hypoglossal triangle); neurophysiology monitoring (BAEP, MEP, CN IX–XII EMG); floor invasion: leave thin residual on brainstem; dissection plane between tumor pseudocapsule and pia."),
        ],
        "img_path": "enhanced_figures/fig_170_8_fourth_ventricle_floor.png",
        "caption_title": "FOURTH VENTRICLE FLOOR (RHOMBOID FOSSA)",
        "caption_body": "The floor of the fourth ventricle (rhomboid fossa) containing the facial colliculus, hypoglossal trigone, vagal trigone, striae medullares, and obex; safe-entry zones are used for intra-axial lesions but avoided for extra-axial tumors.",
    },

    # SLIDE 35 — Endoscopic Third Ventriculostomy (ETV)
    {
        "type": "content",
        "badge": "SURGICAL APPROACHES • ETV",
        "title": "Endoscopic Third Ventriculostomy (ETV)",
        "subtitle": "ETV creates an internal CSF bypass through the floor of the third ventricle to the pre-pontine cistern, treating obstructive hydrocephalus without external shunting.",
        "cards": [
            ("Indications & Patient Selection", "Obstructive hydrocephalus from aqueductal stenosis, tectal glioma, pineal region tumors, posterior fossa masses; ETV Success Score (ETVSS) ≥80 predicts high success probability; age >6 months, no prior shunt, and visible floor improve outcomes; not ideal for communicating hydrocephalus."),
            ("Operative Technique", "Frontal burr hole 3 cm lateral, 1 cm anterior to coronal suture; rigid 0° endoscope via Dandy's point or Kocher's point; traverse foramen of Monro; identify the floor of the third ventricle (mammillary bodies posterior, infundibular recess anterior, basilar artery visible through thinned floor)."),
            ("Perforation & Stoma Creation", "Blunt perforation with a Fogarty balloon catheter or monopolar diathermy through the floor, anterior to the mammillary bodies and posterior to the infundibular recess; stoma expanded to 5–7 mm with balloon inflation; pulsatile CSF flow from stoma confirms patency."),
            ("Outcomes & Complications", "ETV success rate: ~70–80% overall (best in aqueductal stenosis); failure within first 6 months in ~20%; late ETV failure: 5–10% lifetime; complications: basilar artery or thalamoperforator injury (catastrophic), hypothalamic injury, meningitis, subdural hygroma; revision ETV or shunt for failures."),
        ],
        "img_path": "enhanced_figures/fig_170_18_etv_case.png",
        "caption_title": "ENDOSCOPIC THIRD VENTRICULOSTOMY",
        "caption_body": "Endoscopic view through the foramen of Monro showing the third ventricular floor with the mammillary bodies posteriorly and the infundibular recess anteriorly; the stoma is created between these landmarks.",
    },

    # SLIDE 36 — Occipital Transtentorial Approach (Pineal Region)
    {
        "type": "content",
        "badge": "SURGICAL APPROACHES • OCCIPITAL TRANSTENTORIAL",
        "title": "Occipital Transtentorial Approach (Pineal Region)",
        "subtitle": "The occipital transtentorial approach provides wide access to the pineal region, posterior third ventricle, and quadrigeminal cistern via the incisura.",
        "cards": [
            ("Patient Position & Craniotomy", "Three-quarter prone (concord) or prone position with the head slightly flexed; right occipital craniotomy with bone removal extending to the torcula; falx and tentorium define the medial and inferior boundaries respectively; sitting position alternative (air embolism risk)."),
            ("Interhemispheric Dissection", "Dissect along falx toward the straight sinus; occipital bridging veins sacrificed with care (right-sided to minimize risk); tentorium incised parallel and lateral to the straight sinus leaving a cuff for resuturing; exposes the quadrigeminal plate and pineal region."),
            ("Pineal Region Exposure & Resection", "Identify vein of Galen, internal cerebral veins, basal veins of Rosenthal, and great cerebral vein of Galen; tumor dissected from velum interpositum; biopsy versus radical resection based on histological type suspected; GTR for teratomas, biopsy for germinomas."),
            ("Advantages & Limitations", "Superior visualization of pineal region, posterior commissure, and vein of Galen complex; wide corridor without vermian splitting; limitations: occipital lobe retraction risks visual field deficits; contralateral side access limited; vein of Galen injury is catastrophic."),
        ],
        "img_path": "enhanced_figures/fig_170_12_third_ventricle_approaches.png",
        "caption_title": "THIRD VENTRICLE & PINEAL APPROACHES",
        "caption_body": "Comparative schematic of surgical approaches to the posterior third ventricle and pineal region: infratentorial supracerebellar (sitting), occipital transtentorial (concord), and combined supra-infratentorial approaches.",
    },

    # =========================================================
    # SLIDE 37 — PICA Anatomy & Telovelar Reference
    # =========================================================
    {
        "type": "content",
        "badge": "SURGICAL ANATOMY • PICA SEGMENTS",
        "title": "PICA Anatomy: Relevance to Fourth-Ventricular Surgery",
        "subtitle": "A thorough knowledge of PICA segmental anatomy is essential to safe telovelar approach surgery and avoidance of cerebellar and brainstem infarction.",
        "cards": [
            ("PICA Segmental Anatomy", "Five segments: anterior medullary (p1), lateral medullary (p2), tonsillomedullary (p3), telovelotonsillar (p4), cortical (p5); the tonsillomedullary (p3) and telovelotonsillar (p4) segments are directly encountered during the telovelar approach."),
            ("Choroidal PICA Branches", "Medial and lateral posterior choroidal branches supply the tela choroidea, inferior medullary velum, and choroid plexus of the fourth ventricle; these branches must be preserved or coagulated only at the tumor surface to avoid ischemia of the brainstem and cerebellar nuclei."),
            ("PICA Injury Consequences", "P1 (anterior medullary) occlusion: lateral medullary infarction (Wallenberg syndrome); p3/p4 occlusion: inferior cerebellar infarction, ataxia, dysequilibrium; bilateral PICA injury: catastrophic — cerebellar swelling, posterior fossa compartment syndrome."),
            ("Protective Maneuvers", "Preserve PICA branches throughout dissection; use temporary clip during tumor-feeding vessel sacrifice; Doppler ultrasound to confirm PICA patency after tonsillar retraction; ICG video-angiography to verify posterior choroidal flow preservation."),
        ],
        "img_path": "enhanced_figures/fig_170_9_pica_segments.png",
        "caption_title": "PICA SEGMENTAL ANATOMY",
        "caption_body": "The five segments of the PICA and their relationships to the medulla, cerebellar tonsils, and fourth ventricle; the caudal loop at the p3 segment is the critical landmark for telovelar approach entry.",
    },

    # =========================================================
    # SLIDE 38 — Cross-sectional anatomy
    # =========================================================
    {
        "type": "content",
        "badge": "SURGICAL ANATOMY • CROSS SECTIONS",
        "title": "Intraventricular Anatomy: Cross-Sectional Relationships",
        "subtitle": "Understanding the cross-sectional anatomy of each ventricular compartment is prerequisite to selecting and executing the optimal surgical approach.",
        "cards": [
            ("Lateral Ventricle Anatomy", "The body is bounded by the corpus callosum (roof), caudate nucleus (lateral floor), and thalamus (medial floor); the choroid plexus runs along the choroidal fissure; the thalamostriate and septal veins drain to the internal cerebral vein at the venous angle."),
            ("Foramen of Monro & Third Ventricle", "The foramen is bounded anteriorly by the fornix columns and posteriorly by the anterior thalamic nuclei and thalamostriate vein; the third ventricle floor is the hypothalamus; the roof is the tela choroidea between the internal cerebral veins."),
            ("Fourth Ventricle & Posterior Fossa", "Diamond-shaped cavity with the pons and medulla forming the floor; cerebellar vermis and hemispheres form the roof; lateral angles extend as foramina of Luschka; midline foramen of Magendie; tela choroidea separates the cavity from the cisterna magna."),
            ("Surgical Corridors Summary", "Each ventricular compartment requires a tailored corridor: lateral (transcortical/transcallosal), third ventricle (transforaminal/transchoroidal/transtuberculum), fourth ventricle (telovelar/transcerebellomedullary fissure), pineal (infratentorial/supracerebellar or occipital transtentorial)."),
        ],
        "img_path": "enhanced_figures/fig_170_6_cross_sections.png",
        "caption_title": "VENTRICULAR CROSS-SECTIONAL ANATOMY",
        "caption_body": "Axial and coronal cross-sections illustrating the relationships of the ventricular system to surrounding white matter, basal ganglia, thalami, and brainstem — the anatomical substrate for surgical planning.",
    },

    # =========================================================
    # SLIDE 39 — Hydrocephalus Management
    # =========================================================
    {
        "type": "content",
        "badge": "SURGICAL MANAGEMENT • HYDROCEPHALUS",
        "title": "Management of Hydrocephalus in Ventricular Tumors",
        "subtitle": "Hydrocephalus is the most common life-threatening complication of intraventricular tumors and must be addressed urgently before or concurrent with tumor treatment.",
        "cards": [
            ("Acute Hydrocephalus Management", "Emergency EVD placement via Kocher's point for acutely decompensating patients; ICP monitoring guides drainage; if tumor biopsy planned, simultaneous endoscopic ETV + biopsy is the ideal single-stage procedure for appropriate candidates."),
            ("Pre-operative VP Shunt", "Reservoir-controlled VP shunt inserted before definitive tumor surgery in patients with severe hydrocephalus unfit for immediate craniotomy; shunt-first strategy accepted for CPC in infants, pineal GCTs, and brainstem gliomas where RT/chemo is first-line."),
            ("Post-operative Hydrocephalus", "~20–40% of patients develop persistent hydrocephalus after posterior fossa tumor resection despite GTR (arachnoiditis, CSF protein elevation); VP shunt required in this group; endoscopic aqueductoplasty for isolated aqueductal stenosis post-resection."),
            ("ETV vs VP Shunt Comparison", "ETV: no implant, no infection/obstruction risk, natural CSF circulation; VP shunt: reliable, immediate, any age; ETV preferred for obstructive hydrocephalus with ETVSS ≥80; VP shunt preferred for communicating hydrocephalus, infants <6 months, and ETV failure."),
        ],
        "img_path": "assets_images/hydrocephalus.jpg",
        "caption_title": "HYDROCEPHALUS IN VENTRICULAR TUMORS",
        "caption_body": "Bilateral temporal horn dilation and periventricular lucency (transependymal edema) on axial MRI indicating acute-on-chronic obstructive hydrocephalus from a posterior third-ventricular tumor.",
    },

    # =========================================================
    # SLIDE 40 — Intraoperative Neuromonitoring
    # =========================================================
    {
        "type": "content",
        "badge": "INTRAOPERATIVE TOOLS • NEUROMONITORING",
        "title": "Intraoperative Neuromonitoring and Adjuncts",
        "subtitle": "Multimodal intraoperative monitoring and advanced imaging adjuncts maximize safe resection of intraventricular tumors adjacent to eloquent structures.",
        "cards": [
            ("Neurophysiological Monitoring", "Motor evoked potentials (MEPs) from transcranial electrical stimulation: continuous monitoring during tumor resection near corticospinal tract; brainstem auditory evoked potentials (BAEPs) for posterior fossa surgery; CN VII/IX/X/XII free-running and triggered EMG for floor dissection."),
            ("Intraoperative MRI (iMRI)", "High-field (1.5–3T) iMRI allows real-time assessment of residual tumor during surgery; shown to increase GTR rates by ~20% in intraventricular tumors; particularly valuable for SEGA, ependymoma, and CPC where GTR changes prognosis."),
            ("Fluorescence-Guided Surgery", "5-ALA (5-aminolevulinic acid) causes protoporphyrin IX accumulation in high-grade tumors (WHO III ependymoma, CPC); fluorescent residual tumor visible under violet light (Blue 400); FDA-approved for HGG; off-label use in anaplastic ependymoma and CPC."),
            ("Neuronavigation & Ultrasound", "Pre-operative DTI co-registration for optic radiation/corticospinal tract mapping; intraoperative ultrasound for real-time tumor boundary delineation compensating for brain shift; image-guided biopsy accuracy <2 mm from target."),
        ],
        "img_path": "assets_images/dti_tractography.jpg",
        "caption_title": "DTI TRACTOGRAPHY FOR SURGICAL PLANNING",
        "caption_body": "Pre-operative DTI fiber tractography superimposed on structural MRI demonstrating displacement of the corticospinal tract and optic radiations by an atrial meningioma — critical for selecting the safe cortical entry point.",
    },

    # =========================================================
    # SLIDE 41 — Historical Perspective
    # =========================================================
    {
        "type": "content",
        "badge": "HISTORICAL PERSPECTIVE • PIONEERING SURGEONS",
        "title": "Historical Milestones in Ventricular Neurosurgery",
        "subtitle": "The development of ventricular neurosurgery from crude cannulation to modern endoscopic and image-guided microsurgery spans more than a century of innovation.",
        "cards": [
            ("Walter Dandy (1886–1946)", "Father of ventricular surgery; introduced ventriculography (1918) and pneumoencephalography; first described ETV (1922) for hydrocephalus treatment; pioneered open approaches to the third and lateral ventricles; described the anatomy of the choroid plexus and foramen of Monro."),
            ("Da Vinci's Ventricular Observations", "Leonardo da Vinci produced wax casts of the ventricular system (circa 1504) — the first accurate three-dimensional representations of the ventricles; his cross-sectional anatomical drawings established the foundation for neuroanatomy education."),
            ("Modern Microsurgical Era", "Introduction of the operating microscope (1960s) by Kurze and Yasargil; Rhoton's microsurgical anatomy atlas (1970s–2000s) established definitive ventricular anatomical relationships; endoscopic era began with Guiot and Fukushima (1970s–1980s)."),
            ("Molecular Classification Revolution", "WHO 2016 integration of molecular markers into CNS tumor classification; WHO 2021 5th edition established methylation profiling and integrated diagnoses for ependymomas, GCTs, and CNS tumors — transforming treatment stratification and clinical trial design."),
        ],
        "img_path": "assets_images/walter_dandy.jpg",
        "caption_title": "WALTER DANDY — FATHER OF VENTRICULAR SURGERY",
        "caption_body": "Walter Dandy at Johns Hopkins developed ventriculography and was the first surgeon to perform endoscopic third ventriculostomy in 1922 — a procedure that remains a cornerstone of hydrocephalus management today.",
    },

    # =========================================================
    # SLIDE 42 — Davinci Anatomy Reference
    # =========================================================
    {
        "type": "content",
        "badge": "NEUROANATOMY • VENTRICULAR SYSTEM",
        "title": "Ventricular System: Anatomy and CSF Circulation",
        "subtitle": "A detailed understanding of the normal ventricular anatomy and CSF pathways is prerequisite for localizing and resecting ventricular tumors.",
        "cards": [
            ("Ventricular System Components", "Two lateral ventricles (frontal horn, body, atrium, temporal horn, occipital horn) → foramen of Monro → third ventricle → cerebral aqueduct (of Sylvius) → fourth ventricle → foramina of Luschka (lateral) and Magendie (medial) → subarachnoid space."),
            ("Choroid Plexus Distribution", "Choroid plexus in: temporal horn, body and atrium of lateral ventricles (supplied by anterior and posterior choroidal arteries); roof of third ventricle (medial posterior choroidal); roof of fourth ventricle (PICA branches); absent from frontal and occipital horns and cerebral aqueduct."),
            ("CSF Production & Absorption", "~500 mL/day produced mainly by choroid plexus (70%) and ependymal cells (30%); ~150 mL in circulation at any time; reabsorbed at arachnoid granulations (Pacchionian bodies) into venous sinuses; lymphatic drainage via cribriform plate also described."),
            ("Ependymal Lining", "Single layer of ciliated cuboidal ependymal cells lines the entire ventricular system; cilia create CSF flow currents; tanycytes in the third ventricle floor are specialized ependymal cells involved in neuroendocrine signaling; ependymal disruption impairs CSF flow regulation."),
        ],
        "img_path": "assets_images/davinci_ventricles.jpg",
        "caption_title": "DA VINCI'S VENTRICULAR SYSTEM (c.1504)",
        "caption_body": "Leonardo da Vinci's wax injection cast of the human ventricular system — the first accurate representation; demonstrates the lateral ventricles, third ventricle, cerebral aqueduct, and fourth ventricle in three dimensions.",
    },

    # =========================================================
    # SLIDE 43 — Corpus Callosum & Transcallosal Safety
    # =========================================================
    {
        "type": "content",
        "badge": "SURGICAL ANATOMY • CORPUS CALLOSUM",
        "title": "Corpus Callosum: Surgical Anatomy and Transcallosal Safety",
        "subtitle": "The corpus callosum is the principal white matter commissure; its surgical division must respect fiber tract topography to minimize disconnection syndrome.",
        "cards": [
            ("Callosal Topography", "The corpus callosum is divided into rostrum, genu, body, isthmus, and splenium; motor fibers cross in the anterior body (leg), posterior body (arm); language commissures in isthmus and splenium; visual commissures in splenium — injury risks disconnection syndromes."),
            ("Safe Callosotomy Length", "Transcallosal incision limited to ≤2 cm in the anterior body minimizes disconnection risk; bilateral motor or language deficits from extensive callosotomy; the genu and splenium must be preserved; callosotomy of >3 cm causes clinically evident disconnection syndrome."),
            ("Anatomical Landmarks", "Pericallosal arteries (ACA branches) run along the dorsal surface of the corpus callosum on each side — must be identified and retracted medially before callosotomy; the cingulate gyri are retracted laterally; the interhemispheric fissure provides the surgical corridor."),
            ("Post-operative Disconnection Syndrome", "Rare with limited anterior callosotomy; symptoms: left hand apraxia, intermanual conflict, left-sided agraphia, and tactile anomia; alien hand syndrome; spontaneous resolution over months in most cases; irreversible if splenium or posterior body divided."),
        ],
        "img_path": "assets_images/corpus_callosum.jpg",
        "caption_title": "CORPUS CALLOSUM ANATOMY",
        "caption_body": "Midsagittal MRI anatomy of the corpus callosum: rostrum, genu, body, isthmus, and splenium — the anterior body (2 cm) is the safe callosotomy zone for transcallosal ventricular surgery.",
    },

    # =========================================================
    # SLIDE 44 — Subependymoma Spotlight
    # =========================================================
    {
        "type": "content",
        "badge": "SUBEPENDYMOMA • MANAGEMENT",
        "title": "Subependymoma: A Benign Fourth-Ventricular Tumor",
        "subtitle": "Subependymoma (WHO grade I) is a slow-growing, benign intraventricular tumor that often warrants observation; surgery is reserved for symptomatic or growing lesions.",
        "cards": [
            ("Pathology & Epidemiology", "Clusters of small, uniform glial cells embedded in a fibrillary matrix; low cellularity, rare mitoses, no microvascular proliferation or necrosis; GFAP positive; peak incidence 4th–6th decade; 50–60% in fourth ventricle, 40% in lateral ventricle; male predominance."),
            ("Observation Strategy", "Most subependymomas are incidental; annual MRI surveillance; intervention indicated for: enlarging tumor (>0.5 cm/year), symptomatic hydrocephalus, neurological deficits, or uncertainty in diagnosis; natural history often indolent over many years."),
            ("Surgical Resection", "Telovelar approach for fourth-ventricular subependymomas; transcallosal or transcortical for lateral ventricular lesions; GTR is curative — recurrence essentially nil after complete resection; excellent tissue plane with surrounding tissue facilitates surgical dissection."),
            ("Prognosis", "5-year OS ~98–100% after surgical GTR; no adjuvant therapy required; quality of life excellent; fourth-ventricular location carries morbidity from posterior fossa approach; lateral ventricular lesions carry seizure risk from transcortical approach; overall excellent outcome."),
        ],
        "img_path": "assets_images/subependymoma.jpg",
        "caption_title": "SUBEPENDYMOMA — GROSS PATHOLOGY",
        "caption_body": "Gross specimen of a fourth-ventricular subependymoma: a lobulated, firm, grey-white mass with a well-defined border from the adjacent cerebellar tissue; calcification and microcysts are common findings.",
    },

    # =========================================================
    # SLIDE 45 — Epidermoid Cysts & Other Rare IV Tumors
    # =========================================================
    {
        "type": "content",
        "badge": "RARE VENTRICULAR TUMORS • OVERVIEW",
        "title": "Other Intraventricular Lesions: Epidermoids and Rare Tumors",
        "subtitle": "A spectrum of rare lesions including epidermoid cysts, cavernous malformations, metastases, and primary CNS lymphoma may present as intraventricular masses.",
        "cards": [
            ("Epidermoid Cysts", "Inclusion cysts lined by stratified squamous epithelium filled with keratin flakes; 'cauliflower' appearance on MRI; pathognomonic DWI restriction; CPA angle most common but can occur in ventricles; surgical resection via craniotomy; capsule left adherent to brainstem — recurrence if residual capsule."),
            ("Intraventricular Cavernous Malformations", "Rare but documented in lateral/third/fourth ventricles; symptomatic hemorrhage triggers intervention; resection via appropriate ventricular corridor; low recurrence if complete resection; MRI shows 'popcorn' T2* blooming lesion with hemosiderin rim."),
            ("Intraventricular Metastases", "Rare; lung, breast, and melanoma most common; leptomeningeal component frequent; urgent whole-brain RT ± SRS; VP shunt for hydrocephalus; prognosis determined by systemic disease burden; WBRT 30 Gy / 10# palliative standard."),
            ("Primary CNS Lymphoma (PCNSL)", "Can be periventricular or intraventricular in 20%; characteristically crosses corpus callosum; homogeneous enhancement in immunocompetent hosts; biopsy via stereotactic or endoscopic route; avoid steroids pre-biopsy; high-dose methotrexate-based chemotherapy is primary treatment — not surgery."),
        ],
        "img_path": "assets_images/epidermoid_cyst.jpg",
        "caption_title": "EPIDERMOID CYST — PEARL TUMOR",
        "caption_body": "Epidermoid cysts appear as pearlescent masses with a cauliflower surface on gross inspection; DWI restricted diffusion distinguishes them from arachnoid cysts and other CSF-intensity lesions on MRI.",
    },

    # =========================================================
    # SLIDE 46 — SUMMARY / MASTERY SLIDE
    # =========================================================
    {
        "type": "summary",
        "badge": "PART II • SUMMARY & MASTERY",
        "title": "Ventricular Tumors: Key Takeaways",
        "subtitle": "A synthesis of the essential principles in the diagnosis, classification, and surgical management of intraventricular tumors.",
        "cards": [
            ("WHO 2021 Classification Integration", "Molecular profiling is now integral to diagnosis: ZFTA-RELA and YAP1 fusions for ependymoma; BRAF V600E for papillary craniopharyngioma; TP53 for CPC; KIT/RAS for germinoma; H3 K27me3 loss for PF-EPN-A — histology alone is insufficient."),
            ("Extent of Resection as Prognosis Driver", "GTR is the single most powerful prognostic factor for ependymoma, choroid plexus tumors, and meningioma; STR + RT equals GTR for craniopharyngioma (hypothalamic-sparing philosophy); GTR not required for germinoma; mTOR inhibitors replace surgery for many SEGA patients."),
            ("Approach Selection Principles", "Foramen of Monro/third ventricle: transcallosal-transforaminal or Wen approach; large lateral ventricular: transcortical or transcallosal; fourth ventricle: telovelar; pineal: occipital transtentorial or infratentorial supracerebellar; hydrocephalus: ETV preferred over shunt when ETVSS ≥80."),
            ("Critical Anatomy to Protect", "Internal cerebral veins and vein of Galen (thalamic infarction risk); fornix columns (memory); facial colliculus/floor of fourth ventricle (CN VI/VII); PICA segments (cerebellar/brainstem infarction); optic radiations (visual field); hypothalamus (endocrine/behavioral)."),
        ],
        "img_path": "enhanced_figures/fig_170_10_surgical_approaches.png",
        "caption_title": "VENTRICULAR SURGICAL APPROACHES — SUMMARY",
        "caption_body": "Composite illustration of all major surgical corridors to the ventricular system: each approach optimized for tumor type, location, size, and relationship to eloquent neurovascular structures.",
    },

    # =========================================================
    # SLIDE 47 — THANK YOU SLIDE
    # =========================================================
    {
        "type": "thankyou",
        "badge": "PART II • END OF LECTURE",
        "title": "Thank You",
        "subtitle": "Tumors of the Brain Ventricles — Part II of the Neurosurgical Lecture Series. Questions and discussion welcome.",
        "cards": [
            ("References", "WHO Classification of Tumours of the CNS, 5th Edition (2021); Youmans & Winn Neurological Surgery, 8th Ed.; Rhoton AL Jr: Neurosurgery 2002 (anatomy supplements); COG/SIOPE ependymoma trial protocols."),
            ("Further Reading", "Louis DN et al. (2021) The 2021 WHO Classification of Tumors of the Central Nervous System. Neuro Oncol. 23(8):1231–1251; Ramaswamy V et al. Nat Genet 2016 (ependymoma subtypes); Müller HL et al. Lancet Oncol 2019 (craniopharyngioma)."),
            ("Acknowledgements", "Neurosurgery Department Faculty; Neuropathology and Neuro-Oncology Teams; Medical Illustration; Patients and Families who contribute to our understanding through participation in clinical research."),
            ("Disclaimer", "This lecture is for educational purposes only. Clinical decisions must be individualized based on institutional protocols, multidisciplinary tumor board recommendations, and current evidence-based guidelines."),
        ],
        "img_path": "assets_images/part2_thankyou.jpg",
        "caption_title": "END OF PART II",
        "caption_body": "Tumors of the Brain Ventricles — Part II complete. The next session will cover surgical nuances and case-based discussions of complex intraventricular tumor presentations.",
    },

]
