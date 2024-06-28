#Algorytmy

In this repository you can find code for couple of classic algorithms writen in Matlab.

## Dijkstra algorithm
Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a weighted graph, which may represent, for example, road networks. 

Example graph:
![alt text](https://github.com/Nietoperka/algorithms/blob/main/fig4.jpg?raw=true)

In first lines of code you can implement the graph:

![alt text](https://github.com/Nietoperka/algorithms/blob/main/fig2.jpg?raw=true)

    polaczenie_a - list of nodes which have connection
    polaczenie_b - list of nodes which are connected to
    wartosci - costs of the connectons
    xx - list of x coordinates
    yy - list of x coordinates



How it works:

1. Set initial distances for all vertices: 0 for the source node, and infinity for all the other.
2. Choose the unvisited node with the shortest distance from the start to be the current node. So the algorithm will always start with the source as the current node.
3. For each of the current node unvisited neighbor nodes, calculate the distance from the source and update the distance if the new, calculated, distance is lower.
4. We are now done with the current node, so we mark it as visited. A visited node is not checked again.
5. Go back to step 2 to choose a new current node, and keep repeating these steps until all nodes are visited.
6. In the end we are left with the shortest path from the source node to every other node in the graph.



Process of "thinking" is visible in terminal:

![alt text](https://github.com/Nietoperka/algorithms/blob/main/fig1.jpg?raw=true)

    krok - step
    Wierzcholki - nodes
    Koszt - cost
    Poprzednik - previous node



In code there is commented another example, more complex:
![alt text](https://github.com/Nietoperka/algorithms/blob/main/fig5.jpg?raw=true)
