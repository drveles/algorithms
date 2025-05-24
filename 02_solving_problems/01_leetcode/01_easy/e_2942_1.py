class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # не вижу проблемы однопроходно собрать все индексы
        res = []

        for idx, word in enumerate(words):
            if x in word:
                res.append(idx)
        
        return res
