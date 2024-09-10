import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://connectmls.mredllc.com/")
    page.get_by_role("button", name="MRED MEMBERS Click here").click()
    time.sleep(3)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("1011567")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("uverlgxnrib")
    # time.sleep(3)
    page.get_by_role("button", name="LOGIN").click()
    # time.sleep(3)
    time.sleep(40)
    list1=['12050241','11818998','11893692','11924377','11921428','11935121','11945344','11933881','11948571','11959013','11966130','11974039','11963890','12024305','12035317','12031809','12029315','12037763','12022380','12038596','12033050','12036823','12037374','12035015','12037780','12037245','12038460','12042779','12022283','12027857','12039671','12021741','12038222','12030665','12047951','12050199','12041033','12042429','12043443','12054189','12058616','12050433','12044120','12041285','12058611','12055481','12056378','12059720','12057097','12059729','12052168','12048620','12059860','12040878','12043991','12043799','12048950','12047582','12056158','12054997','12048093','12043538','12059437','12058361','12059008','12057499','12050863','12065583','12050988','12040783','12041992','12050627','12053808','12056908','12047691','12039581','12041740','12058031','12056787','12058035','12055006','12059495','12056267','12057402','12060461','12076272','12062274','12069633','12070033','12072354','12070974','12078668','12069274','12073101','12070112','12080056','12062131','12065313','12068774']
    for i in list1:
        print(i)
        start_time = time.time()

        input_field = page.locator('xpath=//*[@id="input-0"]')
        time.sleep(10)
        input_field.fill(f'{i}')
        time.sleep(5)
        input_field.press("Enter")
        time.sleep(15)
        page.get_by_role("button", name="Print listings or Save as PDF").click()
        time.sleep(5)

        page.locator("#dcModal button").filter(has_text="Save as PDF").click()
        time.sleep(15)

        with page.expect_download() as download_info:
            page.frame_locator("iframe[name=\"print_listings_frame\"]").get_by_role("link", name="click here").click()
            time.sleep(10)

        download = download_info.value
        download.save_as(f'{i}.pdf')
        time.sleep(2)
        page.get_by_text("Cancel").click()
        end_time = time.time()  # End timing for the current item
        elapsed_time = end_time - start_time  # Calculate the time taken
        print(f"Completed {i} in {elapsed_time:.2f} seconds")




    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
