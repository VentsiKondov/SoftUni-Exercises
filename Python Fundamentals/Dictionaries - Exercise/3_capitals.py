lst_of_countries = input().split(", ")
lst_of_cities = input().split(", ")

# my_dictionary = {key:value for key, value in zip(lst_of_countries, lst_of_cities)}
#
# for key, value in my_dictionary.items():
#     print(f'{key} -> {value}')

for index in range(0, len(lst_of_countries)):
    print(f'{lst_of_countries[index]} -> {lst_of_cities[index]}')