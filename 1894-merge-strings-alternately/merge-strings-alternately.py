class Solution(object):
    def mergeAlternately(self, word1, word2):
        word=""
        for i in range(max(len(word1),len(word2))):
            if i<len(word1):
                word+=word1[i]
            if i<len(word2):
                word+=word2[i]

        return word            