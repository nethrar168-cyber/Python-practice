a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Answer =", a + b)
elif choice == 2:
    print("Answer =", a - b)
elif choice == 3:
    print("Answer =", a * b)
elif choice == 4:
    if b != 0:
        print("Answer =", a / b)
    else:
        print("Division by zero is not possible")
else:
    print("Invalid choice")