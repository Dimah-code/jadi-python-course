from PyPDF2 import PdfReader

reader = PdfReader(
    "/home/dimah/Public/jadi-python-course/13_working_with_data_files/PDF/PDF-Sample.pdf"
)
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print("Number of pages: ", number_of_pages)

print(
    """

PDF TEXT EXTRACTED:

"""
)

print(text)
