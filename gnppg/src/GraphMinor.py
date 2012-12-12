#!/usr/bin/env sage -python
import os
from graphFunctions import getGraphFromEdgeTupleList
from graphFunctions import cloneGraph
from graphFunctions import cloneList
from graphFunctions import *
from graphFunctions import replaceEdgesWithPaths
from stage2 import *
from copy import deepcopy
import cPickle as pickle
import pprint

from sage.all import *

__author__="Daniel Nussenbaum"
__date__ ="$Mar 30, 2012 3:49:46 PM$"

class GraphMinor:
    edge_list = []
    vertices = []


    def __init__(self, given_edges, given_vertices):
        self.edge_list = deepcopy(given_edges)
        self.vertices = deepcopy(given_vertices)

    def __str__(self):
        return "GraphMinor: " + str(len(self.vertices)) + " vertices and " + str(len(self.edge_list)) + " edges"

    def __repr__(self):
        return "<GraphMinor: " + str(len(self.vertices)) + "," + str(len(self.edge_list)) + ">"

    @classmethod
    def from_sage_graph(cls, sage_graph):
        temp_edge_list = sage_graph.edges()
        temp_vertices = sage_graph.get_vertices()
        return cls(temp_edge_list, temp_vertices)

    @classmethod
    def from_sage_graph_label(cls, sage_graph_label):
        sage_graph = Graph(sage_graph_label)
        temp_sage_edge_list = sage_graph.edges()
        temp_edge_list = [(x,y) for (x,y,z) in temp_sage_edge_list]
        temp_vertices = sage_graph.get_vertices()
        return cls(temp_edge_list, temp_vertices)

    def get_list_of_minors(self):
        # by contracting each edge
        edge_contracted_list = []
        for e in self.edge_list:
            temp_vertices = deepcopy(self.vertices)
            temp_edge_list = deepcopy(self.edge_list)
            [temp_num_vertices, temp_edge_list] = get_graph_contract_edge(temp_edge_list,e)
            edge_contracted_list.append(GraphMinor(temp_edge_list, [x+1 for x in range(temp_num_vertices)]))

        # print "edge_contracted_list: " + str(len(edge_contracted_list))
        # pprint.pprint(edge_contracted_list)
        return edge_contracted_list

    def get_list_of_1_edge_removed(self):
        edge_removed_list = []
        for e in self.edge_list:
            temp_vertices = deepcopy(self.vertices)
            temp_edge_list = deepcopy(self.edge_list)
            temp_edge_list.remove(e)
            edge_removed_list.append(GraphMinor(temp_edge_list, temp_vertices))

        # print "edge_removed_list: " + str(len(edge_removed_list))
        # pprint.pprint(edge_removed_list)
        return edge_removed_list

    def get_gembed_format(self):
        # g = [4, [3, 2, 3, 4], [3, 1, 3, 4], [3, 1, 2, 4], [3, 1, 2, 3]]
        [number_of_vertices, self.edge_list] = relabel_edge_list(self.edge_list)
        self.vertices = [x + 1 for x in range(number_of_vertices)]
        # print "number_of_vertices: ", number_of_vertices 
        # print "self.vertices: ", self.vertices 
        gembed = [number_of_vertices]
        # gembed = [len(self.vertices)]

        graph_dic = getGraphFromEdgeTupleList(self.edge_list)
        # pprint.pprint(graph_dic)
        # this assumes labelling is correct!
        for i in range(len(self.vertices)):
            gembed += [[len(graph_dic[i+1])] + graph_dic[i+1]]

        # print "gembed: " + str(len(gembed) )
        # pprint.pprint(gembed)
        return gembed

    def getCanonicalLabel(self):
        tempSageGraph = Graph()
        tempSageGraph.add_vertices(self.vertices)
        tempSageGraph.add_edges(self.edge_list)
        tempSageLabel = tempSageGraph.canonical_label()
        return tempSageLabel.graph6_string()

    def to_pretty_string(self):
        string_pretty =  "Graph Minor with " + str(len(self.vertices)) + " vertices and " + str(len(self.edge_list)) + " edges"
        string_pretty += "\nvertices: " + str(self.vertices)
        string_pretty += "\negdes: " + str(self.edge_list)
        return string_pretty



def main():
    import embeddingtest
    # dirOutput = os.getcwd()
    # folders = dirOutput.split('/')
    # dirOutput = dirOutput.strip(folders[-1])
    # dirOutput = dirOutput + "output/"
    # filename = "labels-8262"
    # labels_list = pickle.load( open( dirOutput + filename, "rb" ) )
    # # print labels_list
    # g = GraphMinor.from_sage_graph_label(labels_list[0])
    g = GraphMinor.from_sage_graph_label('I?TcdB?Nw')
    print "g: ",g
    print "g: ",relabel_edge_list(g.edge_list)[1]
    print g.get_gembed_format()
    print "embeddingtest: " + str(embeddingtest.graph_embeds(g.get_gembed_format()))
    # g.get_list_of_1_edge_removed()

    # gstring = graphs.CompleteGraph(4).graph6_string()
    # g = GraphMinor.from_sage_graph_label(gstring)
    # l = g.get_list_of_1_edge_removed()
    
    # l = [g.get_list_of_minors()[0]]
    # for gr in l:
    #     print gr
    #     print gr.edge_list
    #     print "\n\n"
    #     print gr.get_gembed_format()
    #     print "embeddingtest: " + str(embeddingtest.graph_embeds(gr.get_gembed_format()))



if __name__ == "__main__":
    print "hello GraphMinor"
    main()