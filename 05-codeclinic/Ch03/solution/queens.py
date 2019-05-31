
# from itertools import permutations

# n = 11
# cols = range(n)
# for vec in permutations(cols):
#     if (n == len(set(vec[i]+i for i in cols)) == len(set(vec[i]-i for i in cols))):
#         print(vec)

# #https://code.activestate.com/recipes/576647-eight-queens-six-lines/
#####################################################################
# nq = 8
# def Permute(queens, row):
#     for i in range(nq):
#         queens[row] = i
#         if Fine(queens, row):
#             if row == nq - 1:
#                 print(queens)
#                 globals()["solutions"] = globals()["solutions"] + 1
#             else:
#                 Permute(queens, row+1)
            
# def Fine(queens, row):
#     c = 0
#     derga = True
#     for i in range(row):
#         c, cur, oth = c+1, queens[row], queens[row-i-1]
#         if (cur == oth) or (cur-c == oth) or (cur+c == oth):
#             derga = False
#             break
#     return(derga)

# globals()["solutions"] = 0
# queens = [0] * nq  #[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
# #print(queens)
# for i in range(nq):
#     queens[0] = i
#     Permute(queens, 1)
# print(globals()["solutions"])
###############################################################################
# import sys
n = 8
cnt = 0
board = [0] * n

def safe(col,row):
    for j in range(col):
        if board[j] == row  or abs(board[j] - row) == abs(col - j) :
            return False
    return True


def nqueen(col):
    for row in range(n):
        if safe(col,row):
            board[col] = row 
            if col == n-1:
                print(board)
                global cnt 
                cnt += 1
                # sys.exit(0)
            else:
                nqueen(col+1)

nqueen(0)
print(cnt)