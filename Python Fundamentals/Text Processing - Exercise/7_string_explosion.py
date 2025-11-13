text = input().strip()

power = 0
result = []

i = 0
while i < len(text):
    ch = text[i]

    if ch == '>':
        result.append('>')

        power += int(text[i + 1])
    else:
        if power > 0:
            power -= 1
        else:
            result.append(ch)

    i += 1

print(''.join(result))
