# sum of two - is there a number in + a number in B thats add up to value?
def sum_of_two(A, B, value):
    complements = [value-num for num in A]
    for complement_num in complements:
        if complement_num in B:
            return True
    return False


A = [1, 2, 3, 4, 5]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = 10
# print(sum_of_two(A, B, value))


# given a list and a sum-return the indexes of the longest sub list that adds up to the sum


def find_longest_sub_list_by_sum(lst, s):
    print(list(enumerate(lst)))


A = [1, 2, 3, 7, 5]
s = 12
print(find_longest_sub_list_by_sum(A, s))
