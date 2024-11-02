class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        else:
            splitted = sentence.split()
            for idx, word in enumerate(splitted):
                if idx < len(splitted) - 1:
                    if splitted[idx][-1] != splitted[idx + 1][0]:
                        return False
        return True
