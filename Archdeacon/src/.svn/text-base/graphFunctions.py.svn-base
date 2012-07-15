# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Daniel Nussenbaum"
__date__ ="$Feb 29, 2012 11:48:58 AM$"
__all__ = ["replaceEdgesWithPaths",
            "getGraphFromEdgePaths", "getGraphFromPathVertices", "cloneListOfGraphs", "cloneGraph", "checkSubGraph",
            "createEdgeList", "createGraph", "graphsEqual", "addPathToGraph", "cycleDFS", "extractCycle",
            "cloneList", "getVertices", "getVerticesInOrder", "getEdgeTuples", "getPath", "getGraphFromEdgeTupleList",
            "getGraphFromVerticesInOrder", "getV8", "createFaces", "joinGraphs", "createEmbeddings", "findNewKey",
            "checkGraphIsomorphism", "graphIsomorphism", "cloneListOfLists", "sortByUniqueness"]

def checkGraphIsomorphism(graph0, graph1):
    keys0 = []
    keys1 = []
    directedEdges0 = 0
    directedEdges1 = 0
    if len(graph0.keys()) != len(graph1.keys()): # Check for same number of vertices
#        print "line 19"
        return False
    
    for k in graph0.keys():
        keys0.append([len(graph0[k]), k, False, -1])
        directedEdges0 += len(graph0[k])
    for k in graph1.keys():
        keys1.append([len(graph1[k]), k, False, -1])
        directedEdges1 += len(graph1[k])
        
    if directedEdges0 != directedEdges1: # Check for same number of directed edges
#        print "line 30"
        return False

#    for k0 in keys0:

    keys0 = sortByUniqueness(keys0)
    keys1 = sortByUniqueness(keys1)
#    print "keys0: " + str(keys0)
#    print "keys1: " + str(keys1)
#    keys0.sort()
#    keys1.sort()
#    keys0.reverse()
#    keys1.reverse()
#    print "keys0: " + str(keys0)
#    print "keys1: " + str(keys1)
    
    return graphIsomorphism(keys0, keys1, graph0, graph1)

def sortByUniqueness(keys):
    """TO BE USED ONLY IN THE FORMAT OF GRAPH ISOMORPHISM """
    dir = {}
    for k in keys:
        if k[0] in dir:
            dir[k[0]].append(k)
        else:
            dir[k[0]] = [k]
    tupleList = []
    for d in dir:
        tupleList.append((len(dir[d]), d))
    tupleList.sort()
    orderedKeys = []
    for t in tupleList:
        orderedKeys += dir[t[1]]
    return orderedKeys

def graphIsomorphism(keys0, keys1, graph0, graph1):#, matching0to1 (keys0, keys1, graph0, graph1, mark):
#    while mark <= len(keys0) and keys0[mark[2]] == False:
#        mark += 1
#    if mark > len(keys0):
#        return True
#    for u in keys1:
#        if u[2] == False and u[0] == keys0[mark][0]:
    for u0 in keys0:
#        print "line 49"
        if u0[2] == False:
            break
    else:
#        print "line 53"
        return True
    for u0 in keys0: # For each vertex u0 in graph0, we will try to find a matching of a vertex v1 in graph2
        if u0[2] == False: # If vertex u0 has not been matched
            for v1 in keys1: # we iterate through all vertices of graph1 to find a match
                if v1[2] == False and v1[0] == u0[0]: # If vertex v1 has not been matched, and the degree(u0) == degree(v1)
                    # Now check if for each vertex ui adjacent to u0, the vertices vi adjacent to vi are either the same or not yet matched
                    for adjacentToV1 in graph1[v1[1]]:
                        keyInfo = -1
                        for adjacentKey in keys1:
                            if adjacentKey[1] == adjacentToV1:
                                keyInfo = adjacentKey
                        if keyInfo[2] == True and keyInfo[3] not in graph0[u0[1]]:
                            break
                    else:
                        tempKeys0 = cloneListOfLists(keys0) # Check that cloneListOfLists works well! Not yet tested!
                        tempKeys1 = cloneListOfLists(keys1)


                        
                        u0NewIndex = keys0.index(u0)
                        v1NewIndex = keys1.index(v1)
                        tempKeys0[u0NewIndex][2] = True
                        tempKeys0[u0NewIndex][3] = v1[1]
                        tempKeys1[v1NewIndex][2] = True
                        tempKeys1[v1NewIndex][3] = u0[1]
                        if graphIsomorphism(tempKeys0, tempKeys1, graph0, graph1):
#                            print "line 80"
                            return True
            else:
                return False
#    print "line 82"
    return False


def checkSubGraph(graph, subgraph):
	keys = graph.keys()
	subkeys = subgraph.keys()
	for k in subkeys:
		if k not in keys:
			return False
		vertices = graph[k]
		subvertices = subgraph[k]
		for v in subvertices:
			if v not in vertices:
				return False
	return True

def findNewKey(dict):
    keys = cloneList(dict.keys())
    keys.sort()
    newKey = 1
    for k in keys:
        if k == newKey:
            newKey += 1
    return newKey


def createEdgeList(filename):
    edges = []
    f =  open(filename, 'r')
    lines = f.readlines()
    for l in lines[1:]:
        temp = l.split()
        if len(temp) == 2:
            edges.append(tuple([int(temp[0]), int(temp[1])]))
    return edges

def createGraph(filename):
    f =  open(filename, 'r')
    lines = f.readlines()
    vertices = int(lines[0])
    graph = {}
    for i in range(vertices):
            graph[i+1] = []
    for l in lines[1:]:
            temp = l.split()
            if len(temp) == 2:
                    graph[int(temp[0])].append(int(temp[1]))
                    graph[int(temp[1])].append(int(temp[0]))
    return graph

def createFaces(filename):
    f =  open(filename, 'r')
    lines = f.readlines()
    faces = {}
    for i in range(len(lines)):
            faces[i+1] = []
    for i in range(len(lines)):
        l = lines[i]
        temp = l.split()
        for v in temp:
            faces[i+1].append(int(v))
    return faces

def createEmbeddings(filename):
    f =  open(filename, 'r')
    lines = f.readlines()
    embeddings = []
    currFaces = {}
    faceIndex = 1
    for l in lines:
        if len(l.strip()) == 1 and l.strip() == '=':
            embeddings.append(currFaces)
            currFaces = {}
            faceIndex = 1
        else:
            currFaces[faceIndex] = []
            temp = l.split()
            for v in temp:
                currFaces[faceIndex].append(int(v))
            faceIndex += 1
    return embeddings

def graphsEqual(g0, g1):
	k0 = g0.keys()
	k0.sort()
	k1 = g1.keys()
	k1.sort()
	if k0 != k1: return False
	for k in k0:
		t0 = g0[k]
		t0.sort()
		t1 = g1[k]
		t1.sort()
		if t0 != t1: return False
	return True

def addPathToGraph(graph, path):
	currGraph = cloneGraph(graph)
	keys = currGraph.keys()
	for v in path:
		if v not in keys:
			currGraph[v] = []
	for i in range(len(path)):
		if i < len(path) -1:
			if path[i+1] not in currGraph[path[i]]: currGraph[path[i]].append(path[i+1])
			if path[i] not in currGraph[path[i+1]]: currGraph[path[i+1]].append(path[i])
	return currGraph


def cycleDFS(graph, visited=[], currentVertex=-1, previousVertex=-1, finalGraph={}):
	keys = graph.keys()
	if currentVertex == -1:
		currentVertex = keys[0]
		visited.append(currentVertex)
		for k in graph.keys():
			finalGraph[k] = []
	options = graph[currentVertex]  # I assume here that each vertex has at least 2 edges incident on it.
	if len(options) < 2:
		print "ERROR!! GRAPH HAS AN VERTEX WITH LESS THAN 2 EDGES"
		print "This implies the graph is no 2-connected"
		print "Check Vertex: " + str(currentVertex) + "\n"
	if previousVertex != -1: options.remove(previousVertex)
	candidate = options[0]
	for v in options:
		if v in visited:
			visited.append(v)
			finalGraph[currentVertex].append(v)
			finalGraph[v].append(currentVertex)
			return [visited, finalGraph]
	visited.append(candidate)
	finalGraph[currentVertex].append(candidate)
	finalGraph[candidate].append(currentVertex)
	return cycleDFS(graph, visited, candidate, currentVertex, finalGraph)

def extractCycle(graph):
	curr = cloneGraph(graph)
	finished = False
	deleteList = []

	while not finished:
		for k,v in curr.iteritems():
			if len(curr[k]) == 1:
				deleteList.append((k,curr[k][0]))

		if len(deleteList) == 0:
			finished = True
		else:
			for i in deleteList:
				curr[i[0]].remove(i[1])
				curr[i[1]].remove(i[0])
			deleteList = []
	for k in curr.keys():
		if len(curr[k]) == 0:
			curr.pop(k)
	return curr

def cloneGraph(graph):
	curr = {}
	for k in graph.keys():
            curr[k] = []
	for k,v in graph.iteritems():
            if len(v) > 0:
                for vi in v:
                    curr[k].append(vi)
	return curr

def cloneList(list):
	newList = []
	for i in list:
		newList.append(i)
	return newList

def cloneListOfLists(list):
    newList = []
    for i in list:
        newList.append(cloneList(i))
    return newList

def cloneListOfGraphs(list):
    newList = []
    for i in list:
        newList.append(cloneGraph(i))
    return newList

def getVertices(graph):
	vertices = []
	for k in graph.keys():
		if len(graph[k]) > 0:
			vertices.append(k)
	return vertices

def getVerticesInOrder(givenGraph):
    graph = cloneGraph(givenGraph)
    vertices = []
    done = False
    keys = graph.keys()
    k = keys[0]
    vertices = [k]
    while not done:
        values = cloneList(graph[k])
        if len(values) == 0:
            done = True
            return vertices
        else:
            vertices.append(values[0])
            graph[k].remove(values[0])
            k = values[0]

def getGraphFromVerticesInOrder(vertices):
    """
    This makes a cycle from vertices in order. The vertices formt he path from s to t.
    This method adds the edge t to s.
    """
    graph = {}
    for i in range(len(vertices)):
        graph[vertices[i]] = []
    for i in range(len(vertices)):
        if i < len(vertices)-1:
            graph[vertices[i]].append(vertices[i+1])
            graph[vertices[i+1]].append(vertices[i])
        else:
            graph[vertices[0]].append(vertices[i])
            graph[vertices[i]].append(vertices[0])
    return graph

def getGraphFromPathVertices(vertices):
    """
    This makes a path from vertices in order. The vertices formt he path from s to t.
    This method creates a graph of the form of a path with input being
    a list [s, v0, v1, v2, ... , vn, t] that is a undirected path
    """
    graph = {}
    for i in range(len(vertices)):
        graph[vertices[i]] = []
    for i in range(len(vertices)):
        if i < len(vertices)-1:
            graph[vertices[i]].append(vertices[i+1])
            graph[vertices[i+1]].append(vertices[i])
#        else:
#            graph[vertices[0]].append(vertices[i])
#            graph[vertices[i]].append(vertices[0])
    return graph

def getEdgeTuples(graph):
    edges = []
    for k, v in graph.iteritems():
        if len(v) > 0:
            for vi in v:
                if (k,vi) not in edges and (vi,k) not in edges:
                    if k < vi:
                        edges.append((k,vi))
                    else:
                        edges.append((vi,k))
    return edges
def getPath(voa,graph):
	"""
	voa is vertices of attachment
	graph is the fragment graph
	this method implements breath first search
	"""
	queue = [[voa[0],[voa[0]]]]
	visitedVertices = [voa[0]]
	while len(queue) > 0:
		currVertex = queue[0][0]
		currPath = queue[0][1]
		queue.remove(queue[0])
		if currVertex != voa[0] and currVertex in voa:
			return currPath
		adjacentVertices = graph[currVertex]
		for v in adjacentVertices:
			if v not in visitedVertices:
				visitedVertices.append(v)
				newPath = cloneList(currPath)
				newPath.append(v)
				queue.append([v, newPath])
	return []

def getGraphFromEdgeTupleList(edges):
	graph = {}
	for e in edges:
		keys = graph.keys()
		if(e[0] not in keys): graph[e[0]] = []
		if(e[1] not in keys): graph[e[1]] = []
		graph[e[0]].append(e[1])
		graph[e[1]].append(e[0])
	return graph

def getGraphFromEdgePaths(edgePaths):
    """
    This takes a dictionary data structure where each key is an edge, and each
    value is a path inside of the edge. So if we have a vertex s and a vertex t,
    and there is a path between (s,t), then the value is a list of vertices of
    the form [s, v0, v1, v2, ... , vn, t] that describes the path from s to t
    """
    graph = {}
    for e in edgePaths.keys():
        graph = joinGraphs(graph, getGraphFromPathVertices(edgePaths[e]))
    return graph

def replaceEdgesWithPaths(embedding, edgePaths):
    "NEED TO ADD BACKWARD EDGES! SO (V1, V0) AND (V0, V1)"
    newEmbedding = cloneGraph(embedding)
    for k in newEmbedding.keys():
        currCycle = newEmbedding[k]
        newCycle = []
        for i in range(len(currCycle)):
            v = currCycle[i]
            if i < len(currCycle) - 1:
                if (v, currCycle[i+1]) in edgePaths:
                    if len(edgePaths[(v, currCycle[i+1])]) > 2:
                        if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                        newCycle += edgePaths[(v, currCycle[i+1])]
                    else:
                        if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                        newCycle.append(v)
                elif (currCycle[i+1], v) in edgePaths:
                    tempPath = cloneList(edgePaths[(currCycle[i+1], v)])
                    if len(tempPath) > 2:
                        if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                        tempPath.reverse()
                        newCycle += tempPath
                    else:
                        if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                        newCycle.append(v)
                else:
                    if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                    newCycle.append(v)
            else: 
                if (v, currCycle[0]) in edgePaths:
                    if len(edgePaths[(v, currCycle[0])]) > 2:
                        if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                        newCycle += edgePaths[(v, currCycle[0])]
                        newCycle.pop()
                    else:
                        if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                        newCycle.append(v)
                elif (currCycle[0], v) in edgePaths:
                    tempPath = cloneList(edgePaths[(currCycle[0], v)])
                    if len(tempPath) > 2:
                        if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                        tempPath.reverse()
                        newCycle += tempPath
                        newCycle.pop()
                    else:
                        if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                        newCycle.append(v)
                else:
                    if len(newCycle) > 0 and newCycle[-1] == v:
                            newCycle.pop()
                    newCycle.append(v)
        newEmbedding[k] = newCycle
    return newEmbedding

def joinGraphs(graph1, graph2):
    """
    graph1 - dictionary graph
    graph2 - dictionary graph
    Join graphs into a new graph. Make sure not to have duplicate edges or vertices.
    """
    keys1 = graph1.keys()
    keys2 = graph2.keys()
    newGraph = cloneGraph(graph1)
    for k in keys2:
        if k not in keys1:
            newGraph[k] = []
        for v in graph2[k]:
            if v not in newGraph[k]:
                newGraph[k].append(v)
        
    
    return newGraph

#NEED TO CODE THIS!
def getV8(original, mapping):
    keys = original.keys()
    mp = mapping.split(',')
    label = {}
    if len(mp) == len(keys):
        for i in range(len(keys)):
            label[keys[i]] = mp


if __name__ == "__main__":
    print "Hello World"
