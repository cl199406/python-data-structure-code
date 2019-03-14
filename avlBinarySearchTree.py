#平衡二叉搜索树

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

class AVL(BinarySearchTree):
	def _put(self,key,value,currentNode):
		if key<currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,value,currentNode.leftChild)
			else:
				currentNode.leftChild=TreeNode(key,value,parent=currentNode)
				self.updateBalance(currentNode.leftChild)
		else:
			if currentNode.hasRightChild():
				self._put(key,value,currentNode.rightChild)
			else:
				currentNode.rightChild=TreeNode(key,value,parent=currentNode)
				self.updateBalance(currentNode.rightChild)
	
	def updateBalance(self,node):
		if node.balanceFactor>1 or node.balanceFactor<-1:
			self.rebalance(node)
			return
		if node.parent!=None:
			if node.isLeftChild():
				node.parent.balanceFactor+=1
			elif node.isRightChild():
				node.parent.balanceFactor-=1
			if node.parent.balanceFactor!=0:
				self.updateBalance(node.parent)
	
	def rotateLeft(self,rotRoot):
		newRoot=rotRoot.rightChild
		rotRoot.rightChild=newRoot.leftChild
		if newRoot.leftChild!=None:
			newRoot.leftChild.parent=rotRoot
		newRoot.parent=rotRoot.parent
		if rotRoot.isRoot():
			self.root=newRoot
		else:
			if rotRoot.isLeftChild():
				rotRoot.parent.leftChild=newRoot
			else:
				rotRoot.parent.rightChild=newRoot
		newRoot.leftChild=rotRoot
		rotRoot.parent=newRoot
		rotRoot.balanceFactor=rotRoot.balanceFactor+1-min(newRoot.balanceFactor,0)
		newRoot.balanceFactor=newRoot.balanceFactor+1+max(rotRoot.balanceFactor,0)
		
	def rotateRight(self,rotRoot):
		newRoot=rotRoot.leftChild
		rotRoot.leftChild=newRoot.rightChild
		if newRoot.rightChild!=None:
			newRoot.rightChild.parent=rotRoot
		newRoot.parent=rotRoot.parent
		if rotRoot.isRoot():
			self.root=newRoot
		else:
			if rotRoot.isLeftChild():
				rotRoot.parent.leftChild=newRoot
			else:
				rotRoot.parent.rightChild=newRoot
		newRoot.rightChild=rotRoot
		rotRoot.parent=newRoot
		rotRoot.balanceFactor=rotRoot.balanceFactor-1-max(newRoot.balanceFactor,0)
		newRoot.balanceFactor=newRoot.balanceFactor-1+min(rotRoot.balanceFactor,0)
	
	def rebalance(self,node):
		if node.balanceFactor<0:
			if node.rightChild.balanceFactor>0:
				self.rotateRight(node.rightChild)
				self.rotateLeft(node)
			else:
				self.rotateLeft(node)
		elif node.balanceFactor>0:
			if node.leftChild.balanceFactor<0:
				self.rotateLeft(node.leftChild)
				self.rotateRight(node)
			else:
				self.rotateRight(node)
			
			