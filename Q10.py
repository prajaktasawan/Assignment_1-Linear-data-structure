# Q10. Write a program to find the smallest number using a stack.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None

        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def get_min(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]


# Example usage
stack = MinStack()
stack.push(5)
stack.push(3)
stack.push(8)
stack.push(2)

smallest = stack.get_min()
print("Smallest number:", smallest)
