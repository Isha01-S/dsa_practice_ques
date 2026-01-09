class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string=""
        for val in s: 
            if val.isalnum():
                string+=val
            

        string=string.lower()
        rev_s=string[::-1]

        if rev_s==string:
            return True
        return False


        