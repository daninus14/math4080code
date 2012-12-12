/* gem.c: test for gembed file.
   Programmed by Christopher Carl Heckman, March 1997. */

#include "graph.h"
#undef NAME
#define NAME "gem: "
#define CR '\n'
#define maxverts 30

int freadgraph (g, f) graph (g); FILE *f;
{
vertex i, j, u, v; unsigned temp;

if (fscanf (f, "%u", &temp) != 1) return 1; 
if ((**g = (char) temp) > maxverts - 2) return 2;
for (i = 1; i <= **g; i++) {
	if (fscanf (f, "%u", &temp) != 1) return 3;
	if ((degree (g,i) = (char) temp) > maxdeg - 2) return 4;
	for (j = 1; j <= degree (g, i); j++)
		if (fscanf (f, "%u", &temp) != 1) return 5;
		else g [i][j] = (char) temp;
	}
for (i = 1; i <= **g; i++) for (j = 1; j <= degree(g, i); j++) {
	if (g [i][j] > **g) return 6;
	for (u = g [i][j], v = 1; (v <= degree(g, u)) && (g[u][v] != i); v ++);
	if (v > degree(g, u)) return 7;
	}
return 0;
}


char main (argc, argv) char argc; char *argv[];
{
graph (g);
FILE *ingraphs; unsigned loop, numgrs; int gem, code;

puts ("\n\n" NAME "version 4.1, March 1997\n");
if (argc != 3) return puts (NAME "usage: embed SURFACE GRAPH_FILE\n");
switch (tolower (argv [1][0])) {
	case 'p' 	: break;
	case 'x'	: argv [1][0] = 'p'; break;
	case 't'	: break;
	case 'h'	: argv [1][0] = 't'; break;
	case 's'	: argv [1][0] = 's'; break;
	default 	: exit (puts (NAME ERR "SURFACE must be one of xhtps\n"));
	}
R_OPEN (ingraphs, argv [2]);
if (fscanf (ingraphs, "%d", &numgrs) != 1) return puts (NAME ERR "number of graphs expected");
for (loop = 1; loop <= numgrs; loop ++) {
	printf (NAME "processing graph #%d of %d in %s\n", loop, numgrs, argv [2]);
	if (code = freadgraph (g, ingraphs)) {
		printf (NAME "illegal graph, code %u\n", code);
		continue;
		}
	fflush (stdout); /* system ("date"); */
	gem = gembed (g, argv [1][0], 1);
/*	system ("date"); */
	switch (gem) {
		case 0: printf (NAME "no ");
			switch (argv [1][0]) {
				case 'p' : printf ("projective"); break;
				case 't' : printf ("toroidal"); break;
				case 's' : printf ("spindle"); break;
				default  : printf ("ERROR"); 
				}
			puts (" embeddings");
			break;
		case 2: puts (NAME "graph is planar");
			break;
		case 1:
		case 3: puts (NAME "graph embeds"); 
			break;
		default: puts (NAME "whoops -- unknown result from gembed()");
			break;
		}
	putchar (CR);
	}
fclose (ingraphs);
printf (NAME "finished with %s\n\n", argv [2]);
// fclose (ingraphs);
return 0;
}
