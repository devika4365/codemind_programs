def findTotalFeet(len_arr,list_numbers):
    feet=0
    for i in range(len_arr):
        feet=feet+(list_numbers[i]//12) # 18--->1 12---->1 27---->2
    return feet
len_arr=int(input())
list_numbers=list(map(int,input().split()))
print(findTotalFeet(len_arr,list_numbers))
