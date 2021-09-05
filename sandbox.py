'''
Playground, random stuff
'''
import PyPDF2

pdf = open('CHK_4758_Monthly_Statement_02012021-02282021.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf)
print(reader.numPages)

page = reader.getPage(0)
print(page.extractText())