class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common=""
        s=strs[0]
        for i in range(len(s)):
            for j in range(1,len(strs)):
                if i>=len(strs[j])or s[i]!=strs[j][i]:
                    return common
                
            common+=s[i]

        return common
    