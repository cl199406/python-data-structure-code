#二叉搜索树

class BinarySearchTree():
	def __init__(self):
		self.root=None
		self.size=0
		
	def length(self):
		return self.size
		
	def __len__(self):
		return self.size
		
	def __iter__(self):
		return self.root.__iter__()
		
	def put(self,key,value):
		if self.root:
			self._put(key,value,self.root)
		else:
			self.root=TreeNode(key,value)
		self.size=self.size+1
		
	def _put(self,key,value,currentNode):
		if key<currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,value,currentNode.leftChild)
			else:
				currentNode.leftChild=TreeNode(key,value,parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key,value,currentNode.rightChild)
			else:
				currentNode.rightChild=TreeNode(key,value,parent=currentNode)
	def __setitem__(self,key,value):
		self.put(key,value)
		
	def get(self,key):
		if self.root:
			res=self._get(key,self.root)
			if res:
				return res.value
			else:
				return None
		else:
			return None
	
	def _get(self,key,currentNode):
		if not currentNode:
			return None
		if key==currentNode.key:
			return currentNode
		elif key<currentNode.key:
			return self._get(key,currentNode.leftChild)
		else:
			return self._get(key,currentNode.rightChild)
	
	def __getitem__(self,key):
		return self.get(key)
		
	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False
			
	def delete(self,key):
		if self.size>1:
			nodeToRemove=self._get(key,self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size=self.size-1
			else:
				raise KeyError('Error,key not in tree!')
		elif self.size==1 and self.root.key==key:
			self.root=None
			self.size=self.size-1
		else:
			raise KeyError('Error,key not in tree!')
			
	def __delitem__(self,key):
		self.delete(key)
		
	def remove(self,node):
		if node.isLeaf():#leaf节点，无子节点
			if node==node.parent.leftChild:
				node.parent.leftChild=None
			else:
				node.parent.rightChild=None
		elif node.hasBothChild():#interior,2个节点
			suc=node.findSuccessor()
			suc.spliceOut()
			node.key=suc.key
			node.value=suc.value
		else:#一个子节点
			if node.hasLeftChild():
				if node.isLeftChild():
					node.leftChild.parent=node.parent
					node.parent.leftChild=node.leftChild
				elif node.isRightChild():
					node.leftChild.parent=node.parent
					node.parent.rightChild=node.leftChild
				else:
					node.replaceNodeData(node.leftChild.key,node.leftChild.value,\
					node.leftChild.leftChild,node.leftChild.rightChild)
			else:
				if node.isLeftChild():
					node.rightChild.parent=node.parent
					node.parent.leftChild=node.rightChild
				elif node.isRightChild():
					node.rightChild.parent=node.parent
					node.parent.rightChild=node.rightChild
				else:
					node.replaceNodeData(node.rightChild.key,node.rightChild.value,\
					node.rightChild.leftChild,node.rightChild.rightChild)
	
	def findSuccessor(self):
		suc=None
		if self.hasRightChild():
			suc=self.rightChild.findMin()
		else:
			if self.parent:
				if self.isLeftChild():
					suc=self.parent
				else:
					self.parent.rightChild=None
					suc=self.parent.findSuccessor()
					self.parent.rightChild=self
		return suc
		
	def findMin(self):
		current=self
		while current.hasLeftChild():
			current=current.leftChild
		return current
		
	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild=None
			else:
				self.parent.rightChild=None
		elif self.hasAnyChild():
			if self.hasLeftChild():
				if self.isLeftChild():
					self.parent.leftChild=self.leftChild
				else:
					self.parent.rightChild=self.leftChild
				self.leftChild.parent=self.parent
			else:
				if self.isLeftChild():
					self.parent.leftChild=self.rightChild
				else:
					self.parent.rightChild=self.rightChild
				self.rightChild.parent=self.parent
				

	
	
class TreeNode():
	def __init__(self,key,value,left=None,right=None,parent=None):
		self.key=key
		self.value=value
		self.leftChild=left
		self.rightChild=right
		self.parent=parent
		
	def hasLeftChild(self):
		return self.leftChild
		
	def hasRightChild(self):
		return self.rightChild
		
	def isLeftChild(self):
		return self.parent and self.parent.leftChild==self
		
	def isRightChild(self):
		return self.parent and self.parent.rightChild==self
		
	def isRoot(self):
		return not self.parent
		
	def isLeaf(self):
		return not (self.leftChild or self.rightChild)
		
	def hasAnyChild(self):
		return self.leftChild or self.rightChild
		
	def hasBothChild(self):
		return self.leftChild and self.rightChild
		
	def replaceNodeData(self,key,value,lc,rc):
		self.key=key
		self.value=value
		self.leftChild=lc
		self.rightChild=rc
		if self.hasLeftChild():
			self.leftChild.parent=self
		if self.hasRightChild():
			self.rightChild.parent=self
	
	def __iter__(self):
		if self:
			if self.hasLeftChild():
				for n in self.leftChild:
					yield n
			yield self.key
			if self.hasRightChild():
				for n in self.rightChild:
					yield n

mytree=BinarySearchTree()
mytree[3]='red'
mytree[4]='blue'
mytree[6]='yellow'
mytree[2]='at'
print(mytree[6])
print(mytree[2])
#node=TreeNode(4,mytree[4])
#mytree.remove(node)
mytree.delete(4)
print(mytree[3])
print(mytree[4])