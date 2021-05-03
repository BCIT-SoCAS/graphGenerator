# Welcome to Random Graph Generator

This is an open source project to support algorithms classes - feel free to download it and use

## Installation
You need to have Python version >=3.6 installed on the computer. If you don't, follow this tutorial:
https://www.python.org/downloads/
You should then be able to run the following command:

    python3 --version

Then, please check if you have `pip` installed as well:

    pip --version

It should come with Python - if the command above doesn't work, install it by following this link:
https://pip.pypa.io/en/stable/installing/
Once you'll have both of these, please download the [main.py](https://raw.githubusercontent.com/BCIT-SoCAS/graphGenerator/main/main.py) and [requirements.txt](https://raw.githubusercontent.com/BCIT-SoCAS/graphGenerator/main/requirements.txt) files into one folder.

Go then to this folder and run the following command:

    pip install -r requirements.txt

If there are no errors, you should be good :)

## How to run program?

Simple! Execute this command:

    python3 main.py

And answer the questions:

    How many nodes?
    5
    Weighted? 0 -> No, 1 -> Yes
    0
    Spring or shell layout? 0 -> Spring, 1 -> Shell
    1

And the result should be similar to this one:
![enter image description here](https://i.ibb.co/P4fHHNY/random-graph.png)


## Layout types

We use two, here is a [nice article](https://towardsdatascience.com/customizing-networkx-graphs-f80b4e69bedf) discussing all options:
![enter image description here](https://miro.medium.com/max/1400/1*1oMFO4lkf1nE6_8WK30W-A.png)


# Examples

Now, below we provide some example questions you can ask students during class.

## Basic Graph Theory

**1.  List the vertices in G**
Hint:  A vertex (plural: vertices) is a point or a node.
**2. List the edges in G**
Hint: An edge is an unordered pair of vertices.
**3. Find a path from node X to Y**
Hint: A path is a walk that doesn’t repeat vertices
**4. Find a cycle in G**
Hint: A cycle is a path that begins and ends at the same vertex
**5. Traverse all nodes in G**
Hint: Use [DFS](https://www.baeldung.com/cs/depth-first-search-intro) or [BFS](https://www.baeldung.com/cs/graph-algorithms-bfs-dijkstra)

## Advanced Graph Theory

**1.  Is the graph a tree? if not, find a cycle.**
Hint: A tree is simply a graph with no cycles.
**2. Determine whether or not the graph is planar.**
Hint: A planar graph is a graph that we can draw without any of the edges crossing.
**3. Does the graph have a spanning tree? If yes, find Minimum Spanning Tree.**
Hint: Every finite connected graph has a spanning tree. A minimum spanning tree is a spanning tree with the smallest total weight of all spanning trees.
**4. Is the graph a bipartite graph?**
Hint: A bipartite graph, also called a bigraph, is a set of vertices decomposed into two disjoint sets such that no two vertices within the same set are adjacent.
**5. Find a maximum matching in a graph.**
Hint: A maximum matching (also known as maximum-cardinality matching) is a matching that contains the largest possible number of edges.
