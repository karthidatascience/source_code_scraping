import tabula
from PyPDF2 import PdfReader, PdfWriter
import pandas as pd
inputpdf = PdfReader(open(r"C:\Users\karthim\Downloads\1.pdf", "rb"))
rows=[]
for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    page = inputpdf.pages[i]
    output.add_page(page)

    # Use tabula to read tables from the current page
    tables = tabula.read_pdf(r"C:\Users\karthim\Downloads\1.pdf", pages=i + 1,
                             multiple_tables=True)
    print(tables)
    f1=[]
    f2=[]
    f3=[]
    f4=[]
    f5=[]
    f6=[]
    f7=[]
    f8=[]
    f9=[]
    f10=[]
    f11=[]
    f12=[]
    f13=[]
    f14=[]
    f15=[]
    f16=[]
    f17=[]
    f18=[]
    f19=[]
    f20=[]
    f21=[]
    f22=[]
    f23=[]
    f24=[]
    f25=[]
    f26=[]
    f27=[]
    f28=[]
    f29=[]
    f30=[]

    for table in tables:
        print(table)

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
            fourteenth_column_values = table.iloc[:, 13].tolist()
            f14.append(fourteenth_column_values)
            fifteenth_column_values = table.iloc[:, 14].tolist()
            f15.append(fifteenth_column_values)
            sixteenth_column_values = table.iloc[:, 15].tolist()
            f16.append(sixteenth_column_values)
            seventeenth_column_values = table.iloc[:, 16].tolist()
            f17.append(seventeenth_column_values)
            eighteenth_column_values = table.iloc[:, 17].tolist()
            f18.append(eighteenth_column_values)
            nineteenth_column_values = table.iloc[:, 18].tolist()
            f19.append(nineteenth_column_values)
            twentieth_column_values = table.iloc[:, 19].tolist()
            f20.append(twentieth_column_values)
            twenty_first_column_values = table.iloc[:, 20].tolist()
            f21.append(twenty_first_column_values)
            twenty_second_column_values = table.iloc[:, 21].tolist()
            f22.append(twenty_second_column_values)
            twenty_third_column_values = table.iloc[:, 22].tolist()
            f23.append(twenty_third_column_values)
            twenty_fourth_column_values = table.iloc[:, 23].tolist()
            f24.append(twenty_fourth_column_values)
            twenty_fifth_column_values = table.iloc[:, 24].tolist()
            f25.append(twenty_fifth_column_values)
            twenty_sixth_column_values = table.iloc[:, 25].tolist()
            f26.append(twenty_sixth_column_values)
            twenty_seventh_column_values = table.iloc[:, 26].tolist()
            f27.append(twenty_seventh_column_values)
            twenty_eighth_column_values = table.iloc[:, 27].tolist()
            f28.append(twenty_eighth_column_values)
            twenty_ninth_column_values = table.iloc[:, 28].tolist()
            f29.append(twenty_ninth_column_values)
            thirtieth_column_values = table.iloc[:, 29].tolist()
            f30.append(thirtieth_column_values)

            print(first_column_values)
            print(second_column_values)
            print(third_column_values)
            print(fourth_column_values)
            print(fifth_column_values)
            print(sixth_column_values)
            print(seventh_column_values)
            print(eighth_column_values)
            print(ninth_column_values)
            print(tenth_column_values)
            print(eleventh_column_values)
            print(twelveth_column_values)
            print(thirteenth_column_values)
            print(fourteenth_column_values)
            print(fifteenth_column_values)
            print(sixteenth_column_values)
            print(seventeenth_column_values)
            print(eighteenth_column_values)
            print(nineteenth_column_values)
            print(twentieth_column_values)
            print(twenty_first_column_values)
            print(twenty_second_column_values)
            print(twenty_third_column_values)
            print(twenty_fourth_column_values)
            print(twenty_fifth_column_values)
            print(twenty_sixth_column_values)
            print(twenty_seventh_column_values)
            print(twenty_eighth_column_values)
            print(twenty_ninth_column_values)
            print(thirtieth_column_values)

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
                "f13": f13,
                "f14": f14,
                "f15": f15,
                "f16": f16,
                "f17": f17,
                "f18": f18,
                "f19": f19,
                "f20": f20,
                "f21": f21,
                "f22": f22,
                "f23": f23,
                "f24": f24,
                "f25": f25,
                "f26": f26,
                "f27": f27,
                "f28": f28,
                "f29": f29,
                "f30": f30,
            }
            rows.append(rows_dict)
            df = pd.DataFrame(rows)
            df.to_csv("HEMPSTEAD_RS18-1-700.csv", index=False)