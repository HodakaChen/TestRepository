class Solution:
    def intToRoman(self, num: int) -> str:
        # 定义每一个数量级可以使用的罗马字母
        d = {
            0: ['I', 'V', 'X'],
            1: ['X', 'L', 'C'],
            2: ['C', 'D', 'M'],
            3: ['M']
        }
        lst = list(str(num))
        num_list = [int(ch) for ch in lst]
        k = len(num_list)-1
        ret = ''
        for n in num_list:
            op = d[k]
            if k == 3:
                ret = ret + 'M'*n
            else:
                if 5 <= n < 9:
                    ret = ret + d[k][1] + d[k][0]*(n-5)
                elif n == 9:
                    ret = ret + d[k][0] + d[k][2]
                elif 1 <= n < 4:
                    ret = ret + d[k][0]*n
                elif n == 4:
                    ret = ret + d[k][0] + d[k][1]
            k -= 1

        return ret

x = Solution()
print(x.intToRoman(1994))