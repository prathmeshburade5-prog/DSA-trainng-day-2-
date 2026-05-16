n=int(input("Enter size:"))
print("Enter Elements:")
arr=[]
for i in range(n):
    ele=int(input("Enter Element:"))
    arr.append(ele)
    
for i in range(len(arr)):
    print(arr[i])