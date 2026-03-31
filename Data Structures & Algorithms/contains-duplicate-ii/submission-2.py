class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, min(len(nums), i + k + 1)):
                if nums[i] == nums[j]:
                    return True
        return False