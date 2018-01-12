a=[1,7,4,1,5,1,6,2,7,2,8,2,9,10,1,1]
arr1 = [i for i,val in enumerate(a) if val==1]
print arr1

arr2 = [i for i,val in enumerate(a) if val==2]
print arr2

#as both arrays are sorted,diff between min element(p) of arr2 and let elements that are just above(p1) n below(p2) p, 
#then min(p1-p,p-p2) is the min distance between 1 and 2 in the given array
a_ptr=0
min=500
while a_ptr<len(arr1):
	if arr2[0]-arr1[a_ptr]>0 and min>arr2[0]-arr1[a_ptr]:
		min=arr2[0]-arr1[a_ptr]
	a_ptr+=1
print min