'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    count = 0
    if len(word) == 0:
        return 0
    elif word[0] == 't' and len(word) > 1:
        if word[1] == 'h':
            return count+1 + count_th(word[1:])
        else: 
            return count_th(word[1:])
    else:
        return count_th(word[1:])

    return count