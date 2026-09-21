import os
import win32com.client

ppt_app = win32com.client.Dispatch("PowerPoint.Application")

f1 = os.path.abspath("Ventricular Tumors_(Part 1).pptx")
f2 = os.path.abspath("Ventricular Tumors_(Part 2).pptx")

p1 = ppt_app.Presentations.Open(f1, WithWindow=False)
print(f"Part 1 Slide Count: {p1.Slides.Count}")
s1_last = p1.Slides(p1.Slides.Count)
s1_last.Export(os.path.abspath("ppt_part1_slide33.png"), "PNG", 1920, 1080)
s1_slide10 = p1.Slides(10)
s1_slide10.Export(os.path.abspath("ppt_part1_slide10.png"), "PNG", 1920, 1080)
p1.Close()

p2 = ppt_app.Presentations.Open(f2, WithWindow=False)
print(f"Part 2 Slide Count: {p2.Slides.Count}")
s2_last = p2.Slides(p2.Slides.Count)
s2_last.Export(os.path.abspath("ppt_part2_slide33.png"), "PNG", 1920, 1080)
s2_slide16 = p2.Slides(16)
s2_slide16.Export(os.path.abspath("ppt_part2_slide16.png"), "PNG", 1920, 1080)
p2.Close()

ppt_app.Quit()
print("Exported PPT verification slides successfully!")

