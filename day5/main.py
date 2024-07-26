from function.calculator import agecalculator
from function.calculator import calculator
from function.calculator import financialcalculator

def main():
    # print("Welcome Dixitk941, It's Day 5")  
    print("1. Calculate Age")
    print("2. Use Simple Calculator")
    print("3. finance")
    print("4. exit")

    choice = input("Choose an option: ")

    if choice == "1":
        agecalculator()
    elif choice == "2":
        calculator()
    elif choice == "3":
        financialcalculator()

    elif choice == "4":
        print("Goodbye!")
        return    
    else:
        print("Invalid choice. Please try again.")

main()        
    

