# import tabula
from PyPDF2 import PdfReader, PdfWriter
import pandas as pd
import re
import pdfplumber
rows=[]
extracted_text1=[]
pdf_path = fr"C:\Users\karthim\Downloads\va500_.pdf"
with open('va1200.txt', 'w', encoding='utf-8') as output_file:
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
        # print(full_text)
        try:

            s1=full_text.split("------------------------------------------------------------------------------------------------------------------------------")
            if len(s1) > 1:
                del s1[0]
                del s1[-1]
            for idx, s1 in enumerate(s1):
                lines = s1.splitlines()
                # print(lines)
                line=lines[1]
                total=line.split(' ')[-1]
                impr = line.split(' ')[-2]
                land = line.split(' ')[-3]
                code=line.split(' ')[-4]
                all=line.split(' ')[:-4]
                # print(str(all))
                acc=re.findall(r"'\d{3,5}',.*?'\]",str(all))
                # print(acc)
                address = re.split(r' \d{3} ', line)
                # print(address[0])
                street = lines[3]
                st1=street.split(' ')[-1]
                # print(st1)
                st2=street.split(' ')[:-1]
                # print(st2)

                print(f'{total}|{impr}|{land}|{code}|{str(all)}|{acc}|{address[0]}|{st1}|{st2}|{lines[2]}|{lines[4]}')
                output_row = f'{total}|{impr}|{land}|{code}|{str(all)}|{acc}|{address[0]}|{st1}|{st2}|{lines[2]}|{lines[4]}'
        except:
            output_row=''
        output_file.write(output_row + '\n')


