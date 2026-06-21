from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices, values decreasing front → back
        result = []

        for right in range(len(nums)):
        # 1. Remove indices that are out of the window
            if dq and dq[0] < right - k + 1:
                dq.popleft()

        # 2. Remove indices whose values are <= current (useless candidates)
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

        # 3. Window is fully formed — record the maximum (front of deque)
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result