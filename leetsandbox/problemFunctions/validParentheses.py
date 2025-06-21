def solve(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return "Invalid"
        else:
            stack.append(char)
    return "Valid" if not stack else "Invalid"

def main(s):
    return solve(s) 