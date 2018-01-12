key='4071321'
alphabet_arr= string.ascii_lowercase
num_arr=range(1,27)
alp_dict=dict(zip(alphabet_arr,num_arr))
str_given='Hi, this is an example'
for i in range(len(str_given)):
	print str_given[i]
	s=str_given[i]
	alp_dict[s.lower()]+key[]