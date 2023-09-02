mod=1000000007
def esum(m,n,K,N):
    if(K==1):
       return n
    else:
        return (N-(m-n)*esum(m,n,K-1,N)%mod)
low,high=map(int,input().split())
K=int(input())
diff=high-low+1
if(diff%2==0):
m=diff//2
n=m
else:
if(low%2==0):
m=(diff-1)//2
n=m+1
else:
m=(diff+1)//2
n=m-1
N=m
for i in range(K-1):
N=(N*(m+n))%mod
out=esum(m,n,K,N)%mod
print(out)