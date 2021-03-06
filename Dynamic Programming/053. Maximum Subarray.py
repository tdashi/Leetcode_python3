Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


跑出来的结果:
             [-2,1,-3, 4,-1, 2, 1,-5, 4]
local_max :  [0, 1, 0, 4, 3, 5, 6, 1, 5]
global_max : [0, 1, 1, 4, 4, 5, 6, 6, 6]

  
'''
clarification
input: list int, negative, None? []?
output: int

1. brute force
use two for loop to list all the subarray, get the max
time: O(n^2), space: O(1)

2. optimal
smaller problem
assume already know the curt_sum for index = i - 1, how to get the new curt_sum for index = i?
dp[i]: curt sum for nums[:i+1]
dp[i] = max(dp[i - 1], 0) + nums[i]
res = max(res, dp[i])

-> optimal to save space:
curt_sum = nums[0]
curt_sum = max(curt_sum, 0) + nums[i]
res = max(res, curt_sum)

time: O(n), space: O(1)
'''
# dp array
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
            res = max(res, dp[i])
        
        return res
# optimal: save space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curt_sum, res = nums[0], nums[0]
        for i in range(1, len(nums)):
            curt_sum = max(curt_sum, 0) + nums[i]
            res = max(res, curt_sum)
        
        return res
  
  
  
  
code:
#greedy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #当所有的nums都小于0时,其maxsum一定是最大的那个值
        if max(nums) < 0:
            return max(nums)
        
        #使用这两个值记录当前最大和,以及全局最大和
        local_num, global_num = 0, 0
        
        for num in nums:
            #每次都需要和0比较,因为当当前和<0,则说明该段num不用计入总sum中
            #判断本地最大值加上当前数字是否还大于0，如果大于0课继续向后找 
            #如果小于0则证明加上后面这个数字“不划算”，还不如本身的local值大，所以在此断掉，初始化local为0 
            local_num = max(0, local_num + num)
            global_num = max(global_num, local_num)
        
        return global_num
        
        
