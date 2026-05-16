rec={}
n=int(input("Enter number of Students:"))
for i in range(n):
    name=input("Enter name:")
    marks=input("Enter percent:")
    rec[name]=marks
    
print(rec)
for x in rec:
    print(x,"\t",rec[x])