#swap the elements at the given indices in the given array
def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp

#place all elements smaller greater than that at the pivot to the left of pivot, and all greater than
#the pivot to the right of it
def partition(arr, iLo, iHi, pivot):
    curLo = iLo
    curHi = iHi - 1
    
    while(curLo < curHi):
        while (curLo < iHi and arr[curLo] <= pivot):
            curLo += 1
        while (curHi >= iLo and arr[curHi] > pivot):
            curHi -= 1
        if curLo < curHi:
            swap(arr, curLo, curHi)
                    
    swap(arr, iLo, curHi)
    return curHi
       
#sort the given list given the high and low indices for sorting     
def quickSort(arr, iLo, iHi):
    if iLo >= iHi:
        return

    pivot = arr[iLo]

    iPivot = partition(arr, iLo, iHi, pivot)

    #sort the list to the left of the pivot
    quickSort(arr, iLo, iPivot)
    #sort the list to the right of the pivot
    quickSort(arr, iPivot +1, iHi)
    
def insertionSort(arr):
    #iterate over whole list
    for i in range(1, len(arr)):
        curr = arr[i]
        prev = i - 1
        
        #shift element before current index to the current index until current item reaches 
        #its proper sorted place in the list
        while prev>= 0 and curr < arr[prev]:
            arr[prev + 1] = arr[prev]
            prev -=1
        arr[prev + 1] = curr
        
    
nums1 = [8, 12 , 4 , 89, 7, 34, 48, 6, 55, 1]
print(nums1)

quickSort(nums1, 0, len(nums1))
print('Quick Sort: ' )
print(nums1)

nums1 = [8, 12 , 4 , 89, 7, 34, 48, 6, 55, 1]

insertionSort(nums1)
print('Insertion sort: ')
print(nums1)