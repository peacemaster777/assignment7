# Q6
def remove_duplicates(arr):
    return list(set(arr))


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


input_array = list(map(int, input("Enter the integer array (space-separated): ").split()))

unique_array = remove_duplicates(input_array)

print("Sorted array:", sorted(unique_array))

# Sort the array using selection sort
sorted_selection = selection_sort(unique_array)
print("Selection sort:", sorted_selection)

# Sort the array using bubble sort
sorted_bubble = bubble_sort(unique_array)
print("Bubble sort:", sorted_bubble)