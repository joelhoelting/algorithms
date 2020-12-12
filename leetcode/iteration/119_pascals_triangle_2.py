"""
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?



Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

"""

def getRow(self, rowIndex: int) -> List[int]:
    prev_row = [1]
    counter = 1
    while counter <= rowIndex:
        next_row = []
        for i in range(0, counter + 1):
            if i == 0 or i == counter:
                next_row.append(1)
            else:
                next_row.append(prev_row[i - 1] + prev_row[i])

        prev_row = next_row
        counter += 1

    return prev_row