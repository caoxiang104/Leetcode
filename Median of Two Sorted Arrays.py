class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        low = 0
        high = n*2
        while low <= high:
            c1 = (low + high) // 2
            c2 = n + m - c1
            if c1 == 0:
                l1 = -float("Inf")
            else:
                l1 = nums1[(c1 - 1)//2]
            if c1 == 2*n:
                r1 = float("Inf")
            else:
                r1 = nums1[c1 // 2]
            if c2 == 0:
                l2 = -float("Inf")
            else:
                l2 = nums2[(c2 - 1) // 2]
            if c2 == 2 * m:
                r2 = float("Inf")
            else:
                r2 = nums2[c2 // 2]
            if l1 > r2:
                high = c1 - 1
            elif l2 > r1:
                low = c1 + 1
            else:
                break
        return (max(l1, l2) + min(r1, r2)) / 2.0


def main():
    s= Solution()
    # num1 = [2, 3, 4, 8, 9, 10, 12]
    # num2 = [1, 2, 3, 5, 6, 7, 15, 17, 20, 23]
    num1 = [3]
    num2 = [-2, -1]
    print(s.findMedianSortedArrays(num1, num2))


if __name__ == '__main__':
    main()