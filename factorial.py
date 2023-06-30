def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n-1) * n

n = 0
try:
    n = int(input("Enter a number:"))
except ValueError:
    print("Invalid number. You must have to insert the integer value only!")
y = fact(n)
print(f"The factorial of {n} is {y}.")
print("This program is added with some features")
