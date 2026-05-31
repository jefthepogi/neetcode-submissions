class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = defaultdict(int)
        res = []
        for i in nums:
            frequent[i] += 1      
        for i in sorted(frequent, key=frequent.get)[-k:]:
            res.append(i)
        return res
