'''1621. Number of Sets of K Non-Overlapping Line Segments'''
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * n for _ in range(k + 1)]

        # 0 segments -> 1 way
        for i in range(n):
            dp[0][i] = 1

        for seg in range(1, k + 1):
            total = 0

            for i in range(1, n):
                total = (total + dp[seg - 1][i - 1]) % MOD
                dp[seg][i] = (dp[seg][i - 1] + total) % MOD

        return dp[k][n - 1]
