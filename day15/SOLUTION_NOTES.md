# Solution Notes

Day 15 was the first problem where I thought it would be useful to write out my thoughts about the solution. Mainly because the solution this time is not completely "original" to me (if anything is truly original).

Given that it is March 2022, it should be obvious that I'm no longer rushing through these problems in a competitive manner. I read the problem, didn't have an immediate solution pop into my head, so I just let it simmer in the background while I went on with work and family life for several days, or maybe even weeks.

When I came back to the problem, and re-read it, it clicked that this risk level map is actually a weighted graph and that the solution is to find the "shortest distance" (or in this case, the least total risk) between two nodes on that graph. I then thought of [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), not because I'm super smart or because I have a good memory or because I use it all the time in real-world applications. None of those things are really true.

About a year ago, I read and worked through the book [Classic Computer Science Problems in Python](https://www.manning.com/books/classic-computer-science-problems-in-python) by [David Kopec](https://twitter.com/davekopec), which has a chapter on graph problems which includes an implementation of Dijkstra's algorithm. I had encountered that algorithm more than 20 years ago in an artificial intelligence class in college, but I seriously doubt I would have remembered it without the more recent exposure.

I started with the implementation of Dijkstra's algorithm from the [source code](https://github.com/davecom/ClassicComputerScienceProblemsInPython) that accompanied the book mentioned above, and then modified it (fairly heavily) to suit the needs of this problem. Eliminating everything I didn't need. Consolidating some things. Changing distance to risk. Converting `str` to `int` where possible for performance. Etc.

It worked great for the sample input, but kept giving me the wrong answer for the actual input. I eventually figured out what I was doing wrong.

The distance from A to B is the same as the distance from B to A. The implementation assumed that, and when adding an edge (e.g. (A, B, 3)) it would also add the reverse of that edge (e.g. (B, A, 3)). Knowing that it added the reverse, I only added the edges for moving "right" and "down" in the map, since the reverse "left" and "up" would be added automatically.

However, the risk level when moving from A to B is not necessarily the same as the risk level when moving from B to A, so I removed that line that automatically added the reverse edge, and I explicitly added the "left" and "up" edges with the appropriate risk levels. Then the computed least total risk level was correct.

