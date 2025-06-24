
def encodeFunctionality(strs):
    finalString = ""
    if strs == []:
        return "bibbidyBob"
    for i in range(len(strs)):
        if (i == len(strs) - 1):
            finalString += strs[i]
        else:
            finalString += strs[i] + "~"
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
