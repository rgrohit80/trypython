# def consecutive(num):
#     # Write your code here
#     le = num // 2
#     count = 0
#     for i in range(1, le + 1):
#         sum = i
#         for j in range(i + 1, le + 2, 1):
#             sum += j
#             if sum == num:
#                 count += 1
#                 break
#             elif sum > num:
#                 break
#     print(count)
#
#
# consecutive(10)

def longestSubsequence(s):
    # Write your code here
    count = 0
    st = ['a', 'e', 'i', 'o', 'u']
    min_ind = 0
    for j in range(len(st) - 1):
        for i in range(min_ind, len(s), 1):
            if s[i] == st[j]:
                count += 1
            elif s[i] == st[j + 1]:
                count += 1
                min_ind += 1
                break
    print(count)


longestSubsequence('aeiaaioooaauuaeiou')
