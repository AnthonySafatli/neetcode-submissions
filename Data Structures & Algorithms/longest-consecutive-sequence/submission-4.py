class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapping = {}
        for num in nums:
            mapping[num] = True

        longest_seq = 0
        current_seq = 0
        for num in mapping.keys():
            if not mapping.get(num-1, False):
                current_seq = 1
                current = num+1
                while mapping.get(current, False):
                    current += 1
                    current_seq += 1
                    
                if current_seq > longest_seq:
                    longest_seq = current_seq
        
        return longest_seq
