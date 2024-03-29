#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0 and x != 0:
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10

        # when the length is an odd number, we can get rid of the middle digit by
        return x == rev or x == rev // 10
# @lc code=end

