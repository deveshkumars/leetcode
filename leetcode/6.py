# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:
#             return s

#         answer = []
#         n = len(s)
#         chars_in_section = 2 * (numRows - 1)

#         for curr_row in range(numRows):
#             index = curr_row
#             while index < n:
#                 answer.append(s[index])

#                 # If curr_row is not the first or last row,
#                 # then we have to add one more character of current section.
#                 if curr_row != 0 and curr_row != numRows - 1:
#                     chars_in_between = chars_in_section - 2 * curr_row
#                     second_index = index + chars_in_between

#                     if second_index < n:
#                         answer.append(s[second_index])
#                 # Jump to same row's first character of next section.
#                 index += chars_in_section

#         return "".join(answer)


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        s = list(s)
        # row1 = list(s[x] for x in range(len(s)) if x % 4 == 0)
        rows = [[] for x in range(numRows)]

        nextrow = 0
        chng = 1
        i = 0

        while i < len(s):
            # print(s[i])
            rows[nextrow].append(s[i])
            nextrow += chng
            if nextrow == (numRows-1):
                chng = -1
            elif nextrow == 0:
                chng = 1
            i += 1
        
        combined_rows = []
        for row in rows:
            combined_rows += row

        return "".join(combined_rows)


