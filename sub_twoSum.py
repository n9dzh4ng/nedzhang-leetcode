class Solution:
	def twoSum(self, nums, target):
		ls=[]
		for i in range(0, len(nums)):
			item=target-nums[i]
			nums[i] = "done"
			if item in nums:
				ls.append(i)
				ls.append(nums.index(item))
		return ls
nums=[1,2,3,4,5]
target=6
a=Solution()
ls=a.twoSum(nums,target)
print ls
