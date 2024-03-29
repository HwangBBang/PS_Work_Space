# n ~ 2n 사이의 소수의 갯수를 구하는 문제
# 범위내의 소수를 판별하는 방법 => 에라토스테네스의 체를 이용

# <에라토스테네스의 체>
# 소수 판별 알고리즘
# 대량의 소수를 빠르게 판별 할 때 사용된다.

# 에라토스테네스의 체는 가장 먼저 소수를 판별할 범위만큼 배열을 할당 후
# 해당하는 값을 넣어주고, 이후에 하나씩 지워나가는 방법을 이용한다.

# 에라토스테네스의 체: 
# 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법
# 1. 1은 제거 
# 2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택, 나머지 2의 배수를 모두 지운다.
# 3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택, 나머지 3의 배수를 모두 지운다.
# 4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택, 나머지 5의 배수를 모두 지운다.
# 5. (반복)


# n~2n 사이 소수판별하는 함수
def eratos(n):
    state = [0,0]+[1]*(2*n-1)
    primeNums = []
    
    for i in range(2,2*n+1):
        # 피벗이 소수라면?
        if state[i] == 1 :
            # 피벗의 배수들의 상태를 0으로
            for j in range(2*i,2*n+1,i):
                state[j] = 0
            if state[i] == 1 and i > n:
                primeNums.append(i)
            
    return len(primeNums)


while 1:
    n = int(input())
    
    if n == 0:
        break
    print(eratos(n))