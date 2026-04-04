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
        #initialize number of char matches to 0 
        matches = 0 
        #for each index in Count (aka each index per letter) for 1st window
        for i in range(26):
            #compare the counts that match (per letter)
            if s1Count[i] == s2Count[i]:
                matches += 1
            else:
                matches += 0 
        #initialize left pointer to beginning
        l = 0
            #for loop starts at len(s1) (since already checked first window) and increments r
        for r in range(len(s1),len(s2)):
            #check matches 
            if matches == 26:
                return True
            # take care of adding char to window from right pointer
            index = ord(s2[r]) - ord('a')
            # increment counter for the letter
            s2Count[index] += 1

            #unequal to equal count --> increment matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            #equal to unequal count --> decrement matches 
            #if the added char is not in s1
            elif s1Count [index] + 1 == s2Count[index]:
                matches -= 1

            #take care of removing char to window
            index = ord(s2[l]) - ord('a')
            # decrement counter for the letter
            s2Count[index] -= 1
            #unequal to equal count --> increment matches 
            if s1Count[index] == s2Count[index]:
                matches += 1
            #equal to unequal count --> decrement matches
            #if the removed char is in s1
            elif s1Count [index] - 1 == s2Count[index]: #now too small
                matches -= 1
            #move left pointer
            l += 1
        return matches == 26
        


            