s="learning python is easy from ashish sir"
ls=s.split()
for i in range(len(ls)):
    ls[i]=ls[i][::-1]
print(s)
print(" ".join(ls))
