#1
# a1 = int(input("Enter the first element of the progression: "))
# d = int(input("Enter the common difference: "))
# n = int(input("Enter the number of elements in the progression: "))
# def arithmetic_progression(a1, d, n):
#     progression = [a1 + (i - 1) * d for i in range(1, n + 1)]
#     return progression

# array = arithmetic_progression(a1, d, n)
# print("Arithmetic progression array:", array)

#2
lst = [int(x) for x in input("Enter the list elements separated by space: ").split()]
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
def find_indexes_in_range(lst, min_value, max_value):
    indexes = [index for index, value in enumerate(lst) if min_value <= value <= max_value]
    return indexes
indexes = find_indexes_in_range(lst, min_value, max_value)
print("Indices of elements in the specified range:", indexes)