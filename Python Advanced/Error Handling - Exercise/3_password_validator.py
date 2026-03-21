class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass

special_characters = '@*&%'

while True:
    command = input()
    if command == "Done":
        break

    password = command
    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")
    if all(x.isdigit() for x in password) or all(x.isalpha() for x in password) or all(x in special_characters for x in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")
    if not any(s in special_characters for s in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")


    if any(s.isspace() for s in password):
        raise PasswordContainsSpacesError("Password must not contain empty spaces")
    print("Password is valid")
