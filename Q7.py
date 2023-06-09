# Q7. Write a program to convert prefix expression to infix expression.
def prefix_to_infix(expression):
    stack = []

    for char in reversed(expression):
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix = "(" + operand1 + char + operand2 + ")"
            stack.append(infix)

    return stack.pop()

# Example usage
prefix_expr = "+*342"
infix_expr = prefix_to_infix(prefix_expr)
print("Infix expression:", infix_expr)
