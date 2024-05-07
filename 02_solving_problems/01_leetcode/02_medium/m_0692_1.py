# 692. Top K Frequent Words
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_dct = {}
        for word in words:
            count_dct[word] = count_dct.get(word, 0) + 1
        
        return  sorted(count_dct.keys(), key=lambda x: (-count_dct[x], x))[:k]

#OK 68%, 96%