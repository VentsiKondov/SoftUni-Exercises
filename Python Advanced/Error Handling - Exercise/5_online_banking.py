pin,balance,age = [int(x) for x in input().split(", ")]


class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


while True:
    command = input()
    if command == "End":
        break
    information = command.split("#")
    if information[0] == "Send Money":
        money_to_send = int(information[1])
        pin_code = int(information[2])
        if money_to_send > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin_code != pin:
            raise PINCodeError("Invalid PIN code")
        if age < 18:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        print(f"Successfully sent {money_to_send:.2f} money to a friend")
        print(f"There is {balance - money_to_send:.2f} money left in the bank account")
    elif information[0] == "Receive Money":
        money_to_receive = int(information[1])
        if money_to_receive < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        print(f"{money_to_receive/2:.2f} money went straight into the bank account")