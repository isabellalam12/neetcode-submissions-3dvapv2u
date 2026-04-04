class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashs = {}
        hasht = {}
        for c in range(len(s)):
            hashs[s[c]] = 1 + hashs.get(s[c],0)
            hasht[t[c]] = 1 + hasht.get(t[c],0)
        if hashs == hasht:
            return True
        return False
            


                
        
            