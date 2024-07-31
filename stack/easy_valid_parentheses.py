'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.
'''
def isValid(s):
    if len(s) % 2 == 1:
        return False
    
    validPairs = {')': '(',
                  ']': '[',
                  '}': '{'
                  }
    
    stack = []

    for symbol in s:
        if symbol in validPairs.keys():
            if stack.pop() != validPairs[symbol]:
                return False
        stack.append(symbol)
    if len(stack) > 0:
        return False
    return True
        