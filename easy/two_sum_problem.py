class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		nums_map = {}
		for index, value in enumerate(nums):
			complement = target - value
			if complement in nums_map:
				print([nums_map[complement], index])
				return [nums_map[complement], index]
			nums_map[value] = index


a = Solution()
a.twoSum([2,7,11,15], 9)
