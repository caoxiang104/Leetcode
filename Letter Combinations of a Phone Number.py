# -*- coding:utf-8 -*-
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return ""
        c = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        list_ = []
        for i in digits:
            list_.append(c[int(i)])
        out_list = []

        def recurse(temp_list, string, index, out):
            if temp_list =="" and index < len(digits) - 1:
                recurse(list_[index + 1], string, index + 1, out)
            for i in temp_list:
                temp = i
                if index == len(digits) - 1:
                    out.append(string + temp)
                else:
                    recurse(list_[index + 1], string+temp, index + 1, out)

        recurse(list_[0], "", 0, out_list)
        return out_list


def main():
    s = Solution()
    print(s.letterCombinations(""))


if __name__ == '__main__':
    main()