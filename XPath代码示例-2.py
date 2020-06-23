from lxml import etree

html = etree.parse('./test.html' , etree.HTMLParser())
result = html.xpath('//li')
print(result)
print(result[0])          #提取到的结果是列表，用[0]索引