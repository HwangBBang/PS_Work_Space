# 정삼각형 2n + 1 개를 이어 붙여
# 아래 길이 n+1 , 윗 길이 n ,
# 위의 n개의 삼각형 중 일부에 정삼각형 붙힘.
# 마름모 란 무엇일까? 어떤 방향으로든 정삼각형 붙이면 마름모야 .
# 예시2  4+ 3 = 7 개중 1개 선택과 2개 선택의 조합을 고르면되는거네?
# dp문제

# n 이 1+0일 때를 관찰하자 .
#   ㅁ
# ㅁ  ㅁ
# dp(1) = 1 + 2


# n 이 2+0일 때를 관찰하자 .
#   ㅁ  ㅁ
# ㅁ  ㅁ  ㅁ
# dp(2) =  dp(1)*2
# -----------------------
# 이전 꺼의 위가 없으면 마름모가 있거나 없거나. 2개
# 이전 꺼의 위가 있으면 마름모가 있거나 없거나. 3개


# 즉 끝이 마름모 인지 정삼각형인지에 따라 dp1, dp2 를 만듦
# 삼각형으로 끝나는 경우에는
#   위에가 없을때 3가지 *2
#   위가있을때 4가지
# 마름모로 끝나는 경우에는
#   위에가없을때 2가지
#   위가 있을때 3가지
# i 번째  경우 수 =삼가형으로끝나는 경우 + 마름모로 끝나는 경우


def solution(n, tops):
    dp_t = [0] * (n + 1)
    dp_d = [0] * (n + 1)
    dp = [0] * (n + 1)
    if tops[0] == 0:
        dp_t[1] = 2
        dp_d[1] = 1
    else:
        dp_t[1] = 3
        dp_d[1] = 1

    dp[1] = dp_t[1]+dp_d[1]

    for i in range(2, n + 1):
        if tops[i-1] == 0:  # 삿갓없음
            # 삼각형으로 끝나는 경우의 수 업데이트
            dp_t[i] = (dp_t[i-1] * 2 + dp_d[i-1]) % 10007
            # 마름모로 끝나는 경우의 수 업데이트
            dp_d[i] = (dp_t[i-1] + dp_d[i-1]) % 10007
            dp[i] = (dp_t[i] + dp_d[i]) % 10007            # 총 경우의 수 업데이트

        else:
            # 삼각형으로 끝나는 경우의 수 업데이트
            dp_t[i] = (dp_t[i-1] * 3 + dp_d[i-1]*2) % 10007
            # 마름모로 끝나는 경우의 수 업데이트
            dp_d[i] = (dp_t[i-1]*1 + dp_d[i-1]*1) % 10007
            dp[i] = (dp_t[i] + dp_d[i]) % 10007            # 총 경우의 수 업데이트

    return dp[n]
