class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed"


def calculator_program():
    calc = Calculator()

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

            if choice == '1':
                result = calc.add(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = calc.subtract(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = calc.multiply(num1, num2)
                operation = "Multiplication"
            elif choice == '4':
                result = calc.divide(num1, num2)
                operation = "Division"

            print(f"\n{operation} result: {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

        redo = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if redo != 'yes':
            print("Exiting the calculator. Goodbye!")
            break


# Run the calculator program
calculator_program()
