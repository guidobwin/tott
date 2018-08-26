# Graphs

## Definition
Nodes/Vertex - a point
Edges - a connection between points

We can attach information to both of these, but most commonly:
* "names" to nodes, sometimes "colour"
* "values" to edges. As an aside, edges can also be "directed", or "undirected"

## Minimum Spanning Trees

Let's consider distributing some "continuous" resource. Say, electricity or water.
Define:
* Node = "location"
* Edge (undirected) = the cost of building the infrastructure between the two nodes
Can we work out the least amount to get full coverage?

Prim's algorithm - Growing a tree
Kruskal's algorithm - Joining forests
Borůvka's algorithm - creating connected sub-graphs (for each node, each edge weight is distinct)

Variant: look at running costs.
This is more likely to be directional (particularly for "tangible" movement like sewerage or water)


## Path Searching

How about finding the optimal route from A to B?
* node to be a city, and 
* edge to be the distance between the city (by road or air...)

Dijkstra!

How about from any A to any B - all at once!

Floyd–Warshall

Now lets consider a Salesman, who has a set of places she wants to visit.
In order to maximize profit, she wants to minimize the distance travelled, or the costs incurred on by the travel.

TSP
* Open problem!
* Enumeration of all paths is still one of the best options.

* General case vs. Metric (triangle inequality)
* NP-hard (truthiness is can be evaluated in polynomial time)