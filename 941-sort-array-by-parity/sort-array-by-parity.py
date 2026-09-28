class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0]*n
        left=0
        right=n-1

        for i in range(0,n):
            if nums[i]%2!=0:
                arr[right]=nums[i]
                right-=1
            elif nums[i]%2==0:
                arr[left]=nums[i]
                left+=1
        return arr