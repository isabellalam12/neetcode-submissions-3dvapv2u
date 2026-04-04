class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #declare a hashmap
        count = {}
        freq = [[] for i in range(len(nums) +1)]
        for n in nums: 
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)

        res = []
        #for loop: for (int i = len(freq)-1;i>=0; i--)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) ==k:
                    return res