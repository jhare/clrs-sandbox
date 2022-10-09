import array as arr

values = arr.array("i", [42, 2, 13, 69, 89, 50, 13])


def insertion_sort(v):
    length = len(v)

    for j in range(1, length):
        key = v[j]
        i = j - 1

        while i > -1 and v[i] > key:
            v[i+1] = v[i]
            i -= 1

        v[i+1] = key


if __name__ == "__main__":
    print("We are in main")

    insertion_sort(values)

    print(values)
