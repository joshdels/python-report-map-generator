from docxtpl import DocxTemplate
import os

# Load template
template_path = "./templates/template.docx"
doc = DocxTemplate(template_path)

# Context for Jinja
context = {
    "lessor": {
        "name": "MONICA S. DELA CRUZ",
        "address": "Brgy. New Pandan, Davao City, Philippines",
        "id": "SSD ID No.0X-123123123-X"
    },
    "lessee": {
        "name": "JOSHUA S. DE LEON",
        "address": "Brgy. Visayan Village, Tagum City, Philippines",
        "id": "PRC REG. NO.X00232322X"
    },
    "property": {
        "name": "Lucky 7, Doors Apartment",
        "location": "Purok 5, Camelia Homes Subd",
        "license": "TCT No. 100-X01505000"
    },
    "rent": {
        "cost_num": 6000,
        "cost_string": "six thousand",
        "start_date": "October 4, 2025"
    },
    "house_rules": [
        "That the LESSOR shall not be liable for any damage by caused by or any damage arising from the failure of the water supply and or electricity installment or the bursting leaking or running of any wash pipes, rain water or water closet and the the LESSOR shall not be liable",
        "No Pets Allowed inside the apartment",
        "The LESSEE shall not sublease the apartment without the written consent of the LESSOR;",
        "No illegal activities shall be conducted within the premises",
        "That the LESSEE hereby acknowledge that space in good tenable condition and hereby aggress"
    ]
}

try:
    doc.render(context)

    # Save output
    output_path = "../results/lease_docxtpl.docx"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
    print(f"File saved at {output_path}")

except Exception as e:
    print(f"Failed to create document: {e}")
