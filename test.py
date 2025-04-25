import numpy as np
import time

# ========== 初始化 ==========
size = 10000  # 栅格尺寸
bands = 5    # 波段数

# 创建测试栅格（整数）
int_array = np.ones((bands, size, size), dtype=np.int32)

# 创建测试栅格（浮点）
float_array = np.full((bands, size, size), 1.5, dtype=np.float32)

# ========== 整数运算 ==========
int_start = time.time()
int_result = (int_array + 2) * 3  # 向量化运算
int_time = time.time() - int_start
print(f"Python整数运算耗时: {int_time:.4f}秒")

# ========== 浮点运算 ==========
float_start = time.time()
float_result = np.sqrt(float_array / 0.5)  # 向量化运算
float_time = time.time() - float_start
print(f"Python浮点运算耗时: {float_time:.4f}秒")