class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        number = 0
        prevous_number = 0
        for char in s[::-1]:
            if roman_map[char] >= prevous_number:
                number += roman_map[char]
            else:
                number -= roman_map[char]
            prevous_number = roman_map[char]
        return number


a = Solution()
print(a.romanToInt('III'))
