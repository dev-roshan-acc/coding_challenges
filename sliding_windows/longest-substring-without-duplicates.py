from checker import OutputChecker


def lengthOfLongestSubstring( s: str) -> int:
    left,result = 0,0
    charSet =  set()
    for right in range (len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result, right - left + 1)
    return result

testChecker = OutputChecker(lengthOfLongestSubstring)

testChecker.run_test(("abcabcbb"), 3, "Test Case 1")      
testChecker.run_test(("bbbbb"), 1, "Test Case 2")        
testChecker.run_test(("pwwkew"), 3, "Test Case 3")       
testChecker.run_test((""), 0, "Test Case 4")              
testChecker.run_test(("dvdf"), 3, "Test Case 5")         