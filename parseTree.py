#二叉分析树分析数学表达式

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

def buildParseTree(fpexp):
	fplist=fpexp.split()#注意[i for i in fpexp]与这个的区别，
	pstack=Stack()       #后者拆分成单个字符
	eTree=BinaryTree('')
	pstack.push(eTree)
	currentTree=eTree
	for i in fplist:
		if i=='(':
			currentTree.insertLeft('')
			pstack.push(currentTree)
			currentTree=currentTree.getLeftChild()
		elif i not in ['+','-','*','/',')']:
			currentTree.setRootVal(int(i))
			parent=pstack.pop()
			currentTree=parent
		elif i in ['+','-','*','/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pstack.push(currentTree)
			currentTree=currentTree.getRightChild()
		elif i==')':
			currentTree=pstack.pop()
		else:
			raise ValueError
	return eTree
def evaluate(parseTree):
	opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
	left=parseTree.getLeftChild()
	right=parseTree.getRightChild()
	if left and right:
		func=opers[parseTree.getRootVal()]
		return func(evaluate(left),evaluate(right))
	else:
		return parseTree.getRootVal()
		
examp=buildParseTree('( ( 10 + 5 ) * 3 )')
print(evaluate(examp))