dp = [0]*1001
dp[1]=1
dp[2]= 3
num=int(input())
for i in range(3,num+1):
    dp[i] = dp[i-1] + dp[i-2] *2

print(dp[num]%10007)
