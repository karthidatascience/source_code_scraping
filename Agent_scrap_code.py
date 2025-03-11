from PyPDF2 import PdfReader, PdfWriter
import pandas as pd
import re
import pdfplumber

rows = []
pdf_path = fr"C:\Users\karthim\Downloads\4_4k.pdf"

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages):
        full_text = page.extract_text()
        if full_text:
            parcel_number = re.findall(r'Parcel Number[\s\-\d]+', full_text)
            match = re.search(r'Agent Information(.*?)Calculations Assessment', full_text, re.DOTALL)
            extracted_text1 = []
            if match:
                extracted_text = match.group(1).strip()
                extracted_text1 = extracted_text.split('\n')
                print(extracted_text1)
            else:
                print(f"No match found on page {page_num + 1}")

            rows_dict = {
                "Page": page_num + 1,
                "Parcel Number": parcel_number,
                "Agent Information": extracted_text1,
            }
            rows.append(rows_dict)

df = pd.DataFrame(rows)
df.to_csv("4_4k.csv", index=False)