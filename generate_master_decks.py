import os, sys, time
sys.stdout.reconfigure(encoding='utf-8')

from pptx import Presentation
from pptx.util import Inches, Pt
import win32com.client

from build_full_presentations import (
    build_content_slide,
    build_title_slide,
    build_summary_slide,
    build_thankyou_slide,
    apply_powerpoint_transitions_and_animations,
    SLIDE_W, SLIDE_H
)
from deck1_data import DECK1_SLIDES
from deck2_data import DECK2_SLIDES

def generate_deck(slides_data, output_path):
    print(f"\n--- Generating {output_path} ({len(slides_data)} slides) ---")
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    total = len(slides_data)
    for idx, s in enumerate(slides_data):
        stype = s.get("type", "content")
        slide_num = idx + 1
        
        if stype == "title":
            build_title_slide(
                prs=prs,
                badge=s["badge"],
                title=s["title"],
                subtitle=s["subtitle"],
                img_path=s["img_path"],
                credits=s["credits"]
            )
        elif stype == "summary":
            build_summary_slide(
                prs=prs,
                badge=s["badge"],
                title=s["title"],
                subtitle=s["subtitle"],
                takeaways=s["cards"],
                img_path=s["img_path"],
                caption_title=s["caption_title"],
                caption_body=s["caption_body"],
                slide_num=slide_num,
                total_slides=total
            )
        elif stype == "thankyou":
            build_thankyou_slide(
                prs=prs,
                badge=s["badge"],
                title=s["title"],
                subtitle=s["subtitle"],
                cards=s["cards"],
                img_path=s["img_path"],
                caption_title=s["caption_title"],
                caption_body=s["caption_body"],
                slide_num=slide_num,
                total_slides=total
            )
        else:
            build_content_slide(
                prs=prs,
                badge=s["badge"],
                title=s["title"],
                subtitle=s["subtitle"],
                cards=s["cards"],
                img_path=s["img_path"],
                caption_title=s["caption_title"],
                caption_body=s["caption_body"],
                slide_num=slide_num,
                total_slides=total
            )

    prs.save(output_path)
    print(f"Saved base presentation: {output_path}")

    # Apply transitions and build animations via COM
    abs_path = os.path.abspath(output_path)
    apply_powerpoint_transitions_and_animations(abs_path)
    print(f"Successfully generated and animated {output_path}!")

if __name__ == "__main__":
    file1 = "Ventricular Tumors_(Part 1).pptx"
    file2 = "Ventricular Tumors_(Part 2).pptx"

    generate_deck(DECK1_SLIDES, file1)
    generate_deck(DECK2_SLIDES, file2)

    print("\nBoth masterclass presentations have been generated and animated successfully!")
