def solution(board, skill):
    answer = 0
    for i in skill:
        # i[0] == 1 -> 파괴, 2 -> 복구
        if i[0] == 1:
            for j in range(i[1], i[3]+1):
                for k in range(i[2], i[4]+1):
                    board[j][k] -= i[5]
        else:
            for j in range(i[1], i[3]+1):
                for k in range(i[2], i[4]+1):
                    board[j][k] += i[5]
    for i in board:
        for j in i:
            if j > 0:
                answer += 1

    return answer
