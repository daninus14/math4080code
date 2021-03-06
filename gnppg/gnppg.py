from src.archdeacon import *
from time import time
import os
import src.et
__author__="Daniel Nussenbaum"
__date__ ="$Sep 02, 2012 04:15:32 PM$"

def testing_et():
    # et.tpp(range(5))
    g = [4, [3, 2, 3, 4], [3, 1, 3, 4], [3, 1, 2, 4], [3, 1, 2, 3]]
    et.gr(g)

def main():

    t0 = time()
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        # print "Help (winter) is coming...." 
        print "Hello. This software is part of ongoing research of Professor Robin Thomas' lab on Graph Theory"
        print "The latest version of this project can be downloaded at https://github.com/daninus14/math4080code"
        print "Project Dependencies: SAGE - http://www.sagemath.org/"
        print "To run the entire project use the following command:"
        print "\"sage gnggp.py -fMMGf\" \n"
        # print "the software"
        print "The software can generate all non-embeddable graphs by adding obstructions starting from a V8 and then find the"
        print "minor minimal non projective plane embeddable graphs"
        print "To only generate this V8 non-embeddable graphs, run the command \"sage gnggp.py -gNPP\" "
        print "running this command will find all such graphs, and create a new directory named \"output\" with the graphs generated"
        print "the software can also find the minor minimal non-embeddable projective planar graphs from those obtained by adding"
        print "obstructions to the V8. To run this, run the command above and then run the command \"sage gnggp.py -fMMG\" " 
        print "alternatively, you can run everything together in one command with \"sage gnggp.py -fMMGf\" "
        print "\nSummary of Options:"
        # print "\t-et which takes 3 arguments and tests embedding"
        print "\t-gNPP which generates Non-Projective Planar (gNPP) graphs with options -output and -keepWork"
        print "\t-fMMG which find the minor minimal Non-Projective Planar (gNPP) graphs for the graphs generated by -gNPP"
        print "\t-fMMGf which generates the minor minimal Non-Projective Planar (gNPP) graphs from scratch"
    elif sys.argv[1] == "-et":
        et(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == '-gNPP': #Generate Non-Projective Planar (gNPP) graphs
        keepWork = False
        output = False
        if len(sys.argv) > 2:
            for condition in sys.argv[2:]:
                if condition == '-output':
                    output = True
                elif condition == '-keepWork':
                    keepWork = True
        generateAllNonProjectivePlanarGraphs(output, keepWork)
    elif sys.argv[1] == '-test':
        if sys.argv[2] == '-gNPP':
            print 'FIGURE OUT HOW TO CALL A TEST!'
    elif sys.argv[1] == "-fMMG":
        findMinorMinimalGraphs()
    elif sys.argv[1] == "-fMMGf":
        findMinorMinimalGraphs(False)
    elif sys.argv[1] == '--results':
        show_prev_results(sys.argv[2])
    else: print sys.argv
    t1 = time()
    print "Total Time: " + str(t1-t0)

## STAGE 3 ALGORITHMS
if __name__ == "__main__":
    import sys
    main()
    # testing_et()

