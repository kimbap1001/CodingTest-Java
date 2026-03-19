import sys
from itertools import combinations
input = sys.stdin.readline

def solve() -> None:
    a=[int(input()) for _ in range(9)]

    for combo in combinations(a,7):
        if sum(combo)==100:
            print(*sorted(combo))
            break

if __name__=="__main__":
    solve()