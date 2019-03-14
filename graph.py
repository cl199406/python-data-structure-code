#邻接表实现图数据结构

class Vertex():
	def __init__(self,key):
		self.id=key
		self.connectedTo={}
		
	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr]=weight
		
	def __str__(self):
		return str(self.id)+' connectedTo:'+str([x.id for x in self.connectedTo])
		
	def getConnections(self):
		return self.connectedTo.keys()
		
	def getId(self):
		return self.id
		
	def getWeight(self,nbr):
		return self.connectedTo[nbr]
		
		
class Graph():
	def __init__(self):
		self.verList={}
		self.numVertices=0
		
	def addVertex(self,key):
		self.numVertices=self.numVertices+1
		newVertex=Vertex(key)
		self.verList[key]=newVertex
		return newVertex
		
	def getVertex(self,n):
		if n in self.verList:
			return self.verList[n]
		else:
			return None
	
	def __contains__(self,n):
		return n in self.verList
		
	def addEdge(self,f,t,cost=0):
		if f not in self.verList:
			nv=self.addVertex(f)
		if t not in self.verList:
			nt=self.addVertex(t)
		self.verList[f].addNeighbor(self.verList[t],cost)
		
	def getVertices(self):
		return self.verList.keys()
		
	def __iter__(self):
		return iter(self.verList.values())
		
if __name__=='__main__':
	gra=Graph()
	for i in range(6):
		gra.addVertex(i)
	print(gra.verList)
	gra.addEdge(0,1,5)
	gra.addEdge(0,5,2)
	gra.addEdge(1,2,4)
	gra.addEdge(2,3,9)
	gra.addEdge(3,4,7)
	gra.addEdge(3,5,3)
	for n in gra:
		for m in n.getConnections():
			print('{}-->{},WEIGHT IS {}'.format(n.getId(),m.getId(),n.getWeight(m)))
	print(gra.getVertices())
	for n in gra:
		print(n)
