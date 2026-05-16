s="ABCDABBCDABBBCCCDDEEEF"
ls=s.split()
ans=" "
for i in range(len(s)):
    if s[i] not in ans:
        ans=ans+s[i]
print(ans)