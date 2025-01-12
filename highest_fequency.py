# Python program to find the highest fequency of element in array

def list_of_frequency(lst: list[int])->dict:
    non_duplicates: set = set(lst)
    freq: dict = {}
    for num in non_duplicates:
        i = 0
        for x in lst:
            if x == num:
                i += 1
        freq[num] = i
    return freq

def highest_frequency(list_of_frequency) -> tuple:
    for key, value in list_of_frequency.items():
            if value == max(list_of_frequency.values()):
                return (key, value)

def main()->None:
    my_arr = [1, 2, 4, 2, 3, 4, 4, 1, 2, 8, 6, 3, 2, 4, 1, 3, 9, 9, 5, 2, 3, 3, 3, 3, 6, 4, 7, 7, 3, 3, 3]

    print('The most frequent number in list is', highest_frequency(list_of_frequency(my_arr))[0], end=' ')
    print('with the fequency of', highest_frequency(list_of_frequency(my_arr))[1])

    # print(type(list_of_frequency(my_arr).values()))

if __name__ == '__main__':
    main()
