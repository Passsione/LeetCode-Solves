class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        output = []

        for row in range(m):
            r = ''
            for col in range(n):
                if (row == 0 and col == 0) or (row == m - 1 and col == n - 1):
                    r += '.'
                    continue
                if col == 0 or row == m - 1:
                    r += '.'
                else:
                    r += '#'
            output.append(r)

        return output
                    