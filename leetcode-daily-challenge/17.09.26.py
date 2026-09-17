class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        
        INF = float('inf')
        
        # best[i] = minimum length of a valid subarray
        # completely inside arr[0...i]
        best = [INF] * n
        
        prefix = 0
        seen = {0: -1}
        
        ans = INF
        min_len = INF
        
        for i in range(n):
            prefix += arr[i]
            
            # Check if a subarray ending at i has sum = target
            if prefix - target in seen:
                start = seen[prefix - target] + 1
                length = i - start + 1
                
                # Need another subarray before this one
                if start > 0 and best[start - 1] != INF:
                    ans = min(ans, length + best[start - 1])
                
                min_len = min(min_len, length)
            
            best[i] = min_len
            
            # Store earliest occurrence of prefix sum
            if prefix not in seen:
                seen[prefix] = i
        
        return -1 if ans == INF else ans
      '''

Code

Testcase
Testcase

Test Result
1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
