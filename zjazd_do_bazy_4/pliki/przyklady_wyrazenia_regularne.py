import re

with open("dane/input.txt") as f:
    data = f.read()
    pattern_mail = re.compile("\w+.\w.@\w+.\.\w+")
    pattern_kod_po = re.compile("\d{2}-\d{3}")
    pattern_dat = re.compile("\d{2} \w+ \d{4}")

    print(pattern_mail.findall(data))
    print(pattern_kod_po.findall(data))
    print(pattern_dat.findall(data))

# text = "122-22-222 312-512-265"
#
# print(pattern.findall(text))
