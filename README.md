Python 3 implementation for Dijkstra's shortest path algorithm


* Arguments :

    - graph : a tuple of 2 elements : a list of nodes (also called vertices), and a list of links between these nodes (also called edges).
     Edges have this format : (sourceNode, targetNode, distanceBetweenThem)
   
    - source : the node from which starts our path
  
    - target : the node where our path ends
  
  
  
  
* Output : 

    - a tuple containing 2 elements : 
        The 1st one is the shortest path from source to target, it is a list of nodes.
        The 2nd is a number, it is the total distance of this path, from source to target
