# 회의실 배정

import sys

n = int(sys.stdin.readline())
meeting = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append([start, end])

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

last, count = 0, 0
for start, end in meeting:
    if start >= last:
        count += 1
        last = end

print(count)

