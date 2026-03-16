def grocery_store(**grocery_text):
    sorted_grocery_text = sorted(grocery_text.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

    return "\n".join(f"{k}: {v}" for k, v in sorted_grocery_text)





print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))








