def merge(arr, l, m, r):
	n1,n2 = m-l+1, r-m	
	leftarray = [0] * n1
	rightarray = [0] * n2
	for i in range(n1):
		leftarray[i] = arr[l+i]
	for i in range(n2):
		rightarray[i] = arr[m+i+1]
	i, j, k = 0, 0, l
	while i < n1 and j < n2:
		if leftarray[i] < rightarray[j]:
			arr[k] = leftarray[i]
			i += 1
		else:
			arr[k] = rightarray[j]
			j += 1
		k += 1
	while i < n1:
		arr[k] = leftarray[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = rightarray[j]
		j += 1
		k += 1
def mergesort(arr, l, r):
	if l < r:
		m = (l+r)/2
		mergesort(arr, l, m)
		mergesort(arr, m+1, r)
		merge(arr, l, m, r)
arr = [12, 11, 13, 5, 6, 7]
l, r = 0, len(arr)-1
mergesort(arr, l, r)
print arr

'''
TIME COMPLEXITY : O(nlogn)
AUXILARY SPACE : O(n)
STABLE: YES
'''