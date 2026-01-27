number_of_guests = int(input())

lst_with_reservations = set()

for _ in range(number_of_guests):
    reservation_code = input()
    lst_with_reservations.add(reservation_code)

while True:
    reservation_code = input()
    if reservation_code == "END":
        break
    if reservation_code in lst_with_reservations:
        lst_with_reservations.remove(reservation_code)

print(len(lst_with_reservations))
sorted_lst = sorted(lst_with_reservations)
[print(reservation_code) for reservation_code in sorted_lst]