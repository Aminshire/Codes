import os
def perform_calculation():
    # Asks the user for the numbers and the opertation
    while True:
        try:
            num_1 = int(input("Enter the first number: "))
            num_2 = int(input("Enter the second number: "))
            while True:
                operation = input("Enter the operation you want to perform: ")
                if operation in ["+", "-", "*", "/"]:
                    break
                else:
                    print("Invalid operator. Please try again.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
# Perform the calculations depending on the operation
    if operation == "+":
        answer = num_1 + num_2
    elif operation == "-":
        answer = num_1 - num_2
    elif operation == "*":
        answer = num_1 * num_2
    else:
        try:
            answer = num_1 / num_2
        except ZeroDivisionError as error:
            print("Cannot divide by 0.")
            print(error)
            return

    print("Result:", answer)
# Writing on to the file
    file_name = input("Enter the file name to write the equation to: ")

    try:
        with open(file_name, "a") as file:
            equation = f"{num_1} {operation} {num_2} = {answer}"
            file.write(equation + "\n")
        print("Equation written to file.")
    except Exception as e:
        print("Error writing to file:", e)
# Checking if the file exists 
def read_from_file():
    file_name = input("Enter the file name to read from: ")

    if not os.path.isfile(file_name):
        print("File does not exist.")
        return
# Reading the contents of the file
    try:
        with open(file_name, "r") as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except Exception as e:
        print("Error reading file:", e)
# Option tree
while True:
    print("Options:")
    print("1 - Perform calculation")
    print("2 - Read from file")
    print("3 - Exit program")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        perform_calculation()
    elif choice == "2":
        read_from_file()
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
