l1=[2,4,3]
l2=[5,6,4,5]
rl=[]

if(len(l1)==len(l2)):
	for i in range(len(l1)):
			rl.append(l1[i]+l2[i])
	print(rl)
else:
	print("Different length of list")
