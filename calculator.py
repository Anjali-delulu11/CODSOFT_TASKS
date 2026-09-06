# CODSOFT Task 2 - Smart Calculator

history = []


def calculator():
    while True:
        print("\n" + "=" * 50)
        print("              🧮 SMART CALCULATOR")
        print("=" * 50)

        print("1. ➕ Addition")
        print("2. ➖ Subtraction")
        print("3. ✖️ Multiplication")
        print("4. ➗ Division")
        print("5. 🔢 Power")
        print("6. 📊 Percentage")
        print("7. 📜 View History")
        print("8. 🚪 Exit")

        print("=" * 50)

        choice = input("Enter your choice: ").strip()

        if choice == "8":
            print("\n👋 Thank you for using Smart Calculator!")
            break

        if choice == "7":
            if not history:
                print("\n📭 No calculation history yet.")
            else:
                print("\n📜 CALCULATION HISTORY")
                print("-" * 50)

                for item in history:
                    print(item)

            continue

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("\n❌ Invalid choice. Please select 1-8.")
            continue

        try:
            num1 = float(input("\nEnter first number: "))

            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                operation = f"{num1} + {num2} = {result}"

            elif choice == "2":
                result = num1 - num2
                operation = f"{num1} - {num2} = {result}"

            elif choice == "3":
                result = num1 * num2
                operation = f"{num1} × {num2} = {result}"

            elif choice == "4":
                if num2 == 0:
                    print("\n❌ Cannot divide by zero.")
                    continue

                result = num1 / num2
                operation = f"{num1} ÷ {num2} = {result}"

            elif choice == "5":
                result = num1 ** num2
                operation = f"{num1} ^ {num2} = {result}"

            elif choice == "6":
                result = (num1 / 100) * num2
                operation = f"{num1}% of {num2} = {result}"

            history.append(operation)

            print("\n✅ Result:", result)

        except ValueError:
            print("\n❌ Please enter valid numbers.")


calculator()