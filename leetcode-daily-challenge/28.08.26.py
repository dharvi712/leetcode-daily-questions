'''3734You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

 

Example 1:

Input: s = "baba", target = "abba"

Output: "baab"

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
The lexicographically smallest permutation that is strictly greater than target is "baab".
Example 2:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
Example 3:

Input: s = "abc", target = "abb"

Output: ""

Explanation:

s has no palindromic permutations. Therefore, the answer is "".

Example 4:

Input: s = "aac", target = "abb"

Output: "aca"

Explanation:

The only palindromic permutation of s is "aca".
"aca" is strictly greater than target. Therefore, the answer is "aca".
 

Constraints:

1 <= n == s.length == target.length <= 300
s and target consist of only lowercase English letters.'''
from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)

        # More than one odd frequency => impossible
        if sum(v % 2 for v in freq.values()) > 1:
            return ""

        # Characters available for the first half
        half = Counter()
        for c in freq:
            half[c] = freq[c] // 2

        m = n // 2

        # Middle character for odd length
        middle = ""
        for c in freq:
            if freq[c] % 2:
                middle = c
                break

        def build(h):
            return h + middle + h[::-1]

        # Check whether prefix can be made from half
        def can_make(prefix):
            cnt = Counter(prefix)

            for c in cnt:
                if cnt[c] > half[c]:
                    return False

            return True

        target_half = target[:m]

        # ------------------------------------------------
        # Case 1: We can make target's first half exactly
        # ------------------------------------------------
        if can_make(target_half):

            candidate = build(target_half)

            # IMPORTANT:
            # Even if the first half is equal, the complete
            # palindrome may still be > target.
            if candidate > target:
                return candidate

        # ------------------------------------------------
        # Case 2:
        # Find the smallest first half > target_half
        # ------------------------------------------------

        for i in range(m - 1, -1, -1):

            prefix = target_half[:i]

            if not can_make(prefix):
                continue

            remaining = half - Counter(prefix)

            # Try the smallest character > target_half[i]
            for code in range(ord(target_half[i]) + 1, ord('z') + 1):

                c = chr(code)

                if remaining[c] > 0:

                    remaining[c] -= 1

                    # Put all remaining characters in sorted order
                    suffix = []

                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        suffix.append(ch * remaining[ch])

                    h = prefix + c + ''.join(suffix)

                    return build(h)

        return ""
