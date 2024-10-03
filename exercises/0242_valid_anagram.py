from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0 for i in range(26)]

        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        return all(c == 0 for c in counter)
