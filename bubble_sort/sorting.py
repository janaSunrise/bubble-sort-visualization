def bubble_sort(array: list):
    new_array = array.copy()

    for i in range(len(new_array)):
        swapped = False  # TO keep track if there is anything to sort.

        for j in range(0, len(new_array) - i - 1):
            if new_array[j] > new_array[j + 1]:
                new_array[j], new_array[j + 1] = new_array[j + 1], new_array[j]

                swapped = True

        if not swapped:
            break

    return new_array
