st=[0,0]
nums=[1,3,2,4]
target=5
List=[0,0]
for i,integer in enumerate(nums):
	for j,integer in enumerate(nums):
		if nums[i]==nums[j]:
			break
		if nums[i]+nums[j]==target:
			List[0]=j
			List[1]=i
			print(List)
