a="abcd"
b="cd"
stri = a
cnt=1
is_found=False

#while(len(stri)<2*len(b)):
while(1):
	if len(a)==len(b):
		tmp=stri+a
		print b,tmp
		if b in tmp:
			print "in"
			is_found = True
			cnt=2
			break

	elif len(a)>len(b):
		print "sfas"
		tmp=stri+a
		print b,tmp
		if b not in a:
			if b in tmp:
				print "in"
				is_found = True
				cnt=2
				break
	else:
		if not b in stri:
			stri=stri+a
			cnt+=1
		else:
			is_found=True
			break
if not is_found:
	cnt=-1
print cnt