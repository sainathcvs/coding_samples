st='cd'
reg='a*b*cd'
bcnt=0
for i in range(0,len(reg)):
	print reg[i],st[bcnt],bcnt
	if reg[i]=='*':
		tmp=st[bcnt]
		bcnt+=1
		while st[bcnt] == tmp:
			bcnt+=1
	elif reg[i]!=st[bcnt] and reg[i+1]!='*':
		print '-1'
		break
	elif reg[i]==st[bcnt]:
		bcnt+=1

		