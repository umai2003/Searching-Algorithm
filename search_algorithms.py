def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


if __name__ == "__main__":
    print("Welcome to Search Algorithms!")
    
    try:
        arr = list(map(int, input("Enter a sorted array of integers (space-separated): ").split()))
        target = int(input("Enter the number to search for: "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        exit()

    print("\nPerforming Binary Search...")
    binary_result = binary_search(arr, target)
    if binary_result != -1:
        print(f"Binary Search: Target found at index {binary_result}.")
    else:
        print("Binary Search: Target not found.")

    print("\nPerforming Linear Search...")
    linear_result = linear_search(arr, target)
    if linear_result != -1:
        print(f"Linear Search: Target found at index {linear_result}.")
    else:
        print("Linear Search: Target not found.")


    print("\nAnalyzing the worst-case scenario for Binary Search:")
    print(f"The worst-case time complexity of Binary Search is O(log n).")
    print("This occurs when the target is repeatedly not found in the middle of the range.")
