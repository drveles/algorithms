# Даны строки s и t, верни true если с помощью одного изменения можно сделать их равными, иначе false

from collections import Counter


def isOneEditDistance(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False

    s_dict = Counter(s)
    t_dict = Counter(t)
    s_diff = s_dict.keys() - (s_dict.keys() & t_dict.keys())
    t_diff = t_dict.keys() - (s_dict.keys() & t_dict.keys())

    if len(s_diff) <= 1 and len(t_diff) <= 1:
        if len(s_diff) and s_dict[s_diff.pop()] != 1:
            return False
        if len(t_diff) and t_dict[t_diff.pop()] != 1:
            return False
    else:
        return False

    return True


if __name__ == "__main__":
    print(isOneEditDistance("", ""))
    print(isOneEditDistance("a", ""))
    print(isOneEditDistance("ab", "abc"))
    print(isOneEditDistance("ab", "abcd"))
