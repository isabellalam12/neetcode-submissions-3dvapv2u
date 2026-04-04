class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closeToOpen: #a key (aka close bracket)
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: #open bracket
                stack.append(c)

        if stack:
            return False
        return True

