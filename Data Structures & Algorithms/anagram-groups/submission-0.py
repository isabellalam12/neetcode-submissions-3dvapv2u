class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #res = {}
        #change to take care of edge case: empty list of strings given 
        res = defaultdict(list)
        for s in strs:
            #count is an array of 26 zeros (rather than sorting which is O(nlogn))
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")]+=1
            #add string s as a value under the count key
            #res[count].append(s)
            #change because lists cannot be keys in python 
            res[tuple(count)].append(s)
        return list(res.values())


        
