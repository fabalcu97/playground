# def odd_sorted(arr):
#     d = {i: n for i, n in enumerate(arr) if n % 2}
#     sorted_values = sorted(d.values())
#     for i, v in enumerate(d.keys()):
#         arr[v] = sorted_values[i]
#     return arr


# print(sorted_arrays([5, 3, 2, 8, 1, 4]))
# print("-----")
# print(sorted_arrays([5, 3, 1, 8, 0]))

#######################

# def solution(s):
#     l = len(s)
#     if l % 2:
#         s += "_"
#     return [s[i: i + 2] for i in range(l, 0, 2)]


# print(solution("sadadad"))

#######################

# def zero(op=None): return 0 if op is None else op(0)
# def one(op=None): return 1 if op is None else op(1)
# def two(op=None): return 2 if op is None else op(2)
# def three(op=None): return 3 if op is None else op(3)
# def four(op=None): return 4 if op is None else op(4)
# def five(op=None): return 5 if op is None else op(5)
# def six(op=None): return 6 if op is None else op(6)
# def seven(op=None): return 7 if op is None else op(7)
# def eight(op=None): return 8 if op is None else op(8)
# def nine(op=None): return 9 if op is None else op(9)


# def plus(right_op): return lambda left_op: left_op + right_op
# def minus(right_op): return lambda left_op: left_op - right_op
# def times(right_op): return lambda left_op: left_op * right_op


# def divided_by(right_op): return lambda left_op: int(
#     left_op / right_op) if right_op != 0 else 0


# print(nine(divided_by(zero())))

#######################

# import functools


# def dig_pow(n, p):
#     number = 0
#     for power, num in enumerate(str(n), p):
#         number += pow(int(num), power)
#     div = number / n
#     return int(div) if div.is_integer() else -1


# print(dig_pow(89, 1))
# print(dig_pow(92, 1))
# print(dig_pow(695, 2))
# print(dig_pow(46288, 3))


#######################

# def tribonacci(signature, n):
#     if n < 3:
#         return signature[0:n]
#     while len(signature) < n:
#         signature.append(sum(signature[-3:])))
#     return signature


# print(tribonacci([1, 1, 1], 10))
# print(tribonacci([0, 0, 1], 10))
# print(tribonacci([0, 1, 1], 10))
# print(tribonacci([1, 0, 0], 10))
# print(tribonacci([0, 0, 0], 10))
# print(tribonacci([1, 2, 3], 10))
# print(tribonacci([3, 2, 1], 10))
# print(tribonacci([1, 1, 1], 1))
# print(tribonacci([300, 200, 100], 0))
# print(tribonacci([0.5, 0.5, 0.5], 30))

#######################

# def find_even_index(arr):
#     for i, _ in enumerate(arr):
#         if sum(arr[0:i]) == sum(arr[i+1:]):
#             return i
#     return -1


# print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
# print(find_even_index([1, 100, 50, -51, 1, 1]),)
# print(find_even_index([1, 2, 3, 4, 5, 6]),)
# print(find_even_index([20, 10, 30, 10, 10, 15, 35]))
# print(find_even_index([20, 10, -80, 10, 10, 15, 35]))
# print(find_even_index([10, -80, 10, 10, 15, 35, 20]))
# print(find_even_index(list(range(1, 100))),)
# print(find_even_index([0, 0, 0, 0, 0]), 0)
# print(find_even_index([-1, -2, -3, -4, -3, -2, -1]))
# print(find_even_index(list(range(-100, -1))),)


###########

# def make_readable(seconds):
#     h = seconds % 99
#     m = seconds % 60
#     s = seconds % 60
#     return f'{h}:{m}:{s}'


# print(make_readable(0))
# print(make_readable(5))
# print(make_readable(60))
# print(make_readable(86399))
# print(make_readable(359999))


##############

# def removNb(n):
#     _sum = n * (n + 1) / 2
#     arr = []
#     for a in range(1, n):
#         tsum = _sum - a
#         b = tsum / (a + 1.0)
#         if b < n and b.is_integer():
#             arr.append((a, b))
#     return arr


# print(removNb(39))
# print(removNb(26))

##############
# https://www.codewars.com/kata/5672682212c8ecf83e000050/discuss

# def dbl_linear(n):
#     arr = [1]
#     for i in range(n):
#         arr.append(2 * arr[i] + 1)
#         arr.append(3 * arr[i] + 1)
#         print(i)
#     arr = list(set(arr))
#     arr.sort()
#     return arr[n]


# print(dbl_linear(10), 22)
# print(dbl_linear(20), 57)
# print(dbl_linear(30), 91)
# print(dbl_linear(50), 175)

##############

# https://www.codewars.com/kata/515bb423de843ea99400000a/train/python

# from math import ceil

# class PaginationHelper:

#     # The constructor takes in an array of items and a integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.collection_length = len(collection)
#         self.items_per_page = items_per_page
#         self._page_count = int(
#             ceil(self.collection_length / self.items_per_page))

#     # returns the number of items within the entire collection
#     def item_count(self):
#         return self.collection_length

#     # returns the number of pages
#     def page_count(self):
#         return self._page_count

#     # returns the number of items on the current page. page_index is zero based
#     # this method should return -1 for page_index values that are out of range
#     def page_item_count(self, page_index):
#         page_index -= 1
#         if page_index >= self._page_count:
#             return -1
#         start = page_index * self.items_per_page
#         end = start + self.items_per_page
#         end = end if end < self.collection_length else -1
#         col = len(self.collection[start:end])
#         print(col)
#         print(self.collection_length, self.items_per_page, page_index, col)
#         return -1 if not col else col

#     # determines what page an item is on. Zero based indexes.
#     # this method should return -1 for item_index values that are out of range
#     def page_index(self, item_index):
#         if item_index < 0 or item_index >= self.collection_length or not self.collection_length:
#             return -1
#         return int(item_index / self.items_per_page)


# collection = range(1, 25)
# helper = PaginationHelper(collection, 10)

# print(helper.page_count(), 3)
# print(helper.item_count(), 24)
# print(helper.page_index(-24), 2)
# print(helper.page_item_count(0))
# print(helper.page_item_count(1))
# print(helper.page_item_count(2))
# print(helper.page_item_count(3))

##############

# def domain_name(url):
#     domain = url.split('://')[-1].split('/')[0].split('.')
#     return domain[0] if domain[0] != 'www' else domain[1]


# print(domain_name("http://google.com"))
# print(domain_name("http://google.co.jp"))
# print(domain_name("www.xakep.ru"))
# print(domain_name("https://youtube.com"))
# print(domain_name("https://hyphen-site.org"))
# print(domain_name("http://www.codewars.com/kata/"))
# print(domain_name("http://www.codewars.com.kataasd/asd/"))
# print(domain_name("rzui1be46c02.fr/"))
# print(domain_name("icann.org"))
# print(domain_name("6qbd1eaeme2pxzy15ytoype.edu/"))

##############

# def valid_parentheses(string):
#     stack = []
#     if not string:
#         return False
#     for i in string:
#         if i == "(":
#             stack.append(i)
#         elif i == ")":
#             if len(stack):
#                 stack.pop()
#             else:
#                 return False
#     return False if len(stack) else True


# print(valid_parentheses("))))(((("))
# print(valid_parentheses("  ("))
# print(valid_parentheses(")test"))
# print(valid_parentheses(""))
# print(valid_parentheses("hi(hi)()"))
# print(valid_parentheses("hi())("))

# def valid_solution(board):
#     for row in range(9):
#         if board[row].count(0):
#             return False
#         v = board[row]
#         h = [board[col][row] for col in range(9)]
#         if sum(set(v)) != sum(set(h)) != 45 or v == h:
#             return False
#     return True


# print(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
#                       [2, 3, 4, 5, 6, 7, 8, 9, 1],
#                       [3, 4, 5, 6, 7, 8, 9, 1, 2],
#                       [4, 5, 6, 7, 8, 9, 1, 2, 3],
#                       [5, 6, 7, 8, 9, 1, 2, 3, 4],
#                       [6, 7, 8, 9, 1, 2, 3, 4, 5],
#                       [7, 8, 9, 1, 2, 3, 4, 5, 6],
#                       [8, 9, 1, 2, 3, 4, 5, 6, 7],
#                       [9, 1, 2, 3, 4, 5, 6, 7, 8]]))

# print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                       [6, 7, 2, 1, 9, 5, 3, 4, 8],
#                       [1, 9, 8, 3, 4, 2, 5, 6, 7],
#                       [8, 5, 9, 7, 6, 1, 4, 2, 3],
#                       [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                       [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                       [9, 6, 1, 5, 3, 7, 2, 8, 4],
#                       [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                       [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

# print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
#                       [6, 7, 2, 1, 9, 0, 3, 4, 9],
#                       [1, 0, 0, 3, 4, 2, 5, 6, 0],
#                       [8, 5, 9, 7, 6, 1, 0, 2, 0],
#                       [4, 2, 6, 8, 5, 3, 7, 9, 1],
#                       [7, 1, 3, 9, 2, 4, 8, 5, 6],
#                       [9, 0, 1, 5, 3, 7, 2, 1, 4],
#                       [2, 8, 7, 4, 1, 9, 6, 3, 5],
#                       [3, 0, 0, 4, 8, 1, 1, 7, 9]]))


##############

# def det(mt):
#     return mt[0][0] * mt[1][1] - mt[0][1] * mt[1][0]


# def determinant(matrix):
#     n = len(matrix)
#     if n == 1:
#         return matrix[0][0]
#     if n == 2:
#         return det(matrix)
#     det_sum = 0
#     k = -1
#     for i in range(0, n):
#         sub_matrix = []
#         k *= -1
#         for j in range(1, n):
#             sub_matrix.append(matrix[j][0:i] + matrix[j][i+1:])
#         det_sum += matrix[0][i] * determinant(sub_matrix) * k
#     return det_sum

# m1 = [[1, 3], [2, 5]]
# m2 = [[2, 5, 3],
#       [1, -2, -1],
#       [1, 3, 4]]
# m3 = [[2, 5, 3, 4],
#       [1, 2, 1, 2],
#       [1, 3, 4, 1],
#       [1, 3, 4, 1]]
# m4 = [[1, 3, 5, 9],
#       [1, 3, 1, 7],
#       [4, 3, 9, 7],
#       [5, 2, 0, 9]]

# print(determinant([[1]]), 1)
# print(determinant(m1), -1)
# print(determinant(m2), "== -20")
# print(determinant(m3), "== 0")
# print(determinant(m4), "== -376")

##############
# import re

# def recoverSecret(triplets):
#     # word = "".join(triplets[0])
#     for triplet in triplets:
#         for i in [0, 1]:
#             for trip in triplets:
#                 if trip == triplet:
#                     continue
#                 inner_part = re.match(
#                     f'{triplet[i]}(\w*){triplet[i + 1]}', "".join(trip))
#                 print(inner_part.groups()[0] if inner_part else '')


# """
# tup
# tsup
# atsup
# hatsup
# hatisup
# whatisup
# """


# secret = "whatisup"
# triplets = [
#     ['t', 'u', 'p'],
#     ['w', 'h', 'i'],
#     ['t', 's', 'u'],
#     ['a', 't', 's'],
#     ['h', 'a', 'p'],
#     ['t', 'i', 's'],
#     ['w', 'h', 's']
# ]

# print(recoverSecret(triplets), secret)

##############

# def last_digit(n1, n2):
#     return pow(n1, n2, 10)

# def last_digit(n1, n2):
#     if not n2:
#         return 1
#     numbers = [str(n1 ** i)[-1] for i in range(1, 9)]
#     return int(numbers[n2 % len(set(numbers)) - 1])


# print(last_digit(132, 0), 1)
# print(last_digit(4, 1), 4)
# print(last_digit(4, 2), 6)
# print(last_digit(9, 7), 9)
# print(last_digit(10, 10 ** 10), 0)
# print(last_digit(2 ** 200, 2 ** 300), 6)
# print(last_digit(3715290469715693021198967285016729344580685479654510946723,
#                  68819615221552997273737174557165657483427362207517952651), 7)

##############

def longest_slide_down(pyramid):
    # values.index(max(values))
    m = max(pyramid[0])
    _sum = m
    print(m)
    x = 0
    for i in range(len(pyramid) - 1):
        sub = pyramid[i+1][x: x+2]
        m = max(sub)
        x += sub.index(m)
        print(m)
        _sum += m
        # print(_sum)
        # print(x)
        # print(0 if x-1 < 0 else x - 1, None if x +
        #       1 > len(pyramid[i+1]) else x+1)
        # print(pyramid[i+1][
        #     0 if x-1 < 0 else x - 1: None if x+1 > len(pyramid[i+1])-1 else x+2])
        # print("====")
    print(_sum)
    # return sum([max(row) for row in pyramid])


# print(longest_slide_down([
#     [3],
#     [7, 4],
#     [2, 4, 6],
#     [8, 5, 9, 3]]), 23)
print(longest_slide_down([
                            [75],
                          [95, 64],
                        [17, 47, 82],
                      [18, 35, 87, 10],
                    [20,  4, 82, 47, 65],
                  [19,  1, 23, 75,  3, 34],
                [88,  2, 77, 73,  7, 63, 67],
              [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
          [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
      [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
  [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]), 1074)
