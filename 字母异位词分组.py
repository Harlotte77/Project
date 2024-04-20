import collections
from typing import List


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sort_list = collections.defaultdict(list)
        for item in strs:
            key = "".join(sorted(item))
            sort_list[key].append(item)
        return list(sort_list.values())


if __name__ == '__main__':
    res = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
