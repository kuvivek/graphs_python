from graphs import Graph

g = { "a": ["d"],
      "b": ["c"],
      "c": ["b", "c", "d", "e"],
      "d": ["a", "c"],
      "e": ["c"],
      "f": []
    }
    
graph = Graph(g)

print "Vertices of the graph:"
print graph.vertices()

print "Edges of graph:"
print graph.edges()

print 'The path from vertex "a" to vertex "b": '
path = graph.find_path("a", "b")
print path

print 'The path from vertex "a" to "f": '
path = graph.find_path("a", "f")
print path

print 'The path from vertex "c" to vertex "c":'
path = graph.find_path("c", "c")
print path

