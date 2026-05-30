class Solution:

    def check(self, T, d, r):
        if T == 0 and d[0] == 0 and d[1] == 0:
            return True


        break1 = math.floor(T/r[0])
        break2 = math.floor(T/r[1])
        break12 = math.floor(T/math.lcm(r[0], r[1]))

        A = break1 - break12
        B = break2 - break12
        C = T - break1 - break2 + break12

        need1 = max(0, d[0]-B)
        need2 = max(0, d[1]-A)

        if need1 + need2 <= C:
            return True
        else:
            return False

    def minimumTime(self, d: List[int], r: List[int]) -> int:
        start = 0
        end = d[0] * r[0] + d[1] * r[1] + r[0] * r[1]
        while start < end:
            print(start, end)
            mid = (start + end) // 2
            if self.check(mid, d, r):
                end = mid
            else:
                
                start = mid + 1
        return end


            

