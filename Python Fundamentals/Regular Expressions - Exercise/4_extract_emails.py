import \
    re

sentence = input()
pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b'
result = re.findall(pattern, sentence)

for item in result:
    print(item[0])