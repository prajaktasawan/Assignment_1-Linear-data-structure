# Q8. Write a program to check if all the brackets are closed in a given code snippet.
def are_brackets_balanced(code):
    stack = []

    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]

    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0 or opening_brackets[closing_brackets.index(char)] != stack[-1]:
                return False
            else:
                stack.pop()

    if len(stack) > 0:
        return False

    return True

# Example usage
code_snippet = "(a + b) * [c - {d + e]"
if are_brackets_balanced(code_snippet):
    print("All brackets are closed.")
else:
    print("Not all brackets are closed.")
