#字梯图问题

from pythonds.graphs.adjGraph import Graph,Vertex
from pythonds.basic.queue import Queue

def buildGraph(wordfile):
	d={}
	g=Graph()
	with open(wordfile,'r') as file:
		for line in file:
			word=line[:-1]
			for i in range(len(word)):
				bucket=word[:i]+'_'+word[i+1:]
				if bucket in d:
					d[bucket].append(word)
				else:
					d[bucket]=[word]
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in word1:
				if word1!=word2:
					g.addEdge(word1,word2)
	return g

def bfs(g,start):
	start.setDistance(0)
	start.setPred(None)
	vertQueue=Queue()
	vertQueue.enqueue(start)
	while (vertQueue.size()>0):
		currentVert=vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if (nbr.getColor()=='white'):
				nbr.setColor('gray')
				nbr.setDistance(currentVert.getDistance()+1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)
		currentVert.setColor('black')

def traverse(y):
	x=y
	while (x.getPred()):
		print(x.getId())
		x=x.getPred()
	print(x.getId())