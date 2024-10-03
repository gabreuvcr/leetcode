class Solution:
    def is_palindrome(self, s: str) -> bool:
        s: list[str] = [letter for letter in s.lower() if letter.isalnum()]
        return s == s[::-1]

    def is_palindrome2(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        s = s.lower()
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if (s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True
