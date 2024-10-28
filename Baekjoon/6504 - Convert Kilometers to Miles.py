#S5_7596_MP3 Songs

cnt=0
while True:
    n=int(input())
    if n==0:
        break

    cnt += 1
    tracks= []

    for _ in range(n):
        tracks.append(input().strip())

    tracks.sort(key=str.casefold)
    print(cnt)

    for t in tracks:
        print(t)
