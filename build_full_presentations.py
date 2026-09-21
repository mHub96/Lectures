import os, sys, time
sys.stdout.reconfigure(encoding='utf-8')

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image
import win32com.client

C_NAVY = RGBColor(15, 30, 54)        # Deep neurosurgical navy
C_CYAN = RGBColor(2, 132, 199)       # Accent cyan / cerulean
C_BODY = RGBColor(51, 65, 85)        # Slate body text
C_MUTED = RGBColor(100, 116, 139)    # Subtitle muted slate
C_CARD_BG = RGBColor(248, 250, 252)  # Clean light panel background
C_BORDER = RGBColor(226, 232, 240)   # Crisp light border
C_WHITE = RGBColor(255, 255, 255)
C_EMERALD = RGBColor(16, 185, 129)   # Emerald for summary
C_PURPLE = RGBColor(124, 58, 237)    # Violet / celebratory for Thank You

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

def add_fitted_image(slide, img_path, left, top, max_w, max_h, name="Image_pic"):
    if not os.path.exists(img_path):
        print(f"Warning: Image path not found: {img_path}")
        return None
    try:
        with Image.open(img_path) as im:
            iw, ih = im.size
        aspect = iw / ih
        if (max_w / max_h) > aspect:
            h = max_h
            w = max_h * aspect
        else:
            w = max_w
            h = max_w / aspect
        img_left = left + (max_w - w) / 2
        img_top = top + (max_h - h) / 2
        pic = slide.shapes.add_picture(img_path, img_left, img_top, width=w, height=h)
        pic.name = name
        return pic
    except Exception as e:
        print(f"Error adding image {img_path}: {e}")
        return None

def build_content_slide(prs, badge, title, subtitle, cards, img_path, caption_title, caption_body, slide_num, total_slides):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # 1. Category Badge
    tb_b = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(11.7), Inches(0.28))
    tb_b.name = "Header_badge"
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p_b = tf_b.paragraphs[0]
    p_b.text = badge.upper()
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = C_CYAN

    # 2. Main Title
    tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.5))
    tb_t.name = "Header_title"
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY

    # 3. Subtitle
    tb_s = slide.shapes.add_textbox(Inches(0.8), Inches(1.18), Inches(11.7), Inches(0.38))
    tb_s.name = "Header_subtitle"
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = subtitle
    p_s.font.size = Pt(11.5)
    p_s.font.color.rgb = C_MUTED

    # 4. Content Cards (Left Column)
    n_cards = len(cards)
    card_start_y = Inches(1.68)
    if n_cards == 2:
        card_h = Inches(2.35)
        gap = Inches(0.25)
    elif n_cards == 3:
        card_h = Inches(1.52)
        gap = Inches(0.18)
    else: # 4 cards
        card_h = Inches(1.15)
        gap = Inches(0.12)
        if n_cards > 4:
            cards = cards[:4]

    for i, (c_head, c_body) in enumerate(cards):
        cy = card_start_y + i * (card_h + gap)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), cy, Inches(6.8), card_h)
        card.name = f"Card_{i}_bg"
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), cy, Inches(0.12), card_h)
        bar.name = f"Card_{i}_bar"
        bar.fill.solid()
        bar.fill.fore_color.rgb = C_CYAN
        bar.line.fill.background()

        tb_c = slide.shapes.add_textbox(Inches(1.05), cy + Inches(0.08), Inches(6.4), card_h - Inches(0.16))
        tb_c.name = f"Card_{i}_text"
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        
        p1 = tf_c.paragraphs[0]
        p1.text = c_head
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = C_NAVY

        p2 = tf_c.add_paragraph()
        p2.text = c_body
        p2.font.size = Pt(9.8) if n_cards >= 4 else Pt(10.5)
        p2.font.color.rgb = C_BODY

    # 5. Explanatory Image Panel (Right Column)
    panel_x = Inches(7.85)
    panel_y = Inches(1.68)
    panel_w = Inches(4.7)
    panel_h = Inches(5.1)

    frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_x, panel_y, panel_w, panel_h)
    frame.name = "Image_frame"
    frame.fill.solid()
    frame.fill.fore_color.rgb = C_WHITE
    frame.line.color.rgb = C_BORDER
    frame.line.width = Pt(1)

    img_max_w = Inches(4.4)
    img_max_h = Inches(3.6)
    img_x = panel_x + Inches(0.15)
    img_y = panel_y + Inches(0.15)
    add_fitted_image(slide, img_path, img_x, img_y, img_max_w, img_max_h, name="Image_pic")

    cap_y = panel_y + Inches(3.85)
    cap_h = Inches(1.1)
    cap_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_x + Inches(0.15), cap_y, Inches(4.4), cap_h)
    cap_box.name = "Image_cap_box"
    cap_box.fill.solid()
    cap_box.fill.fore_color.rgb = RGBColor(241, 245, 249)
    cap_box.line.color.rgb = C_BORDER
    cap_box.line.width = Pt(0.75)

    tb_cap = slide.shapes.add_textbox(panel_x + Inches(0.25), cap_y + Inches(0.06), Inches(4.2), cap_h - Inches(0.1))
    tb_cap.name = "Image_cap_text"
    tf_cap = tb_cap.text_frame
    tf_cap.word_wrap = True
    
    cp1 = tf_cap.paragraphs[0]
    cp1.text = caption_title.upper()
    cp1.font.size = Pt(9.5)
    cp1.font.bold = True
    cp1.font.color.rgb = C_CYAN

    cp2 = tf_cap.add_paragraph()
    cp2.text = caption_body
    cp2.font.size = Pt(8.8)
    cp2.font.color.rgb = C_BODY

    # Footer
    tb_foot = slide.shapes.add_textbox(Inches(0.8), Inches(6.98), Inches(11.75), Inches(0.25))
    tb_foot.name = "Footer"
    tf_foot = tb_foot.text_frame
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = f"Youmans and Winn Neurological Surgery • Chapter 170 | Slide {slide_num} of {total_slides}"
    p_foot.font.size = Pt(8.5)
    p_foot.font.color.rgb = C_MUTED

def build_title_slide(prs, badge, title, subtitle, img_path, credits):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    left_w = Inches(6.8)
    tb_b = slide.shapes.add_textbox(Inches(0.8), Inches(1.2), left_w, Inches(0.35))
    tb_b.name = "Header_badge"
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p_b = tf_b.paragraphs[0]
    p_b.text = badge.upper()
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = C_CYAN

    tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(1.6), left_w, Inches(1.8))
    tb_t.name = "Header_title"
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(28)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY

    tb_s = slide.shapes.add_textbox(Inches(0.8), Inches(3.6), left_w, Inches(1.2))
    tb_s.name = "Header_subtitle"
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = subtitle
    p_s.font.size = Pt(13.5)
    p_s.font.color.rgb = C_MUTED

    tb_c = slide.shapes.add_textbox(Inches(0.8), Inches(5.1), left_w, Inches(1.6))
    tb_c.name = "Card_0_text"
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True
    p_c1 = tf_c.paragraphs[0]
    p_c1.text = "REFERENCE TEXT & SOURCE CURRICULUM"
    p_c1.font.size = Pt(10)
    p_c1.font.bold = True
    p_c1.font.color.rgb = C_NAVY

    for cr in credits:
        p = tf_c.add_paragraph()
        p.text = "• " + cr
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_BODY

    panel_x = Inches(7.85)
    panel_y = Inches(1.2)
    panel_w = Inches(4.7)
    panel_h = Inches(5.4)

    frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_x, panel_y, panel_w, panel_h)
    frame.name = "Image_frame"
    frame.fill.solid()
    frame.fill.fore_color.rgb = C_WHITE
    frame.line.color.rgb = C_BORDER
    frame.line.width = Pt(1)

    add_fitted_image(slide, img_path, panel_x + Inches(0.2), panel_y + Inches(0.2), Inches(4.3), Inches(4.2), name="Image_pic")

    cap_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_x + Inches(0.2), panel_y + Inches(4.5), Inches(4.3), Inches(0.7))
    cap_box.name = "Image_cap_box"
    cap_box.fill.solid()
    cap_box.fill.fore_color.rgb = RGBColor(241, 245, 249)
    cap_box.line.color.rgb = C_BORDER

    tb_cap = slide.shapes.add_textbox(panel_x + Inches(0.3), panel_y + Inches(4.55), Inches(4.1), Inches(0.6))
    tb_cap.name = "Image_cap_text"
    tf_cap = tb_cap.text_frame
    tf_cap.word_wrap = True
    cp = tf_cap.paragraphs[0]
    cp.text = "HIGH-RESOLUTION CEREBRAL VENTRICULAR ANATOMY"
    cp.font.size = Pt(8.5)
    cp.font.bold = True
    cp.font.color.rgb = C_CYAN

def build_summary_slide(prs, badge, title, subtitle, takeaways, img_path, caption_title, caption_body, slide_num, total_slides):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    tb_b = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(11.7), Inches(0.28))
    tb_b.name = "Header_badge"
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p_b = tf_b.paragraphs[0]
    p_b.text = badge.upper()
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = C_EMERALD

    tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.5))
    tb_t.name = "Header_title"
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY

    tb_s = slide.shapes.add_textbox(Inches(0.8), Inches(1.18), Inches(11.7), Inches(0.38))
    tb_s.name = "Header_subtitle"
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = subtitle
    p_s.font.size = Pt(11.5)
    p_s.font.color.rgb = C_MUTED

    card_h = Inches(1.15)
    gap = Inches(0.12)
    card_start_y = Inches(1.68)

    for i, (t_title, t_desc) in enumerate(takeaways[:4]):
        cy = card_start_y + i * (card_h + gap)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), cy, Inches(6.8), card_h)
        card.name = f"Card_{i}_bg"
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), cy, Inches(0.12), card_h)
        bar.name = f"Card_{i}_bar"
        bar.fill.solid()
        bar.fill.fore_color.rgb = C_EMERALD
        bar.line.fill.background()

        tb_c = slide.shapes.add_textbox(Inches(1.05), cy + Inches(0.08), Inches(6.4), card_h - Inches(0.16))
        tb_c.name = f"Card_{i}_text"
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        
        p1 = tf_c.paragraphs[0]
        p1.text = t_title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = C_NAVY

        p2 = tf_c.add_paragraph()
        p2.text = t_desc
        p2.font.size = Pt(9.8)
        p2.font.color.rgb = C_BODY

    panel_x = Inches(7.85)
    panel_y = Inches(1.68)
    panel_w = Inches(4.7)
    panel_h = Inches(5.1)

    frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_x, panel_y, panel_w, panel_h)
    frame.name = "Image_frame"
    frame.fill.solid()
    frame.fill.fore_color.rgb = C_WHITE
    frame.line.color.rgb = C_BORDER
    frame.line.width = Pt(1)

    img_max_w = Inches(4.4)
    img_max_h = Inches(3.6)
    img_x = panel_x + Inches(0.15)
    img_y = panel_y + Inches(0.15)
    add_fitted_image(slide, img_path, img_x, img_y, img_max_w, img_max_h, name="Image_pic")

    cap_y = panel_y + Inches(3.85)
    cap_h = Inches(1.1)
    cap_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_x + Inches(0.15), cap_y, Inches(4.4), cap_h)
    cap_box.name = "Image_cap_box"
    cap_box.fill.solid()
    cap_box.fill.fore_color.rgb = RGBColor(241, 245, 249)
    cap_box.line.color.rgb = C_BORDER

    tb_cap = slide.shapes.add_textbox(panel_x + Inches(0.25), cap_y + Inches(0.06), Inches(4.2), cap_h - Inches(0.1))
    tb_cap.name = "Image_cap_text"
    tf_cap = tb_cap.text_frame
    tf_cap.word_wrap = True
    
    cp1 = tf_cap.paragraphs[0]
    cp1.text = caption_title.upper()
    cp1.font.size = Pt(9.5)
    cp1.font.bold = True
    cp1.font.color.rgb = C_EMERALD

    cp2 = tf_cap.add_paragraph()
    cp2.text = caption_body
    cp2.font.size = Pt(8.8)
    cp2.font.color.rgb = C_BODY

    tb_foot = slide.shapes.add_textbox(Inches(0.8), Inches(6.98), Inches(11.75), Inches(0.25))
    tb_foot.name = "Footer"
    tf_foot = tb_foot.text_frame
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = f"Youmans and Winn Neurological Surgery • Chapter 170 | Slide {slide_num} of {total_slides}"
    p_foot.font.size = Pt(8.5)
    p_foot.font.color.rgb = C_MUTED

def build_thankyou_slide(prs, badge, title, subtitle, cards, img_path, caption_title, caption_body, slide_num, total_slides):
    """Celebratory thank-you slide featuring custom Pixar-style artwork."""
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    tb_b = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(11.7), Inches(0.28))
    tb_b.name = "Header_badge"
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True
    p_b = tf_b.paragraphs[0]
    p_b.text = badge.upper()
    p_b.font.size = Pt(10)
    p_b.font.bold = True
    p_b.font.color.rgb = C_PURPLE

    tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.5))
    tb_t.name = "Header_title"
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY

    tb_s = slide.shapes.add_textbox(Inches(0.8), Inches(1.18), Inches(11.7), Inches(0.38))
    tb_s.name = "Header_subtitle"
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = subtitle
    p_s.font.size = Pt(11.5)
    p_s.font.color.rgb = C_MUTED

    card_h = Inches(1.15)
    gap = Inches(0.12)
    card_start_y = Inches(1.68)

    for i, (t_title, t_desc) in enumerate(cards[:4]):
        cy = card_start_y + i * (card_h + gap)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), cy, Inches(6.8), card_h)
        card.name = f"Card_{i}_bg"
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_BORDER
        card.line.width = Pt(1)

        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), cy, Inches(0.12), card_h)
        bar.name = f"Card_{i}_bar"
        bar.fill.solid()
        bar.fill.fore_color.rgb = C_PURPLE
        bar.line.fill.background()

        tb_c = slide.shapes.add_textbox(Inches(1.05), cy + Inches(0.08), Inches(6.4), card_h - Inches(0.16))
        tb_c.name = f"Card_{i}_text"
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        
        p1 = tf_c.paragraphs[0]
        p1.text = t_title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = C_NAVY

        p2 = tf_c.add_paragraph()
        p2.text = t_desc
        p2.font.size = Pt(9.8)
        p2.font.color.rgb = C_BODY

    panel_x = Inches(7.85)
    panel_y = Inches(1.68)
    panel_w = Inches(4.7)
    panel_h = Inches(5.1)

    frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_x, panel_y, panel_w, panel_h)
    frame.name = "Image_frame"
    frame.fill.solid()
    frame.fill.fore_color.rgb = C_WHITE
    frame.line.color.rgb = C_BORDER
    frame.line.width = Pt(1)

    img_max_w = Inches(4.4)
    img_max_h = Inches(3.6)
    img_x = panel_x + Inches(0.15)
    img_y = panel_y + Inches(0.15)
    add_fitted_image(slide, img_path, img_x, img_y, img_max_w, img_max_h, name="Image_pic")

    cap_y = panel_y + Inches(3.85)
    cap_h = Inches(1.1)
    cap_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_x + Inches(0.15), cap_y, Inches(4.4), cap_h)
    cap_box.name = "Image_cap_box"
    cap_box.fill.solid()
    cap_box.fill.fore_color.rgb = RGBColor(241, 245, 249)
    cap_box.line.color.rgb = C_BORDER

    tb_cap = slide.shapes.add_textbox(panel_x + Inches(0.25), cap_y + Inches(0.06), Inches(4.2), cap_h - Inches(0.1))
    tb_cap.name = "Image_cap_text"
    tf_cap = tb_cap.text_frame
    tf_cap.word_wrap = True
    
    cp1 = tf_cap.paragraphs[0]
    cp1.text = caption_title.upper()
    cp1.font.size = Pt(9.5)
    cp1.font.bold = True
    cp1.font.color.rgb = C_PURPLE

    cp2 = tf_cap.add_paragraph()
    cp2.text = caption_body
    cp2.font.size = Pt(8.8)
    cp2.font.color.rgb = C_BODY

    tb_foot = slide.shapes.add_textbox(Inches(0.8), Inches(6.98), Inches(11.75), Inches(0.25))
    tb_foot.name = "Footer"
    tf_foot = tb_foot.text_frame
    p_foot = tf_foot.paragraphs[0]
    p_foot.text = f"Youmans and Winn Neurological Surgery • Chapter 170 | Slide {slide_num} of {total_slides}"
    p_foot.font.size = Pt(8.5)
    p_foot.font.color.rgb = C_MUTED

def apply_powerpoint_transitions_and_animations(pptx_abs_path):
    """Uses PowerPoint COM to apply slide transitions and manual on-click entrance build animations."""
    print(f"Applying click-triggered transitions and animations to {pptx_abs_path}...")
    ppt_app = win32com.client.Dispatch("PowerPoint.Application")
    pres = ppt_app.Presentations.Open(pptx_abs_path, WithWindow=False)
    
    slide_count = pres.Slides.Count
    for s_num in range(1, slide_count + 1):
        slide = pres.Slides(s_num)
        
        # 1. Slide Transition Effect
        # 1281 = ppEffectFade
        slide.SlideShowTransition.EntryEffect = 1281
        slide.SlideShowTransition.Duration = 0.6
        slide.SlideShowTransition.AdvanceOnClick = True
        
        # 2. Build map of shapes by name
        shape_dict = {}
        for idx in range(1, slide.Shapes.Count + 1):
            sh = slide.Shapes(idx)
            shape_dict[sh.Name] = sh

        # Animate Content / Summary / ThankYou slides by card groups on click
        # Clear any existing timeline effects
        while slide.TimeLine.MainSequence.Count > 0:
            slide.TimeLine.MainSequence(1).Delete()

        # Step-by-step click reveal for cards
        # Find all cards present (Card_0, Card_1, Card_2, Card_3)
        for c_idx in range(6):
            bg_name = f"Card_{c_idx}_bg"
            bar_name = f"Card_{c_idx}_bar"
            text_name = f"Card_{c_idx}_text"
            
            first_shape = None
            if bg_name in shape_dict:
                first_shape = shape_dict[bg_name]
            elif text_name in shape_dict:
                first_shape = shape_dict[text_name]
                
            if first_shape:
                # Trigger on page click (1)
                eff = slide.TimeLine.MainSequence.AddEffect(first_shape, 10, 0, 1) # msoAnimTriggerOnPageClick
                eff.Timing.Duration = 0.35
                
                # Accompanying shapes appear with previous (2)
                if bar_name in shape_dict:
                    eff_b = slide.TimeLine.MainSequence.AddEffect(shape_dict[bar_name], 10, 0, 2)
                    eff_b.Timing.Duration = 0.35
                if text_name in shape_dict and first_shape != shape_dict[text_name]:
                    eff_t = slide.TimeLine.MainSequence.AddEffect(shape_dict[text_name], 10, 0, 2)
                    eff_t.Timing.Duration = 0.35

        # Reveal Image Panel on its own click
        if "Image_frame" in shape_dict:
            eff_frame = slide.TimeLine.MainSequence.AddEffect(shape_dict["Image_frame"], 10, 0, 1) # On Click
            eff_frame.Timing.Duration = 0.35
            
            if "Image_pic" in shape_dict:
                eff_p = slide.TimeLine.MainSequence.AddEffect(shape_dict["Image_pic"], 10, 0, 2) # With Previous
                eff_p.Timing.Duration = 0.35
            if "Image_cap_box" in shape_dict:
                eff_cb = slide.TimeLine.MainSequence.AddEffect(shape_dict["Image_cap_box"], 10, 0, 2)
                eff_cb.Timing.Duration = 0.35
            if "Image_cap_text" in shape_dict:
                eff_ct = slide.TimeLine.MainSequence.AddEffect(shape_dict["Image_cap_text"], 10, 0, 2)
                eff_ct.Timing.Duration = 0.35
        elif "Image_pic" in shape_dict:
            eff_p = slide.TimeLine.MainSequence.AddEffect(shape_dict["Image_pic"], 10, 0, 1)
            eff_p.Timing.Duration = 0.35

    pres.Save()
    pres.Close()
    ppt_app.Quit()
    print(f"Completed manual click transitions & animations for {pptx_abs_path}")

print("Master PowerPoint generator and click-trigger animation engine ready.")
