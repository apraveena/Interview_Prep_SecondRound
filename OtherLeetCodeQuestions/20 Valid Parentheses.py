class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars_dict = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        new_list = []
        for char in s:
            if char in chars_dict.keys():
                new_list.append(char)
            elif char in chars_dict.values():
                if len(new_list) == 0: return False
                top_item = new_list.pop(-1)
                if chars_dict[top_item] != char:
                    return False
        if len(new_list) > 0:
            return False

        return True