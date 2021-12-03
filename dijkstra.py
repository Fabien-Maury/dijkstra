def dijkstra(graph, source, target):
    vertices = graph[0].copy()
    edges = graph[1].copy()
    queue = vertices.copy()
    distances = [1000000000] * len(vertices)
    previous = [None] * len(vertices)
    source_index = vertices.index(source)
    distances[source_index] = 0
    
    while len(queue) > 0:
        distances_in_queue = [distances[vertices.index(vertex)] for vertex in queue]
        current_vertex = queue[distances_in_queue.index(min(distances_in_queue))]
        queue.remove(current_vertex)
        if current_vertex == target:
            break
      
        for edge in edges:
            if ((edge[0] == current_vertex) and (edge[1] in queue)):
                possible_new_distance = distances[vertices.index(current_vertex)] + edge[2]
                
                if possible_new_distance < distances[vertices.index(edge[1])]:
                    distances[vertices.index(edge[1])] = possible_new_distance
                    previous[vertices.index(edge[1])] = current_vertex
    path = [target]
    current_vertex = target
    current_index = vertices.index(current_vertex)
    while current_vertex is not None:
        current_vertex = previous[current_index]
        try:
            current_index = vertices.index(current_vertex)
            path.append(current_vertex)
        except:
            pass
    path.reverse()
    
    return(path)
