import operations

print("*** Simple Calculator ***")
print()
isCalculating = True
isChoosing = True

while isChoosing:
    print("Enter calculator type:")
    print("\tArithmetic Calculator:\t 1")
    print("\tBoundary Calculator:\t 2")
    print("\tArea Calculator:\t\t 3")
    print("\tVolume Calculator:\t\t 4")
    print()

    calc_option = input("Select the calculator: ")
    print()

    if calc_option == "1":
        while isCalculating:
            number1 = int(input("Enter number 1: "))
            number2 = int(input("Enter number 2: "))

            operator = input("Enter the operator: ")

            if operator == "~":
                print()
                print("Going back...")
                print()
                isCalculating = False
            else:
                answer = operations.calculation(number1, number2, operator)
                print(number1, operator, number2, "=", answer)
                print()

        isCalculating = True

    elif calc_option == "2":
        while isCalculating:
            print("Select an option:")
            print("\tFind perimeter of Rectangle: 1")
            print("\tFind circumference of Circle: 2")
            print()

            choice = input("Enter the Choice: ")
            print()

            if choice == "~":
                print()
                print("Going back...")
                print()
                isCalculating = False
            elif choice == "1":
                answer = operations.perimeter()
                print("Perimeter of the Rectangle =", answer)
                print()
            elif choice == "2":
                answer = operations.circumference()
                print("Circumference of the Circle =", answer)
                print()

        isCalculating = True

    elif calc_option == "3":
        while isCalculating:
            print("Select an option:")
            print("\tFind area of Rectangle:\t\t 01")
            print("\tFind area of Circle:\t\t 02")
            print("\tFind area of Parallelogram:\t 03")
            print("\tFind area of Triangle:\t\t 04")
            print("\tFind area of Trapezoid:\t\t 05")
            print("\tFind area of Prism:\t\t\t 06")
            print("\tFind area of Pyramid:\t\t 07")
            print("\tFind area of Cylinder:\t\t 08")
            print("\tFind area of Sphere:\t\t 09")
            print("\tFind area of Cone:\t\t\t 10")
            print()

            choice = input("Enter the Choice: ")
            print()

            if choice == "~":
                print()
                print("Going back...")
                print()
                isCalculating = False
            elif choice == "1" or choice == "01":
                answer = operations.area_rectangle()
                print("Area of the Rectangle =", answer)
                print()
            elif choice == "2" or choice == "02":
                answer = operations.area_circle()
                print("Area of the Circle =", answer)
                print()
            elif choice == "3" or choice == "03":
                answer = operations.area_parallelogram()
                print("Area of the Parallelogram =", answer)
                print()
            elif choice == "4" or choice == "04":
                answer = operations.area_triangle()
                print("Area of the Triangle =", answer)
                print()
            elif choice == "5" or choice == "05":
                answer = operations.area_trapezoid()
                print("Area of the Trapezoid =", answer)
                print()
            elif choice == "6" or choice == "06":
                answer = operations.area_prism()
                print("Area of the Prism =", answer)
                print()
            elif choice == "7" or choice == "07":
                answer = operations.area_pyramid()
                print("Area of the Pyramid =", answer)
                print()
            elif choice == "8" or choice == "08":
                answer = operations.area_cylinder()
                print("Area of the Cylinder =", answer)
                print()
            elif choice == "9" or choice == "09":
                answer = operations.area_sphere()
                print("Area of the Sphere =", answer)
                print()
            elif choice == "10":
                answer = operations.area_cone()
                print("Area of the Cone =", answer)
                print()

        isCalculating = True

    elif calc_option == "4":
        while isCalculating:
            print("Select an option:")
            print("\tFind area of Prism:\t\t\t 01")
            print("\tFind area of Pyramid:\t\t 02")
            print("\tFind area of Cylinder:\t\t 03")
            print("\tFind area of Sphere:\t\t 04")
            print("\tFind area of Cone:\t\t\t 05")
            print()

            choice = input("Enter the Choice: ")
            print()

            if choice == "~":
                print()
                print("Going back...")
                print()
                isCalculating = False
            elif choice == "1" or choice == "01":
                answer = operations.volume_prism()
                print("Volume of the Prism =", answer)
                print()
            elif choice == "2" or choice == "02":
                answer = operations.volume_pyramid()
                print("Volume of the Pyramid =", answer)
                print()
            elif choice == "3" or choice == "03":
                answer = operations.volume_cylinder()
                print("Volume of the Cylinder =", answer)
                print()
            elif choice == "4" or choice == "04":
                answer = operations.volume_sphere()
                print("Volume of the Sphere =", answer)
                print()
            elif choice == "5" or choice == "05":
                answer = operations.volume_cone()
                print("Volume of the Cone =", answer)
                print()

        isCalculating = True

    elif calc_option == "~":
        print("Simple calculator stopped")
        isChoosing = False
