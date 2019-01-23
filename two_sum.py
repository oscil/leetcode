import random


# -----------------------------

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = dict()
        for i, e in enumerate(nums):
            result = target - e
            if result in d:
                return [d[result], i]
            d[e] = i



# ------------------------
if __name__ == '__main__':
    nums = list(range(20))
    random.shuffle(nums)
    s = Solution()

    nums = [-3, 4, 3, 90]
    target = 0

    print(nums)
    out = s.twoSum(nums, target)
    print(out)
    print([nums[out[0]], nums[out[1]]])
