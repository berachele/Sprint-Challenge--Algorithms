'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    count = 0
    if len(word) == 0:
        print("NO WORD")
        return 0
    elif "th" in word:
        print(f'IN ELIF --> count: {count}')
        count = count+1
        print(f'after count: {count}')
        return count_th(word)
    return count