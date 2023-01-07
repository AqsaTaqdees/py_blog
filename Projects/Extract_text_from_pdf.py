pip install pypdf2
import PyPDF2
pdf = open("Linux.pdf","rb")#rb means read binary.Since PDF files contain data in binary format, the permission for the open() method should be set to rb (read binary).
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(1)#getPage() method will help you specify the page number you want to extract text from.
print(page.extract_text())
print(pdf.close())