from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}
        left = 0
        satisfied = 0
        required = len(need)

        res_left, res_len = 0, float("inf")

        for right, c in enumerate(s):
        
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                satisfied += 1

        
            while satisfied == required:
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res_left = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    satisfied -= 1
                left += 1

        return "" if res_len == float("inf") else s[res_left: res_left + res_len]