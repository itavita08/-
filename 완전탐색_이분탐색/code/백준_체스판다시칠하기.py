import sys

n, m = map(int, sys.stdin.readline().split())
color = [sys.stdin.readline().strip() for _ in range(n)]

count = []

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if color[a][b] != 'W':
                        black += 1
                    if color[a][b] != 'B':
                        white += 1
                else:
                    if color[a][b] != 'W':
                        white += 1
                    if color[a][b] != 'B':
                        black += 1
        count.append(white)
        count.append(black)
print(min(count))
