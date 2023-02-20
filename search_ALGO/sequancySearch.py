def sequancy(arr,search):
    for idx,value in enumerate(arr):
        if value == search:
            return idx
    return -1

res = sequancy([9,2,4,8,3,6,5],8)

if res == -1:
    print("Not Found")
else:
    print(f"Found At {res}")