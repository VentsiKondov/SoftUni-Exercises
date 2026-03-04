def get_info(**info):
    name,town,age = info['name'],info['town'],info['age']
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))