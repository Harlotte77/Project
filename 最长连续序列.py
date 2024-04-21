class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        set_nums = set(nums)  # [9, 1, 4, 7, 3, 0, 5, 8, -1, 6]
        longest_streak = 0
        for num in set_nums:
            # 找到序列的开头
            if num - 1 not in set_nums:
                current_num = num
                current_streak = 1
                while current_num + 1 in set_nums:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak


if __name__ == '__main__':
    res = Solution().longestConsecutive([9, 1, 4, 7, 3, 0, 5, -1, 8, -1, 6])
    print(res)
