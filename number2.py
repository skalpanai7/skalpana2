def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a,b=map(int,raw_input().split())
GCD=gcd(a,b)
print(GCD)
