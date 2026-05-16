n=int(input("Enter size:"))
print("Enter Elements:")
arr=[]
for i in range(n):
    ele=int(input("Enter Element:"))
    arr.append(ele)
sum=0    
for i in range(len(arr)):
    sum=sum+arr[i]
print("Sum of List:",sum)
