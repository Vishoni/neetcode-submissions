class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        longest = 0
        for num in numsset:
            if num-1 not in numsset:
                current = num
                count = 1

                while current+1 in numsset:
                    current +=1
                    count +=1

                longest = max(count,longest)
        return longest