class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def backtrack(i, rem, temp):
            if rem == 0:
                ret.append(temp[:])
                return

            if i == len(nums) or rem < 0:
                return
            
            temp.append(nums[i])
            backtrack(i, rem - nums[i], temp)
            temp.pop()
            backtrack(i + 1, rem, temp)

            return

        backtrack(0, target, [])

        return ret