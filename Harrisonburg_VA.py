from PyPDF2 import PdfReader
import re
import pdfplumber

# File paths
pdf_path = r"C:\Users\karthim\Downloads\va500_.pdf"
output_txt_path = r"C:\Users\karthim\Downloads\va500_.txt"

# Open output file
with open(output_txt_path, 'w', encoding='utf-8') as output_file:
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""

        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

        try:
            sections = full_text.split("------------------------------------------------------------------------------------------------------------------------------")
            if len(sections) > 1:
                sections = sections[1:-1]  # Remove first and last empty sections

            for idx, section in enumerate(sections):
                lines = section.splitlines()

                if len(lines) < 5:  # Ensure enough lines exist before processing
                    continue

                line = lines[1]
                words = line.split()

                if len(words) < 7:  # Ensure minimum elements exist in the line
                    continue

                total, impr, land, code = words[-1], words[-2], words[-3], words[-4]
                ac3, ac2, ac1 = words[-5], words[-6], words[-7]

                # Extract address
                address_match = re.split(r' \d{3} ', line)
                address = address_match[0] if address_match else "Unknown"

                street = lines[3]
                street_parts = street.split()
                st1 = street_parts[-1] if street_parts else "Unknown"
                st2 = " ".join(street_parts[:-1]) if street_parts else "Unknown"

                # Construct output row
                output_row = f"{total}|{impr}|{land}|{code}|{ac1}|{ac2}|{ac3}|{address}|{st1}|{st2}|{lines[2]}|{lines[4]}"
                print(output_row)

                # Write to file
                output_file.write(output_row + '\n')

        except Exception as e:
            print(f"Error processing PDF: {e}")
