# -*- coding: utf-8 -*-
"""
This module includes merge sort, quicksort and insertion sort algorithms
"""
# ------------------------------------------------------------
# Insertion Sort
# https://gist.github.com/ameerkat/731870#file-sorts-py
def insertionSort(myList):
	for i in range(1, len(myList)):
		# Copy the key value so we can overwrite it when shifting
		pivot = myList[i]
		j = i - 1
		while j >= 0 and myList[j] > pivot:
			# Shift over all the entries greater than key
			myList[j+1] = myList[j]
			j = j - 1
		# Now copy the key into the appropriate spot left by
		# shifting all the greater values over
		myList[j+1] = pivot
	return myList
# ------------------------------------------------------------
# QuickSort
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
def quickSort(myList):
	quickSortHelper(myList,0,len(myList)-1)

def quickSortHelper(myList,first,last):
	if first<last:
		splitpoint = partition(myList,first,last)
		quickSortHelper(myList,first,splitpoint-1)
		quickSortHelper(myList,splitpoint+1,last)

def partition(myList,first,last):
	pivot = myList[first]
	leftmark = first+1
	rightmark = last
	done = False
	while not done:
		while leftmark <= rightmark and myList[leftmark] <= pivot:
			 leftmark = leftmark + 1
		while myList[rightmark] >= pivot and rightmark >= leftmark:
			 rightmark = rightmark -1
		if rightmark < leftmark:
			 done = True
		else:
			 temp = myList[leftmark]
			 myList[leftmark] = myList[rightmark]
			 myList[rightmark] = temp
	temp = myList[first]
	myList[first] = myList[rightmark]
	myList[rightmark] = temp
	return rightmark
# ------------------------------------------------------------
# Merge Sort
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
def mergeSort(myList):
    if len(myList)>1:
        mid = len(myList)//2
        lefthalf = myList[:mid]
        righthalf = myList[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                myList[k]=lefthalf[i]
                i=i+1
            else:
                myList[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            myList[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            myList[k]=righthalf[j]
            j=j+1
            k=k+1