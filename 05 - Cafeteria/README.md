Initially I assumed I would have to create some sort of optimized structure to aid searching the ranges. But, then I realized
that sorting and merging the ranges would provide an efficient way to check for inclusion of a food ID in a range using a
simple bisect() function. Provided the ranges are non-overlapping, bisect is very efficient:

e.g.

10-20
30-40       <- bisect [10,30,50] using 15 yields position 1
50-60
            <- bisect [10,30,50] using 99 yields 3

Given position 1, we get the next range down (10-20) and confirm that 15 is between 10 and 20.
Given position 3, we get the next range down (50-60) and detect that 99 is NOT between 50 and 60.
