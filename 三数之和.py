class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_list = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k, j = i + 1, n - 1
            while k < j:
                res = nums[i] + nums[j] + nums[k]
                if res == 0:
                    res_list.append([nums[i], nums[k], nums[j]])
                    while k < j and nums[k] == nums[k + 1]:
                        k += 1
                    while k < j and nums[j] == nums[j - 1]:
                        j -= 1
                    k += 1
                    j -= 1
                elif res < 0:
                    k += 1
                else:
                    j -= 1
        return res_list


if __name__ == '__main__':
    res = Solution().threeSum([0,1,1])
    print(res)
