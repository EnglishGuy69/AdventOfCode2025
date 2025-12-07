HINT
====
Part 2 presents a common challenge in that an exhaustive search of all the combinations is prohibitively expensive
due to the exponential increase in combinations. To mitigate this, it is important to cache the result of the
combinations starting at the bottom and working up. That way, each time you hit a node that has been calculated
before, you simply look up the combinations rather than calculating them over and over. The result of a recursive
search of the combinations caches the counts from the bottom and then as each layer is explored, the results are
cached and returned to the recursive layer above.

This is a frequent challenge (and solution) in Advent of Code. 