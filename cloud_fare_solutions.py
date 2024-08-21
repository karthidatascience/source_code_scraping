from time import sleep
from DrissionPage import ChromiumPage,ChromiumOptions

try:
    options = ChromiumOptions()
    driver=ChromiumPage(options)
    driver.get('https://wheatlandassessor.com/ParcelSearch/SD/WLT/AssessorDB/Search.aspx')
    sleep(120)
    i=driver.get_frame('@src^https://challanges.cloudflare.com/cdn-cgi')
    if i:
        e=i('.mark')
        e.click()
    sleep(20)
    driver.quit()
except:
    driver.quit()

