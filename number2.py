def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
m,n=map(int,raw_input().split())
GCD=gcd(m,n)
print(GCD)
