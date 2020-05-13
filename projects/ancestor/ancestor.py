from ancestor_graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # initialize a graph
    # then start inserting the ancestors
    # check to see if values of a provided tuple exist in graph.vertices already
    # If not then add as a vertex and add edges
    # if they do then just add the edges between the two
    graph = Graph()

    for anc_tuple in ancestors:
        if anc_tuple[0] not in graph.vertices and anc_tuple[1] not in graph.vertices:
            graph.add_vertex(anc_tuple[1])
            graph.add_vertex(anc_tuple[0])

            graph.add_edge(anc_tuple[1], anc_tuple[0])

        elif anc_tuple[0] not in graph.vertices:
            graph.add_vertex(anc_tuple[0])
            graph.add_edge(anc_tuple[1], anc_tuple[0])

        elif anc_tuple[1] not in graph.vertices:
            graph.add_vertex(anc_tuple[1])
            graph.add_edge(anc_tuple[1], anc_tuple[0])

        else:
            graph.add_edge(anc_tuple[1], anc_tuple[0])

    # Then do a depth first traversal beginning at the starting_node
    # then do a check for how many nodes return in traversal
    # if the lineage is 3 or more then set the -3 inidice and pass into the get_neighbors call
    # then do a check once again to see if indices -1 and -2 are neighbors
    # if yes then check to see if indice -1 is greater than indice -2, if yes then return indice -2
    # if it only has one ancestor then return the -1 index item
    # if else then return -1

    lineage = graph.dft(starting_node)

    if len(lineage) > 2:
        early_ancestor = lineage[-3]
        parents = graph.get_neighbors(early_ancestor)

        if lineage[-1] in parents and lineage[-2] in parents:
            if lineage[-1] > lineage[-2]:
                return lineage[-2]

    if len(lineage) > 1:
        return lineage[-1]
    else:
        return -1
