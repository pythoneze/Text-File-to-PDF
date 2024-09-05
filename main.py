import glob as gb
from fpdf import FPDF
from pathlib import Path

FILEPATHS = gb.glob("text_files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")


def create_pdf(filepath, content):
    pdf.add_page()

    filename = Path(filepath).stem
    header = filename.title()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=header, ln=1)

    pdf.set_font(family="Arial", size=12)
    pdf.ln()
    pdf.multi_cell(w=0, h=8, txt=content)


def create_and_save_pdfs():
    for filepath in FILEPATHS:
        with open(filepath, "r") as file:
            content = file.read()

        create_pdf(filepath, content)

    pdf.output("animals.pdf")


if __name__ == "__main__":
    create_and_save_pdfs()
