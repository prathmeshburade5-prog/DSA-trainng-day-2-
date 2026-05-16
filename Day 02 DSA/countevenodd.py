n=int(input("Enter size:"))
print("Enter Elements:")
arr=[]
even=0
odd=0
e1=0
o1=0
for i in range(n):
    ele=int(input("Enter Element:"))
    arr.append(ele)
    
for i in range(len(arr)):
    if arr[i]%2==0:
        even=even+arr[i]
        e1=e1+1
    else:
        odd=odd+arr[i]
        o1=o1+1
print("Sum of Even",even)
print("Sum of odd",odd)
print("Count of even:",e1)
print("Count of odd:",o1)
