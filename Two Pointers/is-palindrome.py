
from checker import OutputChecker
def isPalindrome(s: str) -> bool:
    # where l = left and r=right
    l,r = 0,len(s) - 1
    while l<r:
        while l<r and not s[l].isalnum():
            l += 1
        while l<r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


testChecker = OutputChecker(isPalindrome)

testChecker.run_test(("A man, a plan, a canal: Panama"), True, "Test Case 1")
testChecker.run_test(("race a car"), False, "Test Case 2")
testChecker.run_test(("No lemon, no melon"), True, "Test Case 3")
testChecker.run_test(("Was it a car or a cat I saw?"), True, "Test Case 4")
testChecker.run_test(("Hello, World!"), False, "Test Case 5")
    