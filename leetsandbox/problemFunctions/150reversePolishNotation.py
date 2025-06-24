
def reversePolishNotationFunctionality(tokens):
    # token contains the list
    someList = []
    for i in tokens:
        if i == "-":
            num1 = int(someList.pop())
            num2 = int(someList.pop())
            someList.append(num2 - num1)
        elif i == "+":
            num1 = int(someList.pop())
            num2 = int(someList.pop())
            someList.append(num2 + num1)
        elif i == "*":
            num1 = int(someList.pop())
            num2 = int(someList.pop())
            someList.append(num2 * num1)
        elif i == "/":
            num1 = int(someList.pop())
            num2 = int(someList.pop())
            someList.append(int(float(num2) / num1))
        else:
            someList.append(int(i))
    return someList[0]

def main(tokens):
    result = reversePolishNotationFunctionality(tokens)
    print(f"RPN expression: {tokens}")
    print(f"Result: {result}")
    
    # Show step-by-step evaluation
    print("Step-by-step evaluation:")
    stack = []
    for i, token in enumerate(tokens):
        if token in ["+", "-", "*", "/"]:
            num1 = stack.pop()
            num2 = stack.pop()
            if token == "+":
                result_step = num2 + num1
            elif token == "-":
                result_step = num2 - num1
            elif token == "*":
                result_step = num2 * num1
            elif token == "/":
                result_step = int(float(num2) / num1)
            stack.append(result_step)
            print(f"  Step {i+1}: {num2} {token} {num1} = {result_step}, Stack: {stack}")
        else:
            stack.append(int(token))
            print(f"  Step {i+1}: Push {token}, Stack: {stack}")

# EXAMPLE
# main(["2", "1", "+", "3", "*"])
# main(["4", "13", "5", "/", "+"])
