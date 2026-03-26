import zipfile, re
def extract(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read('word/document.xml').decode('utf-8')
        text = re.sub(r'<[^>]+>', '', xml)
        print(text)
        try:
            rels_content = z.read('word/_rels/document.xml.rels').decode('utf-8')
            rels = re.findall(r'Target="(.*?)" TargetMode="External"', rels_content)
            print("\n--- LINKS ---")
            for r in rels: print(r)
        except Exception as e: pass

extract(r'c:\Users\WELCOME\Desktop\portfoliooo\Shivam Sharma LCV4.docx')
