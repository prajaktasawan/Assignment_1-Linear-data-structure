# Q4. Write a program to print the first non-repeated character from a string?
def find_first_non_repeated_char(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in string:
        if char_count[char] == 1:
            return char

    return None

# Example usage
s = "aabccdeeff"

result = find_first_non_repeated_char(s)

if result is not None:
    print("The first non-repeated character is:", result)
else:
    print("There are no non-repeated characters in the string.")
