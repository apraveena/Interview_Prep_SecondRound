def get_words_from_phone_number(phone_number):
    if len(phone_number) == 0:
        return []
    phone_map = {}
    phone_map['2'] = "abc"
    phone_map['3'] = "def"
    phone_map['4'] = "ghi"
    phone_map['5'] = "jkl"
    phone_map['6'] = "mno"
    phone_map['7'] = "pqrs"
    phone_map['8'] = "tuv"
    phone_map['9'] = "wxyz"
    result = []
    phone_number = phone_number.replace("1", "").replace("0", "")
    total_length = len(phone_number)
    #rest of the array to handle
    def helper(slate, curr_idx):
        if len(slate) == total_length:
            result.append("".join(slate))
            return

        nums = phone_map[phone_number[curr_idx]]
        for num_str in nums:
            slate.append(num_str)
            helper(slate, curr_idx+1)
            slate.pop()

    helper([], 0)
    return result

print(get_words_from_phone_number("1234567"))


