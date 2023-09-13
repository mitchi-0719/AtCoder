import random

def main():
    element_count = 100
    li = [i for i in range(element_count)]
    li = shuffle(li)
    print("処理前")
    print_array(li)
    li = bubble_sort(li, True)
    print("処理後")
    print_array(li)

def shuffle(array):
    for i in range(len(array)):
        rand = random.randint(0, len(array)-1)
        array[i], array[rand] = array[rand], array[i]
    return array

def bubble_sort(array, is_asc):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if comp(array[j], array[j+1], is_asc):
                array[j], array[j+1] = array[j+1], array[j]
    return array

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