import re
a='6468536914'
orig_ph='+71(646) 853-6914'
a_removed=re.sub(r'[^\w]', '', orig_ph)
rev_ph=a_removed[::-1]
formatted_ph=''
for i in range(len(rev_ph)):
	if i ==4 or i==7:
		formatted_ph+='-'
	if i==10:
		formatted_ph+='-'
	if i<4:
		formatted_ph+=rev_ph[i]
	else:
		formatted_ph+='*'
if orig_ph.find('+')>-1:
	formatted_ph+='+'
print formatted_ph[::-1]
email='abdfdc@gmail.com'
at_index=email.find('@')
prefix=email[:at_index]
postfix=email[at_index:]
email_masked=prefix[0]+'*****'+prefix[-1]+postfix
print email_masked