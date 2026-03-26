import zipfile
import re

def extract(docx_path):
    with zipfile.ZipFile(docx_path) as docx:
        xml_content = docx.read('word/document.xml').decode('utf-8')
        texts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml_content)
        print('\n'.join(texts))
        
        try:
            rels_content = docx.read('word/_rels/document.xml.rels').decode('utf-8')
            rels = re.findall(r'Target="(.*?)" TargetMode="External"', rels_content)
            print("\n--- LINKS ---")
            for r in rels:
                print(r)
        except Exception as e:
            print("rels error", e)

extract(r'c:\Users\WELCOME\Desktop\portfoliooo\Shivam Sharma LCV4.docx')
