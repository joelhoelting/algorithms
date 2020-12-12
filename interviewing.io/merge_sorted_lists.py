# Write a function that takes in two sorted lists and outputs a sorted list that is their union.
# inputs:
# a = [1, 3, 5, 20]
# b = [-50, -10, 0, 40, 400]
# output: [-50, -10, 0, 1, 3, 5, 20, 40, 400]


def merge_unique(a: 'List', b: 'List') -> 'List':
    len_m = len(a)
    len_n = len(b)

    i = 0
    j = 0

    new_list = []

    for _ in range(0, len_m + len_n - 1):
        if i == len_m:
            new_list.extend(b[j:])
            break
        elif j == len_n:
            new_list.extend(a[i:])
            break

        if a[i] < b[j]:
            new_list.append(a[i])
            i += 1
        elif a[i] > b[j]:
            new_list.append(b[j])
            j += 1

    print(new_list)


a = [1, 3, 5, 20]
b = [-50, -10, 0, 40, 400]
merge_unique(a, b)
