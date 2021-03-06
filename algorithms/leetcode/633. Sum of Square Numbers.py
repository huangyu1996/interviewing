'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
'''
import math


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        for i in range(0, int(math.sqrt(c)) + 1):
            if math.sqrt(c - i * i) - int(math.sqrt(c - i * i)) < 0.00001:
                return True
        return False

    '''
    双指针法
    
    '''

    def judgeSquareSum2(self, c):
        if c < 0:
            return False
        left = 0
        right = int(math.sqrt(c))
        while (left <= right):
            cur = left * left + right * right
            if cur < c:
                left += 1
            elif cur > c:
                right -= 1
            else:
                return True
        return False
