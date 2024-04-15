# arr = [1,2,3,4,5]
#
# d = 4
#
# # while y != 0:
# #     arr = arr[1:] + arr[:1]
# #     y -= 1
#
# arr = arr[d:] + arr[:d]
#
# print(arr)
#

n = 10
queries = [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1]
]

start = [0 for i in range(n)]
for q in queries:
    for i in range(q[0]-1, q[1]):
        start[i] += q[2]
    print(start)
print(max(start))

# numbers = [i+1 for i in range(n)]
# new_list = [0 for n in numbers if n =0]

# print(start)