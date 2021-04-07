applicationID=int(input())
sum_digits=0
while applicationID!=0:
    rem=applicationID%10
    applicationID=applicationID//10
    sum_digits=sum_digits+rem
    if applicationID==0 and sum_digits>26:
        applicationID=sum_digits
        sum_digits=0
print(chr(64+sum_digits)) #64+1=65---A        
