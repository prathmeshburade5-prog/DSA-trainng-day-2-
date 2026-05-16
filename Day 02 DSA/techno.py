no=int(input("Enter no:"))

save=no
n1=no//100
n2=no%100

sum=n1+n2
sqt=sum**2
    
if sqt==save:
    print("no is tech")
else:
    print("no is not tech")