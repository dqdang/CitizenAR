# def knapsack(array, key):
#     diff = key
#     counter = 0
#     rv = []

#     while(counter < len(array)):
#         temp = key
#         diff -= array[counter]
#         if(diff > 0):
#             continue
#         elif(diff == 0):
#             rv.append(array[counter])
#             break
#         else:
#             rv.append(array[counter])
#             counter += 1
#             diff = temp
#     return rv


# key = 50
# array = [2, 8]
# print(knapsack(array, key))

import collections
def topKFrequent(words, k):
    c = collections.Counter(words).items()
    rv = []
    for i in c:
        rv.append(i[0])
    return rv
    # c = collections.Counter(words).keys()



inpt = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(topKFrequent(inpt, k))
