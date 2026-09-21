import os, sys, time, requests
sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'NeurosurgeryLectureBot/1.0 (mailto:neurosurg-lecture@deepmind.com)'}

approach_targets = [
    ('Transcallosal_approach', 'approach_transcallosal_wiki.jpg'),
    ('Parietal_lobe', 'approach_parietal_wiki.jpg'),
    ('Subtemporal_approach', 'approach_subtemporal_wiki.jpg'),
    ('Infratentorial_supracerebellar_approach', 'approach_supracerebellar_wiki.jpg'),
    ('Pineal_region_tumor', 'pineal_tumor_wiki.jpg'),
    ('Craniopharyngioma', 'craniopharyngioma_wiki.jpg'),
    ('Stereotactic_neurosurgery', 'neuronavigation_setup.jpg'),
    ('Intraoperative_neurophysiological_monitoring', 'ionm_setup.jpg')
]

for title, fname in approach_targets:
    out_path = os.path.join('assets_images', fname)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 3000:
        continue
    try:
        url = f'https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=1200'
        r = requests.get(url, headers=headers, timeout=15).json()
        pages = r.get('query', {}).get('pages', {})
        for pid, pdata in pages.items():
            thumb = pdata.get('thumbnail', {}).get('source')
            if thumb:
                img_data = requests.get(thumb, headers=headers, timeout=15).content
                if len(img_data) > 2000:
                    with open(out_path, 'wb') as f:
                        f.write(img_data)
                    print(f"✓ Saved {fname} ({len(img_data)//1024} KB)")
    except Exception as e:
        print(f"Error {title}: {e}")
    time.sleep(1.2)

print("Approach images fetch completed.")

