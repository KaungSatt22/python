def selectionSort(arr):
    for num in range(len(arr)):
        minIdx = num 
        i = num
        for j in range(i,len(arr)):
            if arr[num] > arr[j]:
                minIdx = j 
        arr[num], arr[minIdx] = arr[minIdx], arr[num]
    return arr 

print(selectionSort([9,2,7,5,3,6,4,1]))