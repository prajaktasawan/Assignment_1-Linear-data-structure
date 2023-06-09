# Q3. Write a program to check if two strings are a rotation of each other?
def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concat_str = str1 + str1
    if str2 in concat_str:
        return True
    else:
        return False

# Example usage
s1 = "AACD"
s2 = "ACDA"

if are_rotations(s1, s2):
    print(f"{s1} and {s2} are rotations of each other.")
else:
    print(f"{s1} and {s2} are not rotations of each other.")
