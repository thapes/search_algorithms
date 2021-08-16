import math

def binarySearch(arr, start, end, target):
        if start > end: return False

        midIndex = math.floor((start + end) / 2)
        if arr[midIndex] == target:
            return True
        elif(arr[midIndex] > target):
            return binarySearch(arr, start, midIndex -1, target)
        else:
            return binarySearch(arr, midIndex +1, end, target)


if __name__ == '__main__':

    arr = []
    i = 0
    for _ in range(100):
        i += 1
        arr.append(i)
    start, end, target = 0, len(arr) - 1, 50
    
    print(binarySearch(arr, start, end, target))
