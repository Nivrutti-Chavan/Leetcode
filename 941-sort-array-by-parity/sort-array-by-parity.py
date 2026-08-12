class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]%2!=0:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums