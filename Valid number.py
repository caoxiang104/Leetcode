"""
验证给定的字符串是否为数字。
例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。
"""


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sign_index = 0
        exp_index = 0
        dot_index = 0
        num_index = 0
        k_index = 0
        for i in range(len(s)):
            if s[i] == " ":
                if dot_index or exp_index or sign_index or num_index:
                    k_index = 1
            elif k_index == 1:
                return False
            elif s[i] == "e" or s[i] == "E":
                if exp_index == 0 and num_index:
                    exp_index = 1
                    sign_index = 0
                    num_index = 0
                    dot_index = 0
                else:
                    return False
            elif s[i] == '+' or s[i] == "-":
                if sign_index == 0 and dot_index == 0 and num_index == 0:
                    sign_index = 1
                else:
                    return False
            elif s[i] == '.':
                if dot_index == 0 and exp_index == 0:
                    dot_index = 1
                else:
                    return False
            else:
                if s[i].isdigit():
                    num_index = 1
                    sign_index = 1
                else:
                    return False
        if num_index:
            return True
        else:
            return False


s = Solution()
print(s.isNumber("  -1.23e123"))