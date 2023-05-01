import operations

print("*** Simple Calculator ***")
print()
isCalculating = True
isChoosing = True

while isChoosing:
    print("Enter calculator type:")
    print("\tArithmetic Calculator: 1")
    print("\tSecondary Calculator: 2")
    print()

    calc_option = input("Select the calculator: ")
    print()

    if calc_option == "1":
        while isCalculating:
            number1 = int(input("Enter number 1: "))
            number2 = int(input("Enter number 2: "))

            operator = input("Enter the operator: ")

            if operator == "~":
                print("Going back...")
                print()
                isCalculating = False
            else:
                answer = operations.calculation(number1, number2, operator)
                print(number1, operator, number2, "=", answer)
                print()

    elif calc_option == "2":
        while isCalculating:
            print("Select an option:")
            print("\tFind perimeter: 1")
            print("\tFind area: 2")
            print("\tFind circumference: 3")
            print("\tFind area(circle): 4")
            print()

            choice = input("Enter the Choice: ")

            if choice == "~":
                print("Going back...")
                print()
                isCalculating = False
            elif choice == "1":
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                answer = operations.perimeter(width, height)
                print("Perimeter of the rectangle =", answer)
                print()
            elif choice == "2":
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                answer = operations.area_rect(width, height)
                print("Area of the rectangle =", answer)
                print()
            elif choice == "3":
                radius = int(input("Enter radius: "))
                answer = operations.circumference(radius)
                print("Circumference of the circle =", answer)
                print()
            elif choice == "4":
                radius = int(input("Enter radius: "))
                answer = operations.area_circle(radius)
                print("Area of the circle =", answer)
                print()

    elif calc_option == "~":
        print("Simple calculator stopped")
        isChoosing = False
