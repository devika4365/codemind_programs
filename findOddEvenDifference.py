def findOddEvenDifference(len_of_arr,list_numbers):
    odd=0
    even=0
    for i in range(len_of_arr):
        if list_numbers[i]%2==0:
            even=even+list_numbers[i]
        else:
            odd=odd+list_numbers[i]
    return odd-even        
len_of_arr=int(input())
list_numbers=list(map(int,input().split()))
print(findOddEvenDifference(len_of_arr,list_numbers))
