#使用deque判断回文数

from pythonds.basic.deque import Deque
def fixhwnum(string):
	numlist=[num for num in string]
	qe=Deque()
	for i in numlist:
		qe.addFront(i)
	while qe.size()>1:
		if qe.removeFront()!=qe.removeRear():
			return False
	return True

print(fixhwnum('abcdcba'))
print(fixhwnum('afdefdfa'))