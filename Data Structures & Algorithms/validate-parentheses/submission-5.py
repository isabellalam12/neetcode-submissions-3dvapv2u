class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for c in s: 
            if c == '(' or  c == '[' or c == '{':
                temp.append(c)
            else:
                if temp:
                    check = temp.pop()
                else:
                    return False
                if c == ')' and check != '(':
                    return False 
                elif c == ']' and check != '[':
                    return False
                elif c == '}' and check != '{':
                    return False
        if len(temp) != 0:
            return False
        return True