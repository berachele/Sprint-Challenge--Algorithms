#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I don't know if 'n' is supposed to be the same number in this instance or if they're all different numbers, but I would say this is a O(n) or O(log n). Because this is a while loop, I wouldn't say it's a O(1) because it needs to continuously run until it is done, and depending on the variables of 'n', it would depend greatly on how many times that loop is gone through. But it isn't nested and so that counts for something, it won't combine both runtimes of those loops. I would say that if 'n' was the same variable for all of the times that 'n' is used (while (a < 2*2*2): a = a + 2 * 2) then it will be O(n) because it is growing at the same rate or however much 2 is such as as long as a < 8, a = a + 4 --> everytime. But if 'n' is different, I would say O(log n) because it's not at the same rate, but of course it will always become slower when inputs are really large. But this solution is still pretty good 🤗 


b) This is a nest loop (a while loop inside of a for loop) so it would be the time of each loop added together. I would say this is a O(n^c) because although this works with small amount of inputs, the higher the number of 'n', the more the runtime will grow at a faster rate. I did this problem with n = 10 and it already makes j = 1024. Just imagine how much more that number would be if 'n' was 20, or 30. And to me, those are low numbers. Let's not forget the very high numbers where making this function is supposed to be fast for large inputs of data.


c) O(n log n) becuase this is a recursive function. We do not know the length of 'bunnies', however, if the number of bunnies is a lower data number, then we can assume that it is still going to run pretty fast. But, the larger the number of bunnies grows, it will be harder for the computer to run in the same speed. It will be slowed down because it needs to process however many of the bunnies we have. 10 bunnies will be fast. 100,000+ bunnies is a diferent story though.

## Exercise II
f = (input number, I am using 3)
egg_broken = False

def drop_egg(n):
    if n <= f:
        egg_broken == True
    else:
        egg_broken == False

I give this algorithm in proposal to solve the broken egg crisis from those who dare to use any building to vandalize property and said building and the countless amount of eggs harmed in this encounter. I am assuming that the floor of which the egg is thrown off of is always going to break at a certain floor--thus, I have it defined outside of the function so it always remains the same. I then have egg_broken first set to False because when you first climb the building with your carton of eggs, I'm assuming that the vandalists were atleast decent enough to check the carton for broken eggs before buying. In the method or action of when someone drops an egg, n (story of the building) is determined. 'n' will always be the top of the building because the doors are locked and the boys do parkour (or found a ladder). If 'n' is equal to or lower than the set rule of floors, then the egg is safe! However, if the egg is dropped from any story higher than the set rule of floors, the egg is lost and cannot be put back together again. 

This is O(1) because it doesn't matter how many eggs they have, the outcome will always be the same whether or not the story is less/equal or higher than the set floor rate.