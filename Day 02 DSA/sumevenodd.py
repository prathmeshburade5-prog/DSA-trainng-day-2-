n=int(input("Enter size:"))
print("Enter Elements:")
arr=[]
even=0
odd=0
for i in range(n):
    ele=int(input("Enter Element:"))
    arr.append(ele)
    
for i in range(len(arr)):
    if arr[i]%2==0:
        even=even+arr[i]
    else:
        odd=odd+arr[i]
print("Sum of Even",even)
print("Sum of odd",odd)