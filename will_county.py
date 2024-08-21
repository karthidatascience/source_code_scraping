import time
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


rows=[]
df = pd.read_excel(fr"C:\Users\karthim\Downloads\will_balance1.xlsx")
link2 = df['txroll_CADAccountNumber'].tolist()
for i in range(650,1260):
  url=f'https://www.willcountysoa.com/propertysearch/detail?Mpin={link2[i]}'
  r = requests.get(url)
  try:
    print(url)
    soup = BeautifulSoup(r.content,'html.parser')
    # print(soup)
    owner_name=re.findall(r'<b>Owner Name:<\/b><\/span><\/td>\s<td style="width: 439px"><span id="FormView1_OwnerLabel"><font\scolor="Black" face="Arial,Helvetica,sans-serif"\ssize="5">[^<>]*',str(soup))
    owner_name=' '.join(owner_name).replace('<b>Owner Name:</b></span></td>\n<td style="width: 439px"><span id="FormView1_OwnerLabel"><font color="Black" face="Arial,Helvetica,sans-serif" size="5">','').strip()
    print(owner_name)

    address1=re.findall(r'Street Address:<\/b>\s+<br\/>\s<table cellspacing="0" id="FormView1_DataList1">\s<tr>\s<td><font size="4">\s<span id="FormView1_DataList1_address1Label_0">[^<>]*<\/span>\s<br\/>\s<span id="FormView1_DataList1_address2Label_0">[^<>]*|<span id="FormView1_DataList1_address1Label_0">[^<>]*<\/span>\s+<br\/>\s+<span id="FormView1_DataList1_address2Label_0">[^<>]*',str(soup))
    address1=' '.join(address1)
    address1=re.sub('\s+',' ',address1)
    print(address1)

    sub_division=re.findall(r'Subdivision:[\s]+<\/b>\s+<span id="FormView1_subdivisionLabel"><font color="Black"\s+face="Arial,Helvetica,sans-serif" size="5">[^<>]*',str(soup))
    sub_division=' '.join(sub_division)
    sub_division=re.sub('\s+',' ',sub_division)
    print(sub_division)

    homesite=re.findall(r'Homesite Acres:\s<\/b><\/font><\/td><td align="right" nowrap="nowrap"><font size="5">[^<>]*',str(soup))
    homesite=' '.join(homesite).replace('Homesite Acres: </b></font></td><td align="right" nowrap="nowrap"><font size="5">','').strip()
    print(homesite)


    p_class=re.findall(r'<b>Property Class:\s+<\/b><\/font><\/td><td nowrap="nowrap"><font size="5">[^<>]*',str(soup))
    p_class=' '.join(p_class).replace('<b>Property Class:\xa0\xa0\xa0</b></font></td><td nowrap="nowrap"><font size="5">','').strip()
    print(p_class)

    farm_acres=re.findall(r'<b>Farm Acres:<\/b><\/font><\/td><td align="right" nowrap="nowrap"><font size="5">[^<>]*',str(soup))
    farm_acres=' '.join(farm_acres).replace('<b>Farm Acres:</b></font></td><td align="right" nowrap="nowrap"><font size="5">','').strip()
    print(farm_acres)

    open_space_acres=re.findall(r'<b>Open Space Acres:<\/b><\/font><\/td><td align="right" nowrap="nowrap"><font size="5">[^<>]*',str(soup))
    open_space_acres=' '.join(open_space_acres).replace('<b>Open Space Acres:</b></font></td><td align="right" nowrap="nowrap"><font size="5">','').strip()
    print(open_space_acres)

    total_acres=re.findall(r'<b>Total Acres: <\/b><\/font><\/td><td align="right" nowrap="nowrap"><font size="5">[^<>]*',str(soup))
    total_acres=' '.join(total_acres).replace('<b>Total Acres: </b></font></td><td align="right" nowrap="nowrap"><font size="5">','').strip()
    print(total_acres)

    values_2023=re.findall(r'2024<\/font><\/td><td align="right" width="60"><font color="Black" face="Arial,Helvetica,sans-serif" size="5">[^<>]*<\/font><\/td><td align="right" width="180"><font color="Black">[^<>]*<\/font><\/td><td align="right" width="180"><font color="Black">[^<>]*<\/font><\/td><td align="right" width="180"><font color="Black">[^<>]*<\/font><\/td><td align="right" width="180"><font color="Black">[^<>]*<\/font><\/td><td align="right" width="180"><font color="Black">[^<>]*<\/font><\/td><td align="right" width="180"><font color="Black">[^<>]*<\/font><\/td><td align="right" width="180"><font color="Black">[^<>]*<\/font><\/td><td align="right" width="180"><font color="Black">[^<>]*',str(soup))
    values_2023=' '.join(values_2023)
    values_2023=re.sub('\s+',' ',values_2023)
    print(values_2023)

    legal_desc=re.findall(r'Legal Description"\/>\s+<br\/>\s+<span id="FormView1_leag"><font color="Black" face="Arial,Helvetica,sans-serif" size="5">[^<>]*',str(soup))
    legal_desc=' '.join(legal_desc)
    legal_desc=re.sub('\s+',' ',legal_desc)
    print(legal_desc)

    story=re.findall(r'Style:<\/b><\/font><\/td><td><font face="Arial" size="5">[^<>]*',str(soup))
    story=' '.join(story).replace('Style:</b></font></td><td><font face="Arial" size="5">','').strip()
    print(story)

    year_build=re.findall(r'Year Built:<\/b><\/font><\/td><td><font face="Arial" size="5">[^<>]*',str(soup))
    year_build=' '.join(year_build).replace('Year Built:</b></font></td><td><font face="Arial" size="5">','').strip()
    print(year_build)

    total_sqft=re.findall(r'Total Sq\. Ft:<\/b><\/font><\/td><td><font face="Arial" size="5">[^<>]*',str(soup))
    total_sqft=' '.join(total_sqft).replace('Total Sq. Ft:</b></font></td><td><font face="Arial" size="5">','').strip()
    print(total_sqft)

    bathrooms=re.findall(r'Bathrooms:<\/b><\/font><\/td><td><font face="Arial" size="5">[^<>]*',str(soup))
    bathrooms=' '.join(bathrooms).replace('Bathrooms:</b></font></td><td><font face="Arial" size="5">','').strip()
    print(bathrooms)

    central_air=re.findall(r'Central Air:<\/b><\/font><\/td><td><font face="Arial" size="5">[^<>]*',str(soup))
    central_air=' '.join(central_air).replace('Central Air:</b></font></td><td><font face="Arial" size="5">','').strip()
    print(central_air)

    fireplace=re.findall('Fireplace:<\/b><\/font><\/td><td><font face="Arial" size="5">[^<>]*',str(soup))
    fireplace=' '.join(fireplace).replace('Fireplace:</b></font></td><td><font face="Arial" size="5">','').strip()
    print(fireplace)

    porch=re.findall(r'Porch:<\/b><\/font><\/td><td><font face="Arial" size="5">[^<>]*',str(soup))
    porch=' '.join(porch).replace('Porch:</b></font></td><td><font face="Arial" size="5">','').strip()
    print(porch)

  except:
    soup=''
    owner_name=''
    address1=''
    sub_division=''
    homesite=''
    p_class=''
    farm_acres=''
    open_space_acres=''
    total_acres=''
    values_2023=''
    legal_desc=''
    story=''
    year_build=''
    total_sqft=''
    bathrooms=''
    central_air=''
    fireplace=''
    porch=''

  row_dict = {
      'parcel_number':link2[i],
    'Property Address': address1,
      'owner_name':owner_name,
      'sub_division':sub_division,
      'homesite':homesite,
      'p_class':p_class,
      'farm_acres':farm_acres,
      'open_space_acres':open_space_acres,
      'total_acres':total_acres,
      'values_2023':values_2023,
      'legal_desc':legal_desc,
      'story':story,
      'year_build':year_build,
      'total_sqft':total_sqft,
      'bathrooms':bathrooms,
      'central_air':central_air,
      'fireplace':fireplace,
      'porch':porch

  }
  rows.append(row_dict)
  result_df = pd.DataFrame(rows)
  result_df.to_excel('will_balance1_2.xlsx', index=False)
  time.sleep(2)
