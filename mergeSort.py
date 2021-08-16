import math
import random

def mergeSort(arr):
    if(len(arr) < 2): return arr
    
    middleIndex = math.floor(len(arr) / 2)
    leftArray = arr[:middleIndex]
    rightArray = arr[middleIndex:]
    
    return merge(mergeSort(leftArray), mergeSort(rightArray))


def merge(leftArray, rightArray):
    resultArr = []
    leftIndex = 0
    rightIndex = 0
    
    while leftIndex < len(leftArray) and rightIndex < len(rightArray):
        if(leftArray[leftIndex] < rightArray[rightIndex]):
            resultArr.append(leftArray[leftIndex])
            leftIndex += 1
        else:
            resultArr.append(rightArray[rightIndex])
            rightIndex += 1

    while leftIndex < len(leftArray):
        resultArr.append(leftArray[leftIndex])
        leftIndex += 1
    while rightIndex < len(rightArray):
        resultArr.append(rightArray[rightIndex])
        rightIndex += 1

    return resultArr


def fill_list(n):
    arr = []
    for _ in range(n):
        arr.append(random.randrange(1, 5000))

    return arr


if __name__ == '__main__':

    arr = fill_list(2500)

    print(mergeSort(arr))
