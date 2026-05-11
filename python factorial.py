def find_fact(n):
    fact=1
    for mul in range(1,n+1):
        fact*=mul
    return fact
ans=find_fact(int(input("enter the number n to find factorial :")))
print(ans)
