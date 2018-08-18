def power(n):
    while (n % 2 == 0):
         n /= 2;         
    return n == 1;
    
n=int(input())
if power(n):
	print("yes")
else:
	print("no")
