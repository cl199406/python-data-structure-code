#遍历树

#前序遍历
def preorder(tree):
	if tree:
		print(tree.getRootVal)
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())
	else:
		return None

#后序遍历
def postorder(tree):
	if tree:
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())
		print(tree.getRootVal())
	else:
		return None
		
#中序遍历
def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inorder(tree.getRightChild())
	else:
		return None
def printexp(tree):
	val=''
	if tree:
		val=val+'('+printexp(tree.getLeftChild())
		val=val+str(tree.getRootVal())
		val=val+printexp(tree.getRightChild())+')'
	else:
		val=None
	return val
		

