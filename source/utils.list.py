def findIndex(list, predicate):
	for i in range(len(list)):
		if predicate(list[i], i, list):
			return i
	return -1
		
