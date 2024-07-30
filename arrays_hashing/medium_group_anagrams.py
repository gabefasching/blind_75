'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
'''
def groupAnagrams(strs):
    retDict = {}

    for str in strs:
        letters = 26 * [0]

        for char in str:
            letters[(ord(char) - ord('a'))] += 1
        
        key = tuple(letters)

        if key in retDict:
            retDict[key].append(str)
        else:
            retDict[key] = [str]
        
    return retDict.values()