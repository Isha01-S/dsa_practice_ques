class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s=s.strip()
        # array = []
        # st=""
        # result=""
        # for ch in s:
        #     if ch == " ":
        #         if st=="":
        #             continue
        #         array.append(st)
        #         st = ""
        #     else:
        #         st+=ch
        # array.append(st)
        # for i in range(len(array)-1,-1,-1):
        #     result+=array[i]
        #     if i==0:
        #         break
        #     result+=" "
        # return result

        s = s.strip()          # remove leading/trailing spaces
        words = []
        current_word = ""

        # collect words
        for ch in s:
            if ch == " ":
                if current_word:
                    words.append(current_word)
                    current_word = ""
            else:
                current_word += ch

        # append last word if exists
        if current_word:
            words.append(current_word)

        # build reversed result
        result = ""
        for i in range(len(words) - 1, -1, -1):
            result += words[i]
            if i > 0:
                result += " "

        return result            
        