from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
# YOUR ANSWER
    answer = []
    length = len(nums)
    for i in range(0,length):
        if i == length - 1:
            break
        else:
            for j in range(i+1,length):
                if nums[i] + nums[j] == target:
                    answer = [i,j]
                    return answer
    return answer