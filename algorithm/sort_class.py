import random


class MySort:
    def bubble_sort(self, array, is_asc):
        for i in range(len(array) - 1, 0, -1):
            for j in range(i):
                if self.comp(array[j], array[j + 1], is_asc):
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    def selection_sort(self, array, is_asc):
        for i in range(len(array) - 1):
            buffer_idx = i
            for j in range(i + 1, len(array)):
                if self.comp(array[buffer_idx], array[j], is_asc):
                    buffer_idx = j
            if buffer_idx != i:
                array[i], array[buffer_idx] = array[buffer_idx], array[i]
        return array

    def insertion_sort(self, array, is_asc):
        for i in range(1, len(array)):
            j = i
            while j > 0 and self.comp(array[j - 1], array[j], is_asc):
                array[j], array[j - 1] = array[j - 1], array[j]
                j -= 1
        return array

    def quick_sort(self, array, is_asc):
        pass

    def marge_sort(self, array, is_asc):
        if len(array) == 1:
            return array

        m = len(array) // 2
        a_arr = self.marge_sort(array[0:m], is_asc)
        b_arr = self.marge_sort(array[m:], is_asc)

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
                if self.comp(b_arr[c2], a_arr[c1], is_asc):
                    c.append(a_arr[c1])
                    c1 += 1
                else:
                    c.append(b_arr[c2])
                    c2 += 1

        return c

    def heap_sort(self, array, is_asc):
        pass

    def comp(self, data1, data2, is_asc):
        if is_asc:
            return data1 > data2
        else:
            return data1 < data2

    def shuffle(self, array):
        for i in range(len(array)):
            rand = random.randint(0, len(array) - 1)
            array[i], array[rand] = array[rand], array[i]
        return array


def main():
    s = MySort()
    arr = [i for i in range(100)]

    arr = s.shuffle(arr)

    print("before")
    print(*arr)
    arr = s.marge_sort(arr, True)
    print("after")
    print(*arr)


if __name__ == "__main__":
    main()
