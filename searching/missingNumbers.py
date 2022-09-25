# def missingNumber(arr, brr):
  
#     l = []
#     for i , ele in enumerate(set(brr)):
#         if ele not in arr:
#             l.append(ele)
#         else:
#             if brr.count(ele) > arr.count(ele):
#                 l.append(ele)



   

#     return l

# arr = list(map(int,input('arr: ').rstrip().split()))
# brr = list(map(int,input('brr: ').rstrip().split()))
# print(missingNumber(arr, brr))

def missingNumbers(arr, brr):
    x, y = len(arr), len(brr)
    max_length= max(max(arr), max(brr))
    arr_count , brr_count = [0]*max_length,[0]*max_length
    missing_nums = []
    for num in brr:
        brr_count[num-1] += 1
    for num in arr:
        arr_count[num-1] += 1
    for i in range(max_length):
        if arr_count[i] != brr_count[i]:
            missing_nums.append(i+1)
    return missing_nums,arr_count,brr_count

arr = list(map(int,input('arr: ').rstrip().split()))
brr = list(map(int,input('brr: ').rstrip().split()))
print(missingNumbers(arr, brr))