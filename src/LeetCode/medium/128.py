# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


def solve(nums: List[int]) -> int:
    nums.sort()
        
    m = -1
    curr = 1

    for i in range(1, len(nums)):
        if nums[i] - 1 == nums[i-1]:
            curr += 1
        elif nums[i] != nums[i-1]:
            m = max(m, curr)
            curr = 1

    m = max(m, curr)
        
    if nums == []:
        m = 0

    return m
