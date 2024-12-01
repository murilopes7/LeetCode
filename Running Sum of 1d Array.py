#This is a code of LeetCode
#This is the link https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution(object):
    def runningSum(self, nums):
       return [ sum(nums[:i+1]) for i in range(len(nums)) ]

    print (runningSum("self", [1,2,3,4]))