s1,s2=map(str,raw_input().split())
l1=len(s1)
l2=len(s2)
if l1==l2:
	if s1==s2:
		print s1
	elif s1>s2:
		print s1
	else:
		print s2
elif l1>l2:
	print s1
else:
	print s2
