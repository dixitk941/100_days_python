import math
from datetime import date

# print("hello world")


def agecalculator():
  while True:
    print("Welcome to the Age Calculator!")
    print("1. Calculate Age")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Calculate Age")
        year = int(input("Enter the year you were born: "))
        month = int(input("Enter the month you were born: "))
        day = int(input("Enter the day you were born: "))
        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))
        print(f"You are {age} years old.")
    elif choice == "2":
        print("Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")

agecalculator()     

