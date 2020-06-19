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
    
    # [word[i:i+1] for i in range(0, len(word))]
    for i in range(0, len(word)):
        word[i:i+1]     

        checked = len(word) - len(word)
        
        if word[checked] == 't':
            if word[checked+1] == 'h':
                count+=1
        else:
            checked +=1
            # return count_th(word)

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