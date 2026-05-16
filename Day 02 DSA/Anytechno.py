no=int(input("Enter no:"))
save=no
count=0
while no>0:
    no=no//10
    count=count+1
no=save
if count%2==0:
    mid=count//2
    n1=no//10**mid
    n2=no%10**mid
    sum=n1+n2
    sqt=sum**2
    if sqt==save:
        print("no is tech")
    else:
        print("no is not tech")
else:
    print("Do not run if no is odd")