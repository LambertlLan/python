# __author: Lambert
# __date: 2017/9/8 14:38
import xml.etree.ElementTree as ET

new_xml = ET.Element('news')
time = ET.SubElement(new_xml, 'time', attrib={'encontroller': 'year'})
content = ET.SubElement(new_xml, 'content', attrib={'update': 'no'})
year = ET.SubElement(time, 'year')
year.text = '2017'
month = ET.SubElement(time, 'month')
month.text = '09'
day = ET.SubElement(time, 'day')
day.text = '08'

et = ET.ElementTree(new_xml)

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式
