from math import pi


# Basic Arithmetic Functions

# adding
def addition(number1, number2):
    return number1 + number2


# subtracting
def subtraction(number1, number2):
    return number1 - number2


# multiplying
def multiplication(number1, number2):
    return number1 * number2


# dividing
def division(number1, number2):
    return number1 / number2


# modulus
def modulus(number1, number2):
    return number1 % number2


# power
def power(number1, number2):
    return number1 ** number2


# calculation
def calculation(number1, number2, operator):
    if operator == "+":
        return addition(number1, number2)
    elif operator == "-":
        return subtraction(number1, number2)
    elif operator == "*":
        return multiplication(number1, number2)
    elif operator == "/":
        return division(number1, number2)
    elif operator == "%":
        return modulus(number1, number2)
    elif operator == "^":
        return power(number1, number2)
    else:
        print("Wrong operator")


# Boundary Calculator Functions

# perimeter
def perimeter():
    width = int(input("Enter Width: "))
    height = int(input("Enter Height: "))
    return (width + height) * 2


# circumference
def circumference():
    radius = int(input("Enter Radius: "))
    return 2 * pi * radius


# Area Calculator Functions

# area (rectangle)
def area_rectangle():
    width = int(input("Enter Width: "))
    height = int(input("Enter Height: "))
    return width * height


# area (circle)
def area_circle():
    radius = int(input("Enter Radius: "))
    return pi * radius ** 2


# area (parallelogram)
def area_parallelogram():
    base = int(input("Enter Base Length: "))
    height = int(input("Enter Height: "))
    return base * height


# area (parallelogram)
def area_triangle():
    base = int(input("Enter Base Length: "))
    height = int(input("Enter Height: "))
    return (base * height) / 2


# area (parallelogram)
def area_trapezoid():
    base1 = int(input("Enter Base Length 1: "))
    base2 = int(input("Enter Base Length 2: "))
    height = int(input("Enter Height: "))
    return (base1 + base2) * height / 2


# area (prism)
def area_prism():
    width = int(input("Enter Base Width: "))
    length = int(input("Enter Base Length: "))
    height = int(input("Enter Height: "))
    return 2 * width * length + (width + length) * 2 * height


# area (pyramid)
def area_pyramid():
    width = int(input("Enter Base Width: "))
    length = int(input("Enter Base Length: "))
    slant = int(input("Enter Slant Height: "))
    return (width * length) + slant * (width + length)


# area (cylinder)
def area_cylinder():
    radius = int(input("Enter Radius: "))
    height = int(input("Enter Height: "))
    return (2 * pi * radius ** 2) + (2 * pi * radius * height)


# area (sphere)
def area_sphere():
    radius = int(input("Enter Radius: "))
    return 4 * pi * radius ** 2


# area (cone)
def area_cone():
    radius = int(input("Enter Radius: "))
    slant = int(input("Enter Slant Height: "))
    return (pi * radius ** 2) + (pi * radius * slant)


# Volume Calculator Functions

# volume (prism)
def volume_prism():
    width = int(input("Enter Base Width: "))
    length = int(input("Enter Base Length: "))
    height = int(input("Enter Height: "))
    return width * length * height


# volume (pyramid)
def volume_pyramid():
    return volume_prism() / 3


# volume (cylinder)
def volume_cylinder():
    base_area = area_circle()
    height = int(input("Enter Height: "))
    return base_area * height


# volume (sphere)
def volume_sphere():
    radius = int(input("Enter Radius: "))
    return 4 / 3 * (pi * radius ** 3)


# volume (cone)
def volume_cone():
    return volume_cylinder() / 3
