#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I don't know if 'n' is supposed to be the same number in this instance or if they're all different numbers, but I would say this is a O(n) or O(log n). Because this is a while loop, I wouldn't say it's a O(1) because it needs to continuously run until it is done, and depending on the variables of 'n', it would depend greatly on how many times that loop is gone through. But it isn't nested and so that counts for something, it won't combine both runtimes of those loops. I would say that if 'n' was the same variable for all of the times that 'n' is used (while (a < 2*2*2): a = a + 2 * 2) then it will be O(n) because it is growing at the same rate or however much 2 is such as as long as a < 8, a = a + 4 --> everytime. But if 'n' is different, I would say O(log n) because it's not at the same rate, but of course it will always become slower when inputs are really large. But this solution is still pretty good 🤗 


b) This is a nest loop (a while loop inside of a for loop) so it would be the time of each loop added together. I would say this is a O(n^c) because although this works with small amount of inputs, the higher the number of 'n', the more the runtime will grow at a faster rate. I did this problem with n = 10 and it already makes j = 1024. Just imagine how much more that number would be if 'n' was 20, or 30. And to me, those are low numbers. Let's not forget the very high numbers where making this function is supposed to be fast for large inputs of data.


c) O(n log n) becuase this is a recursive function. We do not know the length of 'bunnies', however, if the number of bunnies is a lower data number, then we can assume that it is still going to run pretty fast. But, the larger the number of bunnies grows, it will be harder for the computer to run in the same speed. It will be slowed down because it needs to process however many of the bunnies we have. 10 bunnies will be fast. 100,000+ bunnies is a diferent story though.

## Exercise II


