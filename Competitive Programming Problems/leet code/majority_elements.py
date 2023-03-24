class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = dict()
        for i in range(len(nums)):
            if nums[i] in elements:
                elements[nums[i]] += 1
            else:
                elements[nums[i]] = 1
        
        return (max(zip(elements.values(), elements.keys()))[1])

solution = Solution()
print(solution.majorityElement([3, 4, 3]))