class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0 or len(nums) == 1: return True
        i = 0
        max_len = 0
        start_point = 0
        while i <= len(nums) - 1:
            if nums[i] == 0:
                return False
            if i + nums[i] >= len(nums) - 1:
                return True
            for j in range(i + 1, i + nums[i]):
                if j + nums[j] >= len(nums) - 1:
                    return True
                elif j + nums[j] > max_len:
                    max_len = j + nums[j]
                    start_point = j
            i = start_point
        return False


s = Solution()
print(s.canJump([3, 2, 1, 0, 4]))