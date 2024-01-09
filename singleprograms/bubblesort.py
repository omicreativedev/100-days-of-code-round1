import random

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate a random array for demonstration
random_array = [random.randint(1, 100) for _ in range(10)]

print("Original Array:", random_array)

# Perform bubble sort
bubble_sort(random_array)

print("Sorted Array:", random_array)
