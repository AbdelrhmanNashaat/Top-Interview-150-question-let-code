class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        last_word = l[-1]
        return len(last_word)
a = Solution()
print(a.lengthOfLastWord('luffy is still joyboy'))
