import random

def main():
    element_count = 100
    li = [i for i in range(element_count)]
    li = shuffle(li)
    print("処理前")
    print_array(li)
    li = selection_sort(li, True)
    print("処理後")
    print_array(li)

def shuffle(array):
    for i in range(len(array)):
        rand = random.randint(0, len(array)-1)
        array[i], array[rand] = array[rand], array[i]
    return array

def selection_sort(array, is_asc):
    for i in range(len(array)-1):
        buffer_idx = i
        for j in range(i+1, len(array)):
            if comp(array[buffer_idx], array[j], is_asc):
                buffer_idx = j
        if buffer_idx != i:
            array[i], array[buffer_idx] = array[buffer_idx], array[i]
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