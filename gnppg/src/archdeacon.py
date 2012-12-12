import pdb
from graphFunctions import *
from stage2Functions import *
from stage1 import *
from stage2 import *
from GraphWithV8 import *
from GraphMinor import *
import embeddingtest
from time import time
import cPickle as pickle 
import os
import gc # garbage collector
__author__="Daniel Nussenbaum"
__date__ ="$Feb 29, 2012 11:15:32 AM$"
__all__ = ["generateAllNonProjectivePlanarGraphs", "findMinorMinimalGraphs", "show_prev_results"]

## STAGE 3 ALGORITHMS

def show_prev_results(filepath):
    labels = pickle.load( open( filepath, "rb" ) )
    new_labels = []
    for label in labels:
        g = GraphMinor.from_sage_graph_label(label)
        if g.getCanonicalLabel() not in new_labels:
            new_labels.append(g.getCanonicalLabel())
    for label in new_labels:
        g = GraphMinor.from_sage_graph_label(label)
        print g.to_pretty_string()
        print "\n"

def findMinorMinimalGraphs(from_scratch=True):
    dirOutput = os.getcwd()
    folders = dirOutput.split('/')
    dirOutput = dirOutput.strip(folders[-1])
    dirOutput = dirOutput + "output/"
    # filename = "labels-8262"
    filename = "non-embedable-labels-57204"
    if from_scratch:
        labels = generateAllNonProjectivePlanarGraphs()
    else:
        labels = pickle.load( open( dirOutput + filename, "rb" ) )
    
    [new_labels, new_non_embedding] = get_minor_minimal_from_list(labels)
    # pdb.set_trace()
    # while len(new_non_embedding) > 0:
    # for i in range(1):
    #     [temp_new_labels, temp_new_non_embedding] = get_minor_minimal_from_list(new_non_embedding)
    #     new_labels += temp_new_labels
    #     new_non_embedding = temp_new_non_embedding
    #     for label in new_non_embedding:
    #         if label in new_labels:
    #             new_non_embedding.remove(label)

    new_labels = list(set(new_labels))

    pickle.dump( new_labels, open( dirOutput + "minor-minimal-labels-" + str(len(new_labels)), "wb" ) )
    pickle.dump( new_non_embedding, open( dirOutput + "non-embedable-labels-" + str(len(new_non_embedding)), "wb" ) )


def get_minor_minimal_from_list(labels):
    new_labels = []
    # non_embedable_dic = {label: False for label in labels}
    embed_problems_list = []
    t0 = time()
    counter = 0
    all_counter = 0
    new_non_embedding = []
    
    for label in labels:
        # not_valid = False
        all_embed = True
        curr_graph = GraphMinor.from_sage_graph_label(label)
        list_edge_contracted_removed = curr_graph.get_list_of_minors() + curr_graph.get_list_of_1_edge_removed()
        del curr_graph
        gc.collect()
        # print "now analyzing label " + label + "\n"
        for temp_graph in list_edge_contracted_removed:
            # t1 = time()
            # print "t1: " + str(t1-t0)
            # print "current temp_graph ", temp_graph
            # print "temp_graph: ", temp_graph.getCanonicalLabel()
            # if temp_graph.getCanonicalLabel() in non_embedable_dic:
            #     break
            embed_status = embeddingtest.graph_embeds(temp_graph.get_gembed_format())
            if embed_status == False:
                # non_embedable_dic[temp_graph.getCanonicalLabel()] = False
                curr_new_label = temp_graph.getCanonicalLabel()
                if curr_new_label not in labels and curr_new_label not in new_non_embedding:
                    new_non_embedding.append(curr_new_label)
                # break
                # not_valid = True
                all_embed = False
            elif embed_status == None:
                embed_problems_list.append(temp_graph.getCanonicalLabel())
                pdb.set_trace()
        # else:
            # new_labels.append(label)
            # counter += 1
        for temp_graph in list_edge_contracted_removed: del temp_graph
        del list_edge_contracted_removed
        gc.collect()
        # if not not_valid:
        if all_embed:
            new_labels.append(label)
            counter += 1
            print "found another one! up to " + str(counter) + " graphs now!"

        all_counter += 1    

    t1 = time()    
    print all_counter, "labels analyzed in t1: " + str(t1-t0)
    print counter, " labels have been added to the list"
    return [new_labels, list(set(new_non_embedding))]
    # if len(new_non_embedding) > 0: 
    #     recurse_labels = get_minor_minimal_from_list(list(set(new_non_embedding)))
    #     t1 = time()    
    #     print all_counter, "labels analyzed in t1: " + str(t1-t0)
    #     print counter, " labels have been added to the list"
    #     return list(set(new_labels + recurse_labels))
    # else: 
    #     t1 = time()    
    #     print all_counter, "labels analyzed in t1: " + str(t1-t0)
    #     print counter, " labels have been added to the list"
    #     return new_labels

def generateAllNonProjectivePlanarGraphs(output=False, keepWork=False, labels=True):
    v8 = GraphWithV8.fromfilename() # This is the original V8 graph we start with
    listCurrGraphs = [v8] # This is a list of graphs
    listCurrGraphsLabels = [] # This is a list of the canonical labels of the curent graphs
    listNPPGLabels = []
#    noEmbedList = []

    fileNumber = 1
    if output or labels:
        dirOutput = os.getcwd()
        folders = dirOutput.split('/')
        dirOutput = dirOutput.strip(folders[-1])
        if not os.path.exists(dirOutput + "output/"):
            os.makedirs(dirOutput + "output/")
        if not os.path.exists(dirOutput + "output/" + "graphs/"):
            os.makedirs(dirOutput + "output/" + "graphs/")
        dirOutput = dirOutput + "output/"
        dirOutputGraphs = dirOutput + "graphs/"
    if keepWork:
        dirInput = os.getcwd()
        foldersInput = dirInput.split('/')
        dirInput = dirInput.strip(foldersInput[-1])
        if not os.path.exists(dirInput + "input/"):
            os.makedirs(dirInput + "input/")
        dirInput = dirInput + "input/"

    orderMagnitude = 10
    currNum = 1
    t0 = time()
    print "t0: " + str(t0)
    counter = 0

    while len(listCurrGraphs) > 0:
        counter += 1
        if counter % 10 == 0:
            t1 = time()
            print "Loop has run " + str(counter) + " times in " + str(t1-t0) + " time"
            if keepWork:
                listFile = open(dirInput + "list-" + str(counter % 1000), "w")
                for i in range(len(listCurrGraphs)):
                    inputGraph = listCurrGraphs[i]
                    listFile.write("Graph " + str(i) + "\n" + inputGraph.toFileString() + "\n\n")
                listFile.close()
#                fileNumber += 1
                print "file created!"
                print dirOutput + "list-" + str(counter % 1000)
        currGraph = listCurrGraphs[0]
        listCurrGraphs = listCurrGraphs[1:]
        # listCurrGraphsLabels = listCurrGraphsLabels[1:]
        if len(listCurrGraphs) > currNum:
            print "len is over " + str(currNum)
            currNum *= orderMagnitude
            t1 = time()
            print "t1: " + str(t1-t0)
        #stage2EmbeddingTest
        #if no, add to no embed list
        #if yes, do the get obstructions, append all the obstruction graphs in the beginning and continue. Simulating a queue.
        currGraphObstructions = getGraphListWithObstructions(currGraph)
        
        if not currGraphObstructions:
            currGraphLabel = currGraph.getCanonicalLabel()
            for nppgLabel in listNPPGLabels:
                if nppgLabel == currGraphLabel:
                    break
            else:
                listNPPGLabels.append(currGraphLabel)

                if output:
                    outputFile = open(dirOutputGraphs + "graph-" + str(fileNumber), "w")
                    outputFile.write(currGraph.toFileString())
                    outputFile.close()
                    print "file created!:     " + dirOutputGraphs + "graph-" + str(fileNumber)
                    fileNumber += 1

        else:
            # listCurrGraphs += currGraphObstructions
            for currGraphObstruction in currGraphObstructions:
                currGraphObstructionLabel = currGraphObstruction.getCanonicalLabel()
                for currGraphLabel in listCurrGraphsLabels:
                    if currGraphLabel == currGraphObstructionLabel:
                        break
                else:
                    listCurrGraphs.append(currGraphObstruction)
                    listCurrGraphsLabels.append(currGraphObstruction.getCanonicalLabel())
    # labelsFile = open(dirOutput + "labels-" + str(len(listNPPGLabels)), "w")
    # labelsFile.write(str(listNPPGLabels))
    # labelsFile.close()
    if labels:
        pickle.dump( listNPPGLabels, open( dirOutput + "labels-" + str(len(listNPPGLabels)), "wb" ) )

    return listNPPGLabels


def getGraphListWithObstructions(graph):
    # FIND AN EMBEDDING THAT WORKS
    #DO THE GET JUMPS
    currEmbedding = graph.getEmbedding()
    if not currEmbedding == False:
        jumps = findJumps(graph, currEmbedding)
    else: return currEmbedding
    return jumps

def findJumps(graph, embedding):
    """
    graph - GraphWithV8 to find embeddings on
    This code finds all the jumps for the given GraphWithV8
    A jump is an edge between

      1) Two non cofacial edges
      2) One vertex and one edge that are not cofacial
      3) Two non cofacial vertices

    THIS RETURNS A LIST OF NEW GRAPHS WITH JUMPS. EACH ONE A NEW JUMP
    """
    #check with stage2EmbeddingTest whether current graph embedds in firstCurrentlyEmbedding
    vertices = graph.getVertices()
    vertexFaces = getVertexFaces(vertices, embedding)
    vertexJumps = findVertexJumps(graph, vertices, vertexFaces)
    edges = graph.getEdges()
    edgeFaces = getEdgeFaces(edges, embedding)
    edgeJumps = findEdgeJumps(graph, edges, edgeFaces, embedding)
    vertexEdgeJumps = findVertexEdgeJumps(graph, vertices, vertexFaces, edges, edgeFaces)

    nonIsomorphicJumps = []
    nonIsomorphicJumpLabels = []
    for currGraph in vertexJumps + vertexEdgeJumps + edgeJumps:
        currGraphLabel = currGraph.getCanonicalLabel()
        for currNonIsomorphicGraphLabel in nonIsomorphicJumpLabels:
            if currNonIsomorphicGraphLabel == currGraphLabel:
                break
        else:
            nonIsomorphicJumps.append(currGraph)
            nonIsomorphicJumpLabels.append(currGraph.getCanonicalLabel())
    
    return nonIsomorphicJumps

def findVertexEdgeJumps(graph, vertices, vertexFaces, edges, edgeFaces):
    vertexEdgeJumps = []
    vertexEdgeJumpLabels = []
    for e in edges:
        for v in vertices:
            coFacial = False
            for emb in edgeFaces[e]:
                if emb in vertexFaces[v]:
                    coFacial = True
            if not coFacial:
                currGraph = graph.clone()
                v0 = currGraph.addVertexInEdge(e)
                currGraph.addEdge(v0, v)
                currGraphLabel = currGraph.getCanonicalLabel()
                for currJumpLabel in vertexEdgeJumpLabels:
                    if currJumpLabel == currGraphLabel:
                        break
                else:
                    vertexEdgeJumps.append(currGraph)
                    vertexEdgeJumpLabels.append(currGraph.getCanonicalLabel())
    return vertexEdgeJumps

def findEdgeJumps(graph, edges, edgeFaces, embedding):
    nonCofacial = []
    edgeJumps = []
    edgeJumpLabels = []
    for e in edges:
        for ei in edges[edges.index(e):]:
            cofacial = False
            if len(edgeFaces[ei]) == 0 or len(ei) != 2:
                print "\n\n\n\nHOUSTON WE HAVE A PROBLEM"
                print "embedding: " + str(embedding)
                print "edgeFaces[ei]: " + str(edgeFaces[ei])
                print "edgeFaces: " + str(edgeFaces)
                print "ei: " + str(ei)
                print "edges: " + str(edges)
                print "embedding: " + str(graph.firstCurrentlyEmbedding)
                print "graph: " + graph.toString()
                return False # DELETE ALL OF THIS, THIS SHOULD NEVER HAPPEN!
            for emb in edgeFaces[ei]:
                if emb in edgeFaces[e]:
                    cofacial = True
            if not cofacial:
                nonCofacial.append((e, ei))
#                print "nonCofacial: " + str(nonCofacial)
    for edgePair in nonCofacial:
        currGraph = graph.clone()
#        print "edgePair: " + str(edgePair)
        v0 = currGraph.addVertexInEdge(edgePair[0])
        v1 = currGraph.addVertexInEdge(edgePair[1])
        currGraph.addEdge(v0, v1)
        currGraphLabel = currGraph.getCanonicalLabel()
        for currJumpLabel in edgeJumpLabels:
            if currJumpLabel == currGraphLabel:
                break
        else:
            edgeJumps.append(currGraph)
            edgeJumpLabels.append(currGraph.getCanonicalLabel())

    return edgeJumps

def getEdgeFaces(edges, embedding):
    edgeFaces = {}
    for e in edges:
        if e[0] == e[1]:
            print 'EDGE FROM V0 TO ITSELF. PROBLEM!'
            print "edge: " + str(e)
            raise Exception('Egde to Itself', e)
        edgeFaces[e] = []
        for emb in embedding.keys():
            if e[0] in embedding[emb] and e[1] in embedding[emb]:
                inFace = abs(embedding[emb].index(e[0]) - embedding[emb].index(e[1])) == 1
                inFace = inFace or ((embedding[emb].index(e[0]) == 0) and (embedding[emb].index(e[1]) == len(embedding[emb])-1))
                inFace = inFace or ((embedding[emb].index(e[1]) == 0) and (embedding[emb].index(e[0]) == len(embedding[emb])-1))
                if inFace:
                    edgeFaces[e].append(emb)
    return edgeFaces

def getVertexFaces(vertices, embedding):
    vertexFaces = {}
    for v in vertices:
        vertexFaces[v] = []
        for e in embedding.keys():
            if v in embedding[e]:
                vertexFaces[v].append(e)
    return vertexFaces

def findVertexJumps(graph, vertices, vertexFaces):
    nonCofacial = []
    vertexJumps = []
    vertexJumpLabels = []
    for v in vertices:
        for vi in vertices[vertices.index(v):]:
            cofacial = False
            for e in vertexFaces[vi]:
                if e in vertexFaces[v]:
                    cofacial = True
            if not cofacial:
                nonCofacial.append((v, vi))
    for edge in nonCofacial:
        currGraph = graph.clone()
        currGraph.addEdge(edge[0], edge[1])
        currGraphLabel = currGraph.getCanonicalLabel()
        for currJumpLabel in vertexJumpLabels:
            if currJumpLabel == currGraphLabel:
                break
        else:
            vertexJumps.append(currGraph)
            vertexJumpLabels.append(currGraph.getCanonicalLabel())


    return vertexJumps




if __name__ == "__main__":
    import sys
    main()

