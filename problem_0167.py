class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i<j:
            sums = numbers[i]+numbers[j]

            if sums < target : i+=1
            elif sums > target : j-=1
            else : return i+1,j+1
        