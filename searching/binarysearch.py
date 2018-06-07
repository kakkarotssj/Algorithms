def dobinarysearch(arr, lower_index, higher_index, number):
	if higher_index >= lower_index:
		mid_index = (lower_index + higher_index) / 2
		if arr[mid_index] == number:
			return mid_index
		else:
			if number < arr[mid_index]:
				index = dobinarysearch(arr, lower_index, mid_index-1, number)
				return index
			else:
				index = dobinarysearch(arr, mid_index+1, higher_index, number)
				return index
	else:
		return -1



print "enter a sorted array"
arr = map(int, raw_input().split())
count_arr = len(arr)
print "enter number you want to search for"
number = input()
lower_index = 0
higher_index = count_arr-1
is_presentindex = dobinarysearch(arr, lower_index, higher_index, number)
print is_presentindex
