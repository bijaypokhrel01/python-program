# Write a python program to check whether a number is prime or not.

def check_prime(n: int)->bool:
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            continue
    return True

variable = int(input("Enter a number:"))
print(f"The number {variable} is a prime" if check_prime(variable)==True else f"The {variable} is not a prime number.")