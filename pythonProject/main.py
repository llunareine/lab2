# 1
# n = input('enter ur firstname')
# print('Hello,', n, '!')

# 2
# n = input('enter ur firstname')
# m = input('enter ur lastname')
# print('Hello,', n, m, '!')

# 3
# n = int(input('enter first number'))
# m = int(input('enter second number'))
# print('The total is', n+m)

# 4
# n = int(input('enter first number'))
# m = int(input('enter second number'))
# k = int(input('enter third number'))
# print('The total is', (n+m)*k)


# 5
# n = int(input('how many slices of pizza'))
# m = int(input('how many slices they have eaten'))
# print('work out how many slices they have left', (n-m))


# 6
# n = input('enter ur name')
# m = int(input('enter ur age'))
# print( n,',next birthday you will be:', m+1)


# 7
# n = int(input('total price of the bill'))
# m = int(input('how many diners there are'))
# print('how much each person must pay:', (n/m))

# 8
# n = int(input('number of days:'))
# print('how many hours are in that number of days:', n*24)
# print('how many minutes are in that number of days:', n*1440)
# print('how many seconds are in that number of days:', n*86400)


# 9
# n = int(input('enter a weight in kilograms:'))
# print('a weight in pounds.:', (n*2,204))

# 10
# n = int(input('enter a number over 100'))
# n<100
# m = int(input('enter a number under 10'))
# m>10
# print('how many times the smaller number goes into the larger number:', (n/m))


# import math
# sqrt1, sqrt2, sqrt3 = math.sqrt(64), math.sqrt(49), math.sqrt(36)
# print(sqrt1,sqrt2, sqrt3)

# import math
# n=9**4
# print(n)



# ============================================================================
# practice#2

# task 1
# n = 'Aiko'
# print(len(n))

# n = input('enter a word')
# print(len(n))

# task2
# n = 'restart'
# print(n.replace(n[5], '&'))
# ne ebu kak

# task 3
# n = '''The lyrics is not that poor!
# The lyrics is poor!'''
# print(n.replace('not that poor!', 'good!'))

# task 4
# list = ['damir', 'pidr', 'daun', 'exercises']
# m = max(list, key=len)
# print('Longest word:', m, 'Length of the longest word', len(m))

# task7
# n = 'damir'
# print(n[::2])

# print(input()[::2])


# def change_sring(str1):
#     return str1[-1:] + str1[1:-1] + str1[:1]
# print(change_sring('abcd'))

# 5
# l = "bekzhan"
# index = int(input("Enter index which you want remove: "))
# l = l[:index] + l[index  + 1::]
# print(l)


# =====================================================

# 1
# str =  'aikoBest87'
#     upper, lower, number, special = 0, 0, 0, 0
#     for i in range(len(str)):
#         if str[i].isupper():
#             upper += 1
#         elif str[i].islower():
#             lower += 1
#         elif str[i].isdigit():
#             number += 1
#         else:
#             special += 1
#     print('Upper case letters:', upper)
#     print('Lower case letters:', lower)
#     print('Number:', number)
#     print('Special characters:', special)




# 3
# # ////////////////////////
# list = ['r','d','i','p']
# (list.reverse())
# print(list)

# n = "rimad dna okia"[::-1]
# print(n)
# ///////////////////////

# def count(s, c):
#     # Count variable
#     res = 0
#
#     for i in range(len(s)):
#
#         # Checking character in string
#         if (s[i] == c):
#             res = res + 1
#     return res
#
#
# # Driver code
# str = "geeksforgeeks"
# c = 'e'
# print(count(str, c))

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# practice 3

# list1 = ['katya', 'riana', 'exgrlfriend', 'etc', 'aiko']
# list1.remove('aiko')
# print(list1)

# task2
# list = ['damir', 'pidr', 'daun', 'ruslan']
# m = max(list, key=len)
# print('longest word:', m, 'length of the longest word', len(m))

# task3
# l2 = [1,3,4]
# l2.clear()
# print(l2)

# task1
# list1 = ['d', 'a', 'm', 'i', 'r', 'p', 'i', 'd', 'r']
# sum = ''.join(list1)
# print(sum)

#5
# tupledamirpidr = (1,2,3,4)
# print(tupledamirpidr)

#6
# tuple1 = ("damir", "someone")
# (pidr, notpidr) = tuple1
# print(pidr)

#7
# t1 = (0,1,2,3,4,5,6,7,8,9)
# print(t1[4], t1[-4])

# 8
# set1 = {4, 5, 8}
# print(set1)

# 11
# set1 = {4, 2, 8}
# set2 = {5, 7, 9}
# set3 = set1.union(set2)
# print(set3)

#12
# setA = {2, 3, 4}
# setA.clear()
# print(setA)


#13
# dickt = {
# "damir": "pidr",
# "sun": "solnce",
# "chicken": "kfc"
# }
# dickt["pidr"] = "damir"
# print(dickt)

# 14
# dickt = {
# "damir": "pidr",
# "sun": "solnce",
# "chicken": "kfc"
# }
# dickt.update({"pidr":"damir"})
# print(dickt)



#15
# exboyfriend1 = {
#     'name': 'Danil',
#     'when': 'at 9 y.o'
# }
# exboyfriend2 = {
#     'name': 'Artem',
#     'when': 'at 12 y.o'
# }
# exboyfriend3 = {
#     'name': 'Arsen',
#     'when': 'at 14 y.o'
# }
# guys_who_had_good_taste = {
#     'exboyfriend1': exboyfriend1,
#     'exboyfriend2': exboyfriend2,
#     'exboyfriend3': exboyfriend3
# }
# print(guys_who_had_good_taste)


from Crypto.Util.number import inverse
from Crypto.Util.number import long_to_bytes

c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537
p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573

d = inverse(e, (p-1)*(q-1))
m = pow(c, d, n)
print(long_to_bytes(m))

