import \
    re

line = input()

while line:
    result = re.findall('\d+', line)
    if result:
        print(' '.join(result), end=' ')
    line = input()