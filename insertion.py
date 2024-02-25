def insertion_sort(list): 
    for i in range(1, len(list)):   
        key = list[i] 
        j = i-1  
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j+1] = key
    return list
    

if __name__ == '__main__':
    numbers = [5, 2, 7, 8, 5, 8, 12, 3, 89, 6]
    insertion_sort(numbers)

