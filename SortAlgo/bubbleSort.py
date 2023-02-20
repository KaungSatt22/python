def bubbleSort(arr):
    for i in range(len(arr)-1, 0,-1):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr 

print(bubbleSort([5,7,8,9,2,1]))