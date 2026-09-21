import os, sys, time, requests
sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets_images', exist_ok=True)
headers = {'User-Agent': 'NeurosurgeryEducationalLecture/1.0 (mailto:neurosurg-lecture@deepmind.com)'}

topics = [
    ('Hydrocephalus', 'hydrocephalus.jpg'),
    ('Parinaud%27s_syndrome', 'parinaud_syndrome.jpg'),
    ('Germinoma', 'germinoma.jpg'),
    ('Central_neurocytoma', 'central_neurocytoma.jpg'),
    ('Pilocytic_astrocytoma', 'pilocytic_astrocytoma.jpg'),
    ('Choroid_plexus_papilloma', 'choroid_papilloma.jpg'),
    ('Meningioma', 'meningioma.jpg'),
    ('Epidermoid_cyst', 'epidermoid_cyst.jpg'),
    ('Subependymoma', 'subependymoma.jpg'),
    ('Ependymoma', 'ependymoma.jpg'),
    ('Lateral_ventricles', 'lateral_ventricles.jpg'),
    ('Third_ventricle', 'third_ventricle.jpg'),
    ('Fourth_ventricle', 'fourth_ventricle.jpg'),
    ('Choroid_plexus', 'choroid_plexus.jpg'),
    ('Corpus_callosum', 'corpus_callosum_wiki.jpg'),
    ('Fornix_(brain)', 'fornix_wiki.jpg'),
    ('Internal_capsule', 'internal_capsule_wiki.jpg'),
    ('Posterior_inferior_cerebellar_artery', 'pica_wiki.jpg'),
    ('Vein_of_Galen', 'vein_of_galen_wiki.jpg'),
    ('Pineal_gland', 'pineal_gland_wiki.jpg'),
    ('Endoscopic_third_ventriculostomy', 'etv_wiki.jpg'),
    ('Diffusion_MRI', 'dti_wiki.jpg'),
    ('Craniotomy', 'craniotomy_wiki.jpg')
]

for title, fname in topics:
    out_path = os.path.join('assets_images', fname)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 3000:
        print(f"Already exists: {fname}")
        continue
    try:
        url = f'https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=1000'
        r = requests.get(url, headers=headers, timeout=15).json()
        pages = r.get('query', {}).get('pages', {})
        for pid, pdata in pages.items():
            thumb = pdata.get('thumbnail', {}).get('source')
            if thumb:
                img_data = requests.get(thumb, headers=headers, timeout=15).content
                if len(img_data) > 1000:
                    with open(out_path, 'wb') as f:
                        f.write(img_data)
                    print(f"Saved: {fname} ({len(img_data)//1024} KB)")
                else:
                    print(f"Too small for {title}")
            else:
                print(f"No thumbnail for {title}")
    except Exception as e:
        print(f"Error for {title}: {e}")
    time.sleep(1.2)

print("Finished downloading Wikipedia medical assets.")

