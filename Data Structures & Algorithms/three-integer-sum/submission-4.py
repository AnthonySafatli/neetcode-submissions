from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        triples = set()

        for num in nums:
            counts[num] += 1

        if counts[0] >= 3:
            triples.add((0, 0, 0))

        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums):
                if j <= i:
                    continue

                if num_i == 0 and num_j == 0:
                    continue

                i_j = num_i + num_j

                target = -i_j
                target_amount = 1
                if target == num_i or target == num_j:
                    target_amount = 2

                if counts[target] >= target_amount:
                    triples.add(tuple(sorted([num_i, num_j, target])))

        result = []
        for triple in triples:
            result.append(list(triple))

        return result

                
                
            


                                        



