n = int(input())

# 상근이 시작 

# 마지막 사람이 1을 뽑 -> dp(n-1)
    # 전 사람이 1뽑 -> dp(n-2)
    # 전 사람이 3뽑 -> dp(n-4)
# 마지막 사람이 3을 뽑 -> dp(n-3)
    # 전 사람이 1뽑 -> dp(n-4)
    # 전 사람이 3뽑 -> dp(n-6)

# n = 5
# 상 창 상 창 상
# 상 창 상
# 상 창 상

# n = 6
# 상 창 상 창 상 창
# 상 창 상 창

# n = 7
# 상 창 상 창 상 창 상
# 상 창 상 창 상 
# 상 창 상 

if n % 2 == 1:
    print("SK")
else:
    print("CY")
    
