import random
import itertools
import time
import numpy
import matplotlib.pyplot as plt

def insertionSort(list_numbers):
    """Sorting Algorithm 1: Insertion Sort - O(n^2)"""
    n = len(list_numbers)
    for position in range(1,n):
        current = list_numbers[position]
        while position >= 1 and list_numbers[position-1]>current:
            list_numbers[position]=list_numbers[position-1]
            position+=-1
        list_numbers[position] = current
    return list_numbers

def selectionSort(list_numbers):
    """Sorting Algorithm 2: Selection Sort - O(n^2)"""
    for i in range(len(list_numbers)-1,0,-1):
        maxima=0
        for location in range(1,i+1):
            if list_numbers[location]>list_numbers[maxima]:
                maxima = location
        temp = list_numbers[i]
        list_numbers[i] = list_numbers[maxima]
        list_numbers[maxima] = temp
    return list_numbers

def bubbleSort(list_numbers):
    """Sorting Algorithm 3: Bubble Sort - O(n)"""
    for j in range(0,len(list_numbers)):
        for i in range(j+1, len(list_numbers)):
            if list_numbers[i] >= list_numbers[j]:
                pass
            else:
                list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]
    return list_numbers

#Simulations
selection = []
insert = []
bubble=[]
n=range(1,600)

for i in range(1,600):
	A = random.sample(range(1,1000),i)
	B = random.sample(range(1,1000),i)
    #Not sure why my terminal required this indentation
        C = random.sample(range(1,1000),i)
	t1 = time.time()
	selectionSort(A)
	t2 = time.time()
	insertionSort(B)
	t3 = time.time()
    #Not sure why my terminal required this indentation
        bubbleSort(C)
    #Not sure why my terminal required this indentation
        t4=time.time()
	selection.append(t2-t1)
	insert.append(t3-t2)
    #Not sure why my terminal required this indentation
        bubble.append(t4-t3)

# Plotting
plt.plot(n,selection)
plt.plot(n,insert)
plt.plot(n, bubble)
plt.ylabel('Time (in Seconds)')
plt.xlabel('List Length (n)')
plt.legend(['SelectionSort','InsertionSort','BubbleSort'],loc='upper left')
plt.show()
