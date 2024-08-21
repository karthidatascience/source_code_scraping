import tabula
from PyPDF2 import PdfReader, PdfWriter
import pandas as pd
inputpdf = PdfReader(open(r"C:\Users\karthim\Downloads\HEMPSTEAD_SCHOOL_DISTRICTS_1_5.pdf", "rb"))
rows=[]
for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    page = inputpdf.pages[i]
    output.add_page(page)

    # Use tabula to read tables from the current page
    tables = tabula.read_pdf(r"C:\Users\karthim\Downloads\HEMPSTEAD_SCHOOL_DISTRICTS_11_15.pdf", pages=i + 1,
                             multiple_tables=True)

    print(f"Tables from page {i + 1}:")
    f1 = []
    f2 = []
    f3 = []
    f4 = []
    f5 = []
    f6 = []
    f7 = []
    f8 = []
    f9 = []
    f10 = []
    f11 = []
    f12 = []
    f13 = []
    for table in tables:
        if len(table) > 0:
            first_column_values = table.iloc[:, 0].tolist()
            f1.append(first_column_values)

            second_column_values = table.iloc[:, 1].tolist()
            f2.append(second_column_values)

            third_column_values = table.iloc[:, 2].tolist()
            f3.append(third_column_values)

            fourth_column_values = table.iloc[:, 3].tolist()
            f4.append(fourth_column_values)

            fifth_column_values = table.iloc[:, 4].tolist()
            f5.append(fifth_column_values)
            sixth_column_values = table.iloc[:, 5].tolist()
            f6.append(sixth_column_values)
            seventh_column_values = table.iloc[:, 6].tolist()
            f7.append(seventh_column_values)
            eighth_column_values = table.iloc[:, 7].tolist()
            f8.append(eighth_column_values)
            ninth_column_values = table.iloc[:, 8].tolist()
            f9.append(ninth_column_values)
            tenth_column_values = table.iloc[:, 9].tolist()
            f10.append(tenth_column_values)
            eleventh_column_values = table.iloc[:, 10].tolist()
            f11.append(eleventh_column_values)
            twelveth_column_values = table.iloc[:, 11].tolist()
            f12.append(twelveth_column_values)
            thirteenth_column_values = table.iloc[:, 12].tolist()
            f13.append(thirteenth_column_values)
            print(first_column_values)
            # print(second_column_values)
            # print(third_column_values)
            # print(fourth_column_values)
            # print(fifth_column_values)
            # print(sixth_column_values)
            # print(seventh_column_values)
            # print(eighth_column_values)
            # print(ninth_column_values)
            # print(tenth_column_values)
            # print(eleventh_column_values)
            # print(twelveth_column_values)
            # print(thirteenth_column_values)
            rows_dict = {
                "f1": f1,
                "f2": f2,
                "f3": f3,
                "f4": f4,
                "f5": f5,
                "f6": f6,
                "f7": f7,
                "f8": f8,
                "f9": f9,
                "f10": f10,
                "f11": f11,
                "f12": f12,
                "f13": f13
            }
            rows.append(rows_dict)
            df = pd.DataFrame(rows)
            df.to_csv("nasses_final_11_15.csv", index=False)

