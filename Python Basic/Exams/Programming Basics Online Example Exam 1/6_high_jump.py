centimeters_to_jump = int(input())

beginning = centimeters_to_jump - 30
number_failed_jumps = 0
total_jumps = 0

while True:
    person_jump = int(input())
    total_jumps += 1

    if person_jump > centimeters_to_jump and beginning >= centimeters_to_jump:
        print(f"Tihomir succeeded, he jumped over {beginning}cm after {total_jumps} jumps.")
        break

    elif person_jump > beginning:
        beginning += 5
        number_failed_jumps = 0

    else:
        number_failed_jumps += 1

    if number_failed_jumps == 3:
        print(f"Tihomir failed at {beginning}cm after {total_jumps} jumps.")
        break

