import numpy as np

np.random.seed(0)   # 시드 고정
rewards = []

for n in range(1, 11):
    reward = np.random.rand()
    rewards.append(reward)
    Q = sum(rewards) / n
    print(Q)

print("\n ----- \n")

# 두 번째 식
np.random.seed(0)   # 시드 고정
Q = 0

for n in range(1, 11):
    reward = np.random.rand()
    Q = Q + (reward - Q) / n
    print(Q)