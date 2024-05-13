import random


def main():
    element_count = 100
    li = [i for i in range(element_count)]
    li = shuffle(li)
    print("処理前")
    print_array(li)
    li = marge_sort(li, True)
    print("処理後")
    print_array(li)


def shuffle(array):
    for i in range(len(array)):
        rand = random.randint(0, len(array) - 1)
        array[i], array[rand] = array[rand], array[i]
    return array


def marge_sort(array, is_asc):
    if len(array) == 1:
        return array

    m = len(array) // 2
    a_arr = marge_sort(array[0:m], is_asc)
    b_arr = marge_sort(array[m:], is_asc)

    c1 = 0
    c2 = 0
    c = []

    while c1 < len(a_arr) or c2 < len(b_arr):
        if c1 == len(a_arr):
            c.append(b_arr[c2])
            c2 += 1
        elif c2 == len(b_arr):
            c.append(a_arr[c1])
            c1 += 1
        else:
            if comp(b_arr[c2], a_arr[c1], is_asc):
                c.append(a_arr[c1])
                c1 += 1
            else:
                c.append(b_arr[c2])
                c2 += 1

    return c


def comp(data1, data2, is_asc):
    if is_asc:
        return data1 > data2
    else:
        return data1 < data2


def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


main()
