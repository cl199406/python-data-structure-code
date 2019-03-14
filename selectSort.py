#selectSort 选择排序

def selectSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionMax=0
		for location in range(1,fillslot+1):
			if alist[location]>alist[positionMax]:
				positionMax=location
		alist[fillslot],alist[positionMax]=alist[positionMax],alist[location]
	return alist
print(selectSort([54,26,93,17,77,31,44,55,20]))