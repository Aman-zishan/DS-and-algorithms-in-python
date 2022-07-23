class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[n]=i
        return        
