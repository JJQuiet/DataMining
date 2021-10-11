import numpy as np

print(np.random.rand(5))  #0-1的均匀分布

print(np.random.randn(5))  # -1 —— 1 的正态分布

print(np.arange(-10,10,2)) # [-10,10)    [-10  -8  -6  -4  -2   0   2   4   6   8]

print(np.arange(12).reshape(3,4)) # [0,12)

print(np.linspace(0,1,11)) # [0,1]分成11份

print(np.logspace(-3,3,7)) # 10^-3 到 10^3 
