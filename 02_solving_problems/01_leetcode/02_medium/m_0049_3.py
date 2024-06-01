class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dct = {}

        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word in anagrams_dct:
                anagrams_dct[sort_word].append(word)
            else: anagrams_dct[sort_word] = [word]
        
        return [sorted(s) for s in (sorted(anagrams_dct.values(), key=lambda x: len(x)))]


# OK 64%, 60%