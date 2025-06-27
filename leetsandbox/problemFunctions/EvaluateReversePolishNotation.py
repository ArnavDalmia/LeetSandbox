
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
    
    output = f"""RPN expression: {tokens}
Result: {result}

Step-by-step evaluation:"""
    
    # Show step-by-step evaluation
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
            output += f"\n  Step {i+1}: {num2} {token} {num1} = {result_step}, Stack: {stack}"
        else:
            stack.append(int(token))
            output += f"\n  Step {i+1}: Push {token}, Stack: {stack}"
    
    return output

# EXAMPLE
# main(["2", "1", "+", "3", "*"])
# main(["4", "13", "5", "/", "+"])
