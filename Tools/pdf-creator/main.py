#!/usr/bin/env python3

from pathlib import Path

from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


pdf = Document()
page = Page()

pdf.append_page(page)
layout = SingleColumnLayout(page)
layout.add(Paragraph("Hello world ! Lets create some pdf"))


with open(Path("test.pdf"), "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, pdf)

#pip install borb
