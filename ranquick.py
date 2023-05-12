import random
import sys
import time
sys.setrecursionlimit(1500)

arr=[]
  
def pivot(low,high):
  r=random.randrange(low,high)
  arr[r],arr[high] = arr[high],arr[r]
  pivot = arr[high]
  i=low-1
  for j in range(low,high):
    if arr[j]<pivot:
      i+=1
      arr[j],arr[i] = arr[i],arr[j]
  arr[i+1],arr[high] = arr[high],arr[i+1]
  return i+1

def quicksort(low,high):
  if low<high:
    p=pivot(low,high)
    quicksort(low,p-1)
    quicksort(p+1,high)

for i in range(100):
  arr.append(random.randint(1,100))

start = time.time()  
quicksort(0,99)
end = time.time()
print(arr)
print("Time taken:",end-start)