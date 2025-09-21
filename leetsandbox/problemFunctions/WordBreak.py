def wordBreakFunctionality(s, wordDict):
    # Dynamic programming approach
    # dp[i] represents whether s[0:i] can be segmented
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                dp[i] = dp[i + len(word)]
            if dp[i]:
                break
    return dp[0]

def main(s, wordDict):
    result = wordBreakFunctionality(s, wordDict)
    
    output = f"""String: '{s}'
Word dictionary: {wordDict}"""
    
    if result:
        output += "\nResult: String can be segmented using the dictionary words"
    else:
        output += "\nResult: String cannot be segmented using the dictionary words"
    
    return output

# EXAMPLE
# main("leetcode", ["leet", "code"])
# main("applepenapple", ["apple", "pen"])
# main("catsandog", ["cats", "dog", "sand", "and", "cat"])
