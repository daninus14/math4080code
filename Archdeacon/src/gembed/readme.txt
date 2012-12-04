
			GEMBED 5.3 (November 2006)

Congratulations on your receipt of the program gembed. This program has been
extensively tested to provide years of accurate results related to embeddability 
of graphs on certain surfaces.

(1) The set of files you have received should include the following:

	makefile	A file for automatic compilation of programs
	graph.h		Macros for graph manipulation
	gembed.c	The main guts of the program
	gem.c		A driver
	inputg.txt  A sample input file for gem.c

To compile the program gem, issue the following command:

	gcc -o gem gem.c gembed.c


(2) The program gem takes a special file, which is of the form:

	#graphs

	#vertices (in 1st graph)
	degree of vertex 1    (list of neighbors, separated by blank spaces)
	degree of vertex 2    (list of neighbors, separated by blank spaces)
	(etc.)
	
	#vertices (in 2nd graph)
	(etc.)
	
	(etc.)


(3) To test embeddability of these graphs, issue the command

	gembed S graph_file

where, if S is one of tThH, will produce all toroidal embeddings of all graphs 
in the file graph_file, or report that there are none; if S is p,P,x,X, it does
the same actions with respect to the projective plane; if S is s or S, GEMBED
peforms the same actions for the spindle surface. A message will also be shown 
if the graph happens to be planar. Consult the source code for gem.c to get
the syntax for an arbitrary call to GEMBED.


(4) Possible error messages which may be reported (and their fixes) are:

	SURFACE must be one of xhtps        See (3).
	number of graphs expected           See (2).
	maxverts exceeded                   See (5A).
	maxedges exceeded                   See (5A).
	maxdeg exceeded                     See (5A).
	invalid graph, vertex #* #*         See (5B).
	maxverts exceeded by vertex label   See (5C).

While this program has been extensively tested, it is still possible that some
bugs will show up. If you see any of the following, please inform the programmer
at the address given at the end, with as much information as possible regarding
your setup:

	too many edges added to g0
	vertex exists
	edge exits
	vetex does not exist
	edge does not exist
	parallel edge in tested graph
	vertex label is zero
	vertex has degree zero
	subdividing loop not allowed
	unidentified option * encountered in setupfiles()
	insufficient arguments on re-read

Other messages which might arise but serve only as warnings (concerning input
graphs) are:

	parallel edge (* *) deleted
	loop at * deleted


(5) Fixes which can be made by the user are:

	(A) Edit the source code. There is a line which says
	
		#define maxverts N
	
	where N is some number. Increase N to any value less than 65530,
	save the modified source code, and recompile. If maxdeg has been
	exceeded, there are too many parallel edges in a graph somewhere. If
	you did not intend this, send a message to the programmer at the 
	address below. If maxedges is exceeded, then the graph is not
	embeddable because it simply has too many edges.

	(B) GEMBED had trouble reading your graph. Somewhere in the adjacency
	list, there is a mistake; it does not define a valid graph. Re-check
	your graph file.

	(C) GEMBED assumes that the vertices are labeled 1,2, ... up to the
	number of vertices in the graph. A graph in your graph file makes
	reference to a vertex which has a label outside of this range. Check
	typing for a missed space. 


(6) New surfaces to check for embeddability will become available when they are 
realized.


(7) All correspondence in regards to this program should be sent to the
address below. 

			Christopher Carl Heckman
			Dept. of Mathematics and Statistics
			Arizona State University
			Tempe, AZ 85287-1804
			
			email: checkman@math.asu.edu
