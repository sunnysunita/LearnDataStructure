user_input = input("enter numbers: ")
list = list(map(int, user_input.split()))
print(list)


def partition(list, si, ei):
    pivort=list[si]
    cout = 0
    for i in range(si, ei + 1):
        if list[i] < pivort:
            cout += 1
    list[si], list[si + cout] = list[si + cout], list[si]  # swapping
    pivort_index = si + cout
    i = si
    j = ei
    while i < j:
        if list[i] < pivort:
            i += 1
        elif list[j] >= pivort:
            j -= 1
        else:
            list[i], list[j] = list[j], list[i]
            i += 1
            j -= 1
    return pivort_index


def quickSort(list, si, ei):
    if si >= ei:
        return
    pivort_index = partition(list, si, ei)
    quickSort(list, si, pivort_index - 1)
    quickSort(list, pivort_index + 1, ei)


quickSort(list, 0, len(list) - 1)
print(list)
