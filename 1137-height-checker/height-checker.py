class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        
        n = len(expected)

        # Bubble Sort
        for i in range(n):
            for j in range(0, n - i - 1):
                if expected[j] > expected[j + 1]:
                    expected[j], expected[j + 1] = expected[j + 1], expected[j]

        # Count differences
        count = 0

        for i in range(n):
            if heights[i] != expected[i]:
                count += 1

        return count