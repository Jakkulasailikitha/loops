count=0
i=1
n=int(input("enter the number"))
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime number")
else:
    print("not a prime number")