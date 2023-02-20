def shellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for num in range(gap,len(arr)):
            tem = arr[num]
            j = num
            while j >= gap and arr[j-gap]> tem:
                arr[j] = arr[j-gap]
                j -=gap 
            arr[j] = tem 
        gap//=2
    return arr 
print(shellSort([9,1,2,7,6,5,8]))