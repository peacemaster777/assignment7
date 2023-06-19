# Q5
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


input_array = list(map(int, input("Enter the integer array with duplicates (space-separated): ").split()))

sorted_array = sorted(input_array)
print("Sorted array:", sorted_array)

element = int(input("Enter the element to search: "))

# Perform binary search on the sorted array
index = binary_search(sorted_array, element)

if index == -1:
    print("Element not found.")
else:
    count = 1           # Count the number of occurrences of the element
    left = index - 1
    right = index + 1

    # Count occurrences to the left of the found index
    while left >= 0 and sorted_array[left] == element:
        count += 1
        left -= 1

    # Count occurrences to the right of the found index
    while right < len(sorted_array) and sorted_array[right] == element:
        count += 1
        right += 1

    print("Number of occurrences of element", element, "is:", count)