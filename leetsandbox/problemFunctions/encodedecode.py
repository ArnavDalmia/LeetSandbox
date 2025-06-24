
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
    print(f"Original list: {strs}")
    
    # Encode
    encoded = encodeFunctionality(strs)
    print(f"Encoded string: '{encoded}'")
    
    # Decode
    decoded = decodeFunctionality(encoded)
    print(f"Decoded list: {decoded}")
    
    # Verify
    if strs == decoded:
        print("✓ Encode/Decode successful!")
    else:
        print("✗ Encode/Decode failed!")

# EXAMPLE
# main(["lint", "code", "love", "you"])
# main(["we", "say", ":", "yes"])
# main([])
