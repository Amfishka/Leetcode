'''
Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"
while "aec" is not).

'''

def isSubsequence(s: str, t: str) -> bool:
    '''
    Берём первый символ из строки s (она должна быть подстрокой) и поочерёдно
    сравниваем со строкой t. Если совпадает, то увеличиваем номер искомого символа
    и смотрим второй символ. Если номер искомого символа = длине строки s, то выводим
    ответ
    '''
    index_on_s = 0
    if s == "":
        return False
    for c in t:
        if c == s[index_on_s]:
            index_on_s += 1
        if index_on_s == len(s):
            return True
    if index_on_s == len(s):
        return True
    else:
        return False

if __name__ == "__main__":
    str1 = "acb"
    str2 = "aqwebsdfc"
    print(isSubsequence(str1, str2))
