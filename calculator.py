import operations

print("*** Simple Calculator ***")
isCalculating = True

print("Enter calculator type:")
print("\tStandard Calculator: 1")
print("\tScientific Calculator: 2")
print()

while isCalculating:
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))

    operator = input("Enter the operator: ")
    if operator == "~":
        print("The calculating process stopped")
        isCalculating = False
    else:
        answer = operations.calculation(number1, number2, operator)
        print(number1, operator, number2, "=", answer)
        print()


