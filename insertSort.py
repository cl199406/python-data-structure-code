#insertSort 插入排序
import time,random
def insertSort(alist):#为插入排序，但是需要做更多的交换，性能稍差。
	start=time.time()
	for num in range(1,len(alist)):
		p=num
		for n in range(num+1):
			if alist[p]<alist[n]:
				alist[p],alist[n]=alist[n],alist[p]
		print(alist)
	print('{}s'.format(time.time()-start))
	return alist

			
def insertSort_(alist):
	start=time.time()
	for index in range(1,len(alist)):
		currentvalue=alist[index]
		position=index
		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position=position-1
		alist[position]=currentvalue
		print(alist)
	print('{}s'.format(time.time()-start))
	return alist
print(insertSort([54,26,93,17,77,31,44,55,20]))
print('------------------------')
print(insertSort_([54,26,93,17,77,31,44,55,20]))
#print(insertSort(random.sample(list(range(100)),50)))
#print(insertSort_(random.sample(list(range(100)),50)))