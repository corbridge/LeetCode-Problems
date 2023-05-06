class Solution(object):
    def containsDuplicate(self, nums):
        new_set = set()

        for num in nums:
            if num in new_set:
                return True
            new_set.add(num)
        return False