class Solution:
    def findRepeatNumber(self, nums):
        dictflag = {}
        for i in range(len(nums)):
            if dictflag.__contains__(nums[i]):
                return nums[i]
            else:
                dictflag[nums[i]] = 0


s = Solution()
r = s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
print(r)
        