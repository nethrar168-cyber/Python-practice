def largest(a, b, c):
    if a > b and a > c:
        print("Largest number =", a)
    elif b > a and b > c:
        print("Largest number =", b)
    else:
        print("Largest number =", c)

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
c = int(input("Enter number three: "))

largest(a, b, c)