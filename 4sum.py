# -*- coding:utf-8 -*-\
"""
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


# O(n^2)
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        s, dic = set(), {}
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                value = nums[i] + nums[j]
                if value in dic.keys():
                    dic[value].append((i, j))
                else:
                    dic[value] = [(i, j)]

        for i in range(n):
            for j in range(i + 1, n):
                exp = target - nums[i] - nums[j]
                if exp in  dic.keys():
                    for temp in dic[exp]:
                        if temp[0] > j:
                            s.add((nums[i], nums[j], nums[temp[0]], nums[temp[1]]))
        return [list(i) for i in s]


def main():
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))


if __name__ == '__main__':
    main()