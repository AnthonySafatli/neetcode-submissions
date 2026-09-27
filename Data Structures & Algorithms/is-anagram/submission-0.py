class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1

        for letter in t:
            count = counts.get(letter, 0)
            if count == 0:
                return False
            
            count = count - 1
            counts[letter] = count
            if count == 0:
                del counts[letter]

        if len(counts.keys()) > 0:
            return False
        else:
            return True
        