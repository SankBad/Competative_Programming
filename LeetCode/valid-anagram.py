class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_dict = {char:s.count(char) for char in set(s)}
        second_dict = {char:t.count(char) for char in set(t)}
        if first_dict==second_dict:
            return True
        else:
            return False
