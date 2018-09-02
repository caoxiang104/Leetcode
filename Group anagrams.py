# -*- coding:utf-8 -*-
"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
"""


# class Solution:
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         if len(strs) == 0: return []
#         out = []
#         temp = [(i, list(strs[i])) for i in range(len(strs))]
#         for i in range(len(temp)):
#             temp[i][1].sort()
#         temp.sort(key=lambda x: x[1])
#         out_temp = [strs[temp[0][0]]]
#         for i in range(1, len(temp)):
#             if temp[i][1] == temp[i-1][1]:
#                 out_temp.append(strs[temp[i][0]])
#             else:
#                 out.append(out_temp)
#                 out_temp = [strs[temp[i][0]]]
#         if out_temp:
#             out.append(out_temp)
#         return out


class Solution:
    # 坑1：for 循环内部不能修改迭代值
    # 坑2: 可变类型包括dict,list都不可以作为字典的key，而原子类型以及tuple则可以
    # tips: list(dic.values())
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for x in strs:
            sorted_x = "".join(sorted(x))
            if sorted_x in dic:
                dic[sorted_x].append(x)
            else:
                dic[sorted_x] = [x]

        return list(dic.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))