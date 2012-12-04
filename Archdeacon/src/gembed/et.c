#include <Python.h> 
#include "graph.h"
#define maxverts 30

static PyObject* hello(PyObject* self, PyObject* args)
{
	const char* name;

	if(!PyArg_ParseTuple(args, "s", &name))
		return NULL;

	printf("Hello %s!\n", name);

	Py_RETURN_NONE;
}

static PyObject* tpp(PyObject* self, PyObject* args)
{
	PyObject* obj;
    PyObject* seq;
    int i, len; 
    PyObject* item;
    long arrayValue;

    if (!PyArg_ParseTuple(args, "O", &obj)){
        printf("Item is not a list\n");
        return NULL;
    }
    seq = PySequence_Fast(obj, "expected a sequence");
    len = PySequence_Size(obj);
    arrayValue = -5;
    printf("[\n");
    for (i = 0; i < len; i++) {
        item = PySequence_Fast_GET_ITEM(seq, i);

        PyObject* objectsRepresentation = PyObject_Repr(item);
        const char* s = PyString_AsString(objectsRepresentation);
        printf("%s\n", s);


        PyObject* objType = PyObject_Type(item);
        PyObject* objTypeString = PyObject_Repr(objType);
        const char* sType = PyString_AsString(objTypeString);
        printf("%s\n", sType);

        arrayValue = PyInt_AsLong(item);
        printf("Finally, a long: %d\n", arrayValue);

    }
    Py_DECREF(seq);
    printf("]\n");
	printf("Item is a list!\n");

	Py_RETURN_NONE;
}

static PyObject* gr(PyObject* self, PyObject* args)
{

    // Making Graphs
    vertex u, v; unsigned temp;
    graph (g);
    int gem;
    // vertex i, j, u, v; unsigned temp;
    // Finish making graphs
    PyObject* obj;
    PyObject* seq;
    int i, len; 
    PyObject* item;
    long arrayValue;

    int numberOfVertices = 0;

    if (!PyArg_ParseTuple(args, "O", &obj)){
        printf("Item is not a list\n");
        return NULL;
    }
    seq = PySequence_Fast(obj, "expected a sequence");
    len = PySequence_Size(obj);
    arrayValue = -5;
    printf("[\n");
    for (i = 0; i < len; i++) {
        item = PySequence_Fast_GET_ITEM(seq, i);

        

        if(i == 0){
            // should add a check to make sure it is an integer!
            numberOfVertices = PyInt_AsLong(item);   
            printf("numberOfVertices: %d\n", numberOfVertices);
            // graph creation
            if ((**g = (char) numberOfVertices) > maxverts - 2) return 2;
            // end graph creation
        } else if(i <= numberOfVertices && i > 0){
            // should add a check to make sure it is a list!
            PyObject* obj_adjacency = item;
            PyObject* seq_adjacency;
            int j = 0, len_adjacency; 
            PyObject* item_adjacency;
            seq_adjacency = PySequence_Fast(obj_adjacency, "expected a sequence");
            len_adjacency = PySequence_Size(obj_adjacency);

            // make sure object is a sequence and put the for loop inside the conditional
            item_adjacency = PySequence_Fast_GET_ITEM(seq_adjacency, j);
            int degreeOfVertex = PyInt_AsLong(item_adjacency);  
            if(degreeOfVertex != len_adjacency - 1){
                printf("degreeOfVertex %d and length %d not matching!\n", degreeOfVertex, len_adjacency);
            }
            int adjacent[degreeOfVertex];
            // graph creation
            if ((degree (g, i) = (char) degreeOfVertex) > maxdeg - 2) return 4;
            // end graph creation
            for (j = 1; j < len_adjacency; j++) {
                item_adjacency = PySequence_Fast_GET_ITEM(seq_adjacency, j);

                // delete this code!
                PyObject* objectsRepresentation = PyObject_Repr(item);
                const char* s = PyString_AsString(objectsRepresentation);
                printf("%s\n", s);
                PyObject* objType = PyObject_Type(item);
                PyObject* objTypeString = PyObject_Repr(objType);
                const char* sType = PyString_AsString(objTypeString);
                printf("%s\n", sType);
                // end delete


                // make sure every object is an int!
                adjacent[j-1] = PyInt_AsLong(item_adjacency);
                printf("%da\n", adjacent[j-1]);
                // make sure first int is the degree and is the same as the length -1 of the array

                // graph creation
                g [i][j] = (char) PyInt_AsLong(item_adjacency);
                // end graph creation
            }

        } else {
            printf("There is something that should not be here!\n");
            PyObject* objectsRepresentation = PyObject_Repr(item);
            const char* s = PyString_AsString(objectsRepresentation);
            printf("%s\n", s);
            PyObject* objType = PyObject_Type(item);
            PyObject* objTypeString = PyObject_Repr(objType);
            const char* sType = PyString_AsString(objTypeString);
            printf("%s\n", sType);
        }
        

    }

    printf("loop is done!\n");

    char s = 'p';
    gem = gembed (g, s, 1);
    printf("gembed is done!\n");
/*  system ("date"); */
    switch (gem) {
        case 0: printf ( "no ");
            switch (s) {
                case 'p' : printf ("projective"); break;
                case 't' : printf ("toroidal"); break;
                case 's' : printf ("spindle"); break;
                default  : printf ("ERROR"); 
                }
            puts (" embeddings");
            break;
        case 2: puts ( "graph is planar");
            break;
        case 1:
        case 3: puts ( "graph embeds"); 
            break;
        default: puts ( "whoops -- unknown result from gembed()");
            break;
    }



    Py_DECREF(seq);
    printf("]\n");
    printf("Item is a list!\n");

    Py_RETURN_NONE;
}

static PyMethodDef EmbedtestMethods[] = 
{
    {"tpp", tpp, METH_VARARGS, "Test whether a given graph is projective planar"},
    {"hello", hello, METH_VARARGS, "Test whether a given graph is projective planar"},
	{"gr", gr, METH_VARARGS, "Test whether a given graph is projective planar"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC

initet(void)
{
	(void) Py_InitModule("et", EmbedtestMethods);
}



// This method reads the graph or returns a fail code. My aim is to modify it so it only reads the graph!
// int freadgraph (g, f) graph (g); FILE *f;
// {
//     vertex i, j, u, v; unsigned temp;

//     // if (fscanf (f, "%u", &temp) != 1) return 1;
//     // if ((**g = (char) temp) > maxverts - 2) return 2;
//     for (i = 1; i <= **g; i++) //here **g is the number of vertices in the graph!
//     {
//         if (fscanf (f, "%u", &temp) != 1) return 3; //graph is illegal because it did not read a value. %u is an unsigned int
//         if ((degree (g, i) = (char) temp) > maxdeg - 2) return 4; //temp is current degree. Checks that it is not greater than max 
//         // degree!  it also assigns g[i][0] to be the degree, and then checks this value is not greater than maxdeg -2. 
//         // maxverts and maxdeg are set to be 30 arbitrarily, so this doesn't actually check graph degree validity, it only checks that 
//         // it's to large computationally!
//         for (j = 1; j <= degree (g, i); j++)
//             if (fscanf (f, "%u", &temp) != 1) return 5; //Now, if it doesn't read a vertex, fail!
//             else g [i][j] = (char) temp; //this reads the vertices in the list and assigns i's neighbor to be temp, and sets it
//             // in order after the degree, so g[i] = [degree, n1, n2, ..., nm] where ni is neighbor i
//     }

//     for (i = 1; i <= **g; i++) for (j = 1; j <= degree(g, i); j++)
//         {
//             if (g [i][j] > **g) return 6; //this checks that the label of each vertex in the respective adjacency lists
//             // do not exceed the number of vertices in the graph as listed in the file.
//             for (u = g [i][j], v = 1; (v <= degree(g, u)) && (g[u][v] != i); v ++); //this loops through all the vertices
//             	// adjacent to u and stops whenever it finds the vertex i, or it finishes the list
//             if (v > degree(g, u)) return 7; // if v is greater than the degree, it means vertex i was not found in the 
//         		// adjacency list for u, meaning the graph is directed. It seems directed graphs are not acceptable!
//         }
//     return 0;
// }


// This method reads the graph or returns a fail code. My aim is to modify it so it only reads the graph!
// int freadgraph (g, f) graph (g); FILE *f;
// {
//     vertex i, j, u, v; unsigned temp;

//     // if (fscanf (f, "%u", &temp) != 1) return 1;
//     if ((**g = (char) temp) > maxverts - 2) return 2;
//     for (i = 1; i <= **g; i++) //here **g is the number of vertices in the graph!
//     {
//         if (fscanf (f, "%u", &temp) != 1) return 3; //graph is illegal because it did not read a value. %u is an unsigned int
//         if ((degree (g, i) = (char) temp) > maxdeg - 2) return 4; //temp is current degree. Checks that it is not greater than max 
//         // degree!  it also assigns g[i][0] to be the degree, and then checks this value is not greater than maxdeg -2. 
//         // maxverts and maxdeg are set to be 30 arbitrarily, so this doesn't actually check graph degree validity, it only checks that 
//         // it's to large computationally!
//         for (j = 1; j <= degree (g, i); j++)
//             if (fscanf (f, "%u", &temp) != 1) return 5; //Now, if it doesn't read a vertex, fail!
//             else g [i][j] = (char) temp; //this reads the vertices in the list and assigns i's neighbor to be temp, and sets it
//             // in order after the degree, so g[i] = [degree, n1, n2, ..., nm] where ni is neighbor i
//     }

//     for (i = 1; i <= **g; i++) for (j = 1; j <= degree(g, i); j++)
//         {
//             if (g [i][j] > **g) return 6; //this checks that the label of each vertex in the respective adjacency lists
//             // do not exceed the number of vertices in the graph as listed in the file.
//             for (u = g [i][j], v = 1; (v <= degree(g, u)) && (g[u][v] != i); v ++); //this loops through all the vertices
//              // adjacent to u and stops whenever it finds the vertex i, or it finishes the list
//             if (v > degree(g, u)) return 7; // if v is greater than the degree, it means vertex i was not found in the 
//              // adjacency list for u, meaning the graph is directed. It seems directed graphs are not acceptable!
//         }
//     return 0;
// }