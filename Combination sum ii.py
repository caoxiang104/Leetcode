# -*- coding:utf-8 -*-
"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
"""


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.combine([], candidates, target)
        return self.res

    def combine(self, result, candidates, target):
        for idx, i in enumerate(candidates):
            if idx != 0 and candidates[idx] == candidates[idx - 1]:
                continue
            if target == i:
                self.res.append(result + [i])
            elif i < target:
                self.combine(result + [i], candidates[idx + 1:], target - i)
            else:
                break
        return


s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))