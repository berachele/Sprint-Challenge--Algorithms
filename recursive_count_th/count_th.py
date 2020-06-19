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
    
    elif word[0] == 't':
        if word[1] == 'h':
            count+=1
    else:
        # newWord = 
        return count_th(word.pop(0)) + count_th(word.pop(0))

    return count


    # elif "th" in word:
    #     print(f'IN ELIF --> count: {count}')
    #     count+=1
    #     print(f'after count: {count}')
    #     # return count_th(word)
    # return count




# myWord = 'math'
# for i in range(0, len(myWord)):
#     myWord[i:i+1]
#     print(f'myWord: {myWord[i:i+1]}')