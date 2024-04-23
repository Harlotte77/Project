from collections import Counter


class Solution(object):
    def findAnagrams_v1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 如果s的长度小于p的长度，则返回空
        if len(s) < len(p):
            return []

        # 记录s和p中每个字符出现的次数
        # Counter返回的是一个字典
        p_count = Counter(p)
        # 先记录s中前长度为p的字符出现的次数
        s_count = Counter(s[:len(p)])

        # 初始化结果列表
        res = []

        # 遍历s中所有可能的起始索引
        for i in range(len(s) - len(p) + 1):

            # 如果当前窗口内字符的怕频数与p中字符的频数相等
            # 则表明找到了一个异位词字串
            if s_count == p_count:
                res.append(i)

            # 如果当前窗口还没有达到s的末尾
            if i + len(p) < len(s):
                # 将窗口左边界字符的频数减一
                s_count[s[i]] -= 1
                # 如果窗口左边字符的频数为0，从哈希表中删除该字符的频数记录
                if s_count[s[i]] == 0:
                    del s_count[s[i]]

                # 将窗口右边界字符的频数加一
                s_count[s[i + len(p)]] += 1
        # 返回异位词字串的起始索引列表
        return res

    # 执行效率很慢，可能会超时
    def findAnagrams_v2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(p)
        res = []
        p_sort = sorted(p)
        s_sort = sorted(s[:len(p)])
        for i in range(len(s) - len(p) + 1):
            if s_sort == p_sort:
                res.append(i)
            if i + len(p) < len(s):
                n = i + n + 1
            s_sort = sorted(s[i + 1:n])
            n = len(p)
        return res


if __name__ == '__main__':
    res = Solution().findAnagrams("cbaebabacd", "abc")
    print(res)
