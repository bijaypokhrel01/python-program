# Write a python program to find the highest common multiple and least common multiple

def hcf(x: int, y: int)->int:
    if x == 0:
        return y
    else:
        if x>y:
            return hcf(x%y, y)
        else:
            return hcf(y%x, x)

def main()->None:
    var1, var2 = int(input('Enter a first number:')), int(input("Enter a second number:"))
    gcd = hcf(var1, var2)
    print("The highest common multiple is {gcd}".format(gcd = gcd))

    lcm = var1 * var2 // gcd
    print("The least common multiple is {lcm}".format(lcm=lcm))


if __name__ == "__main__":
    main()