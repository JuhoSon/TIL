import sys
sys.stdin = open('input.txt')
# 방 호수의 인덱스만큼 0으로 채워진 리스트를 만들어 동선이 완성될때마다
# 해당하는 인덱스에 해당하는 요소를 1씩 더해주기 -> 인덱스 카운팅
# 방을 다 도는데 걸리는 최소 시간은 최대로 겹치는 동선수

# 13579
# 2468
# 1-3, 4-6 도 동선이 겹치는 것으로 생각한다.

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    rooms = [0] * 401
    for i in range(N):
        room = list(map(int, input().split()))
        room1 = min(room)  # 동선 중 왼쪽에 있는 방
        if not room1 % 2:  # 방이 짝수라면 맞은 편 방(+1)도 거친다.
            room1 -= 1
        room2 = max(room)  # 동선 중 오른쪽에 있는 방
        if room2 % 2:  # 방이 홀수라면 맞은 편 방(-1)도 거친다.
            room2 += 1
        for j in range(room1, room2 + 1):
            rooms[j] += 1

    ans = max(rooms)  # 가장 많은 동선을 가진 방
    print(f'#{tc}', ans)
