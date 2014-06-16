NP-Complete Heuristics
======================

This is Python code derived from my 2011 ArchiveDJ playlisting code. It has a Traveling Salesman heuristic and 
a generative clustering component.

##Traveling Salesman
An object is constructed with an array of objects and an optional similarity queue

The traveling salesman function takes either a similarity function (float <= sim(item,item)) or a similarity
queue (sorted array of (item,item,score) triples) If the function is not provided, a O(n^2) similarity queue
is calculated as a preliminary step. The resulting array (cycle) is provided in self.answer

The similarity function takes a similarity metric and can be parameterized with a item to item similarity metric
 and an optional parameter to invert similarity (smaller is better instead of larger is better).
 

##Generative Clustering
An object is constructed with an array of objects, an optional similarity queue, an an optional similarity metric

The traveling salesman also uses a cluster_accept condition with the signature boolean accept(item,set{item})
If no cluster_accept is given, an attempt is made to continue with a guessed default.  cluster_accept function prototype
is provided as a template implementing traditional 'greater than minimum similarity to all members' stop condition.

The output is a set of set of items