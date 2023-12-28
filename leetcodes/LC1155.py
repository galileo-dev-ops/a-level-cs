## This is Leetcode #1155 - Number of Dice Rolls With Target Sum
### https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # initialize the dp array
        dp = [[0 for i in range(target+1)] for j in range(n+1)]
        
        # base case
        dp[0][0] = 1
        
        # iterate through all the dices
        for i in range(1, n+1):
            # iterate through all the possible target values
            for j in range(1, target+1):
                # iterate through all the possible values of the dice
                for l in range(1, k+1):
                    # if the value of the dice is less than the target value
                    if l <= j:
                        # add the number of ways to get the target value with the dice value
                        dp[i][j] += dp[i-1][j-l]
        
        # return the number of ways to get the target value with n dices
        return dp[n][target] % (10**9 + 7)


Solution().numRollsToTarget(2, 6, 7)
