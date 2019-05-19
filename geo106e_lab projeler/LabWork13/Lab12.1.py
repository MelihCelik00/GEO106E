import random
from sort import *

myList_519 = [random.randint(0,100) for i_519 in range(100)]
quickSort(myList_519)

def insertionSort_519(myList_519):
    for i_519 in range(1, len(myList_519)):

        pivot_519 = myList_519[i_519]
        j_519 = i_519 - 1
        while j_519 >= 0 and myList_519[j_519] > pivot_519:

            myList_519[j_519+1] = myList_519[j_519]
            j_519 = j_519 - 1


        myList_519[j_519+1] = pivot_519
    return myList_519