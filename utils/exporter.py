import json
import dicttoxml

def export_results(results, format_: str, filename: str):
    if format_.lower() == 'json':
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, default=str, ensure_ascii=False)
    elif format_.lower() == 'xml':
        with open(filename, 'wb') as f:
            xml_data = dicttoxml.dicttoxml(results)
            f.write(xml_data)
