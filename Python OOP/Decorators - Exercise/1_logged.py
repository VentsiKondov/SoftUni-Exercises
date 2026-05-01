def logged(func):

    def wrapper(*args):
        f_name = func.__name__
        joined_args = ", ".join(str(arg) for arg in args)
        return (f"you called {f_name}({joined_args})\n"
                f"it returned {func(*args)}")
    return wrapper



@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
