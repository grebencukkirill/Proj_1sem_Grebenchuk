import re

with open('text.txt') as file1:
    lines = file1.readlines()
text = ''
for line in lines:
    text += line + '\n'
p1 = re.compile(r'\b\d+\b|\b\w*\d+\w*\b')
p2 = re.compile(r'\b[A-ЯA-Z]+\b|\b[A-ЯA-Z]+[а-яa-z]*[A-ЯA-Z]+\b')
p3 = re.compile(r'\b\w*[а-яА-Я]+\d\w*\b')
p4 = re.compile(r'\b[А-ЯA-Z]\w*\b')
p5 = re.compile(r'\b[аеёиоуыэюяАЕЁИОУЫЭЮЯ]\w*\b')
p6 = re.compile(r'(?<!\b)\d+(?!\b)')
p7 = re.compile(r'^.*\*.*$')
p8 = re.compile(r'^.*\(.*$.*\)|^.*\(.*\).*$')
p9 = re.compile(r'<(\w+)[^>]*>(.*?)<\/\1>')
p10 = re.compile(r'>([^<]+)<')
p11 = re.compile(r'^\s*$')
p12 = re.compile(r'<[^>]+>')

print(re.findall(p1, text))
print(re.findall(p2, text))
print(re.findall(p3, text))
print(re.findall(p4, text))
print(re.findall(p5, text))
print(re.findall(p6, text))
print(re.findall(p7, text))
print(re.findall(p8, text))
print(re.findall(p9, text))
print(re.findall(p10, text))
print(re.findall(p11, text))
print(re.findall(p12, text))

