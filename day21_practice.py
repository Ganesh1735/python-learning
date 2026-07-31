try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter only numbers.")

else:
    print("Your age is",age) 

finally:
    print("Thank you!")