class Solution:
    def recursiveCheck(self, board, word, search_symb_id, checked_pos, start_pos):
        flag = False
        rows_count = len(board)
        column_count = len(board[0])
        start_r, start_c = start_pos
        len_word = len(word)
        if len_word == 1 and word[0] == board[start_r][start_c]:
            return True

        if len_word == rows_count * column_count and search_symb_id + 1 == len_word and (
            start_r > 0 and (start_r - 1, start_c , ) and board[start_r - 1][start_c] == word[search_symb_id] or
            start_c < column_count - 1 and (start_r, start_c + 1,) and board[start_r][start_c + 1] == word[search_symb_id] or 
            start_r < rows_count - 1 and (start_r + 1, start_c) and board[start_r + 1][start_c] == word[search_symb_id] or
            start_c > 0 and (start_r, start_c - 1,) and board[start_r][start_c - 1] == word[search_symb_id]):
            return True
        
        if search_symb_id == len_word:
            return True

        # top
        if start_r > 0 and (start_r - 1, start_c , ) not in checked_pos and board[start_r - 1][start_c] == word[search_symb_id]:
            checked_pos.add((start_r - 1, start_c,))
            if self.recursiveCheck(board, word, search_symb_id + 1, checked_pos, (start_r - 1, start_c,)):
                return True

        # right if
        if start_c < column_count - 1 and (start_r, start_c + 1,) not in checked_pos and board[start_r][start_c + 1] == word[search_symb_id]:
            checked_pos.add((start_r, start_c + 1,))
            if self.recursiveCheck(board, word, search_symb_id + 1, checked_pos, (start_r, start_c + 1,)):
                return  True

        # bottom
        if start_r < rows_count - 1 and (start_r + 1, start_c) not in checked_pos and board[start_r + 1][start_c] == word[search_symb_id]:
            checked_pos.add((start_r + 1, start_c,))
            if self.recursiveCheck(board, word, search_symb_id + 1, checked_pos, (start_r + 1, start_c,)):
                return  True

        # left    
        if start_c > 0 and (start_r, start_c - 1,) not in checked_pos and board[start_r][start_c - 1] == word[search_symb_id]:
            checked_pos.add((start_r, start_c - 1,))
            if self.recursiveCheck(board, word, search_symb_id + 1, checked_pos, (start_r, start_c - 1,)):
                return  True
        
        return False

    def exist(self, board, word):
        checked_pos = set()
        rows_count = len(board)
        column_count = len(board[0])

        for id_r in range(rows_count):
            for id_c in range(column_count):
                if word[0] == board[id_r][id_c]:
                    checked_pos.add((id_r, id_c,))
                    if self.recursiveCheck(board, word, 1, checked_pos, (id_r, id_c,)):
                        return True
                    checked_pos.clear()

        return False



if __name__ == "__main__":
    Solution().exist([["a","A","A","A"],["a","a","A","A"],["a","a","a","A"],["a","a","A","a"],["A","a","a","A"],["a","A","a","a"]], "aaaaaAAAaaaAAA")


# WA if