import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
import win32com.client

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

slide = prs.slides.add_slide(prs.slide_layouts[6])

# Header
tb = slide.shapes.add_textbox(Inches(1), Inches(0.5), Inches(10), Inches(1))
tb.name = "Header_title"
tb.text_frame.text = "Test Manual Click Reveal"

# Card 0
c0_bg = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(2), Inches(5), Inches(1))
c0_bg.name = "Card_0_bg"
c0_text = slide.shapes.add_textbox(Inches(1.2), Inches(2.1), Inches(4.5), Inches(0.8))
c0_text.name = "Card_0_text"
c0_text.text_frame.text = "Card 1 content appears on click 1"

# Card 1
c1_bg = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(3.5), Inches(5), Inches(1))
c1_bg.name = "Card_1_bg"
c1_text = slide.shapes.add_textbox(Inches(1.2), Inches(3.6), Inches(4.5), Inches(0.8))
c1_text.name = "Card_1_text"
c1_text.text_frame.text = "Card 2 content appears on click 2"

# Image box
img_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7), Inches(2), Inches(5), Inches(4))
img_box.name = "Image_frame"

prs.save("test_anim_named.pptx")

# Apply COM animations
ppt_app = win32com.client.Dispatch("PowerPoint.Application")
pres = ppt_app.Presentations.Open(os.path.abspath("test_anim_named.pptx"), WithWindow=False)

s = pres.Slides(1)
s.SlideShowTransition.EntryEffect = 1281 # Fade
s.SlideShowTransition.Duration = 0.5
s.SlideShowTransition.AdvanceOnClick = True

# Animate in exact order
shape_dict = {s.Shapes(i).Name: s.Shapes(i) for i in range(1, s.Shapes.Count + 1)}

# Click 1: Card 0
if "Card_0_bg" in shape_dict:
    eff1 = s.TimeLine.MainSequence.AddEffect(shape_dict["Card_0_bg"], 10, 0, 1) # OnPageClick
    eff1.Timing.Duration = 0.3
if "Card_0_text" in shape_dict:
    eff2 = s.TimeLine.MainSequence.AddEffect(shape_dict["Card_0_text"], 10, 0, 2) # WithPrevious
    eff2.Timing.Duration = 0.3

# Click 2: Card 1
if "Card_1_bg" in shape_dict:
    eff3 = s.TimeLine.MainSequence.AddEffect(shape_dict["Card_1_bg"], 10, 0, 1) # OnPageClick
    eff3.Timing.Duration = 0.3
if "Card_1_text" in shape_dict:
    eff4 = s.TimeLine.MainSequence.AddEffect(shape_dict["Card_1_text"], 10, 0, 2) # WithPrevious
    eff4.Timing.Duration = 0.3

# Click 3: Image
if "Image_frame" in shape_dict:
    eff5 = s.TimeLine.MainSequence.AddEffect(shape_dict["Image_frame"], 10, 0, 1) # OnPageClick
    eff5.Timing.Duration = 0.3

print(f"MainSequence effects count: {s.TimeLine.MainSequence.Count}")
for idx in range(1, s.TimeLine.MainSequence.Count + 1):
    eff = s.TimeLine.MainSequence(idx)
    print(f"Effect {idx}: Shape={eff.Shape.Name}, TriggerType={eff.Timing.TriggerType}")

pres.Save()
pres.Close()
ppt_app.Quit()
print("Success!")

