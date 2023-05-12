import random
import time
import sys
sys.setrecursionlimit(1500)

def lumptoquicksort(arr, start , stop):
    if(start < stop):
        pivotindex = lumptopartitionrand(arr,\
                             start, stop)
        lumptoquicksort(arr , start , pivotindex-1)
        lumptoquicksort(arr, pivotindex + 1, stop)

def lumptopartitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return lumptopartition(arr, start, stop)
 
def lumptopartition(arr,start,stop):
    pivot = start 
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)

def hoarquicksort(arr, start, stop):
    if(start < stop):
        pivotindex = hoarpartitionrand(arr,\
                              start, stop)
        hoarquicksort(arr , start , pivotindex)
        hoarquicksort(arr, pivotindex + 1, stop)
 

def hoarpartitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] =\
        arr[randpivot], arr[start]
    return hoarpartition(arr, start, stop)
 
def hoarpartition(arr,start,stop):
    pivot = start 
    i = start - 1
    j = stop + 1
    while True:
        while True:
            i = i + 1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j = j - 1
            if arr[j] <= arr[pivot]:
                break
        if i >= j:
            return j
        arr[i] , arr[j] = arr[j] , arr[i]
        
        
n = 100000
arr = []

for i in range(n):
    arr.append(random.randint(1,100))

#LUMPTO
start=time.time()
lumptoquicksort(arr, 0, n - 1)
end=time.time()

print("Lumpto: ",end-start)

#HOAR
start=time.time()
hoarquicksort(arr, 0, n - 1)
end=time.time()

print("Hoar: ",end-start)        