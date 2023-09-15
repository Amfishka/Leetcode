'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters
 in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead,
be stored in the input character array chars. Note that group lengths that
are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
'''

def compress(chars: list[str]) -> int:
    '''

    '''
    curent_char = ''
    count_char = 1
    res = []
    for c in chars:
        if c == curent_char:
            count_char += 1
        elif curent_char != '':
            res.append(curent_char)
            if count_char > 1:
                res.extend(list(str(count_char)))
            curent_char = c
            count_char = 1
        else:
            curent_char = c
    res.append(curent_char)
    if count_char > 1:
        res.extend(list(str(count_char)))
    for k,v in enumerate(res):
        chars[k] = v
    return len(res), chars

if __name__ == "__main__":
    l = ["a","b","b","b"]
    print(compress(l))