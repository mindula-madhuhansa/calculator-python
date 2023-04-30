import operations

print("*** Simple Calculator ***")
isCalculating = True

while isCalculating:
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))

    operator = input("Enter the operator: ")
    if operator == "~" or number1 == "~" or number2 == "~":
        print("The calculating process stopped")
        isCalculating = False
    else:
        answer = operations.calculation(number1, number2, operator)
        print(number1, operator, number2, "=", answer)
        print()


