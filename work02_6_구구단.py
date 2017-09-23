#세로 구구단
for x in range(1, 16):
    for y in range(1, 16):
        print("%d X %d = %d" %(x, y, x*y))

#오른쪽 정렬
for x in range(1, 16):
    for y in range(1, 16):
        print("%3d X %3d = %3d" %(x, y, x*y))

#왼쪽 정렬
for x in range(1, 16):
    for y in range(1, 16):
        print("%-3d X %-3d = %-3d" %(x, y, x*y))

#가로 구구단
for y in range(1, 16):
    print()     #줄바꿈 시키는 명령어
    for x in range(1, 16):
        print("%3d X %3d = %-3d" %(x, y, x*y),end="")