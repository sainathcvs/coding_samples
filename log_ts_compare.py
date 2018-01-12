import re
import time

#Inputs
lines=['2016-02-12T03:21:56Zjkkkjhjkhklsadfjklsajfklasjklfjkasljfkljasklfj',
'2016-02-12T03:21:57Zjhjkhj','2016-02-12T03:21:58Zjkhjkhjkhlkhlkhlk','2016-02-12T03:21:59Z']
beg='2016-02-12T03:21:57Z'
end='2016-02-12T03:21:60Z'

ts_arr=[]
for c in lines:
	tmp=re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z',c)
	if tmp:
		ts_arr.append(tmp.group())

pattern='%Y-%m-%dT%H:%M:%SZ'
beg_epoch=int(time.mktime(time.strptime(beg, pattern)))
end_epoch=int(time.mktime(time.strptime(end, pattern)))

final_indices=[]
for i in range(len(ts_arr)):
	ts_epoch=int(time.mktime(time.strptime(ts_arr[i], pattern)))
	if ts_epoch>=beg_epoch and ts_epoch<end_epoch:
		final_indices.append(i)

for i in range(len(final_indices)):
	print lines[final_indices[i]]