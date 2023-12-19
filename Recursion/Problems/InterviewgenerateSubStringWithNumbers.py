'''
     * Given a word, generate all potential abbreviations that can result from
     * replacing non-adjacent substrings with their lengths.
     *
     * <p>e.g. "ab" becomes ["ab", "2", "a1", "1b"]
     *
     * @param a string containing only lowercase letters
     * return all abbreviations
     *
'''
#My solution in interview with interviewer help
def generate_sub_str_my_solution(s):
    result = []

    def helper(slate, i, last_num):
        if i == len(s):
            result.append("".join([str(x) for x in slate]))
            return

        initial_len = len(slate)
        # add the character as itself
        slate.append(s[i])
        helper(slate, i + 1, 0)
        slate.pop()

        # Adding number instead of the character
        if i > 0 and str(slate[-1]).isdigit():
            slate.pop()
        slate.append(last_num + 1)
        helper(slate, i + 1, last_num + 1)
        if len(slate) > initial_len:
            slate.pop()

    helper([], 0, 0)
    return result

#Suneetha and my code
def generate_sub_str(s):
    result = []
    def helper(slate, i):
        if i == len(s):
            result.append("".join([str(x) for x in slate]))
            return
        #add character
        slate.append(s[i])
        helper(slate, i+1)
        slate.pop()
        #add number
        should_pop = True
        if len(slate) > 0 and str(slate[-1]).isdigit():
            slate[-1] += 1
            should_pop = False
        else:
            slate.append(1)
        helper(slate, i+1)
        if should_pop:
            slate.pop()
        else:
            slate[-1] -= 1

    helper([], 0)
    return result

#interviewer alternate idea
def generate_sub_str_with_bool(s):
    result = []
    def format_result(arr):
        n = len(arr[0])
        result = []
        for item in arr:
            temp = []
            for i in range(n):
                if item[i]:
                    if len(temp)>0 and str(temp[-1]).isdigit():
                        temp[-1] += 1
                    else:
                        temp.append(1)
                else:
                    temp.append(s[i])

            result.append("".join([str(x) for x in temp]))
        return result

    def helper(slate, i):
        if len(s) == i:
            result.append(slate[:])
            return

        slate.append(True)
        helper(slate, i + 1)
        slate.pop()

        slate.append(False)
        helper(slate, i + 1)
        slate.pop()

    helper([], 0)
    print(format_result(result))


print(generate_sub_str_with_bool("abc"))


''' Interviewer Ke Li's code
    /**
     * Given a word, generate all potential abbreviations that can result from
     * replacing non-adjacent substrings with their lengths.
     *
     * <p>e.g. "ab" becomes ["ab", "2", "a1", "1b"]
     *
     * @param a string containing only lowercase letters
     * return all abbreviations
     */
    public static List<String> generateAbbreviations(String word) {
        StringBuilder slate = new StringBuilder();
        List<String> result = new ArrayList<>();
        helper(word, 0, slate, result);
        return result;
    }
    
    private static void helper(String word, int start, StringBuilder slate, List<String> result) {
        if (start >= word.length()) {
            result.add(slate.toString());
            return;
        }
        
        for (int end = start; end <= word.length(); ++end) {
            int prevLen = slate.length();
            int len = end - start;

            if (len > 0) {
                slate.append(len);
            }
            
            if (end < word.length()) {
                slate.append(word.charAt(end));
            }
            
            helper(word, end + 1, slate, result);
            slate.setLength(prevLen);
        }
    }

'''
