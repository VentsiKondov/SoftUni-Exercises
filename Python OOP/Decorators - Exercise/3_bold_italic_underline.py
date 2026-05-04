def make_bold(func):
    def wrapper(*text):
        return f'<b>{func(*text)}</b>'

    return wrapper

def make_italic(func):
    def wrapper(*text):
        return f'<i>{func(*text)}</i>'
    return wrapper

def make_underline(func):
    def wrapper(*text):
        return f'<u>{func(*text)}</u>'
    return wrapper

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

