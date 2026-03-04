
class Solution(object):
    def twoSum(self, nums, target):
       for i in range (0,n):
           for j in range (i+1,n):
              if nums[i]+nums[j]==target:
                  return[i,j]
       return[-1,-1]        
                     
nums=[2,7,11,15]
n=len(nums)
target = 26
result=Solution().twoSum(nums,target)
print(result)   

