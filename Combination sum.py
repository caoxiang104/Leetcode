# -*- coding:utf-8 -*-
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
"""


# class Solution:
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         num_dict = [[] for i in range(target + 1)]
#         for i in range(len(candidates)):
#             for j in range(1, target//candidates[i]+1):
#                 num_dict[candidates[i]*j].append([candidates[i] for k in range(j)])
#                 for k in range(1, target - candidates[i]*j + 1):
#                     if num_dict[k]:
#                         for m in num_dict[candidates[i]*j]:
#                             for n in num_dict[k]:
#                                 num_dict[candidates[i]*j + k].append(n + m)
#         out = []
#         for i in range(len(num_dict[target])):
#             num_dict[target][i].sort()
#             if num_dict[target][i] not in out:
#                 out.append(num_dict[target][i])
#         return out


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.combine([], candidates, target)
        return self.res

    def combine(self, temp_list, candidates, target):
        for idx, i in enumerate(candidates):
            if target == i:
                self.res.append(temp_list + [i])
            elif i < target:
                self.combine(temp_list + [i], candidates[idx:], target - i)
            else:
                break


s = Solution()
print(s.combinationSum([2, 1], 4))