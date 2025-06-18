import os
from PyPDF2 import PdfWriter, PdfReader
import re
# file = open(r"C:\Users\karthim\Downloads\201-450.pdf","rb")
# reader1 = PdfReader(file)

from PyPDF2 import PdfWriter, PdfReader
import re
import time

# Open the input PDF file
inputpdf = PdfReader(open(r"C:\Users\karthim\Downloads\sothold.pdf","rb"))


# Loop through each page of the input PDF file
for i in range(len(inputpdf.pages)):

    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    text = inputpdf.pages[i].extract_text()
    # print(text)
    # d2=''
    # s4 = re.findall(r'CAD A\/C#  [^\r\n]+\s[\w\d\-\.]+', text)
    # s6 = d2.join(s4)
    # s6 = s6.split('   ')[0]
    # acc_num = re.sub(r'\s+','',s6).replace('CADA/C#','')
    # acc_num = f'{acc_num}_Mail Out'
    print(i)
    with open(f"{i}.pdf", "wb") as outputStream:
        output.write(outputStream)
    # time.sleep(1)

