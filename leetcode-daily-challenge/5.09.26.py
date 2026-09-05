class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        suffix_min = [0] * n

        # Build suffix minimum
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Find first stable index
        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            instability = prefix_max - suffix_min[i]

            if instability <= k:
                return i

        return -1
      '''3904
