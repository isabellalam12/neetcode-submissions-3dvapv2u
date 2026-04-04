class Solution:

    def encode(self, strs: List[str]) -> str:
        #create empty string to hold result 
        res = ""
        for s in strs:
            #add length of string then # delimitor then the string 
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #create empty list to hold result 
        res = []
        #pointer to element 0 
        i = 0
        # while not at the end of the megastring
        while i < len(s):
            # set j end pointer equal to beginning of word
            j = i 

            #increment j pointer while there is no # 
            while s[j] != "#":
                j+=1
            
            #convert the number length incoded to an int 
            length = int(s[i:j])
            #append j+1 (skip over the #) to j+1+length 
            res.append(s[j+1:j+1+length])
            #set beginning i pointer to end of word
            i = j + 1 + length 
        return res


