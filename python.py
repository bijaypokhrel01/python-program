# Python program to reverse the string
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

word = input("Enter any word:")
s = reverse(word)
print(s)