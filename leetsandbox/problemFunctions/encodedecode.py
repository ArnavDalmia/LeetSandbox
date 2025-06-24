
def encodeFunctionality(s):
    finalString = ""
    if s == []:
        return "bibbidyBob"
    for i in range(len(s)):
        if (i == len(s) - 1):
            finalString += s[i]
        else:
            finalString += s[i] + "~"
    return finalString 

def decodeFunctionality(s):
    if s == "bibbidyBob":
        return []
    tempList = s.split("~")
    return tempList

def main(strs):
    output = f"Original list: {strs}\n"
    
    # Encode
    encoded = encodeFunctionality(strs)
    output += f"Encoded string: '{encoded}'\n"
    
    # Decode
    decoded = decodeFunctionality(encoded)
    output += f"Decoded list: {decoded}\n"
    
    # Verify
    if strs == decoded:
        output += "✓ Encode/Decode successful!"
    else:
        output += "✗ Encode/Decode failed!"
    
    return output

# EXAMPLE
# main(["lint", "code", "love", "you"])
# main(["we", "say", ":", "yes"])
# main([])
