import re
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

rows = []

url1 = 'https://www.naics.com/everything-sic/'
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.content, 'html.parser')
s1 = soup1.find_all('table', class_='table table-striped twodigit')

for table in s1:
    rows1 = table.find_all('tr')
    for row1 in rows1:
        columns1 = row1.find_all('td', class_='first_child')

        if columns1:
            for k in columns1:
                k1 = re.findall(
                    r'<td class="first_child"><a href="https:\/\/www\.naics\.com\/sic-codes-counts-division\/\?div=[^<>]*\>[^<>]*',
                    str(k))

                if k1:
                    s1 = ''.join(k1)
                    name = s1.split('">')[2]
                    url2 = s1.split('">')[1].replace('<a href="', '').strip()
                    print(url2)

                    r2 = requests.get(url2)
                    soup2 = BeautifulSoup(r2.content, 'html.parser')
                    s3 = soup2.find_all('table', class_='table table-striped')

                    for table1 in s3:
                        rows2 = table1.find_all('tr')
                        for row2 in rows2:
                            columns2 = row2.find_all('td', class_='first_child')
                            if columns2:
                                unique_links = set()
                                for l in columns2:
                                    links = l.find_all('a', href=True)
                                    for link in links:
                                        href_value = link['href']
                                        if href_value not in unique_links:
                                            unique_links.add(href_value)
                                            print(href_value)
                                            r3 = requests.get(href_value)
                                            soup3 = BeautifulSoup(r3.content, 'html.parser')
                                            k5 = soup3.find_all('table', class_='table table-striped')
                                            for table2 in k5:
                                                rows3 = table2.find_all('tr')
                                                for row3 in rows3:
                                                    columns3 = row3.find_all('td', class_='first_child')
                                                    if columns3:
                                                        # print(columns3)
                                                        unique_links1 = set()
                                                        for l1 in columns3:
                                                            links1 = l1.find_all('a', href=True)
                                                            for link_ in links1:
                                                                href_value1 = link_['href']
                                                                if href_value1 not in unique_links1:
                                                                    unique_links1.add(href_value1)
                                                                    print(href_value1)
                                                                    r4 = requests.get(href_value1)
                                                                    soup4 = BeautifulSoup(r4.content, 'html.parser')
                                                                    k6 = soup4.find_all('table',
                                                                                        class_='table table-striped')
                                                                    for table3 in k6:
                                                                        rows_ = table3.find_all('tr')
                                                                        for row3_ in rows_:
                                                                            columns4 = row3_.find_all('td',
                                                                                                     class_='first_child')
                                                                            if columns4:
                                                                                print(columns4)
                                                                            row_dict = {
                                                                                'name': name,
                                                                                'url2': url2,
                                                                                'href_value': href_value,
                                                                                'columns1': columns1,
                                                                                'columns2': columns2,
                                                                                'columns3': columns3,
                                                                                'columns4':columns4
                                                                            }
                                                                            rows.append(row_dict)
                                                                            result_df = pd.DataFrame(rows)
                                                                            result_df.to_excel('SIC1.xlsx', index=False)
