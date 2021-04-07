def findLargeSmallDifference(len_arr,list_numbers):
    Large=max(list_numbers)
    Small=min(list_numbers)
    return Large-Small
len_arr=int(input())
list_numbers=list(map(int,input().split()))
print(findLargeSmallDifference(len_arr,list_numbers))
