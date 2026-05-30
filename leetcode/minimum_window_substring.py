class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substrings = []
        s = list(s)
        mhp = {}
        n = len(list(t))
        mhp_size = n
        for x in list(t):
            if x in mhp:
                mhp[x] += 1
            else:
                mhp[x] = 1
        mhp_og = mhp.copy()
        shortest = (-1, -1)
        mhp_size = n
        for left in range(len(s)):
            if left == 0:
                right = 1
                if s[left] in mhp:
                    mhp[s[left]] -= 1
                    mhp_size -= 1
            else:
                if s[left-1] in mhp:
                    mhp[s[left-1]] += 1
                    if mhp[s[left-1]] > 0:
                        mhp_size += 1
                else:
                    pass

            while mhp_size > 0 and right < len(s):
                if s[right] in mhp and mhp[s[right]] > 0:
                    mhp_size -= 1
                    mhp[s[right]] -= 1
                elif s[right] in mhp and mhp[s[right]] <= 0:
                    mhp[s[right]] -= 1
                right += 1
                
            if mhp_size > 0:
                break
            if shortest[0] == -1:
                shortest = (left, right)
            elif shortest[1] - shortest[0] > right - left:
                shortest = (left, right)

        return "".join(s[shortest[0]:shortest[1]])


        #     if s[left] not in mhp_og:
        #         continue
        #     mhp = mhp_og.copy()
        #     right = left
        #     while mhp_size > 0 and right < len(s):
        #         if s[right] in mhp and mhp[s[right]] > 0:
        #             mhp[s[right]] -= 1
        #             mhp_size -= 1
        #         right += 1
        #     if left == 9:
        #         print(right, mhp, mhp_size)
        #     if right == len(s) and mhp_size > 0:
        #         pass
        #     else:
        #         substrings.append((left, right))

        # if len(substrings) == 0:
        #     return ""
        # shortest = substrings[0]
        # print(substrings)
        # for x in substrings:
        #     if x[1] - x[0] < shortest[1] - shortest[0]:
        #         shortest = x

        # substrings = ["".join(x) for x in substrings]
        # final_answer = substrings[0] if len(substrings) > 0 else -1
        # if final_answer == -1:
        #     return ""
        # shortest = substrings[0][0] - substrings[0][1]
        # for x in substrings:
        #     if x[1] - x[0] < shortest:

        # print(substrings)
        # return final_answer

