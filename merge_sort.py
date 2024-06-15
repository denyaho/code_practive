import math

def merge(arr):
    return mergeHelper(arr, 0, len(arr) - 1)

def mergeHelper(arr, start, end):
    # 配列が 1 つになるまで再帰的に分割していきます
    # 1 つになったらマージ作業へ移ります
    if start == end: return [arr[start]]

    # 配列が 2 つ以上の時には leftArray と rightArray に分割し続けます
    middle = math.floor((start+end)/2)
    leftArr = mergeHelper(arr,start, middle)
    rightArr = mergeHelper(arr,middle+1,end)
    
    # leftArr と rightArr それぞれの最後に無限大を入れておくことで、ソートが完了するまで比較し続けることができます
    leftArr.append(math.inf)
    rightArr.append(math.inf)

    l = len(leftArr) + len(rightArr) - 2
    li = 0
    ri = 0

    # 右と左がソートされた後、結合されます
    merged = []
   
    # leftarray と rightarray を比較して、どちらが先に merged に入るか決めます
    while (li+ri) < l:
        if leftArr[li] <= rightArr[ri]:
            merged.append(leftArr[li])
            li = li+1
        else:
            merged.append(rightArr[ri])
            ri = ri+1
      
    # leftArray と rightArray の全ての値が merged に入るまで繰り返します。
    return merged

arr1 = [34,4546,32,3,2,8,6,76,56,45,34,566,1];
print(arr1)
print(merge(arr1))