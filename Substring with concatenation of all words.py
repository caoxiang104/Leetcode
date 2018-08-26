# -*- coding:utf-8 -*-
"""
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
"""


# class Solution:
#     def __init__(self):
#         self.wordstrs = set()
#
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         if not words or not s:
#             return []
#         lengthWord = len(words[0])
#         length = lengthWord * len(words)
#         result = []
#         firstwords = set([i[0] for i in words])
#         i = 0
#         words.sort()
#         while i <= len(s) - length:
#             if s[i] in firstwords:
#                 temp = self.splitString(lengthWord, s[i:i+length])
#                 temp.sort()
#                 if temp == words:
#                     result.append(i)
#             i += 1
#         return result
#
#     def splitString(self, length, string):
#         out = []
#         n = len(string)
#         i = 0
#         while i <= n - length:
#             out.append(string[i:i+length])
#             i += length
#         return out


# class Solution:
#     def __init__(self):
#         self.wordstrs = set()
#
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         self.wordstrings(words, "")
#         if not words:
#             return []
#         length = len(words) * len(words[0])
#         result = []
#         for i in range(len(s)):
#             if len(s) >= i + length and s[i:i + length] in self.wordstrs:
#                 result.append(i)
#         return result
#
#     def wordstrings(self, words, string):
#         if not words:
#             self.wordstrs.add(string)
#         else:
#             for i in range(len(words)):
#                 self.wordstrings(words[:i] + words[i + 1:], string + words[i])


class Solution:
    """
    输入:
       s = "barfoothefoobarman", words = ["foo","bar"]
    输出:
       [0,9]
    解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
    输出的顺序不重要, [9,0] 也是有效答案。
    """
    def __init__(self):
        self.wordstrs = set()

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []
        length_word = len(words[0])
        length_words = length_word * len(words)
        len_s = len(s)
        result = []
        words_dict = dict()
        for i in words:
            if i in words_dict:
                words_dict[i] += 1
            else:
                words_dict[i] = 1
        for i in range(length_word):
            self.findSubString(i, i, length_word, length_words, len_s, result, s, words_dict)
        return result

    def findSubString(self, cur_point, start_point, length_word, length_words, len_s, result, s, words_dict):
        temp_dict = dict()
        while cur_point <= len_s - length_word:
            word = s[cur_point:cur_point + length_word]
            cur_point += length_word
            if word not in words_dict.keys():
                temp_dict.clear()
                start_point = cur_point
            else:
                if word in temp_dict:
                    temp_dict[word] += 1
                else:
                    temp_dict[word] = 1
                while temp_dict[word] > words_dict[word]:
                    temp_dict[s[start_point:start_point+length_word]] -= 1
                    start_point += length_word
                if cur_point - start_point == length_words:
                    result.append(start_point)


s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))