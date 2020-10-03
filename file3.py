#Using FOR and WHILE loops in python
#Finding sum of 1 to n integers using loops in python
n=int(input())
sum=0
i=0
while i<=n:
   sum=sum+i
   i+=1
print("Sum of",n,"integers using while loop =",sum)
sum=0 
for i in range(1,n+1):
    sum=sum+i
print("Sum of",n,"integers using for loop =",sum)
