class Solution:
    def twoSum_v1(self, nums, target: int):
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

    def twoSum_v2(self, nums, target):
        num_dict = {}
        for key, value in enumerate(nums):
            print(key, value)
            complement = target - value
            if complement in num_dict:
                return [num_dict[complement], key]
            num_dict[value] = key
        return None


if __name__ == '__main__':
    result = Solution().twoSum_v2([2, 7, 11, 15], 9)
    print(result)
