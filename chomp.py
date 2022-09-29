def grid(m, n, M):
    for i in range(0, m):
        for j in range(0, n):
            print(M[i][j], end='')
        print()

def erase(a, b ,M):
    for i in range(a, len(M)):
        for j in range(b, len(M[0])):
            M[i][j] = " "
            

def main():
    valid = False
    while not valid:
        try:
            m = int(input())
            n = int(input()) 
            valid = True
        except ValueError:
            pass

    print("Start the game!!!")
    M = [['*' for i in range(n)] for j in range (m)]
    grid(m, n, M)
    not_end = True
    i = 0
    while not_end:
        i = i%2
        i += 1
        valid = False
        while not valid:
            try:
                move = input((f"Player {i} move: "))
                move = map(int, move.split(" "))
                a, b = move
                a -= 1
                b -= 1
                if (a >= m or b >= n) or M[a][b] == " ":
                    raise ValueError
                valid = True
            except Exception:
                print("Try again") 
        erase(a, b, M)
        grid(m, n, M)
        if a == b == 0:
            not_end = False
    print(f"Game end!\nPlayer {i%2 + 1} win the game!!!")


main()
