# To change this template, choose Tools | Templates
# and open the template in the editor.

from graphFunctions import *

__author__="Daniel Nussenbaum"
__date__ ="$Feb 29, 2012 12:24:59 PM$"
__all__ = ["planarityTest", "getFragmentFaces"]

def planarityTest(originalGraph):
	graph = cloneGraph(originalGraph)
	[path, cycleGraph] = cycleDFS(graph)
	potentialEdges = getEdgeTuples(graph)

	currGraph = extractCycle(cycleGraph)
	currVertices = getVerticesInOrder(currGraph)
	currEdges = getEdgeTuples(currGraph)
	faces = {} # This is a dictionary of each face. Consider also storing a dictionary of each vertex and to which
	faces[1] = tuple(currVertices) # faces it belongs to
	faces[2] = tuple(currVertices)


	done = False
	while not done:
		[fragments, fragmentFaces, fragmentVOAs] = getFragmentFaces(potentialEdges, currEdges, currVertices, faces)
		if graphsEqual(originalGraph, currGraph):
			done = True
			print "PLANAR"
			return True

		if len(fragments) > 0:
			currFragment = fragments[0]
			for k in fragmentFaces.keys():
				if len(fragmentFaces[k]) == 0:
					print currGraph
					print originalGraph
					print fragments
					print faces
					print "NON PLANAR"
					return False
				elif len(fragmentFaces[k]) < len(fragmentFaces[currFragment]):
					currFragment = k
			#Now choose a path p between two vertices of attachment of the selected B (currFragment).
			# Embed P accross a face in F(B). Call resulting graph Gi+1 and update list of face boundries
			# if Gi+1 == Gi, return planar

			#This can be changed so that we do not loop through every vertex. Just get the graph, get the keys, check if a VOA is in keys()
			# and then just send it as the first vertex of the voa list! or as another parameter

			#~ print "curr fragment" + str(currFragment)
			#do case to manage when fragment is just an edge
			if len(currFragment) == 2 and type(currFragment[0]) == int:
				path = list(currFragment)
				candidateFace = fragmentFaces[currFragment][0]
				candidateVertices = faces[candidateFace]
			else:

				candidateFace = fragmentFaces[currFragment][0]
				candidateVertices = faces[candidateFace]
				currFragmentEdges = list(currFragment)
				pathVerticesOfAttachment = []
				for e in currFragmentEdges:
					if e[0] in candidateVertices:
						pathVerticesOfAttachment.append(e[0])
					elif e[1] in candidateVertices:
						pathVerticesOfAttachment.append(e[1])

				currFragmentGraph = getGraphFromEdgeTupleList(currFragmentEdges)
				path = getPath(pathVerticesOfAttachment, currFragmentGraph) #code this! get a path that has both edges
			#embed path in face, add to graph. update faces. compare graphs, old and new. if same, PLANAR
			if len(path) == 0:
				print "\nERROR: Finding Path between vertices of attachment in face: " + str(candidateFace)
				return False

			#Here the code is not the same as the algorith from the book. The reason is to account for the case where there is a
			#tree connected to a vertex of attachment or a cycle connected to a vertex of attachment.
			#In this case, there will be no path between 2 vertices of attachment. The result from the getPath
			#method will be also a path, just not attached to two vertices of attachment.

			newFace0 = cloneList(path)
			lastV = newFace0[len(newFace0)-1]
			newFace1 = cloneList(path)
			newFaceBeginningIndex = candidateVertices.index(lastV)
			#~ print "cv" + str(candidateVertices)
			newFaceEndIndex = candidateVertices.index(newFace0[0])
			i = 0
			j = 0
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
				return True
				done = True
			else:
				currGraph = newGraph
				currVertices = getVertices(currGraph)
				currEdges = getEdgeTuples(currGraph)




def getFragmentFaces(potentialEdges, currEdges, verticesOfAttachment, faces):
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
	potentialFragmentEdges = []
	for e in potentialEdges:
		if e not in currEdges:
			potentialFragmentEdges.append(e)
#        print "\n\n potentialFragmentEdges: " + str(potentialFragmentEdges)

	fragmentFaces = {}
        fragmentVOAs = {}
	fragments = []
	for e in potentialFragmentEdges:
		if e[0] in verticesOfAttachment and e[1] in verticesOfAttachment:
			fragments.append(e)
			potentialFragmentEdges.remove(e)
			fragmentFaces[(e)] = []
                        fragmentVOAs[(e)] = list(e)
			for f in faces.keys():
				if e[0] in faces[f] and e[1] in faces[f]:
					fragmentFaces[(e)].append(f)

	#~ print "Edge Fragments: " + str(fragments)
	#~ print "Edge Fragment Faces: " + str(fragmentFaces)


	# Select an edge from potentialFragmentEdges that has a vertex of attachment, then find the fragment.
	while len(potentialFragmentEdges) > 0:
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
                    #~ print "\n while loop is done with following values:"
                    #~ print "edges to explore: " + str(edgesToExplore)
                    #~ print "newEdgesToExplore: " + str(newEdgesToExplore)
                    #~ print "potentialFragmentEdges: " + str(potentialFragmentEdges)
                    #~ print "clonePotentialFragmentEdges: " + str(clonePotentialFragmentEdges)
                    #~ print "\n"
                else:
                    edgesToExplore = edgesToExplore + newEdgesToExplore
                    newEdgesToExplore = []

            currFragmentFaces = faces.keys()
            for v in linksInVOA:
                for f in currFragmentFaces:
                    if v not in faces[f]:
                        currFragmentFaces.remove(f)

            #~ print "currFragment: " + str(currFragment)
            #~ print "currFragmentFaces: " + str(currFragmentFaces)

            fragments.append(tuple(currFragment))
            fragmentFaces[tuple(currFragment)] = currFragmentFaces
            fragmentVOAs[tuple(currFragment)] = cloneList(linksInVOA)


	#~ print "\n\n All Fragments: " + str(fragments)
	#~ print "\n\n All Fragment Faces: " + str(fragmentFaces)


	return [fragments, fragmentFaces, fragmentVOAs]




if __name__ == "__main__":
    print "Hello World"
