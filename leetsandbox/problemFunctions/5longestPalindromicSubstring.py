
def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return [l+1, r-1]

def expandEven(s, l, current):
    left = l
    right = current + 1

    if (s[l] == s[current]):
        left -= 1

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return [left+1, right-1]

def longestPalindromeFunctionality(s):
    if len(s) < 2:
        return s

    tempHighest = ""
    for i in range(1, len(s)):
        value = expand(s, i-1, i+1)
        otherVal = expandEven(s, i-1, i)

        tempString = ""
        for j in range(value[0], value[1]+1):
            tempString += s[j]
        if len(tempString) > len(tempHighest):
            tempHighest = tempString
        
        tempString = ""
        for j in range(otherVal[0], otherVal[1]+1):
            tempString += s[j]
        if len(tempString) > len(tempHighest):
            tempHighest = tempString
    return tempHighest

def main(s):
    result = longestPalindromeFunctionality(s)
    print(f"Input string: '{s}'")
    print(f"Longest palindromic substring: '{result}'")
    print(f"Length: {len(result)}")
    
    # Show all palindromes found
    palindromes = set()
    for i in range(len(s)):
        # Odd length palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palindromes.add(s[l:r+1])
            l -= 1
            r += 1
        
        # Even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            palindromes.add(s[l:r+1])
            l -= 1
            r += 1
    
    print(f"All palindromes found: {sorted(palindromes, key=len, reverse=True)}")

# EXAMPLE
# main("babad")
# main("cbbd")
# main("a")
