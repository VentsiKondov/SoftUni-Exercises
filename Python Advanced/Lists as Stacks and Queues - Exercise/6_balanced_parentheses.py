

parentheses = input()
open_parenthesis = []

for pr in parentheses:
    if pr in '{[(':
        open_parenthesis.append(pr)
    elif pr in "}])":
        if not open_parenthesis:
            print('NO')
            exit()
        if f"{open_parenthesis[-1]+ pr }" in  "{}[]()":
            open_parenthesis.pop()
        else:
            print("NO")
            exit()

print("YES")

