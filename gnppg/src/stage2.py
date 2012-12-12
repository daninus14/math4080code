#! /usr/bin/python
from graphFunctions import *
from stage2Functions import *
from stage1 import *
from time import time

__author__="Daniel Nussenbaum"
__date__ ="$Apr 6, 2012 4:01:27 PM$"

def main():

    if sys.argv[1] == "-et":
        et(sys.argv[2], sys.argv[3], sys.argv[4])


## STAGE 2 ALGORITHM BELOW THIS LINE

def et(graphFilename, subGraphFilename, facesFilename):
    t0 = time()
    originalGraph = createGraph(graphFilename)
    originalSubGraph = createGraph(subGraphFilename)
    originalEmbedding = createFaces(facesFilename)


    print stage2EmbeddingTest(originalGraph, originalSubGraph, originalEmbedding)
    t1 = time()
    print "Total Time: " + str(t1-t0)

def stage2EmbeddingTest(originalGraph, originalSubGraph, originalEmbedding):
	"""
	graph - Normal Graph Dictionary
	subGraph - Normal Graph Dictionary
	embedding - Faces Dictionary

	returns faces to embed G

	So H is embedded in the faces already given. So it has a planar embedding in the plane
	or projective planar embedding in the projective plane.
	A G embedding extending H would be to just start with H on the faces, as given, and then try
	to add edges and vertices of G (fragments) such that each addition continues to embed.
	So the subgraph grows until it either becomes the full graph, and embeds, or if it adds
	another fragment, it will no longer embed.

	#for each fragment and candidate face. Join fragment and face in a graph. planarityTest2(joined graph,
        #face cycle, face which is 1 for cycle)
	## Assume embedding has dictionary of number of face to vertices in a cycle
	## fragment faces returns a list of numbers that the fragments embbeds in

	#remove faces accordingly if planarity testing returns False for that fragment
	"""
	graph = cloneGraph(originalGraph)
	subgraph = cloneGraph(originalSubGraph)
	embedding = cloneGraph(originalEmbedding)
	potentialEdges = getEdgeTuples(graph)
	currEdges = getEdgeTuples(subgraph)
	currVertices = getVertices(subgraph)
	faces = cloneGraph(embedding)

	if not checkSubGraph(graph, subgraph):
            print "NOT A SUBGRAPH"
            return False
        if graphsEqual(graph, subgraph):
#            print "GRAPHS EQUAL"
            return embedding

#        print "currVertices: " + str(currVertices )
	[fragments, allFragmentFaces, fragmentVOAs] = getFragmentFaces2(potentialEdges, currEdges, currVertices, faces)
	potentialFaces = cloneGraph(allFragmentFaces)

#        print "allFragmentFaces: " + str(allFragmentFaces)
#        print "faces: " + str(faces)
	for currFragment in fragments:
		fragmentFaces = allFragmentFaces[currFragment]
		for currFace in fragmentFaces:
                    currFaceEmbeddingGraph = getGraphFromVerticesInOrder(embedding[currFace])

                    if type(currFragment[0]) is tuple:
                       currFragmentGraph = getGraphFromEdgeTupleList(list(currFragment))
                    else:
                       currFragmentGraph = getGraphFromEdgeTupleList([currFragment])

#                    currFragmentGraph = getGraphFromEdgeTupleList([currFragment])
                    currGraph = joinGraphs(currFragmentGraph, currFaceEmbeddingGraph)
                    tempFace = {}
                    tempFace[1] = embedding[currFace] #Not 100% sure about this!
#                    print "\n\n\n\nIT HAPPENS HERE\n\n\n\n"
#                    print "currGraph: " + str(currGraph)
#                    print "currFaceEmbeddingGraph: " + str(currFaceEmbeddingGraph)
#                    print "tempFace: " + str(tempFace)
                    if not planarityTest3(currGraph, currFaceEmbeddingGraph, tempFace): #embedding[currFace]
                            potentialFaces[currFragment].remove(currFace)
#        print "\n\n ==============\ngraph: " + str(graph)
#        print "subgraph: " + str(subgraph)
#        print "faces: " + str(faces)
#        print "fragments: " + str(fragments)
#        print "potentialFaces: " + str(potentialFaces)
#        print "fragmentVOAs: " + str(fragmentVOAs)
#        print "NOW CALLING EMBEDDING TEST \n ==============\n\n"
	return embeddingTest(graph, subgraph, faces, fragments, potentialFaces, fragmentVOAs)

def embeddingTest(graph, subgraph, faces, fragments, potentialFaces, fragmentVOAs):
    """NEED TO DOCUMENT THIS URGENTLY! WHAT DOES EACH VARIABLE MEAN???
    graph - graph to embedd in subgraph
    subgraph - current graph to which we will be adding fragments of first variable originally it's the V8.
    faces - current faces of subgraph.
    fragments - fragments of graph that can be added to subgraph
    potentialFaces - face candidates to embedd each fragment in subgraph

    QUESTION: Do I even need to be passing graph here?
    """
#    print "====embeddingTest======"
#    print "fragments: " + str(fragments)
#    print "potentialFaces: " + str(potentialFaces)
#    print "====end of embeddingTest=====\n"
    ## STAGE 2 - STEP 3:
#    print fragments
    fragmentToEmbed = fragments[0]
    numberOfFaces = len(potentialFaces[fragmentToEmbed])
    for currFragment in fragments:
            if len(potentialFaces[currFragment]) == 0:
#                print "NOT ENOUGH FRAGMENT FACES"
                return False
            elif len(potentialFaces[currFragment]) == 1:
                numberOfFaces = len(potentialFaces[currFragment])
                fragmentToEmbed = currFragment
            elif len(potentialFaces[currFragment]) < numberOfFaces:
                numberOfFaces = len(potentialFaces[currFragment])
                fragmentToEmbed = currFragment
    #embedd fragmentToEmbedd. if successful, return True, else try other face if possible.

    ## STAGE 2 - STEP 4:
    if numberOfFaces > 2:
            print "NUMBER OF FACES IS GREATER THAN 2 - SOMETHING IS WRONG"

    facesToEmbedd = potentialFaces[fragmentToEmbed]
    for i in range(numberOfFaces):
            currEmbeddingFaces = cloneGraph(faces)
            currGraph = cloneGraph(subgraph)
            currFragments = cloneList(fragments)
            currFragments.remove(fragmentToEmbed)

            currFace = facesToEmbedd[i]
            currFaceAsGraph = getGraphFromVerticesInOrder(currEmbeddingFaces[currFace])
#            newSubgraph = joinGraphs(currFaceAsGraph, getGraphFromEdgeTupleList([fragmentToEmbed]))
#            print "fragmentToEmbed: " + str(fragmentToEmbed)
            if type(fragmentToEmbed[0]) is tuple:
#                print "getGraphFromEdgeTupleList([fragmentToEmbed]): " + str(getGraphFromEdgeTupleList(list(fragmentToEmbed)))
                newSubgraph = joinGraphs(currFaceAsGraph, getGraphFromEdgeTupleList(list(fragmentToEmbed)))
            else:
#                print "getGraphFromEdgeTupleList([fragmentToEmbed]): " + str(getGraphFromEdgeTupleList([fragmentToEmbed]))
                newSubgraph = joinGraphs(currFaceAsGraph, getGraphFromEdgeTupleList([fragmentToEmbed]))
            currFaceAsEmbedding = {}
            currFaceAsEmbedding[currFace] = currEmbeddingFaces[currFace]
#            print "\n\nnewSubgraph: " + str(newSubgraph)
#            print "currFaceAsGraph: " + str(currFaceAsGraph)
#            print "fragmentToEmbed: " + str(fragmentToEmbed)
#            print "currFaceAsEmbedding: " + str(currFaceAsEmbedding)
            newFaces = planarityTest3(newSubgraph, currFaceAsGraph, currFaceAsEmbedding)
#            print "newFaces: " + str(newFaces)
            ##NEW CHANGE IF PLANARITY TESTING RETURNS FALSE
            if newFaces:
            ##END OF NEW CHANGE IF PLANARITY TESTING RETURNS FALSE

                currEmbeddingFaces.pop(currFace)
                for newFaceKey in newFaces.keys():
                    currEmbeddingKeys = currEmbeddingFaces.keys()
                    if newFaceKey not in currEmbeddingKeys:
                        currEmbeddingFaces[newFaceKey] = newFaces[newFaceKey]
                    else:
                        i = 1
                        doneFindingKeyValue = False
                        while not doneFindingKeyValue:
                            if i not in currEmbeddingKeys:
                                currEmbeddingFaces[i] = newFaces[newFaceKey]
                                doneFindingKeyValue = True
                            else: i+=1

                if type(fragmentToEmbed[0]) is tuple:
                   currGraph = joinGraphs(currGraph, getGraphFromEdgeTupleList(list(fragmentToEmbed)))
                else:
                   currGraph = joinGraphs(currGraph, getGraphFromEdgeTupleList([fragmentToEmbed]))
#                currGraph = joinGraphs(currGraph, getGraphFromEdgeTupleList([fragmentToEmbed]))
                currPotentialFaces = cloneGraph(potentialFaces)
                currPotentialFaces = updatePotentialFaces(currFragments, fragmentVOAs, currEmbeddingFaces)

#                print "\n===========\ngraph: " + str(graph)
#                print "currGraph: " + str(currGraph)
#                print "currEmbeddingFaces: " + str(currEmbeddingFaces)
#                print "currFragments: " + str(currFragments)
#                print "currPotentialFaces: " + str(currPotentialFaces)
#                print "fragmentVOAs: " + str(fragmentVOAs)
#                print "RECURSIVE CALLING EMBEDDING TEST \n ==============\n\n"

                if graphsEqual(graph, currGraph): return currEmbeddingFaces
                returnEmbedding = embeddingTest(graph, currGraph, currEmbeddingFaces, currFragments, currPotentialFaces, fragmentVOAs)
                if not returnEmbedding == False:
                    return returnEmbedding


    return False


def updatePotentialFaces(currFragments, fragmentVOAs, currEmbeddingFaces):
    """Code:

    Now, we need to update the face candidates for only the fragments that have that face we just removed
    as a face candidate. To do it, check which vertices of attachment each fragment used to attach in the face,
    and then on all the new faces added, check whether any of the new faces has all of the vertices of attachment
    of the fragment being considered.

    If current face is in fragment potentials, then remove it, and check if the vertices of attachment for that fragment
    is in any of the new faces. if VOAs are in new faces, for each face, add that face for that fragment's potential faces

    """

    faces = cloneGraph(currEmbeddingFaces)
    fragmentFaces = {}
    for fragment in currFragments:
        fragmentFaces[fragment] = []
        for f in faces.keys():
            if fragmentVOAs[fragment][0] in faces[f] and fragmentVOAs[fragment][1] in faces[f]:
                fragmentFaces[fragment].append(f)
    return fragmentFaces



def planarityTest2(originalGraph, originalSubGraph, embedding):
#    print "\n\n\n Planarity Test Called \n\n ========\n"
#    print "Graph: " + str(originalGraph)
#    print "SubGrahp: " + str(originalSubGraph)
#    print "Embedding (cycle): " + str(embedding) + '\n'
    graph = cloneGraph(originalGraph)
    currGraph = cloneGraph(originalSubGraph)
    potentialEdges = getEdgeTuples(graph)
    currVertices = getVerticesInOrder(currGraph)
#    currGraph = cloneGraph(originalSubGraph)
    currEdges = getEdgeTuples(currGraph)
#    print originalSubGraph
#    print currGraph
    faces = cloneGraph(embedding)
#    print "faces: " + str(faces)
    done = False
    while not done:
            wrongInput = [(1, 4), (1, 6), (1, 5), (2, 4), (2, 6)]

            if potentialEdges == wrongInput:
                print "HOORAY! WrongInput found!"

            [fragments, fragmentFaces, fragmentVOAs] = getFragmentFaces2(potentialEdges, currEdges, currVertices, faces)
#            print "Potential Edges: " + str(potentialEdges)
#            print "Curr Edges: " + str(currEdges)
#            print "Fragments: " + str(fragments)
            if graphsEqual(originalGraph, currGraph):
                    done = True
#                    print "PLANAR"
                    return faces

            if len(fragments) > 0:
                    currFragment = fragments[0]
                    for k in fragmentFaces.keys():
                            if len(fragmentFaces[k]) == 0:
#                                    print currGraph
#                                    print originalGraph
#                                    print fragments
#                                    print faces
#                                    print "NON PLANAR"
                                    return False
                            elif len(fragmentFaces[k]) < len(fragmentFaces[currFragment]):
                                    currFragment = k

                    if len(currFragment) == 2 and type(currFragment[0]) == int:
                            path = list(currFragment)
                            candidateFace = fragmentFaces[currFragment][0]
                            candidateVertices = faces[candidateFace]
                    else:

                            candidateFace = fragmentFaces[currFragment][0]
                            candidateVertices = faces[candidateFace]
                            currFragmentEdges = list(currFragment)
                            pathVerticesOfAttachment = []
#                            print "candidate vertices, curr fragment"
#                            print candidateVertices
#                            print currFragment
#                            print candidateFace

                            for e in currFragmentEdges:
                                    if e[0] in candidateVertices:
                                            pathVerticesOfAttachment.append(e[0])
                                    elif e[1] in candidateVertices:
                                            pathVerticesOfAttachment.append(e[1])

                            currFragmentGraph = getGraphFromEdgeTupleList(currFragmentEdges)
#                            print pathVerticesOfAttachment
#                            print currFragmentGraph
                            path = getPath(pathVerticesOfAttachment, currFragmentGraph)

                    if len(path) == 0:
                        print "\nERROR: Finding Path between vertices of attachment in face: " + str(candidateFace)
                        return False

#                    print 'candidateVertices' + str(candidateVertices)
#                    print 'fragments: ' + str(fragments)
#                    print 'path: ' + str(path)

                    newFace0 = cloneList(path)
                    lastV = newFace0[len(newFace0)-1]
                    newFace1 = cloneList(path)
                    newFaceBeginningIndex = candidateVertices.index(lastV)
                    newFaceEndIndex = candidateVertices.index(newFace0[0])
                    i = 0; j = 0
                    if newFaceBeginningIndex < newFaceEndIndex:
                            i = newFaceBeginningIndex
                            j = newFaceEndIndex
                    else:
                            j = newFaceBeginningIndex
                            i = newFaceEndIndex
                    newFace0 = newFace0 + list(candidateVertices[i+1:j])
                    newFace1 = newFace1 + list(candidateVertices[j+1:])
                    newFace1 = list(candidateVertices[:i]) + newFace1
                    faces[candidateFace] = tuple(newFace0)
                    faces[len(faces)+1] = tuple(newFace1)
                    newGraph = addPathToGraph(currGraph, path)
                    if graphsEqual(newGraph,currGraph):
                            return faces
                            done = True
                    else:
                            currGraph = newGraph
                            currVertices = getVertices(currGraph)
                            currEdges = getEdgeTuples(currGraph)

## END OF STAGE 2 ALGORITHM

## PLANARITY TESTING CODE BELOW THIS LINE




if __name__ == "__main__":
    import sys
    main();
