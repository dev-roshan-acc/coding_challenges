def isvalid_anagram(s:str,t:str):
    if len(s) != len(t): return False
    count_char = {}
    for char in s:
        count_char[char] = count_char.get(char,0) +1
    for char in t:
        if char not in count_char or count_char[char] ==0:
            return False
        count_char[char] -=1
    return True   

# example 1
s = "racecar"
t = "carrace"
print (isvalid_anagram(s,t))

# example 2
s = "jar"
t = "jam"
print (isvalid_anagram(s,t))


# example 3
s = "xx"
t = "x"
print (isvalid_anagram(s,t))