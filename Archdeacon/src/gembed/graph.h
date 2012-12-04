#include <stdio.h>
#include <string.h>

/* #define maxverts 30 */
#define maxdeg maxverts
#define maxedges (3 * (maxverts) + 2)
#define ERR "error: "

#define graph(g) vertex g [maxverts][maxdeg]
#define degree(g,x) ((g)[x][0])
void *malloc (size_t);
// void *malloc (unsigned int);
#define ALLOC(result, count, type)							\
        if ((result = (type *) malloc ((unsigned) (count) * sizeof (type))) == NULL){	\
                puts ("out of memory");							\
                exit (1);								\
                }
#define R_OPEN(p,f) {								\
	if ((p = fopen (f, "r")) == NULL)  {					\
		printf ("can't open %s.  program teminated\n\n", f);		\
		exit (1);							\
		}								\
	}
#define copy(h,g) {register vertex i, j;						\
	for (i = **h = **g; i ; i--) for (j = degree (h, i) = degree (g, i); j ; j--)	\
		h [i][j] = g [i][j]; }

#if maxverts > 40
	typedef unsigned vertex;
#else
	typedef char vertex;
#endif
