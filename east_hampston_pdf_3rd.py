import pandas as pd
import re
# Read the Excel file
df = pd.read_excel(fr"C:\Users\karthim\Downloads\sk2.xlsx")
rows=[]
results = []
with open('east_demo.txt', 'w') as file:
    for index, row in df.iterrows():
        col1 = row['s1']
        # print(col1)
        col2 = row['s2']
        l1=re.findall(r'[\d\,\.]+ [\d]+ [\d]+ [\w]+c20',col2)
        # print(l1)
        col3=row['s3']
        l2=re.findall(r'[\d\,\.]+ Town [\d]+ [\w]+g11',col3)
        # print(l2)
        col4=row['s4']
        # l4=re.findall(r'[\d\,\.]+ BAS STA \$',col4)
        #
        sheet = f'{col1}|{l1}|{l2}|{col4}'
        print(sheet)
        # file.write(sheet + '\n')