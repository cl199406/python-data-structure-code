#计算后缀表达式的结果

from pythonds.basic.stack import Stack
def fixPostexpr(postexpr):
	tokenlist=[num for num in postexpr]
	stack=Stack()
	for token in tokenlist:
		if token not in ['+','-','*','/']:
			stack.push(int(token))
		else:
			result=match(token,stack.pop(),stack.pop())
			stack.push(result)
	return stack.pop()

def match(a,b,c):
	if a=='*':
		return c*b
	elif a=='/':
		return c/b
	elif a=='+':
		return c+b
	else:
		return c-b
print(fixPostexpr('456*+'))
print(fixPostexpr('45/6-'))
print(fixPostexpr('64*7-1+62/-'))
print(fixPostexpr('78+32+/'))
print(4/5-6)