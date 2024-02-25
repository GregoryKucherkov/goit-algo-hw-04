def bubble_sort(list):
    n = len(list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


if __name__ == '__main__':
    numbers = [6, 7, 9, 3, 8, 19]
    bubble_sort(numbers)

