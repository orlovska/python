def check_block(block):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if sorted(block) == numbers:
        return 1
    else:
        return 0


def validSolution(board):
    result = []
    for horizontal_block in board:
        result.append(check_block(horizontal_block))

    vertical_block = []
    for colomn in range(9):
        for row in range(9):
            vertical_block.append(board[row][colomn])
        result.append(check_block(vertical_block))
        vertical_block = []

    square_block1 = []
    square_block2 = []
    square_block3 = []
    for row in range(9):
        for colomn in range(3):
            square_block1.append(board[row][colomn])
            if len(square_block1) == 9:
                result.append(check_block(square_block1))
                square_block1 = []
        for colomn in range(3, 6):
            square_block2.append(board[row][colomn])
            if len(square_block2) == 9:
                result.append(check_block(square_block2))
                square_block2 = []
        for colomn in range(6, 9):
            square_block3.append(board[row][colomn])
            if len(square_block3) == 9:
                result.append(check_block(square_block3))
                square_block3 = []

    if 0 in result:
        return False
    else:
        return True


print(
    validSolution(
        [
            [1, 3, 2, 5, 7, 9, 4, 6, 8],
            [4, 9, 8, 2, 6, 1, 3, 7, 5],
            [7, 5, 6, 3, 8, 4, 2, 1, 9],
            [6, 4, 3, 1, 5, 8, 7, 9, 2],
            [5, 2, 1, 7, 9, 3, 8, 4, 6],
            [9, 8, 7, 4, 2, 6, 5, 3, 1],
            [2, 1, 4, 9, 3, 5, 6, 8, 7],
            [3, 6, 5, 8, 1, 7, 9, 2, 4],
            [8, 7, 9, 6, 4, 2, 1, 3, 5],
        ]
    )
)


print(
    validSolution(
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]
    )
)

