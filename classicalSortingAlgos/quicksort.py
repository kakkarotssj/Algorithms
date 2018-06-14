def partition(arr, l, r):
	pivot = arr[r]
	wall = l-1
	for i in range(l, r):
		if arr[i] >= pivot:
			pass
		else:
			arr[i], arr[wall+1] = arr[wall+1], arr[i]
			wall += 1
	arr[wall+1], arr[r] = pivot, arr[wall+1]
	return wall+1
def quicksort(arr, l , r):
	if l < r:
		sortedindex = partition(arr, l, r)
		quicksort(arr, l, sortedindex-1)
		quicksort(arr, sortedindex+1, r)	
arr = [12, 11, 13, 5, 6, 7]
l, r = 0, len(arr)-1
quicksort(arr, l, r)
print arr

'''
WORST CASE: O(n*n): when pivot always chosen as the smallest or biggest
BEST CASE : O(nlogn) 
'''