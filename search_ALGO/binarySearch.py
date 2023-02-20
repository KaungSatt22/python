def binarySearch(sortedArr,search):
    first = 0
    last = len(sortedArr) - 1
    while first <= last:
        mid = (first + last) // 2
        midValue = sortedArr[mid]
        if midValue == search:
            return mid 
        else:
            if midValue < search:
                last = mid - 1
            else:
                first = mid + 1
    return -1

res = binarySearch([10,20,30,40,50,60],30)
if res == -1:
    print("Not Found")
else:
    print(f"Found At {res}")