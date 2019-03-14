#堆的实现

class BinHeap():
	def __init__(self):
		self.heaplist=[0]
		self.currentSize=0
	
	def insert(self,num):
		self.heaplist.append(num)
		self.currentSize=self.currentSize+1
		size=self.currentSize
		while size>0:
			if self.heaplist[size]<heaplist[size//2]:
				self.heaplist[size],self.heaplist[size//2]=\
				self.heaplist[size//2],self.heaplist[size]
			size=size//2
	def minChild(self,i):
		if i*2+1>self.currentSize:#只有一个子节点
			return i*2
		else:
			if self.heaplist[i*2]>=self.heaplist[i*2+1]:
				return i*2+1
			else:
				return i*2
				
	def perDown(self,i):
		while (i*2)<=self.currentSize:
			min=self.minChild(i)
			if self.heaplist[i]>self.heaplist[min]:
				self.heaplist[i],self.heaplist[min]=\
				self.heaplist[min],self.heaplist[i]
			i=min
	
	def delMin(self):
	#先交换在pop同样可以，但效率更低，赋值比交换效率高。
		val=self.heaplist[1]
		self.heaplist[1]=self.heaplist[self.currentSize]
		self.currentSize=self.currentSize-1
		self.heaplist.pop()
		self.perDown(1)
		return val
	
	def BuildHeap(self,alist):
		i=len(alist)//2
		self.currentSize=len(alist)
		self.heaplist=[0]+alist
		while i>0:
			self.perDown(i)
			i=i-1

bh=BinHeap()
bh.BuildHeap([9,5,6,2,3])
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())

		
				
			
				
		