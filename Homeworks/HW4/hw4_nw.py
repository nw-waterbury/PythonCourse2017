
def insertionSort(list_numbers):
    """Sorting Algorithm 1: Insertion Sort - O(n^2)"""
	n = len(list_numbers)
	for position in range(1,n):
		current = list_numbers[position]
		while position >= 1 and list_numbers[position-1]>current:
			list_numbers[position]=list_numbers[position-1]
			position+=-1
		list_numbers[position] = current

def bubbleSort(list_numbers):
    for j in range(0,len(list_numbers)):
        for i in range(j+1, len(list_numbers)):
            if list_numbers[i] >= list_numbers[j]:
                pass
            else:
                list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]
    return list_numbers
