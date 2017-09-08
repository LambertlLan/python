# __author: Lambert
# __date: 2017/9/8 14:02
import xml.etree.ElementTree as ET

tree = ET.parse('XML_test.xml')
root = tree.getroot()
# 查看数据
ET.dump(root)
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text, i.attrib)
# 修改数据

for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('update', 'yes')

tree.write('xml_test.xml')  # 名字一样会覆盖大小写不一样也会覆盖
