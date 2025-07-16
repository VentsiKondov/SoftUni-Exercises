from math import floor

record_seconds = float(input())
metres = float(input())
seconds_for_one_meter = float(input())
persons_seconds = metres * seconds_for_one_meter
slower = floor(metres / 15) * 12.5
finals_seconds = persons_seconds + slower
if finals_seconds < record_seconds:
    print(f'Yes, he succeeded! The new world record is {finals_seconds:.2f} seconds.')
else:
    print(f"No, he failed! He was {(finals_seconds-record_seconds):.2f} seconds slower.")