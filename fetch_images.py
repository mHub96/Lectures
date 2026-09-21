import os, sys, requests
sys.stdout.reconfigure(encoding='utf-8')


os.makedirs('assets_images', exist_ok=True)
headers = {'User-Agent': 'NeurosurgeryEducationalLecture/1.0 (academic lecture presentation)'}

def download_file(url, out_path):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 5000:
        return True
    try:
        r = requests.get(url, headers=headers, timeout=20)
        if r.status_code == 200 and len(r.content) > 1000:
            with open(out_path, 'wb') as f:
                f.write(r.content)
            print(f"Downloaded: {out_path} ({len(r.content)//1024} KB)")
            return True
        else:
            print(f"Failed {url}: status {r.status_code}")
            return False
    except Exception as e:
        print(f"Error {url}: {e}")
        return False

def search_and_download(query, out_filename, fallback_queries=[]):
    out_path = os.path.join('assets_images', out_filename)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 5000:
        return out_path
    
    queries = [query] + fallback_queries
    for q in queries:
        api_url = 'https://commons.wikimedia.org/w/api.php'
        params = {
            'action': 'query',
            'generator': 'search',
            'gsrsearch': f'{q} filetype:bitmap',
            'gsrnamespace': 6,
            'gsrlimit': 5,
            'prop': 'imageinfo',
            'iiprop': 'url|size|mime',
            'format': 'json'
        }
        try:
            r = requests.get(api_url, params=params, headers=headers, timeout=15).json()
            pages = r.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                title = pdata.get('title', '')
                ii = pdata.get('imageinfo', [{}])[0]
                url = ii.get('url')
                mime = ii.get('mime', '')
                w = ii.get('width', 0)
                h = ii.get('height', 0)
                if url and ('image/jpeg' in mime or 'image/png' in mime) and w >= 400 and h >= 300:
                    # Avoid svg-generated tiny thumbnails or unrelated banners
                    if download_file(url, out_path):
                        return out_path
        except Exception as e:
            print(f"Search error for '{q}': {e}")
            continue
    return None

targets = [
    # Historical
    ("Walter Dandy", "walter_dandy.jpg", ["Walter E. Dandy neurosurgeon"]),
    ("Leonardo da Vinci ventricles wax", "davinci_ventricles.jpg", ["Leonardo da Vinci brain ventricles", "Leonardo da Vinci anatomy skull"]),
    
    # Ventricular anatomy & hydrocephalus
    ("Human ventricular system 3D", "ventricular_system_3d.png", ["ventricular system brain", "ventricles brain lateral third fourth"]),
    ("Hydrocephalus MRI", "hydrocephalus_mri.jpg", ["obstructive hydrocephalus MRI brain", "triventricular hydrocephalus"]),
    ("Parinaud syndrome tectum", "parinaud_tectum.jpg", ["midbrain tectum pineal anatomy", "dorsal midbrain syndrome"]),
    ("Endoscopic third ventriculostomy", "etv_anatomy.jpg", ["third ventriculostomy endoscopy", "tuber cinereum basilar artery"]),
    ("Germinoma brain MRI", "pineal_germinoma_mri.jpg", ["pineal tumor MRI", "intracranial germinoma"]),
    
    # Neuroimaging
    ("CISS MRI brain", "ciss_fiesta_mri.jpg", ["FIESTA MRI cerebellopontine", "constructive interference steady state MRI"]),
    ("DTI tractography corticospinal optic", "dti_tractography.jpg", ["diffusion tensor imaging brain tractography", "Meyer loop optic radiation"]),
    ("Superior sagittal sinus bridging veins", "bridging_veins.jpg", ["dural venous sinuses brain", "superior sagittal sinus anatomy"]),
    
    # Anatomical corridors & regions
    ("Corpus callosum anatomy sagittal", "corpus_callosum.jpg", ["corpus callosum sagittal MRI", "corpus callosum parts"]),
    ("Internal capsule brain anatomy", "internal_capsule.jpg", ["internal capsule basal ganglia horizontal", "internal capsule horizontal cut"]),
    ("Velum interpositum internal cerebral veins", "velum_interpositum.jpg", ["internal cerebral veins vein of Galen", "vein of galen malformation or anatomy"]),
    ("Intraoperative neuromonitoring MEP SSEP", "neuromonitoring.jpg", ["intraoperative neurophysiological monitoring", "brain mapping craniotomy"]),
    ("Brain tubular retractor", "tubular_retractor.jpg", ["tubular brain retractor neurosurgery", "transsulcal brain port"]),
    ("Transcallosal approach brain", "transcallosal_approach.jpg", ["interhemispheric transcallosal approach", "interhemispheric corridor"]),
    ("Transcortical transventricular approach", "transcortical_approach.jpg", ["middle frontal gyrus corticotomy", "transfrontal approach lateral ventricle"]),
    ("Supracerebellar infratentorial approach", "supracerebellar_approach.jpg", ["supracerebellar infratentorial corridor", "pineal region surgical approach"]),
    ("Occipital transtentorial approach", "occipital_transtentorial.jpg", ["Poppen approach pineal", "occipital transtentorial corridor"]),
    ("Telovelar approach Matsushima", "telovelar_approach.jpg", ["telovelar approach fourth ventricle", "uvulotonsillar space fourth ventricle"]),
    
    # Tumors & Histology
    ("Ependymoma micro", "ependymoma_histology.jpg", ["ependymoma perivascular pseudorosettes", "ependymoma H&E"]),
    ("Central neurocytoma intermed mag", "central_neurocytoma_histology.jpg", ["central neurocytoma histology", "central neurocytoma fried egg"]),
    ("Pilocytic astrocytoma Rosenthal fibers", "pilocytic_astrocytoma_histology.jpg", ["pilocytic astrocytoma histology", "Rosenthal fibers astrocytoma"]),
    ("Choroid plexus papilloma histology", "choroid_papilloma_histology.jpg", ["choroid plexus papilloma micro", "choroid plexus papilloma"]),
    ("Meningioma psammoma bodies micro", "meningioma_histology.jpg", ["meningioma psammoma bodies", "meningioma whorls histology"]),
    ("Epidermoid cyst brain MRI", "epidermoid_cyst_mri.jpg", ["epidermoid cyst MRI DWI", "epidermoid brain tumor"]),
    ("Dermoid cyst brain MRI", "dermoid_cyst_mri.jpg", ["dermoid cyst brain CT", "dermoid rupture lipid droplets"]),
    ("Subependymoma histology", "subependymoma_histology.jpg", ["subependymoma micro", "subependymoma H&E"])
]

print(f"Searching and downloading {len(targets)} targets...")
for query, out_name, fallbacks in targets:
    res = search_and_download(query, out_name, fallbacks)
    if res:
        print(f"✓ {out_name}")
    else:
        print(f"✗ Failed: {out_name}")
