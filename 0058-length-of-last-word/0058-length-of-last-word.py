class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        max_length=0
        s=s.strip()
        for ch in s:
            if ch==" ":
                max_length=0
                
            else:
                max_length+=1

        return max_length
        