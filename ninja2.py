n, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans += 1
if x % 2 == 0:
    ans += 1
print(ans)