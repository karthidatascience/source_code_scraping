import os
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time
import base64


def save_blob_content(page, blob_url, download_path):
    content = page.evaluate("""
        (blobUrl) => {
            return fetch(blobUrl).then(response => response.blob()).then(blob => {
                return new Promise((resolve, reject) => {
                    const reader = new FileReader();
                    reader.onloadend = () => resolve(reader.result);
                    reader.onerror = reject;
                    reader.readAsDataURL(blob);
                });
            });
        }
    """, blob_url)

    base64_content = content.split(',')[1]
    binary_content = base64.b64decode(base64_content)

    with open(download_path, 'wb') as f:
        f.write(binary_content)
    print(f"File downloaded and saved at: {download_path}")


def run(playwright, download_dir):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    try:
        page.goto("https://agentappeals.comalad.org/Account/Login")

        page.fill('input[placeholder="Email Address *"]', 'edocs@poconnor.com')
        page.fill('input[placeholder="Password *"]', 'Oconnor1234*')
        page.click('#login-btn')

        time.sleep(60)

        page.click('a.nav-link[title="Appeal Summary"]')
        time.sleep(60)

        list1 = ['42966','24319','138638']
        for k in list1:
            page.get_by_placeholder("Property ID").click()
            page.get_by_placeholder("Property ID").fill(f"{k}")
            page.get_by_role("button", name="Search").click()
            time.sleep(10)

            try:
                page.click("td.text-center.align-middle >> a.uploadCadDocument")
                time.sleep(10)

                pdf_names = [row.query_selector('td:nth-child(1)').inner_text().strip() for row in
                             page.query_selector_all('#cadDocDetails tr')]

                pdf_icon_selector = 'tr td i.fa-solid.fa-file-pdf'
                pdf_links = page.query_selector_all(pdf_icon_selector)

                for i, pdf_link in enumerate(pdf_links):
                    with context.expect_page() as new_page_info:
                        pdf_link.click()
                        time.sleep(13)

                    new_page = new_page_info.value
                    new_page.wait_for_load_state('networkidle')

                    time.sleep(3)
                    blob_url = new_page.url

                    if pdf_names and len(pdf_names) > i:
                        pdf_name = pdf_names[i]
                    else:
                        pdf_name = f"downloaded_file_{i}"

                    download_path = os.path.join(download_dir, f'{k}--{pdf_name}.pdf')
                    save_blob_content(new_page, blob_url, download_path)

                    new_page.close()

                close_button_selector = "button.btn-close.btnClose[data-bs-dismiss='modal'][aria-label='Close']"
                page.click(close_button_selector)

            except PlaywrightTimeoutError as e:
                print(f"Timeout error occurred for Quick Ref ID {k}: {e}")

    except PlaywrightTimeoutError as e:
        print(f"Timeout error occurred: {e}")

    finally:
        browser.close()


custom_download_dir = r"C:\Users\karthim\Downloads\Download_pdfs"
os.makedirs(custom_download_dir, exist_ok=True)

with sync_playwright() as playwright:
    run(playwright, custom_download_dir)
