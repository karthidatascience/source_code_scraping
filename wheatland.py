import PyPDF2
import pandas as pd
import re
import pdfplumber
list1=['01-28-201-073-0000.pdf','01-35-301-016-0000.pdf','01-06-410-098-0000.pdf','01-06-410-096-0000.pdf','01-06-310-014-0000.pdf','01-06-310-004-0000.pdf']
rows=[]
for i in list1:
    pdfpath=fr"C:\Users\karthim\Downloads\{i}"
    print(i)
    with pdfplumber.open(pdfpath) as pdf:
        try:  # No need for 'rb' mode here
            full_text = ''
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
            # print(full_text)
            parcel = re.findall(r'Parcel Number:.*',full_text)
            print(parcel)
            address=re.findall(r'Address:.*',full_text)
            print(address)
            city=re.findall(r'City:.*',full_text)
            print(city)
            Neighborhood=re.findall(r'Neighborhood:.*',full_text)
            print(Neighborhood)
            subdivision=re.findall(r'Subdivision:.*',full_text)
            print(subdivision)
            lot_number=re.findall(r'Lot Number:.*',full_text)
            print(lot_number)
            block_unit=re.findall(r'Block Unit:.*',full_text)
            print(block_unit)
            lot_size=re.findall(r'Lot Size:.*',full_text)
            print(lot_size)
            style=re.findall(r'Style:.*',full_text)
            print(style)
            construction=re.findall(r'Construction:.*',full_text)
            print(construction)
            year_built=re.findall(r'Year Built:.*',full_text)
            print(year_built)
            half_baths=re.findall(r'Half Baths:.*',full_text)
            print(half_baths)
            full_baths=re.findall(r'Full Baths:.*',full_text)
            print(full_baths)
            basement_area=re.findall(r'Basement Area:.*',full_text)
            print(basement_area)
            basement_area_finished=re.findall(r'Basement Area Finished:.*',full_text)
            print(basement_area_finished)
            central_air=re.findall(r'Central Air:.*',full_text)
            print(central_air)
            garage_type=re.findall(r'Garage Type:.*',full_text)
            print(garage_type)
            first_floor=re.findall(r'First Floor:.*',full_text)
            print(first_floor)
            second_floor=re.findall(r'Second Floor:.*',full_text)
            print(second_floor)
            third_floor=re.findall(r'Third Floor:.*',full_text)
            print(third_floor)
            misc_floor=re.findall(r'Misc\. Floor:.*',full_text)
            print(misc_floor)
            total_living_area=re.findall(r'Total Living Area:.*',full_text)
            print(total_living_area)
            values=re.findall(r'Code\n2024.*',full_text)
            print(values)
            rows_dict = {
                'page': i,
                'Parcel': parcel,
                'Address': address,
                'City': city,
                'Neighborhood': Neighborhood,
                'Subdivision': subdivision,
                'Lot Number': lot_number,
                'Block Unit': block_unit,
                'Lot Size': lot_size,
                'Style': style,
                'Construction': construction,
                'Year Built': year_built,
                'Half Baths': half_baths,
                'Full Baths': full_baths,
                'Basement Area': basement_area,
                'Basement Area Finished': basement_area_finished,
                'Central Air': central_air,
                'Garage Type': garage_type,
                'First Floor': first_floor,
                'Second Floor': second_floor,
                'Third Floor': third_floor,
                'Misc. Floor': misc_floor,
                'Total Living Area': total_living_area,
                'Code 2024': values

            }
            rows.append(rows_dict)
            df = pd.DataFrame(rows)
            df.to_excel("wheatland.xlsx", index=False)

 
        except Exception as e:
            print(f"Error processing page {i}: {e}")

