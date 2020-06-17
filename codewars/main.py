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

def dbl_linear(n):
    arr = [1]
    for i in range(n):
        arr.append(2 * arr[i] + 1)
        arr.append(3 * arr[i] + 1)
        print(i)
    arr = list(set(arr))
    arr.sort()
    return arr[n]


print(dbl_linear(10), 22)
print(dbl_linear(20), 57)
print(dbl_linear(30), 91)
print(dbl_linear(50), 175)
