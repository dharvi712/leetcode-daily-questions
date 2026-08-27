'''ou are given two strings `s` and `target`, both having length `n`, consisting of lowercase English letters.

Return the **lexicographically smallest permutation** of `s` that is **strictly** greater than `target`. If no permutation of `s` is lexicographically strictly greater than `target`, return an empty string.

A string `a` is **lexicographically strictly greater **than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears later in the alphabet than the corresponding letter in `b`.

**Example 1:**

**Input:** s = "abc", target = "bba"

**Output:** "bca"

**Explanation:**

- The permutations of `s` (in lexicographical order) are `"abc"`, `"acb"`, `"bac"`, `"bca"`, `"cab"`, and `"cba"`.
- The lexicographically smallest permutation that is strictly greater than `target`is `"bca"`.

**Example 2:**

**Input:** s = "leet", target = "code"

**Output:** "eelt"

**Explanation:**

- The permutations of `s` (in lexicographical order) are `"eelt"`, `"eetl"`, `"elet"`, `"elte"`, `"etel"`, `"etle"`, `"leet"`, `"lete"`, `"ltee"`, `"teel"`, `"tele"`, and `"tlee"`.
- The lexicographically smallest permutation that is strictly greater than `target`is `"eelt"`.

**Example 3:**

**Input:** s = "baba", target = "bbaa"

**Output:** ""

**Explanation:**

- The permutations of `s` (in lexicographical order) are `"aabb"`, `"abab"`, `"abba"`, `"baab"`, `"baba"`, and `"bbaa"`.
- None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

**Constraints:**

- `1 <= s.length == target.length <= 300`
- `s` and `target` consist of only lowercase English letters.'''
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Match target from left to right
        i = 0
        while i < n:
            x = ord(target[i]) - ord('a')

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            i += 1

        # i is the first position we cannot match.
        # If i == n, target itself is possible.
        # We still need to find a strictly greater permutation.
        if i == n:
            i = n - 1
            cnt[ord(target[i]) - ord('a')] += 1

        # Try to make the string greater.
        # We go from right to left because we want
        # the longest possible prefix equal to target.
        for pos in range(i, -1, -1):

            if pos < i:
                # Restore target[pos], because we move backwards.
                x = ord(target[pos]) - ord('a')
                cnt[x] += 1

            x = ord(target[pos]) - ord('a')

            # Find the smallest character greater than target[pos]
            for c in range(x + 1, 26):
                if cnt[c] > 0:

                    cnt[c] -= 1

                    # Prefix stays equal to target
                    ans = target[:pos] + chr(c + ord('a'))

                    # Smallest possible suffix
                    for j in range(26):
                        ans += chr(j + ord('a')) * cnt[j]

                    return ans

        return ""
