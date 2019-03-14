#bubbleSort 冒泡排序

def bubbleSort(alist):
	num=len(alist)
	for m in range(num-1,0,-1):
		for n in range(m):
			if alist[n]>alist[n+1]:
				alist[n],alist[n+1]=alist[n+1],alist[n]
	return alist
print(bubbleSort([23,56,12,45,8,34]))
print(bubbleSort([54,26,93,17,77,31,44,55,20]))