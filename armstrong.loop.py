# to find the armstrong the number
num=int(input("enter the number:"))
user=len(str(num))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit**user
    temp=temp//10
if sum==num:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")



# l=[4,8,[6,1],2,3]
# print(l[0])
    