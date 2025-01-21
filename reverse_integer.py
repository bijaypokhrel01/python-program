# Write a program to reverse an integer in python.

# Define a function named as reverse_int
def reverse_int(input_data: int):
    var = input_data
    count: int = 0
    total: int = 0
    while var > 0:
        var = var//10
        count+=1
    for i in range(count, 0, -1):
        n = input_data%10
        total = total + n * 10 ** (i-1)
        input_data = input_data//10
    return total

input_data = int(input("Enter a any digits number: "))
result = reverse_int(input_data)
print('The reverse of {input} is {output}'.format(input=input_data, output=result))



