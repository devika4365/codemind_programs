def findMaxDifference(len_arr,list_numbers):
    maximum=-1
    difference=0
    for i in range(len_arr-1):
        difference=list_numbers[i]-list_numbers[i+1]
        if difference>maximum:
            maximum=difference
    return maximum        
len_arr=int(input())
list_numbers=list(map(int,input().split()))
print(findMaxDifference(len_arr,list_numbers))
