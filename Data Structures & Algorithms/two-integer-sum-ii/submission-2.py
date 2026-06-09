class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pos = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    pos.append(i+1)
                    pos.append(j+1)
        return pos

        