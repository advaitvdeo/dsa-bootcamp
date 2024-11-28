# trying itrative approach using stack
import re
# def decodeString(s):
#     stack = []
#     i = 0
#     while i < len(s):
#         while s[i] != ']':
#             stack.append(s[i])
#             i += 1
#
#         string = ""
#         while stack and stack[-1] != '[':
#             string += stack.pop()
#
#         string = string[::-1]
#         if stack:
#             stack.pop()
#         val = 0
#         place = 0
#         while stack and stack[-1].isdigit():
#             val += int(stack.pop())*10**place
#             place += 1
#
#         stack.append(string * val)
#         i += 1
#     return stack

# 1 stack approach
def decodeString(s):
    stack = []
    for i in range(len(s)):
        if s[i] == ']':
            # create string until [
            string = ""
            while stack and stack[-1] != '[':
                string += stack.pop()

            # pop [
            stack.pop()

            # create number
            val = 0
            place = 0
            while stack and stack[-1].isdigit():
                val += int(stack.pop()) * 10**place
                place += 1

            while val:
                for j in range(len(string)-1, -1, -1):
                    stack.append(string[j])
                val -= 1
        else:
            stack.append(s[i])

    result = ["" for i in range(len(stack))]
    for i in range(len(stack)-1, -1, -1):
        result[i] = stack[i]
    return ''.join(result)


# 2 stack approach
# this is very confusing because when we find '[', we have to append the results that were previously generated
# similarly when we find ']' we have to pop from stack and append current string to decode string
# then make current_string same as decode string
# lets not use this appraoch
def decideString_2stack(s):
    countStack = []
    stringStack = []
    currentString = ""
    val = 0
    for i in range(len(s)):
        if s[i].isdigit():
            val = val*10 + int(s[i])
        elif s[i] == '[':
            countStack.append(val)
            stringStack.append(currentString)
            currentString = ""
            val = 0
        elif s[i] == ']':
            decode_string = stringStack.pop()
            current_count = countStack.pop()
            for j in range(current_count-1, -1, -1):
                decode_string.append(currentString)
            currentString = decode_string
        else:
            currentString.append(s[i])
    return currentString


index = 0
# recursion approach
def decodeString_recursive(s):
    global index
    result = ""
    while index < len(s) and s[index] != ']':
        if not s[index].isdigit():
            result += s[index]
            index += 1
        else:
            val = 0
            while index < len(s) and s[index].isdigit():
                val = val * 10 + int(s[index])
                index += 1

            # ignore [
            index += 1

            # make recursive call
            decode_string = decodeString_recursive(s)

            # ignore ]
            index += 1

            while val:
                result += decode_string
                val -= 1

    return result


s = "3[a]2[bc]"
#s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
print(decodeString(s))

print(decodeString_recursive(s))
