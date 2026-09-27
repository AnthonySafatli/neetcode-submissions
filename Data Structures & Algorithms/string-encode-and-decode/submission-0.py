class Solution:

    def encode(self, strs: List[str]) -> str:
        meta = str(len(strs))

        encoded = ""

        for s in strs:
            meta += "." + str(len(s))
            encoded += s

        return meta + "." + encoded

    def decode(self, s: str) -> List[str]:
        got_count = False
        count_str = ""
        count = None

        got_counts = False
        counts = None
        current_count = 0

        strs = None

        for char in s:
            if not got_count:
                if char != ".":
                    count_str += char
                    continue
                else:
                    count = int(count_str)
                    got_count = True
                    counts = [""] * count
                    strs = [""] * count
                    continue

            if not got_counts:
                if char != ".":
                    counts[current_count] += char
                    continue
                else:
                    counts[current_count] = int(counts[current_count])
                    current_count += 1
                    if current_count == count:
                        got_counts = True
                        current_count = 0
                    continue
            
            while counts[current_count] == 0:
                current_count += 1

            strs[current_count] += char
            counts[current_count] -= 1

        return strs
            
                        


