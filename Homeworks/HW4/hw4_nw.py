
def insertionSort(numbers):
    """Sorting Algorithm 2: Insertion Sort - O(n^2)"""
	n = len(numbers)
	for position in range(1,n):
		current = numbers[position]
		while position >= 1 and numbers[position-1]>current:
			numbers[position]=numbers[position-1]
			position+=-1
		numbers[position] = current
        
def BubbleSort(list):
    for j in range(0,len(list)):
        for i in range(j+1, len(list)):
            if list[i] >= list[j]:
                pass
            else:
                list[i], list[j] = list[j], list[i]
    return list
