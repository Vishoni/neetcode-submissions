class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ""
        prefix = strs[0]
        for i in range(1, n):
            current = strs[i]
            j = 0
            while j < min(len(prefix), len(current)):
                if prefix[j] != current[j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix