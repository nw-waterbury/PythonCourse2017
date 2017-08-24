
def insertionSort(numbers):
    """Sorting Algorithm 2: Insertion Sort - O(n^2)"""
	n = len(numbers)
	for position in range(1,n):
		current = numbers[position]
		while position >= 1 and numbers[position-1]>current:
			numbers[position]=numbers[position-1]
			position+=-1
		numbers[position] = current
