class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}  # 哈希表记录字符的最新位置
        longest = 0  # 最长子串的长度
        left = 0  # 左指针

        # 遍历字符串
        for right in range(len(s)):
            char = s[right]  # 当前字符

            # 如果当前字符重复且位置在左指针之后
            if char in char_index and char_index[char] >= left:
                # 移动左指针到重复字符的后一个位置
                left = char_index[char] + 1

            # 更新哈希表中当前字符的位置
            char_index[char] = right

            # 更新最长子串的长度
            longest = max(longest, right - left + 1)

        return longest


if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring("abcabcbb")
    print(res)
