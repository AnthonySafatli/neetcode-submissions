class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        freqs = [[] for _ in range(n + 1)]
        for num, count in counts.items():
            freqs[count].append(num)

        answer = []
        for i in range(n):
            idx = (i * -1) - 1
            array = freqs[idx]
            for num in array:
                answer.append(num)
            
            if len(answer) >= k:
                return answer