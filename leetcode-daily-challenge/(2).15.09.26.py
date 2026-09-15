'''2472. Maximum Number of Non-overlapping Palindrome Substrings'''
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i] = maximum number of palindromes
        # using the first i characters
        dp = [0] * (n + 1)

        # pal[i][j] = True if s[i:j+1] is palindrome
        pal = [[False] * n for _ in range(n)]

        # Build palindrome table
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if length <= 2:
                    pal[i][j] = (s[i] == s[j])
                else:
                    pal[i][j] = (s[i] == s[j] and pal[i + 1][j - 1])

        # DP
        for i in range(1, n + 1):
            # Don't take a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Try every possible starting point
            for j in range(i - k + 1):
                if i - j >= k and pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]
