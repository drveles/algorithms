"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. N
ote that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

# Я могу использовать дополнительную память?


aaaaffffc
a4f4c 

# Я хочу создать отдельный массив, для результата.
# Я хочу создать два указателя, один будет смотреть на последний + 1 вставленный символ
# Второй указатель будет бежать по массиву. И принудительно записывать информацию в начало.
# А еще будет счетчик добавленных символов.
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2: 
            return len(chars)
        left = right = 0

        while right < len(chars):
            curr_char = chars[right]
            temp_ctr = 1
            
            while right < len(chars) - 1  and chars[right] == chars[right + 1]:
                right += 1
                temp_ctr += 1
            
            chars[left] = curr_char
            for ch in str(temp_ctr) if temp_ctr > 1 else "":
                left += 1
                chars[left] = ch
            left += 1
            right += 1

        return left 
