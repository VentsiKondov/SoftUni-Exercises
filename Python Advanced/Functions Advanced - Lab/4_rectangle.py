def rectangle(a,b):
    if type(a) == int and type(b) == int:
        def area():
            return a * b
        def perimeter():
            return 2 * a + 2 * b
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    else:
        return "Enter valid values!"

print(rectangle(2, 10))
print(rectangle('2', 10))