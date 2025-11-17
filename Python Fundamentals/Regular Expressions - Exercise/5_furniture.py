import \
    re

command = input()
pattern = r'>>([A-z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)'


bought_items = []
total_sum = 0

while command != 'Purchase':
    result = re.search(pattern, command)
    if result:
        name,price,quantity = result.groups()
        total_sum += int(quantity) * float(price)
        bought_items.append(name)


    command = input()

print('Bought furniture:')
if bought_items:
    print('\n'.join(bought_items))
print(f'Total money spend: {total_sum:.2f}')