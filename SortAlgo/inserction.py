def inserction(arr):
    for num in range(1,len(arr)):
        tem = arr[num]
        j = num 
        while j > 0 and arr[j-1]> tem:
            arr[j] = arr[j-1]
            j-=1
        arr[j]= tem 
    return arr

print(inserction([4,7,6,8,9,2,3]))