# my_dictionary = {"shards":0, "fragments":0, "motes":0}
# items = input().split()
# obtained = False
# while not obtained:
#     for i in range(0, len(items), 2):
#         value = int(items[i])
#         key = items[i + 1].lower()
#         if key not in my_dictionary:
#             my_dictionary[key] = 0
#         my_dictionary[key] += value
#         if my_dictionary["shards"] >= 250:
#             obtained = True
#             my_dictionary["shards"] -= 250
#             print("Shadowmourne obtained!")
#         elif my_dictionary["fragments"] >= 250:
#             obtained = True
#             my_dictionary["fragments"] -= 250
#             print("Valanyr obtained!")
#         elif my_dictionary["motes"] >= 250:
#             obtained = True
#             my_dictionary["motes"] -= 250
#             print("Dragonwrath obtained!")
#         if obtained:
#             break
#     if obtained:
#         break
#
# for key, value in my_dictionary.items():
#     print(f'{key}:{value}')
#

my_dictionary = {"shards":0, "fragments":0, "motes":0}

FRAGMENTS_FOR_VALANYR = 250
MOTES_FOR_DRAGONWRATH= 250
SHARDS_FOR_SHADOWMOURNE = 250


new_items = []
while True:
    try:
        items = input().split()
        new_items.extend(items)
    except EOFError:
        break




def elements(items, my_dictionary):
    message = ''
    for index in range(0, len(items), 2):
        value = int(items[index])
        item = items[index+1].lower()
        my_dictionary[item] = my_dictionary.get(item, 0) + value
        if my_dictionary['shards'] >= SHARDS_FOR_SHADOWMOURNE:
            my_dictionary['shards'] -= SHARDS_FOR_SHADOWMOURNE
            message ="Shadowmourne obtained!"
            break
        elif my_dictionary['fragments'] >= FRAGMENTS_FOR_VALANYR:
            my_dictionary['fragments'] -= FRAGMENTS_FOR_VALANYR
            message = "Valanyr obtained!"
            break
        elif my_dictionary['motes'] >= MOTES_FOR_DRAGONWRATH:
            my_dictionary['motes'] -= MOTES_FOR_DRAGONWRATH
            message = "Dragonwrath obtained!"
            break
    return message, my_dictionary

text, my_dictionary = elements(new_items, my_dictionary)
print(text)
for key, value in my_dictionary.items():
    print(f"{key}: {value}")































# list_with_items = input().split()
# digit_lst = []
# items_lst =[]
# junk_dict ={}
# wrong_names = []
# wrong_values = []
# num = 0
# dragonwrath = False
# shadowmourne = False
# valanyr = False
#
# for item in list_with_items:
#     if item.isdigit():
#         digit_lst.append(int(item))
#     else:
#         if item.lower() == "motes":
#             items_lst.append(item.lower())
#             if digit_lst[-1] >= 250:
#                 digit_lst[-1] -= 250
#                 dragonwrath = True
#         elif item.lower() == "shards":
#             items_lst.append(item.lower())
#             if digit_lst[-1] >= 250:
#                 digit_lst[-1] -= 250
#                 shadowmourne = True
#         elif item.lower() == "fragments":
#             items_lst.append(item.lower())
#             if digit_lst[-1] >= 250:
#                 digit_lst[-1] -= 250
#                 valanyr = True
#         else:
#             wrong_names.append(item)
#             wrong_values.append(digit_lst[-1])
#             digit_lst.pop()


# # my_dictionary = {items_lst[i]: digit_lst[i] for i in range(len(list_with_items))}
# zipped = zip(digit_lst, items_lst)
# wrong_zipped = zip(wrong_values, wrong_names)
# junk_dict = {k:v for (v,k) in wrong_zipped}
# my_dict = {k:v for (v,k) in zipped}
#
# print(my_dict)
# print(junk_dict)
#
# if valanyr:
#     print("Valanyr obtained!")
#     for k, v in my_dict.items():
#         print(f'{k.lower()}: {v}')
# elif shadowmourne:
#     print("Shadowmourne obtained!")
#     for k, v in my_dict.items():
#         print(f'{k.lower()}: {v}')
# elif dragonwrath:
#     print("Dragonwrath obtained!")
#     for k, v in my_dict.items():
#         print(f'{k.lower()}: {v}')
#
# for k, v in junk_dict.items():
#     print(f'{k}: {v}')





