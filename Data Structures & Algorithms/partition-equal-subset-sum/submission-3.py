class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        partition = total // 2

        memo = {}

        def dfs(i, curr_sum):
            if i == len(nums):
                return True if curr_sum == 0 else False

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            skip = dfs(i + 1, curr_sum) 
            take = dfs(i + 1, curr_sum - nums[i]) 

            memo[(i, curr_sum)] = skip or take
            
            return memo[(i, curr_sum)]

        return dfs(0, partition)


            