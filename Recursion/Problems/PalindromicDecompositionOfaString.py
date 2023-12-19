def generate_palindromic_decomposition(s):
    result = []
    def is_palindrome(str1):
        l, r = 0, (len(str1) - 1)
        while l < r:
            if str1[l] != str1[r]:
                return False
            l += 1
            r -= 1
        return True

    def helper(slate, i, last_str):
        #base case
        if i == len(s):
            if is_palindrome(last_str):
                result.append("".join(slate))
            return

        #adding the character case
        slate.append(s[i])
        helper(slate, i + 1, last_str + s[i])
        slate.pop()

        if is_palindrome(last_str):
            slate.append("|")
            slate.append(s[i])
            helper(slate, i + 1, s[i])
            slate.pop()
            slate.pop()
        else:
            return

    helper([s[0]],1, s[0] )
    return result

print(generate_palindromic_decomposition("abcb"))
print(generate_palindromic_decomposition("ab"))
print(generate_palindromic_decomposition("aba"))
generate_palindromic_decomposition("abaa")
generate_palindromic_decomposition("abaaaaac")
