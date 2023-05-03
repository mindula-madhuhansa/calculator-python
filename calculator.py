import calculatorpackage.standardcalculator as standard
import calculatorpackage.shapecalculator as shape
import calculatorpackage.convertercalculator as converter
import os


# clear console method
def clear_console():
    # Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Mac/Linux
    else:
        _ = os.system('clear')


clear_console()
print("*** Simple Calculator ***")
print()
isCalculating = True
isChoosing = True

# main menu - select calculator/converter type
while isChoosing:
    print("Calculator")
    print("\tStandard:\t\t 01")
    print("\tBoundary:\t\t 02")
    print("\tArea:\t\t\t 03")
    print("\tVolume:\t\t\t 04")
    print("\tProgrammer:\t\t 05")
    print()
    print("Converter")
    print("\tLength:\t\t\t 06")
    print()

    calc_option = input("Select Calculator/Converter: ")
    print()

    # check which type of calculator/converter selected

    # arithmetic calculator
    if calc_option == "1" or calc_option == "01":
        clear_console()
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
                answer = standard.calculation(number1, number2, operator)
                print(number1, operator, number2, "=", answer)
                print()

        clear_console()
        isCalculating = True

    # boundary calculator
    elif calc_option == "2" or calc_option == "02":
        clear_console()
        while isCalculating:
            print("Select an option:")
            print("\tFind perimeter of Rectangle:\t 01")
            print("\tFind circumference of Circle:\t 02")
            print()

            choice = input("Enter the Choice: ")
            print()

            if choice == "~":
                print()
                print("Going back...")
                print()
                isCalculating = False
            elif choice == "1" or choice == "01":
                answer = shape.perimeter()
                print("Perimeter of the Rectangle =", answer)
                print()
            elif choice == "2" or choice == "02":
                answer = shape.circumference()
                print("Circumference of the Circle =", answer)
                print()

        clear_console()
        isCalculating = True

    # area calculator
    elif calc_option == "3" or calc_option == "03":
        clear_console()
        while isCalculating:
            print("Select an option:")
            print("\tFind area of Rectangle:\t\t 01")
            print("\tFind area of Circle:\t\t 02")
            print("\tFind area of Parallelogram:\t 03")
            print("\tFind area of Triangle:\t\t 04")
            print("\tFind area of Trapezoid:\t\t 05")
            print("\tFind area of Prism:\t\t 06")
            print("\tFind area of Pyramid:\t\t 07")
            print("\tFind area of Cylinder:\t\t 08")
            print("\tFind area of Sphere:\t\t 09")
            print("\tFind area of Cone:\t\t 10")
            print()

            choice = input("Enter the Choice: ")
            print()

            if choice == "~":
                print()
                print("Going back...")
                print()
                isCalculating = False
            elif choice == "1" or choice == "01":
                answer = shape.area_rectangle()
                print("Area of the Rectangle =", answer)
                print()
            elif choice == "2" or choice == "02":
                answer = shape.area_circle()
                print("Area of the Circle =", answer)
                print()
            elif choice == "3" or choice == "03":
                answer = shape.area_parallelogram()
                print("Area of the Parallelogram =", answer)
                print()
            elif choice == "4" or choice == "04":
                answer = shape.area_triangle()
                print("Area of the Triangle =", answer)
                print()
            elif choice == "5" or choice == "05":
                answer = shape.area_trapezoid()
                print("Area of the Trapezoid =", answer)
                print()
            elif choice == "6" or choice == "06":
                answer = shape.area_prism()
                print("Area of the Prism =", answer)
                print()
            elif choice == "7" or choice == "07":
                answer = shape.area_pyramid()
                print("Area of the Pyramid =", answer)
                print()
            elif choice == "8" or choice == "08":
                answer = shape.area_cylinder()
                print("Area of the Cylinder =", answer)
                print()
            elif choice == "9" or choice == "09":
                answer = shape.area_sphere()
                print("Area of the Sphere =", answer)
                print()
            elif choice == "10":
                answer = shape.area_cone()
                print("Area of the Cone =", answer)
                print()

        clear_console()
        isCalculating = True

    # volume calculator
    elif calc_option == "4" or calc_option == "04":
        clear_console()
        while isCalculating:
            print("Select an option:")
            print("\tFind volume of Prism:\t\t 01")
            print("\tFind volume of Pyramid:\t\t 02")
            print("\tFind volume of Cylinder:\t 03")
            print("\tFind volume of Sphere:\t\t 04")
            print("\tFind volume of Cone:\t\t 05")
            print()

            choice = input("Enter the Choice: ")
            print()

            if choice == "~":
                print()
                print("Going back...")
                print()
                isCalculating = False
            elif choice == "1" or choice == "01":
                answer = shape.volume_prism()
                print("Volume of the Prism =", answer)
                print()
            elif choice == "2" or choice == "02":
                answer = shape.volume_pyramid()
                print("Volume of the Pyramid =", answer)
                print()
            elif choice == "3" or choice == "03":
                answer = shape.volume_cylinder()
                print("Volume of the Cylinder =", answer)
                print()
            elif choice == "4" or choice == "04":
                answer = shape.volume_sphere()
                print("Volume of the Sphere =", answer)
                print()
            elif choice == "5" or choice == "05":
                answer = shape.volume_cone()
                print("Volume of the Cone =", answer)
                print()

        clear_console()
        isCalculating = True

    # programmer calculator
    elif calc_option == "5" or calc_option == "05":
        clear_console()
        pass

    # length converter
    elif calc_option == "6" or calc_option == "06":
        clear_console()
        print("Millimeters(mm):\t 01")
        print("Centimeters(cm):\t 02")
        print("Decimeter(dm):\t\t 03")
        print("Meters(m):\t\t 04")
        print("Kilometers(km):\t\t 05")
        print("Inches(in):\t\t 06")
        print("Feets(ft):\t\t 07")
        print("Yards(yd):\t\t 08")
        print("Miles(mi):\t\t 09")
        print("Nautical Miles(NM):\t 10")
        while isCalculating:
            units = ["mm", "cm", "dm", "m", "km", "in", "ft", "yd", "mi", "NM"]
            print()

            converter_unit = input("Enter Converter unit: ")
            if converter_unit == "~":
                print()
                print("Going back...")
                print()
                isCalculating = False
            else:
                converted_unit = input("Enter Converted unit: ")
                if converted_unit == "~":
                    print()
                    print("Going back...")
                    print()
                    isCalculating = False
                else:
                    converter_value = int(input("Enter Converter value: "))
                    answer = converter.length_converter(converter_unit, converted_unit, converter_value)
                    print()
                    print(converter_value, units[int(converter_unit) - 1], "=", answer, units[int(converted_unit) - 1])
                    print()

        clear_console()
        isCalculating = True

    elif calc_option == "~":
        print("Simple calculator stopped")
        isChoosing = False
