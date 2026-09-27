class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

        length = len(s)

        idx1 = -1
        idx2 = 0
        while True:
            idx1 += 1
            char1 = None
            if idx1 != length:
                char1 = s[idx1]

            while char1 not in valid_chars and char1 is not None:
                idx1 += 1
                if idx1 != length:
                    char1 = s[idx1]
                else:
                    char1 = None

            idx2 -= 1
            char2 = None
            if idx2 != (length+1) * -1:
                char2 = s[idx2]

            while char2 not in valid_chars and char2 is not None:
                idx2 -= 1
                if idx2 != (length+1) * -1:
                    char2 = s[idx2]
                else:
                    char2 = None

            if char1 is None and char2 is None:
                return True
            if s[idx1].lower() == s[idx2].lower():
                continue
            else:
                return False

        


        