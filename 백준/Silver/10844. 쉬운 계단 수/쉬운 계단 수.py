# 
import sys
input = sys.stdin.readline

# 45656 ? 인잡한 자리가 1 씩 차이가난다.
# N 주어질 때, 총 계단의 길이가 N 인 계단수를 구하자.
# N = 1 일때는 어떻게 될까? 

# N = 1 일때는 한자리 모든수가 가능하다 0씩 차이난다고 볼 수 있기 때문
# N = 2 일때는? 10의자리는 N = 1일때와같다. 겹치니 점화식을 사용하기위해 
# N = k 일때 dp[k]는 계단 수의 갯수라고 하자.
# 다시 N = 2 일때를 살펴보자 10의자리는 N = 1일때와 같으므로
# (십의 자리])(일의 자리) = (dp[1])(dp[1]+-1) = dp[1]*2 - 1(10일때)
# dp 테이블이만들어지기위해서는 자리수와 앞에오는 자리를 통제할 수있어야한다.
# 따라서 2차원 dp 테이블로 만들어야한다. 

# dp[자리 수 1][앞에 어떤 수?] = 현재 자리수 + 앞에 어떤 수 = 갯수  
# 정답은 sum(dp[n])

# dp[1][1] ~ dp[1][9] = 1
#  1  2  3  4  5  6  7  8  9  
#  1  1  1  1  1  1  1  1  1

# dp[2][1] = 1 , dp[2][2] ~ dp[2][8] = 2 ,dp[2][9] = 1
# 0  1  2  3  4  5  6  7  8  9  
# 1  1  2  2  2  2  2  2  2  1

# dp[3][1]~ dp[3][8] 
#  1  2  3  4  5  6  7  8 
# dp[3][1~8] = dp[2][0~7] + dp[2][1~9]
# dp[3][9] = dp[2][8]

# dp[현재 자리수][0] = dp[현재 자리수 -1][1]
# dp[현재 자리수][1~8] = dp[현재 자리수 -1][앞의 수 +-1]
# dp[현재 자리수][9] = dp[현재 자리수 -1][8]
n = int(input())

dp = [0]*(n+1)
dp[1] = [1 for _ in range(1,10)] +[0]

for i in range(2,n+1):
    dp[i] = [0 for _ in range(0,11)]


for i in range(2,n+1):
    
    dp[i][0] = dp[i-1][1]
    
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
    
    dp[i][9] = dp[i-1][8]

print(sum(dp[n])%1000000000)