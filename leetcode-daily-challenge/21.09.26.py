class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            rem = num % k
            new_dp = [0] * k

            # Start a new subarray
            new_dp[rem] += 1

            # Extend previous subarrays
            for r in range(k):
                new_rem = (r * rem) % k
                new_dp[new_rem] += dp[r]

            dp = new_dp

            for r in range(k):
                ans[r] += dp[r]

        return ans
      '''

Code

Testcase
Testcase

Test Result
3524. Find X Value of Array I''''
