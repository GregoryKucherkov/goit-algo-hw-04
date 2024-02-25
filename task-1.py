import timeit
import random 

from bubble_sort import bubble_sort 
from merge import merge_sort
from insertion import insertion_sort
from radix import radix_sort

if __name__ == '__main__':
    small_data = [random.randint(1, 1000) for _ in range(100)]
    medium_data = [random.randint(1, 10_000) for _ in range(1000)]
    large_data = [random.randint(1, 1000_000) for _ in range(1, 10_000)]

    tsmall_buble = timeit.timeit(lambda: bubble_sort(small_data), number = 3)
    tsmall_merge = timeit.timeit(lambda: merge_sort(tuple(small_data)), number = 3)
    tsmall_radix = timeit.timeit(lambda: radix_sort(small_data), number = 3)
    tsmall_insert = timeit.timeit(lambda: insertion_sort(small_data), number = 3)
    tsmall_Timsort = timeit.timeit(lambda: small_data[:].sort(), number = 3) 
    tsmall_Timsorted = timeit.timeit(lambda: sorted(small_data), number = 3) 

    tmedium_buble = timeit.timeit(lambda: bubble_sort(medium_data), number = 3)
    tmedium_merge = timeit.timeit(lambda: merge_sort(medium_data), number = 3)
    tmedium_insert = timeit.timeit(lambda: insertion_sort(medium_data), number = 3)
    tmedium_radix = timeit.timeit(lambda: radix_sort(medium_data), number = 3)
    tmedium_Timsort = timeit.timeit(lambda: medium_data[:].sort(), number = 3) 
    tmedium_Timsorted = timeit.timeit(lambda: sorted(medium_data), number = 3) 

    tlarge_buble = timeit.timeit(lambda: bubble_sort(large_data), number = 1)
    tlarge_merge = timeit.timeit(lambda: merge_sort(large_data), number = 1)
    tlarge_insert = timeit.timeit(lambda: insertion_sort(large_data), number = 1)
    tlarge_radix = timeit.timeit(lambda: radix_sort(large_data), number = 1)
    tlarge_Timsort = timeit.timeit(lambda: large_data[:].sort(), number = 1) 
    tlarge_Timsorted = timeit.timeit(lambda: sorted(large_data), number = 1) 

    print(f"| {'Algorithm':<20} | {'Small':<20} | {'Medium':<20} | {'Large':<20} |")
    print(f"| {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")

    print(f"| {'Bubble Sort':<20} | {tsmall_buble:20.5f} | {tmedium_buble:20.5f} | {tlarge_buble:20.5f} |")
    print(f"| {'Merge Sort':<20} | {tsmall_merge:20.5f} | {tmedium_merge:20.5f} | {tlarge_merge:20.5f} |")
    print(f"| {'Insertion Sort':<20} | {tsmall_insert:20.5f} | {tmedium_insert:20.5f} | {tlarge_insert:20.5f} |")
    print(f"| {'Radix Sort':<20} | {tsmall_radix:20.5f} | {tmedium_radix:20.5f} | {tlarge_radix:20.5f} |")
    print(f"| {'Tim_sort':<20} | {tsmall_Timsort:20.5f} | {tmedium_Timsort:20.5f} | {tlarge_Timsort:20.5f} |")
    print(f"| {'Tim_sortED':<20} | {tsmall_Timsorted:20.5f} | {tmedium_Timsorted:20.5f} | {tlarge_Timsorted:20.5f} |")

