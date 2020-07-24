'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    i = 0
    if len(word) <= 1:
        return i
    elif word[0] == 't' and word[1] == 'h':
        i += 1
    return i + count_th(word[1:])
    