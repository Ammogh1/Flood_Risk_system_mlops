from docx import Document

def replace_in_doc(doc_path, new_doc_path, replacements):
    doc = Document(doc_path)
    for p in doc.paragraphs:
        for key, val in replacements.items():
            if key in p.text:
                # Try to replace in runs
                for run in p.runs:
                    if key in run.text:
                        run.text = run.text.replace(key, val)
                
                # If still in p.text after run replacements, fallback to replacing the whole paragraph text
                if key in p.text:
                    p.text = p.text.replace(key, val)
                    
    doc.save(new_doc_path)

if __name__ == '__main__':
    replacements = {
        "Driving Risk Prediction System": "Hybrid Flood Risk Prediction System",
        "Driving Risk": "Flood Risk",
        "driving-risk-system": "Flood_Risk_system_mlops",
        "driving-risk-app": "flood-risk-app",
        "deepankreddya": "ammogh1",
        "Random Forest, RNN, QSVC": "Machine Learning models, CNN, and Quantum VQC"
    }
    
    replace_in_doc("DevOps_MLOps_Tools_Report (1).docx", "Flood_Risk_MLOps_Tools_Report.docx", replacements)
    print("Document successfully modified and saved as Flood_Risk_MLOps_Tools_Report.docx")
