class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        current = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if nums[i - 1] == current:
                    result.append(str(current))
                else:
                    result.append(f"{current}->{nums[i - 1]}")
                current = nums[i]

        if current == nums[-1]:
            result.append(str(current))
        else:
            result.append(f"{current}->{nums[-1]}")

        return result
