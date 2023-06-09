# Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_pairs(arr, target):
    pairs = []
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.append(pair)
        seen.add(num)

    return pairs

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 9

result = find_pairs(nums, target_sum)
print(f"Pairs that sum up to {target_sum}:")
for pair in result:
    print(pair)
