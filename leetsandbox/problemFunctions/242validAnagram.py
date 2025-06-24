
def validAnagramFunctionality(s, t):
    if len(s) != len(t):
        return False

    letters = [0] * 26
    for i in s:
        letters[(ord(i) - ord('a'))] += 1
    for i in t:
        letters[(ord(i) - ord('a'))] -= 1
    if letters != [0] * 26:
        return False
    return True

def main(s, t):
    result = validAnagramFunctionality(s, t)
    
    output = f"""String 1: '{s}'
String 2: '{t}'"""
    
    if result:
        output += "\nResult: Valid anagram"
    else:
        output += "\nResult: Not a valid anagram"
    
    return output

# EXAMPLE
# main("anagram", "nagaram")
# main("rat", "car")
