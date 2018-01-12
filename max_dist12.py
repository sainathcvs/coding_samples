a=[1,7,4,1,5,1,6,12,7,12,8,12,9,10,1,1]
p1=-1
p2=-1
lp1=-1
lp2=-1
for index in range(len(a)):
	if p1==-1 and a[index]==1:
		p1 = index
	elif p2==-1 and a[index]==2:
		p2=index
	elif a[index]==2 and p1!=-1:
		lp1=index
	elif a[index]==1 and p2!=-1:
		lp2=index
print max(lp1-p1,lp2-p2)