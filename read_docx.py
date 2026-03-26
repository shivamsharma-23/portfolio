import zipfile
import xml.etree.ElementTree as ET

def extract(docx_path):
    with zipfile.ZipFile(docx_path) as docx:
        xml_content = docx.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [t.text for t in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
            if texts:
                print(''.join(texts))
        
        try:
            rels_content = docx.read('word/_rels/document.xml.rels')
            rels = ET.fromstring(rels_content)
            print("\n--- LINKS ---")
            for r in rels.iter('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                if r.get('TargetMode') == 'External':
                    print(r.get('Target'))
        except Exception:
            pass

extract(r'c:\Users\WELCOME\Desktop\portfoliooo\Shivam Sharma LCV4.docx')
