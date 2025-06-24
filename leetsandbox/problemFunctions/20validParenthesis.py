
def validParenthesisFunctionality(s):
    result = []
    for i in s:
        if i == '[' or i == '{' or i == '(':
            # open type
            result.append(i)
        else:
            # entered the close case
            if len(result) <= 0:
                return False

            if i == ']':
                if result[len(result)-1] == '[':
                    result.pop()
                else:
                    return False
            elif i == ')':
                if result[len(result)-1] == '(':
                    result.pop()
                else:
                    return False
            else:
                if result[len(result)-1] == '{':
                    result.pop()
                else:
                    return False
    return result == []

def main(s):
    result = validParenthesisFunctionality(s)
    print(f"Input string: '{s}'")
    if result:
        print("Result: Valid parentheses")
    else:
        print("Result: Invalid parentheses")

# EXAMPLE
# main("()[]{}")
# main("([)]")
