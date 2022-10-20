#!/usr/bin/python3

"""Program that solves the N queens problem
The N queens puzzle is the challenge of
placing N non-attacking queens on an
N×N chessboard"""


if __name__ == "__main__":
    from sys import argv
    ls = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(n):
        ls.append([i, None])

    def i_exist(y):
        """check that queen already exists"""
        for x in range(n):
            if y == ls[x][1]:
                return True
        return False

    def to_reject(x, y):
        """to reject or not"""
        if (i_exist(y)):
            return False
        i = 0
        while(i < x):
            if abs(ls[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_ans(x):
        """clear the answers in the case of failure"""
        for i in range(x, n):
            ls[i][1] = None

    def nqueens(x):
        """recursion to find the solution"""
        for y in range(n):
            clear_ans(x)
            if to_reject(x, y):
                ls[x][1] = y
                if (x == n - 1):
                    print(ls)
                else:
                    nqueens(x + 1)

    nqueens(0)
