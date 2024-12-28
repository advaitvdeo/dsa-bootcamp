class Solution:
    def wordPatternMatch(self, pattern, s):

        ht = {}
        hs = set()

        def solve(p_index, s_index):
            if p_index >= len(pattern):
                return s_index >= len(s)

            p_ch = pattern[p_index]
            if p_ch in ht:
                s_word = ht[p_ch]
                if s[s_index: s_index+len(s_word)] == s_word:
                    return solve(p_index+1, s_index + len(s_word))
                return False
            else:
                for i in range(s_index, len(s)):
                    new_word = s[s_index:i+1]
                    if new_word in hs:
                        continue
                    hs.add(new_word)
                    ht[p_ch] = new_word
                    if solve(p_index+1, s_index + len(new_word)):
                        return True
                    del ht[p_ch]
                    hs.remove(new_word)
            return False
        return solve(0, 0)



a = Solution()
pattern = "abab"
s = "redblueredblue"
print(a.wordPatternMatch(pattern, s))
