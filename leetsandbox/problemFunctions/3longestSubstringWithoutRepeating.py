
def longestSubstringWithoutRepeatingFunctionality(s):
    if not s:
        return 0
    if s == "":
        return 0
    if len(s) <= 1:
        return 1
    
    letter = {}
    start = 0
    maxlength = 0
    
    for end, char in enumerate(s):
        if char in letter and letter[char] >= start:
            start = letter[char] + 1
        maxlength = max(maxlength, end - start + 1)
        letter[char] = end
    return maxlength

def main(s):
    result = longestSubstringWithoutRepeatingFunctionality(s)
    print(f"Input string: '{s}'")
    print(f"Length of longest substring without repeating characters: {result}")
    
    # Show the sliding window process
    if s:
        print("Sliding window process:")
        letter = {}
        start = 0
        maxlength = 0
        best_substring = ""
        
        for end, char in enumerate(s):
            if char in letter and letter[char] >= start:
                start = letter[char] + 1
            current_length = end - start + 1
            if current_length > maxlength:
                maxlength = current_length
                best_substring = s[start:end+1]
            letter[char] = end
            print(f"  Position {end}: '{char}' -> Window: '{s[start:end+1]}' (length: {current_length})")
        
        print(f"Longest substring found: '{best_substring}'")

# EXAMPLE
# main("abcabcbb")
# main("bbbbb")
# main("pwwkew")
