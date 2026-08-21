'''3116.Kth Smallest Amount With Single Denominators
you are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.

 

Example 1:

Input: coins = [3,6,9], k = 3

Output: 9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:

Input: coins = [5,2], k = 7

Output: 12

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.

 

Constraints:

1 <= coins.length <= 15
1 <= coins[i] <= 25
1 <= k <= 2 * 109
coins contains pairwise distinct integers. 
code:'''
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd

        n = len(coins)

        # Remove redundant coins.
        # If a smaller coin divides a larger coin,
        # every multiple of the larger coin is already covered.
        coins.sort()
        useful = []

        for c in coins:
            redundant = False
            for x in useful:
                if c % x == 0:
                    redundant = True
                    break
            if not redundant:
                useful.append(c)

        coins = useful
        n = len(coins)

        # Count how many valid amounts are <= x
        def count(x):
            ans = 0

            # Inclusion-exclusion over all subsets
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        g = gcd(lcm, coins[i])
                        lcm = lcm // g * coins[i]

                        # No multiple of this LCM can be <= x
                        if lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                amount = x // lcm

                if bits % 2 == 1:
                    ans += amount
                else:
                    ans -= amount

            return ans

        # The smallest coin alone can produce k amounts,
        # so this is always a valid upper bound.
        left = 1
        right = coins[0] * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
