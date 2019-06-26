from graphs import Graph

G1 = {"a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
}

G2 = {"a" : ["d","f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["a"]
}

G3 = {"a" : ["d","f"],
      "b" : ["c","b"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["a"]
}


graph1 = Graph(G1)
print graph1
print graph1.is_connected()

graph2 = Graph(G2)
print graph2
print graph2.is_connected()

graph3 = Graph(G3)
print graph3
print graph3.is_connected()

