import sys

def binary_search(numbers, search_key):
    """
    Perform binary search on a sorted list.
    
    Args:
    numbers (list): Sorted list of numbers.
    search_key (int): Number to search for.
    
    Returns:
    int: Index of search_key if found, -1 otherwise.
    """
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == search_key:
            return mid  # Return the index if the element is found
        elif search_key < numbers[mid]:
            high = mid - 1  # Search in the lower half
        else:
            low = mid + 1  # Search in the upper half

    return -1  # Element not found

# Command-line argument validation
if len(sys.argv) < 2:
    print("Usage: python script.py <size>")
    sys.exit(1)

try:
    size = int(sys.argv[1])  # Get the array size from the command line
except ValueError:
    print("Error: Size must be an integer.")
    sys.exit(1)

# Input numbers for the array
numbers = []
print(f"Enter {size} numbers for the sorted array:")
for i in range(size):
    while True:  # Input validation loop
        try:
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Ensure the array is sorted
numbers.sort()

# Input the search key
while True:
    try:
        search_key = int(input("Enter the element to be searched: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Perform binary search
index = binary_search(numbers, search_key)

# Output the result
if index == -1:
    print(f"The number {search_key} was not found in the array.")
else:
    print(f"The number {search_key} was found at index {index}.")
