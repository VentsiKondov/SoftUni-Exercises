def pass_validation(password):
    digit_count = 0
    letter_count = 0
    not_letter_count = 0
    is_valid = False
    if not 6<=len(password)<=10:
        print('Password must be between 6 and 10 characters')
    for char in password:
        if char.isdigit():
            digit_count += 1
            is_valid = True
        elif char.isalpha():
            letter_count += 1
        else:
            is_valid = False
            not_letter_count += 1
            if not_letter_count == 1:
                print("Password must consist only of letters and digits")

    if digit_count < 2:
        print('Password must contain at least 2 digits')
        is_valid = False
    if is_valid:
        print('Password is valid')

password = input('Enter password: ')
pass_validation(password)
