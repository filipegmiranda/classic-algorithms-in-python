from array import *

array_input = array('i', [1, 2, 3, 4, 5, 6, 7, 1, -1, 10, 9, 12, -2, 3, 3, 3, 99])


def split_arr(arr):
    length = len(arr) / 2
    return arr[:length], arr[length:]


def merge(arr_i, arr_j):
    k = len(arr_i) + len(arr_j)
    arr_out = array('i')
    i = 0
    j = 0
    i_end = False
    j_end = False
    while k > 0:
        if not i_end:
            if not j_end and arr_i[i] < arr_j[j]:
                arr_out.append(arr_i[i])
                i += 1
                if i == len(arr_i):
                    i_end = True
            elif not j_end and arr_i[i] > arr_j[j]:
                arr_out.append(arr_j[j])
                j += 1
                if j == len(arr_j):
                    j_end = True
            else:
                arr_out.append(arr_i[i])
                i += 1
                if i == len(arr_i):
                    i_end = True
        elif not j_end:
            arr_out.append(arr_j[j])
            j += 1
            if j == len(arr_j):
                j_end = True
        k -= 1
    return arr_out


def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        a1, a2 = split_arr(arr)
        return merge(merge_sort(a1), merge_sort(a2))


print(merge_sort(array_input))
