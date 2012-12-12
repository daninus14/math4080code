# To change this template, choose Tools | Templates
# and open the template in the editor.
from archdeacon import *
from archdeacon import findVertexEdgeJumps
from graphFunctions import checkGraphIsomorphism
from graphFunctions import *
from stage2Functions import *
from stage1 import *
from stage2 import *
from GraphWithV8 import *

import unittest


class  GraphWithV8TestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = GraphWithV8()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_graphWithV8(self):
        #assert x != y;
        #self.assertEqual(x, y, "Msg");
        self.fail("TODO: Write test")

    def test_getEmbedding(self):

#        self.fail("TODO: Write test")
        graph = GraphWithV8.fromfilename() # This is the original V8 graph we start with
        print graph.toString()
        vertex9 = graph.addVertexInEdge((1,2))
        vertex10 = graph.addVertexInEdge((4,5))
        vertex11 = graph.addVertexInEdge((7,8))
        vertex12 = graph.addVertex()
        graph.addEdge(9, 12)
        graph.addEdge(10, 12)
        graph.addEdge(11, 12)
        print graph.toString()
        currEmbedding = graph.getEmbedding()
#        jumps = findJumps(v8, currEmbedding)
#        for j in jumps:
#            print j.toString() + "\n\n"

        

def test_getEmbedding():
    graph = GraphWithV8.fromfilename() # This is the original V8 graph we start with
#    print graph.toString()
    vertex9 = graph.addVertexInEdge((1,2))
    vertex10 = graph.addVertexInEdge((4,5))
    vertex11 = graph.addVertexInEdge((7,8))
    vertex12 = graph.addVertex()
    graph.addEdge(9, 12)
    graph.addEdge(10, 12)
    graph.addEdge(11, 12)
    print graph.toString()
    print "\n\nGET EMBEDDING CALL\n\n"
    currEmbedding = graph.getEmbedding()

def test_gANPPG():
    v8 = GraphWithV8.fromfilename() # This is the original V8 graph we start with
    list = [v8] # This is a list of graphs
    noEmbedList = []

    orderMagnitude = 10
    currNum = 1

    while len(noEmbedList) < 400:
        currGraph = list[0]
        list = list[1:]
        if len(list) > currNum:
            print "len is over " + str(currNum)
            currNum *= orderMagnitude
        #stage2EmbeddingTest
        #if no, add to no embed list
        #if yes, do the get obstructions, append all the obstruction graphs in the beginning and continue. Simulating a queue.
        currGraphObstructions = getGraphListWithObstructions(currGraph)

        if not currGraphObstructions:
#            print "currGraph: " + currGraph.toString()
#            print currGraph.getEmbedding()
#            print currGraph.firstCurrentlyEmbedding
            noEmbedList.append(currGraph)
        else:
            list += currGraphObstructions
#            print "currGraphObstructions: " + str(currGraphObstructions)
#    for graph in noEmbedList:
#        print "\n\nNo Embed Graph: " + graph.toString()
    print "noEmbedList: " + str(len(noEmbedList))
    print "List: " + str(len(list))
    return noEmbedList


def test_findEdgeJumps():
    v8 = GraphWithV8.fromfilename() # This is the original V8 graph we start with
    list = [v8] # This is a list of graphs
    graph = list[0]
    print "Original V8: " + graph.toString()
    embedding = graph.getEmbedding()
    print "\nEmbedding: " + str(embedding)
    edges = graph.getEdges()
    edgeFaces = getEdgeFaces(edges, embedding)
    edgeJumps = findEdgeJumps(graph, edges, edgeFaces, embedding)
    print "\n\n ***********\nEdge Jumps\n***********\n\n"
    print "Total Jumps Found: " + str(len(edgeJumps))
#    print "g0: " + edgeJumps[0].toString()
#    print "g1: " + edgeJumps[1].toString()
#    print "iso: " + str(checkGraphIsomorphism(edgeJumps[0].getGraph(), edgeJumps[1].getGraph()))
    for j in edgeJumps:
        print "\n\n" + j.toString() + "\n\n"
    return True

def test_findVertexJumps():
    v8 = GraphWithV8.fromfilename() # This is the original V8 graph we start with
    list = [v8] # This is a list of graphs
    graph = list[0]
    edges = graph.getEdges()
    embedding = graph.getEmbedding()
    edgeFaces = getEdgeFaces(edges, embedding)
    edgeJumps = findEdgeJumps(graph, edges, edgeFaces, embedding)
    graph = edgeJumps[0]
    print "Original V8: " + graph.toString()
    embedding = graph.getEmbedding()
    print "\nEmbedding: " + str(embedding)
    vertices = graph.getVertices()
    vertexFaces = getVertexFaces(vertices, embedding)
    vertexJumps = findVertexJumps(graph, vertices, vertexFaces)
    print "\n\n***********\nVertex Jumps\n***********\n\n"
    print "Total Jumps Found: " + str(len(vertexJumps))
    for j in vertexJumps:
        print "\n\n" + j.toString() + "\n\n"
    return True

def test_findVertexEdgeJumps():
    v8 = GraphWithV8.fromfilename() # This is the original V8 graph we start with
    list = [v8] # This is a list of graphs
    graph = list[0]
    print "Original V8: " + graph.toString()
    embedding = graph.getEmbedding()
    print "\nEmbedding: " + str(embedding)
    vertices = graph.getVertices()
    vertexFaces = getVertexFaces(vertices, embedding)
    edges = graph.getEdges()
    edgeFaces = getEdgeFaces(edges, embedding)
    vertexEdgeJumps = findVertexEdgeJumps(graph, vertices, vertexFaces, edges, edgeFaces)
    print "\n\n***********\nVertex Edge Jumps\n***********\n\n"
    print "Total Jumps Found: " + str(len(vertexEdgeJumps))
    for j in vertexEdgeJumps:
        print "\n\n" + j.toString() + "\n\n"
    return True

def test_sortByUniqueness():
    a = [(5,1), (5,2), (8,1), (2,3,5)]
    print "a:" + str(a)
    a = sortByUniqueness(a)
    print "a:" + str(a)
    

if __name__ == '__main__':
#    unittest.main()
#    test_getEmbedding()
    import sys
    if len(sys.argv) == 1:
        test_gANPPG()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-ejumps':
            test_findEdgeJumps()
        elif sys.argv[1] == '-vjumps':
            test_findVertexJumps()
        elif sys.argv[1] == '-vejumps':
            test_findVertexEdgeJumps()
        elif sys.argv[1] == '-sort':
            test_sortByUniqueness()
        

