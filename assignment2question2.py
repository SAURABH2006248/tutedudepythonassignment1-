n = int(input("enter the till which you want print and sum "))
sum=0
for i in range(1,n+1):
    print(i)
    sum=sum+i
print(f"the sum of numbers from 1 to {n} is :{sum} ")
