string=raw_input()
list=[]
for i in string:
	if i.isdigit():
		list.append(i)
print "".join(list)
