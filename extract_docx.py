from docx import Document
import sys

def extract_text(filename):
    try:
        doc = Document(filename)
        text = []
        for p in doc.paragraphs:
            text.append(p.text)
        with open('extracted_report.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(text))
        print("Extraction complete.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    extract_text("DevOps_MLOps_Tools_Report (1).docx")
