def anagramGroups(strs: list[str]):
    anagram_hash = {}
    for word in strs:
        key = tuple(sorted(word))
        if key in anagram_hash:
            anagram_hash[key].append(word)
        else:
            anagram_hash[key] = [word]
    return list(anagram_hash.values())
        
    
strs = ["act","pots","tops","cat","stop","hat"]   
print(anagramGroups(strs))


strs = ["x"]
print(anagramGroups(strs))


strs = [""]
print(anagramGroups(strs))
