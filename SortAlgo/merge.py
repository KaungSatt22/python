def mergeSort(leftArr,rightArr):
    results = []
    left_idx,right_idx = 0 ,0 
    while left_idx < len(leftArr) and right_idx < len(rightArr):
        if leftArr[left_idx] < rightArr[right_idx]:
            results.append(leftArr[left_idx])
            left_idx+=1
        else:
            results.append(rightArr[right_idx])
            right_idx+=1
    if left_idx < len(leftArr):
        results.extend(leftArr[left_idx:])
    if right_idx < len(rightArr):
        results.extend(rightArr[right_idx:])
    return results

def merge(arr):
    if len(arr) < 2:
        return arr 
    else:
        mid = len(arr) // 2
        return mergeSort(merge(arr[:mid]),merge(arr[mid:]))

print(merge([9,2,7,5,6,1,4]))