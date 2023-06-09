# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Example usage
nums = [1, 2, 3, 4, 5]
print("Original array:", nums)

reverse_array(nums)
print("Reversed array:", nums)
