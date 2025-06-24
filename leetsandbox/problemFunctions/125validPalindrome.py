
def validPalindromeFunctionality(s):
    text = ''.join(x for x in s if x.isalnum())
    text = text.lower()
    if len(text) <= 2:
        if len(text) <= 1:
            return True
        if text[0] == text[1]:
            return True
        else:
            return False
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        else:
            left += 1
            right -= 1

    return True

def main(s):
    result = validPalindromeFunctionality(s)
    
    output = f"Input string: '{s}'\n"
    if result:
        output += "Result: Valid palindrome"
    else:
        output += "Result: Not a valid palindrome"
    
    return output

# EXAMPLE
# main("A man, a plan, a canal: Panama")
# main("race a car")
