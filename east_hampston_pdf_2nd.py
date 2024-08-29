import pdfplumber
import re
import pandas as pd
rows = []

# Open the PDF file
list1=['1']
for i in list1:
    pdf_path = fr"C:\Users\karthim\Downloads\hampston\{i}.pdf"
    print(i)
    with pdfplumber.open(pdf_path) as pdf:
        try:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
            if full_text is None:
                continue
            # print(full_text)
            parcel = re.findall(r'\d{6}\s\d{3}\.\d{3}\-\d{4}\-\d{3}\.\d{3}\s\d{4}', full_text)
            # print(parcel)
            for k in parcel:
                print(k)
            s2 = re.split(r'\d{6}\s\d{3}\.\d{3}\-\d{4}\-\d{3}\.\d{3}\s\d{4}', full_text)
            del s2[0]
            for s3 in s2:
                # print(s3)
                # print('--')
                l1=re.findall(r'[\d\,\.]+ County [\d\,]+',s3)
                print(l1)
                l2=re.findall(r'[\d\,\.]+ Town [\d\,]+',s3)
                # print(l2)
                lines = s3.splitlines()
                third_line = lines[2]
                # print(third_line)
                s1=f"{l1}|{l2}|{third_line}"
                print(s1)
                rows_dict={
                    'k1':k,
                    'k2':s1,
                    'page': i
                }
                rows.append(rows_dict)
                df = pd.DataFrame(rows)
                df.to_excel("east.xlsx", index=False)




        except Exception as e:
            print(f"Error processing page {i}: {e}")