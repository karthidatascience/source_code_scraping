import pandas as pd


df=pd.read_csv(fr"C:\Users\karthim\Downloads\north_all.csv")
rows = []
with open('north_all.txt', 'w', encoding='utf-8') as output_file:
    for index, row in df.iterrows():
        s1 = row['f1'].replace(', ','|').split('|')
        # print(s1)
        # print(len(s1))
        s2 = row['f2'].replace(', ','|').split('|')
        # print(s2)
        # print(len(s2))
        s3 = row['f3'].replace("', '",'|').split('|')
        if len(s1) != len(s3):
            s3 = row['f3'].split(",")
        if len(s1) != len(s3):

            print(f"Still mismatch in row s3: {index}")
            # print(f"Row data: {row.to_dict()}\n")

        s4 = row['f4'].replace("nan","'nan'").replace("', '",'|').replace("','","|").split('|')
        # print(s4)
        if len(s1) != len(s4):
            s4 = row['f4'].split(",")
        if len(s1) != len(s4):
            print(f"row s4: {index}")
            # print(f'{len(s1)}--{len(s4)}')
            # print(f"Row data: {row.to_dict()}\n")
        # # print(len(s4))
        s5 = row['f5'].replace("', '",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s5):
            print(f"row s5: {index}")
            # print(f'{len(s1)}--{len(s5)}')
            # print(f"Row data: {row.to_dict()}\n")
        #
        s6 = row['f6'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s6):
            print(f"row s6: {index}")
            print(f'{len(s1)}--{len(s6)}')
            print(f"Row data: {row.to_dict()}\n")
        s7 = row['f7'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s7):
            print(f"row s7: {index}")
            print(f'{len(s1)}--{len(s7)}')
            print(f"Row data: {row.to_dict()}\n")
        #
        s8 = row['f8'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s8):
            print(f"row s8: {index}")
            print(f'{len(s1)}--{len(s8)}')
            print(f"Row data: {row.to_dict()}\n")
        # # print(len(s8))
        s9 = row['f9'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s9):
            print(f"row s9: {index}")
            print(f'{len(s1)}--{len(s9)}')
            print(f"Row data: {row.to_dict()}\n")

        s10 = row['f10'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s10):
            print(f"row s10: {index}")
            print(f'{len(s1)}--{len(s10)}')
            print(f"Row data: {row.to_dict()}\n")
        #
        s11 = row['f11'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s11):
            print(f"row s11: {index}")
            print(f'{len(s1)}--{len(s11)}')
            print(f"Row data: {row.to_dict()}\n")
        #
        s12 = row['f12'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s12):
            print(f"row s11: {index}")
            print(f'{len(s1)}--{len(s12)}')
            print(f"Row data: {row.to_dict()}\n")

        s13 = row['f13'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s13):
            print(f"row s13: {index}")
            print(f'{len(s1)}--{len(s13)}')
            print(f"Row data: {row.to_dict()}\n")

        s14 = row['f14'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').replace(', ',"|").split('|')
        if len(s1) != len(s14):
            print(f"row s14: {index}")
            print(f'{len(s1)}--{len(s14)}')
            print(f"Row data: {row.to_dict()}\n")

        s15 = row['f15'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').replace(', ',"|").split('|')
        if len(s1) != len(s15):
            print(f"row s15: {index}")
            print(f'{len(s1)}--{len(s15)}')
            print(f"Row data: {row.to_dict()}\n")
        s16 = row['f16'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').replace(', ',"|").split('|')
        if len(s1) != len(s16):
            print(f"row s16: {index}")
            print(f'{len(s1)}--{len(s16)}')
            print(f"Row data: {row.to_dict()}\n")
        s17 = row['f17'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').replace(', ',"|").split('|')
        if len(s1) != len(s17):
            print(f"row s17: {index}")
            print(f'{len(s1)}--{len(s17)}')
            print(f"Row data: {row.to_dict()}\n")
        s18 = row['f18'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').replace(', ',"|").split('|')
        if len(s1) != len(s18):
            print(f"row s18: {index}")
            print(f'{len(s1)}--{len(s18)}')
            print(f"Row data: {row.to_dict()}\n")
        s19 = row['f19'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').replace(', ',"|").split('|')
        if len(s1) != len(s19):
            print(f"row s19: {index}")
            print(f'{len(s1)}--{len(s19)}')
            print(f"Row data: {row.to_dict()}\n")
        s20 = row['f20'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').replace(', ',"|").split('|')
        if len(s1) != len(s20):
            print(f"row s20: {index}")
            print(f'{len(s1)}--{len(s20)}')
            print(f"Row data: {row.to_dict()}\n")
        s21 = row['f21'].replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').split('|')
        if len(s1) != len(s21):
            print(f"row s21: {index}")
            print(f'{len(s1)}--{len(s21)}')
            # print(f"Row data: {row.to_dict()}\n")
        s22 = row['f22'].split(',')
               # .replace("', '",'|').replace("','",'|').replace("''", "','").replace('", "','|').replace(', ',"|").split('|'))
        if len(s1) != len(s22):
            print(f"row s22: {index}")
            print(f'{len(s1)}--{len(s22)}')
            # print(f"Row data: {row.to_dict()}\n")


        s23 = row['f23'].split(",")
        if len(s1) != len(s23):
            print(f"row s23: {index}")
            print(f'{len(s1)}--{len(s23)}')
            print(f"Row data: {row.to_dict()}\n")
        s24 = row['f24'].split(",")
        if len(s1) != len(s24):
            print(f"row s24: {index}")
            print(f'{len(s1)}--{len(s24)}')
            print(f"Row data: {row.to_dict()}\n")
        # print(len(s24))
        s25 = row['f25'].split(",")
        if len(s1) != len(s25):
            print(f"row s25: {index}")
            print(f'{len(s1)}--{len(s25)}')
            print(f"Row data: {row.to_dict()}\n")

        s26 = row['f26'].split(",")
        if len(s1) != len(s26):
            print(f"row s26: {index}")
            print(f'{len(s1)}--{len(s26)}')
            print(f"Row data: {row.to_dict()}\n")
        # # print(len(s26))
        s27 = row['f27'].split(",")
        if len(s1) != len(s27):
            print(f"row s25: {index}")
            print(f'{len(s1)}--{len(s27)}')
            print(f"Row data: {row.to_dict()}\n")
        # # print(len(s27))
        s28 = row['f28'].split(",")
        if len(s1) != len(s28):
            print(f"row s28: {index}")
            print(f'{len(s1)}--{len(s28)}')
            print(f"Row data: {row.to_dict()}\n")
        # # print(len(s28))
        s29 = row['f29'].split(",")
        if len(s1) != len(s29):
            print(f"row s29: {index}")
            # print(f'{len(s1)}--{len(s29)}')
            # print(f"Row data: {row.to_dict()}\n")
        # # print(len(s29))
        s30 = row['f30'].split(",")
        if len(s1) != len(s30):
            print(f"row s30: {index}")
            print(f'{len(s1)}--{len(s30)}')
            print(f"Row data: {row.to_dict()}\n")
        # print(len(s30))


        # #
        # Check if lengths match
        if len(s1) == len(s2)== len(s3)==len(s4)==len(s5)==len(s6)==len(s7)==len(s8)==len(s9)==len(s10)==len(s11)==len(s12)==len(s13)==len(s14)==len(s15)==len(s16)==len(s17)==len(s18)==len(s19)==len(s20)==len(s21)==len(s22)==len(s23)==len(s24)==len(s25)==len(s26)==len(s27)==len(s28)==len(s29)==len(s30):
            print(f"Mismatch in row index: {index}")

            for i in range(len(s2)):
                k2 = f"{s1[i].strip()} | {s2[i].strip()} |{s3[i].strip()}|{s4[i].strip()}|{s5[i].strip()}|{s6[i].strip()}|{s7[i].strip()}|{s8[i].strip()}|{s9[i].strip()}|{s10[i].strip()}|{s11[i].strip()}|{s12[i].strip()}|{s13[i].strip()}|{s14[i].strip()}|{s15[i].strip()}|{s16[i].strip()}|{s17[i].strip()}|{s18[i].strip()}|{s19[i].strip()}|{s20[i].strip()}|{s21[i].strip()}|{s22[i].strip()}|{s23[i].strip()}|{s24[i].strip()}|{s25[i].strip()}|{s26[i].strip()}|{s27[i].strip()}|{s27[i].strip()}|{s28[i].strip()}|{s29[i].strip()}|{s30[i].strip()}"
                # print(k2)
                output_file.write(k2 + '\n')