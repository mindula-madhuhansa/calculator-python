# adding
def addition(number1, number2):
    return number1 + number2


# subtracting
def subtraction(number1, number2):
    return number1 - number2;


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
        multiplication(number1, number2)
    elif operator == "/":
        return division(number1, number2)
    elif operator == "%":
        return modulus(number1, number2)
    elif operator == "^":
        return power(number1, number2)
    else:
        print("Wrong operator")
