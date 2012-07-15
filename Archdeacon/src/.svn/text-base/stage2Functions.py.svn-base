#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.
from graphFunctions import *
__author__="Daniel Nussenbaum"
__date__ ="$Mar 13, 2012 10:12:06 AM$"
__all__ = ["getFragmentFaces2", "planarityTest3"]

def getFragmentFaces2(potentialEdges, currEdges, verticesOfAttachment, faces):
	"""

	potentialEdges -- all edges in beginning graph
	currEdges -- edges on current graph
	verticesOfAttachment -- vertices of current graph to which edges can be attached to
	faces -- dictionary with faces as keys and vertices as values

	Algorithm:
	1) Remove edges on current graph from potentialEdges and call this new set potentialFragmentEdges
	2) Find all fragments that are edges with both vertices in the graph.
	2.1) Determine the faces in which those fragments exist.
	2.3) Remove those edges from potentialEdges.
	3) Select an Edge from potentialEdges that is adjacent to the original graph in at least one edge.
	3.1) While there exist open vertices of the current edge set do:
	(an open vertex is the vertex of an edge that is not part of another edge in the same set, or adjacent to the original graph)
	3.2) find the other edge that connetcs to each open vertex remove from potentialEdges,
	or determine if it's not empty because it is in the original graph.
	3.3) if no edge was added to the set, fragment is complete
	3.4) go on to next adjacent edge to the original graph in the potential edges, repeat 3.2 and 3.3
	3.5) when potneialEdges is empty, end loop.

	This returns Fragments and a dictionary with each fragment's face.
	Fragments is a list of fragments. Each fragment is a set of edges. Format is [[()]]

	Notes: Change potentialEdges name with allEdges. Then make a method for doing edges set a minus edge set b.

	"""
#        print "\n\n\n\ngetFragmentFaces2\n BEGINING"
#        print "potential edges: " + str(potentialEdges)
#        print "curr edges: " + str(currEdges)
#        print "VOAs: " + str(verticesOfAttachment)
#        print "faces" + str(faces)


	potentialFragmentEdges = []
	for e in potentialEdges:
		if e not in currEdges:
			potentialFragmentEdges.append(e)
#        print "\n\n potentialFragmentEdges: " + str(potentialFragmentEdges)

        copyOfPotentialFragmentEdges = cloneList(potentialFragmentEdges)

#        print "copyOfPotentialFragmentEdges: " + str(copyOfPotentialFragmentEdges)

	fragmentFaces = {}
        fragmentVOAs = {}
	fragments = []
	for e in copyOfPotentialFragmentEdges:
		if e[0] in verticesOfAttachment and e[1] in verticesOfAttachment:
#                        print "edge considered: " + str(e)
			fragments.append(e)
			potentialFragmentEdges.remove(e)
			fragmentFaces[(e)] = []
                        fragmentVOAs[(e)] = list(e)
			for f in faces.keys():
				if e[0] in faces[f] and e[1] in faces[f]:
					fragmentFaces[(e)].append(f)
#                                        print "Edge: " + str(e) + " added to potential face: " + str(f)
#                                else: print "edge: " + str(e) + " not in face: " + str(faces[f]) + " key: " + str(f)

#	print "Edge Fragments: " + str(fragments)
#	print "Edge Fragment Faces: " + str(fragmentFaces)


	# Select an edge from potentialFragmentEdges that has a vertex of attachment, then find the fragment.
	while len(potentialFragmentEdges) > 0:
#            print "this should not be here! because this should be empty: " + str(potentialFragmentEdges)
            tempEdge = potentialFragmentEdges[0]
            potentialFragmentEdges.remove(tempEdge)
            edgesToExplore = [tempEdge]
            currFragment = []
            newEdgesToExplore = []
            linksInVOA = []
            done = False
            while not done:
                for e in edgesToExplore:
                    for i in range(2):
                        if e[i] not in verticesOfAttachment:
                            clonePotentialFragmentEdges = cloneList(potentialFragmentEdges)
                            for ej in clonePotentialFragmentEdges:
                                if e[i] in ej: ## if there are edges which have the same vertices, this breaks!
                                    newEdgesToExplore.append(ej)
                                    potentialFragmentEdges.remove(ej)
                        else:
                            linksInVOA.append(e[i])
                    currFragment.append(e)
                    edgesToExplore.remove(e)
                if len(newEdgesToExplore) == 0 and len(edgesToExplore) == 0:
                    done = True
#                    print "\n while loop is done with following values:"
#                    print "edges to explore: " + str(edgesToExplore)
#                    print "newEdgesToExplore: " + str(newEdgesToExplore)
#                    print "potentialFragmentEdges: " + str(potentialFragmentEdges)
#                    print "clonePotentialFragmentEdges: " + str(clonePotentialFragmentEdges)
#                    print "\n"
                else:
                    edgesToExplore = edgesToExplore + newEdgesToExplore
                    newEdgesToExplore = []

            currFragmentFaces = faces.keys()
#            print "linksInVOA: " + str(linksInVOA)
#            print "currFragmentFaces: " + str(currFragmentFaces)
#            print "faces: " + str(faces)
            tempCurrFragmentFaces = cloneList(currFragmentFaces)
            for v in linksInVOA:
                for f in currFragmentFaces:
                    if v not in faces[f]:
                        if f in tempCurrFragmentFaces:
                            tempCurrFragmentFaces.remove(f)
#                        currFragmentFaces.remove(f)

            currFragmentFaces = tempCurrFragmentFaces
#            print "currFragment: " + str(currFragment)
#            print "currFragmentFaces: " + str(currFragmentFaces)
            
            if 1 != len(currFragment):
                fragments.append(tuple(currFragment))
                fragmentFaces[tuple(currFragment)] = currFragmentFaces
                fragmentVOAs[tuple(currFragment)] = cloneList(linksInVOA)
            else:
                fragments += currFragment
                fragmentFaces[currFragment[0]] = currFragmentFaces
                fragmentVOAs[currFragment[0]] = cloneList(linksInVOA)

#            print fragments


#	print "\n\n All Fragments: " + str(fragments)
#	print "\n\n All Fragment Faces: " + str(fragmentFaces)


#        print "\n\n\n\ngetFragmentFaces2\n END"
	return [fragments, fragmentFaces, fragmentVOAs]



def planarityTest3(originalGraph, originalSubGraph, embedding):
    """THIS PLANARITY TESTING AIMS TO SOLVE PROBLEMS ENCOUNTERED WHEN A FRAGMENT IS NOT 2 CONNECTED WITH THE GRAPH.
    CAUTION! ASSUMPTION BROKEN. PROGRAM MAY CRASH!!!"""
#    print "\n\n\n Planarity Test Called \n\n ========\n"
#    print "Graph: " + str(originalGraph)
#    print "SubGrahp: " + str(originalSubGraph)
#    print "Embedding (cycle): " + str(embedding) + '\n'
    graph = cloneGraph(originalGraph)
    currGraph = cloneGraph(originalSubGraph)
    potentialEdges = getEdgeTuples(graph)
    currVertices = getVerticesInOrder(currGraph)
    currEdges = getEdgeTuples(currGraph)
    faces = cloneGraph(embedding)
#    print "faces: " + str(faces)
    done = False
    while not done:
            [fragments, fragmentFaces, fragmentVOAs] = getFragmentFaces2(potentialEdges, currEdges, currVertices, faces)
#            print "\n\nPotential Edges: " + str(potentialEdges)
#            print "Curr Edges: " + str(currEdges)
#            print "Fragments: " + str(fragments)
#            print "fragmentFaces: " + str(fragmentFaces)
#            print "fragmentVOAs: " + str(fragmentVOAs)
            if graphsEqual(originalGraph, currGraph):
                    done = True
#                    print "PLANAR"
#                    print "faces: " + str(faces)
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
                        print "IT HAPPENS HERE LINE 206"
                        print "\nERROR: Finding Path between vertices of attachment in face: " + str(candidateFace)
                        return False

#                    print 'candidateVertices' + str(candidateVertices)
#                    print 'fragments: ' + str(fragments)
#                    print 'path: ' + str(path)

                    newFace0 = cloneList(path)
                    lastV = newFace0[len(newFace0)-1]

                    """ THIS CODE IS ADDED HERE TO CHECK THAT THE LAST EDGE ACTUALLY CONNECTS. iF IT DOESN'T, SINCE THE GRAPH IS INTERNALLY 2
                    CONNECTED, THEN WE ASSUME THE EDGE CROSSES OVER OUTSIDE THE CYCLE. THIS IS ONLY IN THE CONTEXT OF THE STAGE 2 ALGORITHM!"""
                    ##BEGINNING OF NEW CODE
                    if lastV not in candidateVertices or newFace0[0] not in candidateVertices:
                        return False

                    ##ENDING OF NEW CODE

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
#                    print "newFace0: " + str(newFace0)
#                    print "list(candidateVertices[i:j]): " + str(list(candidateVertices[i:j]))
#                    print "candidateVertices: " + str(candidateVertices)
#                    newFace0 = newFace0 + list(candidateVertices[i+1:j])
                    if candidateVertices[i] == newFace0[0]:
                        tempNewFace0 = cloneList(newFace0)
                        tempNewFace0.reverse()
                        newFace0 = tempNewFace0 + list(candidateVertices[i+1:j])
                    elif candidateVertices[i] == newFace0[-1]:
                        newFace0 = newFace0 + list(candidateVertices[i+1:j])
                    if candidateVertices[j] == newFace1[-1]:
                        newFace1 = newFace1 + list(candidateVertices[j+1:])
                    elif candidateVertices[j] == newFace1[0]:
                        tempNewFace1 = cloneList(newFace1)
                        tempNewFace1.reverse()
                        newFace1 = tempNewFace1 + list(candidateVertices[j+1:])
                    else:
                        print "POTENTIALLY SOMETHING WENT WRONG WHEN CREATING THE FACE!\nPLEASE CHECK FACE CYCLE!"
                        print "list(candidateVertices[j+1:]): " + str(list(candidateVertices[j+1:]))
                        print "newFace1: " + str(newFace1)
                        newFace1 = newFace1 + list(candidateVertices[j+1:])
                        print "newFace1: " + str(newFace1)
                    newFace1 = list(candidateVertices[:i]) + newFace1
#                    print "newFace1: " + str(newFace1)
#                    print "newFace0: " + str(newFace0)
#                    print "candidateFace: " + str(candidateFace)
#                    print "len(faces)+1: " + str(len(faces)+1)
                    faces[candidateFace] = tuple(newFace0)
                    faces[findNewKey(faces)] = tuple(newFace1)
#                    print "faces: " + str(faces)
                    newGraph = addPathToGraph(currGraph, path)
                    if graphsEqual(newGraph,currGraph):
                            return faces
                            done = True
                    else:
                            currGraph = newGraph
                            currVertices = getVertices(currGraph)
                            currEdges = getEdgeTuples(currGraph)



if __name__ == "__main__":
    print "Hello World";
