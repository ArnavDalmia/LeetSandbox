def reverse(s):
    return s[::-1]

def main(s):
    if not s:
        return "ERROR: String is empty. Please enter a valid string."
    return f"The reversed string is: {reverse(s)}" 