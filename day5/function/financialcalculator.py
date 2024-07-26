def financialcalculator():
    while True:
        print("Welcome to the Financial Calculator!")
        print("1. Calculate Simple Interest")
        print("2. Calculate Compound Interest")
        print("3. Calculate Future Value")
        print("4. Calculate Present Value")
        print("5. Exit")
    
        choice = input("Choose an option: ")
    
        if choice == "1":
            print("Calculate Simple Interest")
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time in years: "))
            simple_interest = (principal * rate * time) / 100
            print(f"The simple interest is {simple_interest}")
        elif choice == "2":
            print("Calculate Compound Interest")
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time in years: "))
            compound_interest = principal * (1 + rate / 100) ** time
            print(f"The compound interest is {compound_interest}")
        elif choice == "3":
            print("Calculate Future Value")
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time in years: "))
            future_value = principal * (1 + rate / 100) ** time
            print(f"The future value is {future_value}")
        elif choice == "4":
            print("Calculate Present Value")
            future_value = float(input("Enter the future value: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time in years: "))
            present_value = future_value / (1 + rate / 100) ** time
            print(f"The present value is {present_value}")
        elif choice == "5":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

        financialcalculator()            