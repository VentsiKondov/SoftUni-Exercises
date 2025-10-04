def factorial(n1,n2):
    sum1 = 1
    sum2 = 1
    for i in range(1, n1 + 1 ):
        sum1 *= i
    for i in range(1, n2 + 1 ):
        sum2 *= i
    division = f"{sum1/sum2:.2f}"
    return division

number1= int(input())
number2 = int(input())
print(factorial(number1, number2))



