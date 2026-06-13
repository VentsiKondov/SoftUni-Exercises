def get_primes(list_of_numbers):
    for num in list_of_numbers:
        if num <= 1:
            continue

        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            yield num

print(list(get_primes([-2, 0, 0, 1, 1, 0])))