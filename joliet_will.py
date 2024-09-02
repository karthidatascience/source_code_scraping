import pdfplumber
import re
import pandas as pd
rows = []

df = pd.read_excel(r"C:\Users\karthim.OCNHOU\Downloads\joliet_acc.xlsx")
parcel_numbers = df['txroll_cadaccountnumber'][18000:19500].astype(str).tolist()
# print(parcel_numbers)
for i in parcel_numbers:
    pdf_path = fr"C:\Users\karthim.OCNHOU\Downloads\joliet\{i}"
    print(i)
    with pdfplumber.open(pdf_path) as pdf:
        try:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
            # print(full_text)
            parcel = re.findall(r'.*\nParcel Number',full_text)
            print(parcel)
            address=re.findall(r'.*\nAddress',full_text)
            print(address)
            city=re.findall(r'.*\nCity',full_text)
            print(city)
            Neighborhood=re.findall(r'.*\nNeighborhood',full_text)
            print(Neighborhood)
            subdivison=re.findall(r'.*\nSubdivision',full_text)
            print(subdivison)
            lot_number=re.findall(r'.*\nLot Number',full_text)
            print(lot_number)
            block_unit=re.findall(r'.*\nBlock Unit',full_text)
            print(block_unit)
            lot_size=re.findall(r'.*\nLot Size',full_text)
            print(lot_size)
            style=re.findall(r'.*\nStyle',full_text)
            print(style)
            Construction=re.findall(r'.*\nConstruction',full_text)
            print(Construction)
            year_built=re.findall(r'.*\nYear Built',full_text)
            print(year_built)
            half_baths=re.findall(r'.*\nHalf Baths',full_text)
            print(half_baths)
            full_baths=re.findall(r'.*\nFull Baths',full_text)
            print(full_baths)
            basement_area=re.findall(r'.*\nBasement Area:',full_text)
            print(basement_area)
            basement_area_finished=re.findall(r'.*\nBasement Area Finished',full_text)
            print(basement_area_finished)
            central_air=re.findall(r'.*\nCentral Air',full_text)
            print(central_air)
            garage_type=re.findall(r'.*\nGarage Type',full_text)
            print(garage_type)
            garage_area=re.findall(r'.*\nGarage Area:',full_text)
            print(garage_area)
            first_floor=re.findall(r'.*\nFirst Floor',full_text)
            print(first_floor)
            second_floor=re.findall(r'.*\nSecond Floor',full_text)
            print(second_floor)
            third_floor=re.findall(r'.*\nThird Floor',full_text)
            print(third_floor)
            total_living_area=re.findall(r'.*\nTotal Living Area',full_text)
            print(total_living_area)
            values=re.findall(r'Code\n2024.*',full_text)
            print(values)
            sale=re.findall(r'Type\n.*',full_text)
            print(sale)
            type=re.findall(r'.*\nType:',full_text)
            print(type)
        except:
            parcel=''
            address=''
            city=''
            Neighborhood=''
            subdivison=''
            lot_number=''
            block_unit=''
            lot_size=''
            style=''
            Construction=''
            year_built=''
            half_baths=''
            basement_area=''
            basement_area_finished=''
            central_air=''
            garage_type=''
            first_floor=''
            second_floor=''
            third_floor=''
            total_living_area=''
            values=''
            sale=''
            garage_area=''
            type=''




        rows_dict = {
            'page': i,
            'parcel': parcel,
            'address': address,
            'city': city,
            'neighborhood': Neighborhood,
            'subdivison': subdivison,
            'lot_number': lot_number,
            'block_unit': block_unit,
            'lot_size': lot_size,
            'style': style,
            'Construction': Construction,
            'year_built':year_built,
            'half_baths':half_baths,
            'full_baths':full_baths,
            'basement_area':basement_area,
            'basement_area_finished':basement_area_finished,
            'central_air':central_air,
            'garage_type':garage_type,
            'garage_area':garage_area,
            'first_floor':first_floor,
            'second_floor':second_floor,
            'third_floor':third_floor,
            'total_living_area':total_living_area,
            'type':type,
            'values':values,
            'sale':sale

        }
        rows.append(rows_dict)
        df = pd.DataFrame(rows)
        df.to_excel("joliet13.xlsx", index=False)
