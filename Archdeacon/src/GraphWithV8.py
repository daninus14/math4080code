import GraphWithV8
from graphFunctions import getGraphFromEdgeTupleList
from graphFunctions import cloneGraph
from graphFunctions import cloneList
from graphFunctions import *
from graphFunctions import replaceEdgesWithPaths
from stage2 import *
__author__="Daniel Nussenbaum"
__date__ ="$Mar 30, 2012 3:49:46 PM$"

class GraphWithV8:
    """V8 class implementation """
    v8Vertices = []
    v8EdgePaths = {} # Key = Edge, Value = Path
    v8Embeddings = [] # List of Dictionaries?
    graphEdgeList = []
    graphVertices = []
    graphVertexNameCounter = 0
    firstCurrentlyEmbedding = 0

    def __init__(self, edges, vertices, embeddings, edgePaths, v8Vertices, newVertexName):
        #load here the V8!
        self.v8Vertices = cloneList(v8Vertices)
        self.v8EdgePaths = cloneGraph(edgePaths)
        self.v8Embeddings = cloneListOfGraphs(embeddings)
        self.graphEdgeList = cloneList(edges)
        self.graphVertices = cloneList(vertices)
        self.firstCurrentlyEmbedding = 0
        self.graphVertexNameCounter = newVertexName



    @classmethod
    def fromfilename(cls, edges="/home/daniel/NetBeansProjects/Archdeacon/graphs/v8-files/v8-edges", embeddings="/home/daniel/NetBeansProjects/Archdeacon/graphs/v8-files/v8-possible-faces"):
        edgeList = createEdgeList(edges)
        v8Embeddings = createEmbeddings(embeddings)
        return GraphWithV8.fromV8(edgeList, v8Embeddings)

    @classmethod
    def fromV8(cls, edges, embeddings):
        v8Vertices = []
        graphEdgeList = cloneList(edges)
        v8Embeddings = cloneListOfGraphs(embeddings)
        v8EdgePaths = {}
        graphVertices = []
        graphVertexNameCounter = 0
        for e in graphEdgeList:
            v8EdgePaths[e] = list(e)
        for e in graphEdgeList:
            if e[0] not in v8Vertices:
                v8Vertices.append(e[0])
                graphVertices.append(e[0])
                if e[0] > graphVertexNameCounter:
                    graphVertexNameCounter = e[0]
            if e[1] not in v8Vertices:
                v8Vertices.append(e[1])
                graphVertices.append(e[1])
                if e[1] > graphVertexNameCounter:
                    graphVertexNameCounter = e[1]
        return cls(graphEdgeList, graphVertices, v8Embeddings, v8EdgePaths, v8Vertices, graphVertexNameCounter)

    @classmethod
    def fromData(cls, graphEdgeList, graphVertices, v8Embeddings, v8EdgePaths, v8Vertices):
        graphVertexNameCounter = 0
        for v in self.graphVertices:
            if graphVertexNameCounter < v:
                graphVertexNameCounter = v + 1
        return cls(graphEdgeList, graphVertices, v8Embeddings, v8EdgePaths, v8Vertices, graphVertexNameCounter)


    def getV8Embeddings(self):
        return self.v8Embeddings

    def getVertices(self):
        return cloneList(self.graphVertices)

    def getEdges(self):
        return cloneList(self.graphEdgeList)

    def getGraph(self):
        return getGraphFromEdgeTupleList(self.graphEdgeList)

    def getV8Embedding(self, i):
        return self.v8Embeddings[i]

    def getEmbedding(self):
        currEmbedding = False
        if not self.firstCurrentlyEmbedding < len(self.v8Embeddings):
            self.firstCurrentlyEmbedding = 0
            print "HELLO WORLD! LINE 87 GRAPHWITHV8"
        currGraph = getGraphFromEdgeTupleList(self.graphEdgeList)
#        print "\n\nself.graphEdgeList: " + str(self.graphEdgeList)
#        print "currGraph: " + str(currGraph)
        # getGraphFromEdgeTupleList IS WORKING
        v8SubGraph = getGraphFromEdgePaths(self.v8EdgePaths)
#        print "\n\nself.v8EdgePaths: " + str(self.v8EdgePaths)
#        print "v8SubGraph: " + str(v8SubGraph)
#        print "currGraph: " + str(currGraph)
        # getGraphFromEdgePaths SEEMS TO BE WORKING!
#        print "range(self.firstCurrentlyEmbedding,len(self.v8Embeddings)): " + str(range(self.firstCurrentlyEmbedding,len(self.v8Embeddings)))
        for i in range(self.firstCurrentlyEmbedding,len(self.v8Embeddings)):
#                print "NEED TO CHANGE FORMAT OF GRPAHWITHV8 TO NORMAL DICTIONARY GRAPH FORMAT"
#            print "\n\ncurrGraph: " + str(currGraph)
#            print "v8SubGraph: " + str(v8SubGraph)
#            print "self.v8Embeddings[i]: " + str(self.v8Embeddings[i])
#            print "self.v8EdgePaths: " + str(self.v8EdgePaths)
#            print self.toString()
            tempEmbedding = replaceEdgesWithPaths(self.v8Embeddings[i], self.v8EdgePaths)
#            print "tempEmbedding: " + str(tempEmbedding)

            # EVERYTHING SEEMS TO BE WORKING UNTIL STAGE2 EMBEDDING TEST

            currEmbedding = stage2EmbeddingTest(currGraph, v8SubGraph, tempEmbedding) #self.v8Embeddings[i])
#            print "currEmbedding: " + str(currEmbedding)
            if not currEmbedding == False:
                self.firstCurrentlyEmbedding = i
                return currEmbedding
            # this should update the first embeddible index if it works
        return False

    def getV8SubGraph():
            return getGraphFromEdgePaths(self.v8EdgePaths)

    def addEdge(self, v0, v1):
        """
        This only adds an edge to the edge list. Vertices should exist before edge can be added.
        This does not modify edgePaths. If you would like to modify them, then add vertices.
        """
        if v0 in self.graphVertices and  v1 in self.graphVertices and (v0,v1) not in self.graphEdgeList:
            self.graphEdgeList.append((v0,v1))
        else: raise Exception("invalid vertices: " + str(v0) + ", " + str(v1))



    def addVertex(self):
        if self.graphVertexNameCounter + 1 not in self.graphVertices:
            self.graphVertexNameCounter += 1
            self.graphVertices.append(self.graphVertexNameCounter)
            return self.graphVertexNameCounter
        else: raise Exception("Something failed!"  + str(self.graphVertexNameCounter+1) + " is already on the graph!")

    def addVertexInEdge(self, edge):
        """
        ADD CODE TO  REMOVE ORIGINAL EDGE FROM EDGE LIST AND MODIFY EDGE PATHS AS APPROPIATE IF IT'S A KEY
        CODE TO ADD TWO NEW EDGES! AND INCLUDE THEM ON EDGE LIST

        WHAT HAPPENS IF EDGE IS PART OF PATH????
        """
        if edge in self.graphEdgeList:
            if edge in self.v8EdgePaths.keys():
                if not len(self.v8EdgePaths[edge]) == 2:
                    raise Exception(self.v8EdgePaths[edge], "should be only length two", edge)
                else:
                    newVertex = self.addVertex()
                    self.graphEdgeList.remove(edge)
                    self.graphEdgeList.append((edge[0], newVertex))
                    self.graphEdgeList.append((newVertex, edge[1]))
                    self.v8EdgePaths[edge] = [edge[0], newVertex, edge[1]]
                    return newVertex
            else:
                 # Remove previous edge from Edge List and add two new edges
                 # update paths to account for this change by:
                 # Check which paths contain the vertices in the original edge
                 # Then there should be only one path that has vertices in successive order
                 # Note that the edge should not be at the beginning and end because of the previous check that it is not
                 # an edge from the original V8
                 newVertex = self.addVertex()
                 self.graphEdgeList.remove(edge)
                 self.graphEdgeList.append((edge[0], newVertex))
                 self.graphEdgeList.append((newVertex, edge[1]))
                 potentialPaths = []
                 for path in self.v8EdgePaths.keys():
                     if edge[0] in self.v8EdgePaths[path] and edge[1] in self.v8EdgePaths[path]:
                         if abs(self.v8EdgePaths[path].index(edge[0]) - self.v8EdgePaths[path].index(edge[1])) == 1:
                            potentialPaths.append(path)
                 if len(potentialPaths) == 1:
                     path = potentialPaths[0]
                     first = min(self.v8EdgePaths[path].index(edge[0]), self.v8EdgePaths[path].index(edge[1]))
                     second = max(self.v8EdgePaths[path].index(edge[0]), self.v8EdgePaths[path].index(edge[1]))
                     self.v8EdgePaths[path] = self.v8EdgePaths[path][:first+1] + [newVertex] + self.v8EdgePaths[path][second:]
                 return newVertex
        else:
            raise Exception(edge, " not in ", self.graphEdgeList)


    def clone(self):
        return GraphWithV8(self.graphEdgeList, self.graphVertices, self.v8Embeddings, self.v8EdgePaths, self.v8Vertices, self.graphVertexNameCounter)


    def toString(self):
        currStr = ""
        currStr += "\n==============================\nGraph with a V8\n=============================="
        currStr += "\nedgeList: " + str(self.graphEdgeList)
        currStr += "\nvertices: " + str(self.graphVertices)
        currStr += "\nedgePaths: " #+ str(self.v8EdgePaths)
        indent = "\t"
        i = 0
        for e in self.v8EdgePaths.keys():
            currStr += "\n" + indent + str(e) + ": " + str(self.v8EdgePaths[e])
            i+=1
        currStr += "\n==============================\n"
#        print self.v8Embeddings
        return currStr

    def toFileString(self):
        currStr = ""
#        currStr += "\n==============================\nGraph with a V8\n=============================="
        currStr += "edgeList: " + str(self.graphEdgeList)
        currStr += "\nvertices: " + str(self.graphVertices)
        currStr += "\nv8EdgePaths: " + str(self.v8EdgePaths)
        currStr += "\nv8Vertices: " + str(self.v8Vertices)
        currStr += "\nv8Embeddings: " + str(self.v8Embeddings)
#        currStr += "\nedgePaths: " #+ str(self.v8EdgePaths)
#        indent = "\t"
#        i = 0
#        for e in self.v8EdgePaths.keys():
#            currStr += "\n" + indent + str(e) + ": " + str(self.v8EdgePaths[e])
#            i+=1
#        currStr += "\n==============================\n"
#        print self.v8Embeddings
        return currStr


    def printStuff(self):
        self.toString()
#         PRINTS
        i = 0
#        for e in self.v8Embeddings:
#            print str(i) + ": " + str(e)
#            i+=1
#        print "\n"
#        print "edgeList: " + str(self.graphEdgeList)
#        print "edgePaths: " + str(self.v8EdgePaths)
#        print "vertices: " + str(self.graphVertices)
#        self.addEdge(1, 4)
#        print "edgeList: " + str(self.graphEdgeList)
##        self.addEdge(1, 17)
##        print "edgeList: " + str(self.graphEdgeList)
#        self.addVertex()
#        print "vertices: " + str(self.graphVertices)
#        self.addVertex()
#        print "vertices: " + str(self.graphVertices)
        print "\n\n Now we add a vertex in edge (4,5) and a vertex in edge (2,3). Edge (9,10)"
        newVertex = self.addVertexInEdge((4,5))
        newVertex1 = self.addVertexInEdge((2,3))
#        newVertex2 = self.addVertexInEdge((2,newVertex1))
        print "The new vertices are: " + str(newVertex) + " and " + str(newVertex1)
        self.addEdge(newVertex, newVertex1)
        print self.toString()
        

        


if __name__ == "__main__":
    g = GraphWithV8.fromfilename()
    #TESTING STUFF
#    g.printStuff()
#    print g.toString()
#    g.addVertex()
#    v = g.addVertexInEdge((9,10))
#    g.addEdge(v, 3)
#    print "getEmbedding"
#    print g.getEmbedding()