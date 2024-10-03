from collections import Counter

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    def is_anagram_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter: list[int] = [0 for _ in range(26)]

        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        return all(c == 0 for c in counter)
