import collections


def reverseString(s):
    right = len(s) - 1
    left = 0

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverseInt(x):
    nums = [i for i in str(abs(x))]

    reversed_nums = nums[::-1]

    joined_nums = int("".join(reversed_nums))
    if joined_nums > (2 ** 31 - 1):
        return 0
    elif x < 0:
        return joined_nums * -1
    else:
        return joined_nums


def firstUniqChar(s):
    char_hash = {}
    for index, letter in enumerate(s):
        if letter not in char_hash:
            char_hash[letter] = [index, 1]
        else:
            char_hash[letter][1] += 1
    for letter in char_hash:
        if char_hash[letter][1] == 1:
            return char_hash[letter][0]
    return -1


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    letter_count1 = collections.Counter(s)
    letter_count2 = collections.Counter(t)

    for letter in letter_count2:
        if letter not in s:
            return False
        elif letter_count1[letter] != letter_count2[letter]:
            return False
    return True


def isPalindrome(s):
    letters_list = [letter.lower() for letter in s if letter.isalnum()]
    return letters_list == letters_list[::-1]

def myAtoi(s):
    s = s.lstrip()
    if not s:
        return 0

    i = 0
    sign = 1

    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        i += 1
        sign = -1

    parsed = 0
    while i < len(s):
        current = s[i]
        if not current.isdigit():
            break
        else:
            parsed = parsed * 10 + int(current)
        i += 1

    parsed *= sign

    if parsed > 2**31 - 1:
        return 2**31-1
    elif parsed <= -2**31:
        return -2**31
    else:
        return parsed



def strStr(haystack, needle):
    i = 0
    while i < len(haystack):
        if needle[0] == haystack[i]:
            if haystack[i:i + len(needle)] == needle:
                return i
        i += 1
    return -1

def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]

    prefix = ""
    i = 0

    while i < len(min(strs)):
        for j in range(1, len(strs)):
            word1 = strs[j]
            word2 = strs[j - 1]
            if not word1 or not word2:
                return prefix
            if word1[i] != word2[i]:
                return prefix
        prefix += strs[j][i]
        i += 1
    return prefix





if __name__ == "__main__":
    strs = ["dog", "racecar", "car"]
    strs2 = ["flower", "flow", "flight"]
    strs3 = [""]
    strs7 = ["a"]
    strs4 = ["",""]
    strs5 = ["","b"]
    strs6 = ["ab", "a"]

    print(longestCommonPrefix(strs7))






