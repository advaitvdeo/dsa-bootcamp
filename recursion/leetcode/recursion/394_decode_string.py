class Solution:
    def decodeString(self, s):
        # iterative solution using stack
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # get the base string
                base_str = ""
                while stack and stack[-1] != '[':
                    base_str = stack.pop() + base_str
                # pop [
                stack.pop()

                # get digit
                k = 0
                while stack and stack[-1].isdigit():
                    k = k * 10 + int(stack.pop())

                temp_ans = base_str * k
                for c in temp_ans:
                    stack.append(c)
        return ''.join(stack)

    index = 0
    def decodeString_recursive(self, s):
        k = 0
        res = ""
        while self.index < len(s):
            # take care of digit
            if s[self.index].isdigit():
                k = k * 10 + int(s[self.index])
            # next recustive call to get temp_ans
            elif s[self.index] == '[':
                self.index += 1
                temp_ans = self.decodeString_recursive(s)
                # multiple temp ans with k
                res += temp_ans * k
                k = 0
            # return if we find ]
            elif s[self.index] == ']':
                return res
            # else keep adding characters
            else:
                res += s[self.index]
            self.index += 1
        return res

a = Solution()
s = "2[abc]3[cd]ef"
print(a.decodeString(s))
print(a.decodeString_recursive(s))