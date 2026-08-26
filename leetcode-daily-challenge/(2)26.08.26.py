'''374.
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n'''
class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)          # provided API
            if result == 0:
                return mid
            elif result == -1:            # mid is too high
                high = mid - 1
            else:                         # result == 1, mid is too low
                low = mid + 1
        return -1  # unreachable if a valid answer is guaranteed
