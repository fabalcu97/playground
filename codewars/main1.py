# def sort_array(array):
#     odd = {}
#     even = {}
#     for idx, number in enumerate(array):
#         if number % 2:
#             odd[idx] = number
#         else:
#             even[idx] = number
#     odd_sorted = list(odd.values())
#     odd_sorted.sort()
#     even_sorted = list(even.values())
#     even_sorted.sort(reverse=True)
#     new_arr = [None] * len(array)
#     for number, index in zip(odd_sorted, odd.keys()):
#         new_arr[index] = number
#     for number, index in zip(even_sorted, even.keys()):
#         new_arr[index] = number
#     return new_arr


# print(sort_array([5, 3, 2, 8, 1, 4, 11]), [1, 3, 8, 4, 5, 2, 11])
# print(sort_array([2, 22, 37, 11, 4, 1, 5, 0]), [22, 4, 1, 5, 2, 11, 37, 0])
# print(sort_array([1, 111, 11, 11, 2, 1, 5, 0]), [1, 1, 5, 11, 2, 11, 111, 0])
# print(sort_array([]), [])

###################################

def valid_solution(board):
    flat_list = [item for sublist in board for item in sublist]
    if flat_list.count(0):
        return False
    for idx in range(9):
        horizontal = board[idx]
        vertical = [board[jdx][idx] for jdx in range(9)]
        if sum(horizontal) == sum(vertical) != 45:
            return False
    for idx in range(0, 9, 3):
        for jdx in range(0, 9, 3):
            board[idx:idx + 3][jdx:jdx+3]
    return True


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True)

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 1],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True)


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 0, 3, 4, 9],
                      [1, 0, 0, 3, 4, 2, 5, 6, 0],
                      [8, 5, 9, 7, 6, 1, 0, 2, 0],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 0, 1, 5, 3, 7, 2, 1, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False)
