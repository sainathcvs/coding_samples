a=[5,2,3,6,7,5]
i=3
j=0
while j<len(a):
	print a[i],a[j]
	if i!=j:
		if a[i]<a[j]:
			print 'in 1',i
			if i<j:
				i+=1
			else:
				tmp=a[i]
				del a[i]
				a.insert(0,tmp)
				j+=1
				i+=1																																																							
		elif a[i]>a[j]:
			print 'in 2',i
			tmp=a[i]
			del a[i]
			a.insert(j,tmp)
			i+=1
		else:
			print 'in 3',i
			tmp=a[i]
			del a[i]
			a.insert(0,tmp)
			j+=1
			i+=1
		print a