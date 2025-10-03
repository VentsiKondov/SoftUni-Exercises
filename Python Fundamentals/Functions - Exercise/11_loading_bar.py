def loading_bar(number):
    percentage = int(number / 10)
    points =  int(10 - percentage)
    if percentage == 10:
        print(f'{number}% Complete! \n[%%%%%%%%%%]')
    else:
        print(f'{number}% [{percentage * "%"}{points*"."}] \nStill loading...')

number =int(input())
loading_bar(number)