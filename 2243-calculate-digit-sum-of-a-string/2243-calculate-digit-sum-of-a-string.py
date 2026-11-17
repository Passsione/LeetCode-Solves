class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            temp = []
            step = ceil(len(s) / k)
            for i in range(step):
                digits = s[:k] if len(s) >= k else s
                total = 0
                for d in digits:
                    total += int(d)
                temp.append(str(total))
                if len(s) >= k:
                    s = s[k:]
                else: 
                    s = []
            s = "".join(temp)

        return s



                