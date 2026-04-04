class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        #create empty list with each letter as category
        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            #take ascii value of 1st s1 char then 
            #subtract from ord('a') to get a number in the 26 index
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1
        matches = 0 
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
            else:
                matches += 0 
        l = 0
            #for loop starts at len(s1) and increments r
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count [index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count [index] - 1 == s2Count[index]: #now too small
                matches -= 1
            l += 1
        return matches == 26
        


            