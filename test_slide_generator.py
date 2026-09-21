import os, sys
sys.stdout.reconfigure(encoding='utf-8')
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

blank_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_layout)

C_NAVY = RGBColor(15, 30, 54)
C_CYAN = RGBColor(2, 132, 199)
C_BODY = RGBColor(51, 65, 85)
C_MUTED = RGBColor(100, 116, 139)
C_CARD_BG = RGBColor(248, 250, 252)
C_BORDER = RGBColor(226, 232, 240)

# Header Category Tracker
tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(11.7), Inches(0.28))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "HISTORICAL PERSPECTIVES • FOUNDATIONS OF NEUROSURGERY"
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = C_CYAN

# Main Title
tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.5))
tf_title = tb_title.text_frame
p_title = tf_title.paragraphs[0]
p_title.text = "Pioneering Milestones in Ventricular Surgery"
p_title.font.size = Pt(22)
p_title.font.bold = True
p_title.font.color.rgb = C_NAVY

# Subtitle
tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.18), Inches(11.7), Inches(0.4))
tf_sub = tb_sub.text_frame
p_sub = tf_sub.paragraphs[0]
p_sub.text = "From ancient ventricular localization to Walter Dandy's revolutionary first lateral ventricular tumor resection."
p_sub.font.size = Pt(11.5)
p_sub.font.color.rgb = C_MUTED

# Left Column - Cards
card_data = [
    ("3rd Century BC — Herophilos", "Described the four cerebral ventricles ('four small stomachs') and their communications, establishing the earliest anatomical record."),
    ("1504 — Leonardo da Vinci", "Performed the first cerebral wax cast ventriculography via bovine brain, accurately mapping ventricular geometry for the first time."),
    ("1764 — Cotugno & Magendie", "Defined cerebrospinal fluid (CSF) physiology, proving ventricles are filled with fluid rather than animal spirits ('vital pneuma')."),
    ("1918–1933 — Walter Dandy", "Pioneered air ventriculography, endoscopic choroid plexectomy, and performed the first direct surgical resection of a lateral ventricle ependymoma.")
]

card_top = Inches(1.72)
card_h = Inches(1.15)
gap = Inches(0.14)

for i, (head, body) in enumerate(card_data):
    top_pos = card_top + i * (card_h + gap)
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_pos, Inches(6.8), card_h)
    card.fill.solid()
    card.fill.fore_color.rgb = C_CARD_BG
    card.line.color.rgb = C_BORDER
    card.line.width = Pt(1)
    
    # Accent bar
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), top_pos, Inches(0.12), card_h)
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_CYAN
    bar.line.fill.background()
    
    tb = slide.shapes.add_textbox(Inches(1.05), top_pos + Inches(0.08), Inches(6.4), card_h - Inches(0.16))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = head
    p1.font.size = Pt(12)
    p1.font.bold = True
    p1.font.color.rgb = C_NAVY
    
    p2 = tf.add_paragraph()
    p2.text = body
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = C_BODY

# Right Column - Explanatory Image Panel
panel_left = Inches(7.9)
panel_top = Inches(1.72)
panel_w = Inches(4.65)
panel_h = Inches(5.02)

img_panel = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_left, panel_top, panel_w, panel_h)
img_panel.fill.solid()
img_panel.fill.fore_color.rgb = RGBColor(255, 255, 255)
img_panel.line.color.rgb = C_BORDER
img_panel.line.width = Pt(1)

# Add fitted image
img_path = 'assets_images/walter_dandy.jpg'
if os.path.exists(img_path):
    with Image.open(img_path) as im:
        iw, ih = im.size
    aspect = iw / ih
    max_w = Inches(4.35)
    max_h = Inches(3.45)
    if max_w / max_h > aspect:
        h = max_h
        w = max_h * aspect
    else:
        w = max_w
        h = max_w / aspect
    img_left = panel_left + Inches(0.15) + (max_w - w) / 2
    img_top = panel_top + Inches(0.15) + (max_h - h) / 2
    slide.shapes.add_picture(img_path, img_left, img_top, width=w, height=h)

# Caption Box
caption_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, panel_left + Inches(0.15), panel_top + Inches(3.72), Inches(4.35), Inches(1.15))
caption_box.fill.solid()
caption_box.fill.fore_color.rgb = RGBColor(241, 245, 249)
caption_box.line.color.rgb = C_BORDER
caption_box.line.width = Pt(0.75)

c_tb = slide.shapes.add_textbox(panel_left + Inches(0.25), panel_top + Inches(3.77), Inches(4.15), Inches(1.05))
c_tf = c_tb.text_frame
c_tf.word_wrap = True
cp1 = c_tf.paragraphs[0]
cp1.text = "HISTORICAL FIGURE: WALTER E. DANDY (1886–1946)"
cp1.font.size = Pt(9.5)
cp1.font.bold = True
cp1.font.color.rgb = C_CYAN

cp2 = c_tf.add_paragraph()
cp2.text = "Father of modern ventricular surgery, inventor of ventriculography, and pioneer of the transcallosal approach for direct intraventricular tumor resection."
cp2.font.size = Pt(9)
cp2.font.color.rgb = C_BODY

prs.save('prototype_slide.pptx')

