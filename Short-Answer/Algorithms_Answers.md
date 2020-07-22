#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I don't know if 'n' is supposed to be the same number in this instance or if they're all different numbers, but I would say this is a O(n). Because this is a while loop, I wouldn't say it's a O(1) because it needs to continuously run until it is done, and depending on the variables of 'n', it would depend greatly on how many times that loop is gone through. But it isn't nested and so that counts for something, it won't combine both runtimes of those loops. I would say that if 'n' was the same variable for all of the times that 'n' is used (while (a < 2*2*2): a = a + 2 * 2) then it will be O(n) because it is growing at the same rate or however much 2 is such as as long as a < 8, a = a + 4 --> everytime. 


b) This is a nest loop (a while loop inside of a for loop) so it would be the time of each loop added together. I would say this is a O(n^c) because although this works with small amount of inputs, the higher the number of 'n', the more the runtime will grow at a faster rate. I did this problem with n = 10 and it already makes j = 1024. Just imagine how much more that number would be if 'n' was 20, or 30. And to me, those are low numbers. Let's not forget the very high numbers where making this function is supposed to be fast for large inputs of data.


c) O(n) would be this case even though it is a recursion method. Because even though you are adding 2 to each recursion, it is still only returning the amount of 'bunnies' that you give it, thus being O returning n times: O(n)

## Exercise II
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def drop_egg(n, f_dropped):
    lowest_f = n[0]
    highest_f = n[-1]
    while lowest_f <= highest_f:
        f = (lowest_f + highes_f) /2
        if f_dropped < n[f]:
            highest_f = f -1
        elif f > n[f]:
            lowest_f +1
        else:
            return f
        

In this scenario where we don't know what floor the eggs will break, and we want to find out as quickly as possible, I have come up with a binary search method for this algorithm. 'n' story building will be an array of those stories. In calling the method, you pass in what building you are in (each building will have different stories) and what floor number you are on when you drop an egg. Binary search is the quickest because if you drop an egg on floor 5 and it breaks, you know that it will also break on level 6, 7, 8, 9, and 10. Thus, the level that the egg won't break will be lower than six. We check the next middle of the floors until we find what floor the egg doesn't break on and return that number. 

This will be runtime of O(n log n) because each time it is running, it is cutting list in half instead of having to go through every single floor in the building.