Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.


code:
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        step = 0
        curt_end = 0
        longest = 0
        
        for i in range(len(nums)):
            #如果当前的index超过了当前层最远的地方（curt_end）
            if i > curt_end:
                #此时需要加一步，并且更新前层最远的地方到最远位置 
                step += 1
                curt_end = longest
            
            #实时更新最远位置
            longest = max(longest, nums[i] + i)
        
        return step