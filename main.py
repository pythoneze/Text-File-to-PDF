from fpdf import FPDF
import glob as gb
from pathlib import Path

FILEPATHS = gb.glob("text_files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in FILEPATHS:        
    pdf.add_page()

    filename = Path(filepath).stem
    header = filename.title()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=header, ln=1)

pdf.output("animals.pdf")
