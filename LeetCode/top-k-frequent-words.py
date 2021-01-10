import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_dict = collections.Counter(words)
        count_arr = [a for a, b in sorted(count_dict.items(), key = lambda item: (-item[1], item))]
        return count_arr[:k]
