# aking the user  for input to print the tables
i=1
user=int(input("enter the number where we can start the table here:"))
while i<=user:
    j=1
    while j<=10:
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1
    print()