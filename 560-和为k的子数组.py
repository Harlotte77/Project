class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # count = 0
        # hash_dict = {0: 1}
        # target = 0
        # for i in range(len(nums)):
        #     target += nums[i]
        #     count += hash_dict.get(target - k, 0)
        #     hash_dict[target] = hash_dict.get(target, 0) + 1
        # return count

        count = 0
        sum_dict = {}
        sum_dict[0] = 1
        target = 0
        for i in range(len(nums)):
            target += nums[i]
            if target - k in sum_dict:
                count += sum_dict[target - k]
            sum_dict[target] = sum_dict.get(target, 0) + 1

        return count



if __name__ == '__main__':
    res = Solution().subarraySum(nums=[1,-1,0], k=0)
    print(res)
