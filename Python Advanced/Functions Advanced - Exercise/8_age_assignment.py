def age_assignment(*names, **kwargs):
    result = []
    for name in names:
        for key in kwargs:
            if name.startswith(key):
                result.append(f"{name} is {kwargs[key]} years old.")
    return "\n".join(sorted(result))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))