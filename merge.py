from PyPDF2 import PdfWriter

merger = PdfWriter()

input1 = open("pdf_merger.py/document1.pdf", "rb")
input2 = open("pdf_merger.py/document2.pdf", "rb")
input3 = open("pdf_merger.py/document3.pdf", "rb")



merger.append(input1)
merger.append(input2)
merger.append(input3)

output = open("document-output.pdf", "wb")
merger.write(output)


merger.close()
output.close()