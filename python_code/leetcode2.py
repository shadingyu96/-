class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dct = {}
        # for i, j in enumerate(nums):
        #     cp = target - j
        #     if cp in dct:
        #         return [dct[cp], i]
        #     else:
        #         dct[j] = i
        hash_map = dict()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [i, hash_map[target - x]]
            else:
                hash_map[x] = i


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([3, 2, 4], 6))
