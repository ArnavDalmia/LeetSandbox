
class MinStack:
    def __init__(self):
        self.obj = []
        self.min_stack = []

    def push(self, val):
        self.obj.append(val)
        temp = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(temp)

    def pop(self):
        if self.obj:
            self.obj.pop()
            self.min_stack.pop()

    def top(self):
        return self.obj[-1] if self.obj else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

def main():
    output = "MinStack operations demonstration:\n"
    
    # Create stack
    stack = MinStack()
    output += "Created MinStack\n"
    
    # Test operations
    operations = [
        ("push", -2),
        ("push", 0),
        ("push", -3),
        ("getMin", None),
        ("pop", None),
        ("top", None),
        ("getMin", None)
    ]
    
    for op, val in operations:
        if op == "push":
            stack.push(val)
            output += f"Push {val} -> Stack: {stack.obj}, Min: {stack.getMin()}\n"
        elif op == "pop":
            popped = stack.top()
            stack.pop()
            output += f"Pop {popped} -> Stack: {stack.obj}, Min: {stack.getMin()}\n"
        elif op == "top":
            result = stack.top()
            output += f"Top: {result}\n"
        elif op == "getMin":
            result = stack.getMin()
            output += f"Min: {result}\n"
    
    return output.rstrip()

# EXAMPLE
# main()
