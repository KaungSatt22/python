from random import randint
def Quick(arr):
    if len(arr) <=1:
        return arr 
    pivot = arr[randint(0,len(arr)-1)]
    left = 0
    right = len(arr) - 1
    while left <= right:
        while left < len(arr) and arr[left] < pivot:
            left +=1
        while right > 0 and arr[right] > pivot:
            right -=1
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left +=1
            right -=1
        elif left == right:
            left+=1
    leftArr = Quick(arr[0: right+1])
    rightArr = Quick(arr[left: len(arr)])
    return leftArr + rightArr

print(Quick([8,9,7,4,5,6,2,1]))
    
