def merge(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge(arr[0:mid])
    right = merge(arr[mid:len(arr)])
    leftpoint = 0
    rightpoint = 0
    res = []
    while leftpoint < len(left) and rightpoint < len(right):
        if left[leftpoint] > right[rightpoint]:
            res.append(right[rightpoint])
            rightpoint += 1
        else:
            res.append(left[leftpoint])
            leftpoint += 1

    if leftpoint != len(left):
        res += left[leftpoint:]
    else:
        res += right[rightpoint:]

    return res


print(merge([1,3,4,5,2,4,2,1,3]))