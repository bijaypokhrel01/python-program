# WAP to find the sum of digits of a number using recursive function.
def digits_sum(n_digits: int)->int:
    if n_digits == 0:
        return 0
    else:
        return n_digits%10 + digits_sum(n_digits//10)

input_val = int(input("Enter a any digits number: "))
print(f"The sum of digits of a given number: {digits_sum(input_val)}")
