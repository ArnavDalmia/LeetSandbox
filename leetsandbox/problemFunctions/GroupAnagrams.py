
def isAnagram(s, t):
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

def anagramRec(strs):
    if len(strs) <= 1:
        return [strs]

    tempList = strs

    anagramList = []
    anagramList.append(tempList[0])
    notAnagramList = []
    for j in range(1, len(tempList)):
        if (isAnagram(tempList[0], tempList[j]) or tempList[0] == tempList[j]):
            anagramList.append(tempList[j])
        else:
            notAnagramList.append(tempList[j])

    if len(notAnagramList) >= 1:
        return [anagramList] + anagramRec(notAnagramList)

    return [anagramList]

def groupAnagramsFunctionality(strs):
    return anagramRec(strs)

def main(strs):
    result = groupAnagramsFunctionality(strs)
    
    output = f"""Input strings: {strs}
Grouped anagrams:"""
    
    for i, group in enumerate(result):
        output += f"\n  Group {i + 1}: {group}"
    
    return output

# EXAMPLE
# main(["eat", "tea", "tan", "ate", "nat", "bat"])
# main(["tops", "act", "cat"])
