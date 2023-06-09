# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
# Infix Notation: Infix notation is the most common way of writing arithmetic expressions, where operators are written between the operands. For example: 3 + 4 * 2.

# Prefix Notation: Prefix notation, also known as Polish notation, is a way of writing arithmetic expressions where operators are placed before their operands. For example: + 3 * 4 2.

# Postfix Notation: Postfix notation, also known as Reverse Polish notation (RPN), is a way of writing arithmetic expressions where operators are placed after their operands. For example: 3 4 2 * +.
def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix = char + operand1 + operand2
            stack.append(prefix)

    return stack.pop()

# Example usage
postfix_expr = "34*2+"
prefix_expr = postfix_to_prefix(postfix_expr)
print("Prefix expression:", prefix_expr)
