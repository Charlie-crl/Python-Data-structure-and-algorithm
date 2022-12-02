class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 轮转到7就不用转了
        k = k % n
        # 先倒序
        self.reverse(nums, 0, len(nums) - 1)
        # 分为两组（[0:k-1],[k:nums.size-1]）分别再倒过来
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
