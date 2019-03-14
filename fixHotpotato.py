#烫手山芋问题

from pythonds.basic.queue import Queue
def fixhotpotato(namelist,num):
	q=Queue()
	for name in namelist:
		q.enqueue(name)
	while q.size()>1:
		for i in range(num):
			q.enqueue(q.dequeue())
		q.dequeue()
	return q.dequeue()
	
print(fixhotpotato(['a','b','c','d','e','f','g'],7))