def findTotalDistance(len_arr,list_numbers):
    total_distance=0
    for i in range(len_arr-1):
        total_distance=total_distance+abs(list_numbers[i]-list_numbers[i+1])
    return total_distance    
len_arr=int(input())
list_numbers=list(map(int,input().split()))
print(findTotalDistance(len_arr,list_numbers))
