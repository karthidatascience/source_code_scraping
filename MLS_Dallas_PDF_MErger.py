import re
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import unquote
from PyPDF2 import PdfMerger
from PyPDF2 import PdfWriter, PdfReader
import os


# file_path = r"C:\Users\karthim\Downloads\dallas_merger.xlsx"
# df = pd.read_excel(file_path)
list1=['https://www.dallascad.org/AppraisalRecord.aspx?ID=005455000T0420000&Pin=8VA3JC']
for i in list1:
    url = f'{i}'
    # print(url)
    try:
        page1 = requests.get(url)
        soup2 = BeautifulSoup(page1.content, 'html.parser')
        accno=soup2.find('span',id='lblTitle')
        if accno is not None:
            accno = accno.text.replace('Appraisal Record for Acct', '')
            if not os.path.exists(accno):
              os.mkdir(accno)
            print(accno)
            all_urls = soup2.find_all('a')

            pdf_files = []
        # print(all_urls)
            for url in all_urls:
              name=url.text
              try:
                  if 'PDF' in url['href']:
                    pdf_url = ''
                    if 'https' not in url['href']:
                      pdf_url = 'https://www.dallascad.org/' + url['href']
                    else:
                      pdf_url = url['href']
                    # print(f'{name}', pdf_url)

                    pdf_response = requests.get(pdf_url)
                    filename = unquote(name)
                    with open(os.path.join(accno, f"{filename}.pdf"), "wb") as outputStream:
                      outputStream.write(pdf_response.content)
                      pdf_files.append(os.path.join(accno, f"{filename}.pdf"))
              except Exception as e:
                  print(f"An error occurred while downloading PDF file for {name}: {e}")
            try:
                merger = PdfMerger()
                for pdf in pdf_files:
                    merger.append(pdf)
                with open(os.path.join(accno, f'{accno}.pdf'), 'wb') as output_file:
                    merger.write(output_file)
            except Exception as e:
                print(f"An error occurred while merging PDF files for {accno}: {e}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while requesting {url}: {e}")

    time.sleep(3)



