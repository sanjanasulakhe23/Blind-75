class Solution(object):
    def reverseWords(self, s):
        word=s.strip().split()
        word.reverse()
        return " ".join(word)
        