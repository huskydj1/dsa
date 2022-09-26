# Introduction to Graphs

Graphs represent things and their relationships to other things. In the language of [graph theory](https://www.tutorialspoint.com/graph_theory/graph_theory_introduction.htm), things are called nodes, and relationships between nodes are called edges. These structures are used to model many real-life systems, including road networks, protein interactions, and social networks. For example, on Instagram, users could be represented as nodes, and two friends could have an edge connecting them to represent their relationship.

![A network of buildings and roads represented as a graph](images/Road%20Network.webp)
*A real [road network](https://transportgeography.org/contents/methods/graph-theory-definition-properties/graph-representation-real-network/) can be modelled using a graph. Here, buildings are nodes and streets are edges.*

<br>

## Types of Edges

### Weighted and Unweighted Edges

An edge between two nodes can have a weight. A weight is a quantitative value associated with the edge. For example, in road networks, edge weights often indicate the distance between two locations or nodes. Edges in social networks are often unweighted because a user following another user should have the same importance regardless of who is involved.

![An unweighted edge and a weighted edge](images/Weighted%20Edge.svg)

<br>

### Directed and Undirected Edges

An edge between two nodes can also have a direction. Edges in social networks are often directed; one user following another user doesn't imply the second user following back. On the other hand, a network of pedestrian pathways has undirected edges because movement along any path (edge) is possible in both directions.

![An undirected edge and a directed edge](images/Direct%20Edge.svg)

<br>

## Representation of Graphs

Two ways to represent a graph in code are an [adjacency matrix](https://www.javatpoint.com/what-is-an-adjacency-matrix) and an [adjacency list](https://www.programiz.com/dsa/graph-adjacency-list). The following examples are based on the graph below. This is a directed, unweighted graph because there are one-way edges and no edge has an associated weight.

![A directed, unweighted graph with four nodes](images/Graph%20Example.png)

<br>

### Adjacency Matrix

An adjacency matrix is an $n \times n$ array, where $n$ is the number of nodes in the graph. Each element of the matrix describes the connection between a pair of nodes.

Suppose `A` is the adjacency matrix of a graph. If the graph is unweighted, `A[i][j]` is a boolean value; truthy if there is an edge from `i` to `j`, and falsy otherwise. On the other hand, if the graph is weighted, then `A[i][j]` is the edge weight (0 if the edge does not exist).

For undirected graphs, if there is an edge between nodes `i` and `j`, then `A[i][j]` and `A[j][i]` are equal because an edge from `i` to `j` is the same thing as an edge from `j` to `i`. In directed graphs, however, `A[i][j]` does not necessarily equal `A[j][i]`.

Adjacency matrices can also represent graphs with loops: edges that connect vertices to themselves. `A[i][i]` corresponds to an edge connecting node `i` to itself.

The above graph would be represented as such:

|       | **1** | **2** | **3** | **4** |
|-------|-------|-------|-------|-------|
| **1** | 0     | 0     | 1     | 1     |
| **2** | 1     | 0     | 0     | 1     |
| **3** | 0     | 0     | 0     | 1     |
| **4** | 0     | 0     | 0     | 0     |

The value of `A[1][3]` is 1 because there is an edge from node `1` to node `3`. However, there is no edge from node `3` to node `1`, so `A[3][1]` is 0.

Adjacency matrices require $O(N^2)$ space, so they may not be ideal especially if memory is a constraint. Another way to represent graphs is with adjacency lists. 

<br>

### Adjacency List

An adjacency list is a list of $n$ lists, where $n$ is the number of nodes. The $i$-th list in the adjacency list consists of the nodes that node $i$ connects to. In the example graph, node 2 connects to nodes 1 and 4, so the second list contains 1 and 4.

| _Node_ | _Outward Edges_ |
|--------|-----------------|
| **1**  | 3, 4            |
| **2**  | 1, 4            |
| **3**  | 4               |

Adjacency lists require $O(E)$ memory. For sparse graphs (graphs with relatively few edges), adjacency lists are much more space-efficient than adjacency matrices. However, they are slower to check whether two nodes are adjacent to each other. Adjacency matrices perform this operation in constant time.

<hr>

## Exercises

1. Show that the adjacency matrix of an undirected graph is symmetric.

<details>
    <summary>Solution</summary>
    <h2>Java</h2>
    ...
    <h2>Python</h2>
    ...
</details>

<br>

2. Implement both an adjacency matrix and an adjacency list of an unweighted, undirected graph in code. Complete the following exercises for both data structures.
   1. Create a method that initializes the data structure.
   2. Create methods for adding and removing edges between nodes.
   3. Create a method that returns the degree (number of connected edges) of an input node.
   4. Create a method that returns the total number of edges in a graph.

<details>
    <summary>Solution (Adjacency Matrix)</summary>
    <h2>Java</h2>
    ...
    <h2>Python</h2>
    ...
</details>

<details>
    <summary>Solution (Adjacency List)</summary>
    <h2>Java</h2>
    ...
    <h2>Python</h2>
    ...
</details>