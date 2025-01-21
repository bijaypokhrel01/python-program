# Write a program to find the addition of two number using recursive.

def addition(x: int, y: int)->int:
    if x == 0:
        return y
    else:
        return 1 + addition(x-1, y)


def main()->None:
    num1, num2 = int(input("Enter a first number:")), int(input("Enter a second number"))
    result = addition(num1, num2)
    print("The addition of {num1} and {num2} is {result}".format(num1=num1, num2=num2, result=result))

if __name__ == "__main__":
    main()