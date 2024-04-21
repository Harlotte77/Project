class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i, j = 0, len(height) - 1
        target = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            target = max(target, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return target


if __name__ == '__main__':
    res = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(res)
