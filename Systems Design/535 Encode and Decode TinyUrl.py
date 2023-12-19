class Codec:
    __urls = {}


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        import random, string
        # all_chars = [chr(ord("a") + i) for i in range(26)]
        while True:
            # short_url = "".join(random.choices(all_chars, k=6))
            code = "".join(random.choices(string.ascii_letters + string.digits, k = 6))
            short_url = "http://tinyurl.com/" + code
            if short_url not in self.__urls:
                break

        self.__urls[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl not in self.__urls:
            return "Url not found"
        return self.__urls[shortUrl]

#Solution from leetcode -- can learn from it.
class Codec1:
    from collections import defaultdict
    import string

    codeDB, urlDB = defaultdict(), defaultdict()
    chars = string.ascii_letters + string.digits

    def getCode(self) -> str:
        import random
        code = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code

    def encode(self, longUrl: str) -> str:
        if longUrl in self.urlDB: return self.urlDB[longUrl]
        code = self.getCode()
        while code in self.codeDB: code = self.getCode()
        self.codeDB[code] = longUrl
        self.urlDB[longUrl] = code
        return code

    def decode(self, shortUrl: str) -> str:
        return self.codeDB[shortUrl]


# Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.decode(codec.encode(url)))

'''
If we were to use naive approach and use a counter to generate short url.
Atleast we can sue base64 to generate short short url when the counter gets too large
below is the code from ik foundation material

Almost pseudo code, not sure if it works
'''
counter = 0
hash_map = {}
import string

def encode(long_url):
    global counter
    counter += 1
    digits = string.digits + string.ascii_letters + "-" + "_"
    digit_list = []
    curr_val = counter
    while curr_val >= 64:
        quotient = curr_val//64
        remainder = curr_val % 64
        digit_list.append(digits[remainder])
        curr_val = quotient
    if curr_val > 0:
        digit_list.append(digits[curr_val])
    digit_list.reverse()
    short_url = "".join(digit_list)
    hash_map[short_url] = long_url
    return "http://bit.ly" + short_url

def decode(short_url):
    #clip out http://bit.ly portion and get the url from hashmap
    return hash_map[short_url[13:]]