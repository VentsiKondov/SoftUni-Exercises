from collections import \
    deque

customers = deque()

while True:
    line = input()
    if line == 'End':
        break
    if line == "Paid":

        for c in range(len(customers)):
            current_customer = customers.popleft()
            print(current_customer)
        continue
    customers.append(line)
print(f'{len(customers)} people remaining.')