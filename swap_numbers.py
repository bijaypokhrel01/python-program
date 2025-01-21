# Write a program to swap the two variables without using third variable.

def swap_numbers(a: int, b: int)->tuple:
    a, b = b, a
    return a, b

input1, input2 = int(input("Enter a first number:")), int(input("Enter a second number:"))
print(f"Initially, a = {input1} and b = {input2}")
input1, input2 = swap_numbers(input1, input2)
print('After swapping!')
print(f"a = {input1} and b = {input2}")

