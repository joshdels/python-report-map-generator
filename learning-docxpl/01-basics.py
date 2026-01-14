from docxtpl import DocxTemplate
import sys

try:
    doc = DocxTemplate("template.docx")

    context = {
        "date": "January 9, 2026",
        "lessor": {
            "name": "Monica S. Dela Cruz",
            "address": "Brgy. New Pandan, Davao City"
        },
        "rent": 15000,
        "has_penalty": False
    }

    doc.render(context)
    doc.save("../results/output.docx")
    
    print("Document generated succesfully")
    
except Exception as e:
    print("Failed to generate document", e, file=sys.stderr)