import sys
import heapq
input= sys.stdin.readline
q = list()
n=int(input())
for i in range(n):
    num=int(input())
    if num == 0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q,(abs(num),num))