# from archdeacon import *
from time import time
import os
import et
__author__="Daniel Nussenbaum"
__date__ ="$Sep 02, 2012 04:15:32 PM$"

def testing_et():
    # et.tpp(range(5))
    g = [4, [3, 2, 3, 4], [3, 1, 3, 4], [3, 1, 2, 4], [3, 1, 2, 3]]
    et.gr(g)

def main():

    t0 = time()
    if len(sys.argv) == 1 or sys.argv[1] == "--help":
        print "Help (winter) is coming...." 
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
    else: print sys.argv
    t1 = time()
    print "Total Time: " + str(t1-t0)

## STAGE 3 ALGORITHMS
if __name__ == "__main__":
    import sys
    # main()
    testing_et()

