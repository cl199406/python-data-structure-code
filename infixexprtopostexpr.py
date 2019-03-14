#中缀表达式转后缀表达式
from pythonds.basic.stack import Stack

def infixtoPostfix(infixexpr):
	prec={'*':3,'/':3,'+':2,'-':2,'(':1}
	opstack=Stack()
	postfixlist=[]
	tokenlist=[num for num in infixexpr]
	for token in tokenlist:
		if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
			postfixlist.append(token)
		elif token=='(':
			opstack.push(token)
		elif token==')':
			toptoken=opstack.pop()
			while toptoken !='(':
				postfixlist.append(toptoken)
				toptoken=opstack.pop()
		else:
			while (not opstack.isEmpty()) and (prec[opstack.peek()]>=prec[token]):
				postfixlist.append(opstack.pop())
			opstack.push(token)
	while not opstack.isEmpty():
		postfixlist.append(opstack.pop())
	return ''.join(postfixlist)

print(infixtoPostfix("((A*B)+(C*D))"))
print(infixtoPostfix("(A+B)*C-(D-E)*(F+G)"))
