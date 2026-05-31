class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            O = [0] * 26
            for c in word:
                O[ord(c) - ord('a')] += 1
            hashmap[tuple(O)].append(word)

        return list(hashmap.values())
            

                


        