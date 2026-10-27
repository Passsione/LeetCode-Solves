class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        output = []

        for row in range(m):
            r = ''
            for col in range(n):
                if col == 0 or row == m - 1:
                    r += '.'
                else:
                    r += '#'
            output.append(r)

        return output
                    