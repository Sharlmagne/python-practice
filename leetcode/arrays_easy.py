import collections


def removeDuplicates(nums):
    """
    Iterate through the array and compare the current value with the value to the left
    If value to the left is equal to the current value, add that value to the end
    If not, increment the index of the array
    Return the value of the j
    :param nums:
    :return:
    """
    j = 1
    for i in range(1, len(nums)):
        if nums[j] == nums[j - 1]:
            nums.append(nums.pop(j))
        else:
            j += 1
    return j


def maxProfit(prices):
    """
    Create a variable to track the max profit
    Iterate through the list and compare the current value to the left value
    If the value on the left is greater that the value on the right, caculate the profit and add it to the max profit
    return the max profit at the end of the loop
    :param prices:
    :return:
    """
    max_profit = 0
    for i in range(1, len(prices)):
        price1 = prices[i]
        price2 = prices[i - 1]
        if price1 > price2:
            max_profit += price1 - price2
    return max_profit


def rotate(nums, k):
    """
    For thr number of rotations, pop the value at the end of the list and insert it at the beginning
    :param nums:
    :param k:
    :return:
    """
    for rotations in range(k):
        nums.insert(0, nums.pop())


def containsDuplicate(nums):
    """
    Iterate through the array and pop the current value.
    Check if the current value is in the array after popping it.
    If the value is still in the array, then a duplicate exists, return True.
    If not, return False
    :param nums:
    :return:
    """
    i = 0
    while i < len(nums):
        popped = nums.pop(i)
        i += 1
        if popped in nums:
            return True
    return False


def singleNumber(nums):
    """
    Sort the array
    Iterate through the array by 2 and check if
        The array is larger than 1
        The current value is not equal to the value to the left
        If the current index is the second to last value
    If an of the conditions are true, break the loop
    g bv

    :param nums:
    :return:
    """
    nums.sort()
    i = 1
    unique = 0
    while i < len(nums):
        if len(nums) == 1:
            break
        if nums[i] != nums[i - 1]:
            unique = nums[i - 1]
            break
        if i == len(nums) - 2:
            unique = nums[-1]
            break
        i += 2
    return unique


def intersect(nums1, nums2):
    p1 = p2 = 0  # Create pointers

    # Sort arrays
    nums1.sort()
    nums2.sort()

    intersects = []

    # Repeat until one pointer gets to the end
    while p1 != len(nums1) and p2 != len(nums2):
        if nums1[p1] == nums2[p2]:
            intersects.append(nums1[p1])
            p1 += 1
            p2 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        elif nums1[p1] < nums2[p2]:
            p1 += 1
    return intersects


def plusOne(digits):
    i = len(digits) - 1
    while i >= 0:
        if digits[i] < 9:
            digits[i] += 1
            break
        else:
            digits[i] = 0
            if i == 0:
                digits = [1] + digits
            i -= 1
    return digits

    # numbers = str((int("".join(map(str, digits))) + 1))
    # digits = [int(x) for x in numbers]
    #
    # return digits


def moveZeroes(nums):
    if len(nums) > 1:
        i = 0
        j = 0
        while i + j < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                j += 1
            else:
                i += 1


def twoSum(nums, target):
    # j = 0
    # while j < len(nums):
    #     diff = target - nums[j]
    #     for k in range(len(nums)):
    #         if nums[k] == diff and k != j:
    #             return [k, j]
    #     j += 1
    hashmap = {}
    for i in range(len(nums)):
        num = nums[i]
        if num not in hashmap:
            hashmap[target - num] = i
        else:
            return [hashmap[num], i]
    return True


def rotate(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # Save the Top Left value
            top_left = matrix[top][left + i]

            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left

        left += 1
        right -= 1


def isValildSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            if (board[row][col] in rows[row]
                    or board[row][col] in cols[col]
                    or board[row][col] in squares[(row // 3, col // 3)]):
                return False
            rows[row].add(board[row][col])
            cols[col].add(board[row][col])
            squares[(row // 3, col // 3)].add(board[row][col])
    return True


def isValildSudoku2(board):
    # Initialize sets
    # cols = {k: v for (k, v) in zip(range(9), [set() for i in range(9)])}
    # rows = {k: v for (k, v) in zip(range(9), [set() for i in range(9)])}
    cols = {}
    rows = {}
    squares = {}

    for i in range(9):
        cols[i] = set()
        rows[i] = set()
        for j in range(9):
            squares[(i // 3, j // 3)] = set()

    # Loop through the board
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            if (board[row][col] in rows[row]
                    or board[row][col] in cols[col]
                    or board[row][col] in squares[(row // 3, col // 3)]):
                return False
            rows[row].add(board[row][col])
            cols[col].add(board[row][col])
            squares[(row // 3, col // 3)].add(board[row][col])
    return True



def player_moves(moves_input):
    moves = [*moves_input]
    player = "wendy"
    endgame = False
    i = 2

    while not endgame:
        if player == "wendy":
            if i == len(moves):
                endgame = True
                player = "bob"
            elif moves[i - 2] == moves[i] and moves[i] == player[0]:
                moves.pop(i - 1)
                i = 2
                player = "bob"
            else:
                i += 1

        if player == "bob":
            if i == len(moves):
                endgame = True
                player = "bob"
            elif moves[i - 2] == moves[i] and moves[i] == player[0]:
                moves.pop(i - 1)
                i = 2
                player = "wendy"
            else:
                i += 1

    return player


if __name__ == "__main__":
    # nums = [2, 7, 11, 15]
    # nums2 = [1, 2, 4]
    # nums3 = [3, 3]
    # nums4 = [1, 2, 3]
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    #     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    #     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    moves = "wwwbbbbwww"

    print(player_moves(moves))
    # print(isValildSudoku2(board2))
    # nums = [2, 2, 1]
    # nums2 = [4,1,2,1,2]
    # nums3 = [1]
    # print(singleNumber(nums2))
