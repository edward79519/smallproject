import numpy as np

# input 參數
arr_num = np.array([264, 286, 308, 330,  276, 299, 322, 345,  288, 312, 336, 360])
target = 1500
delta = 0.003

# 將 input arr_num 換成 [label, num] 形式
print(arr_num)
arr_label = np.array([])
for a in arr_num:
    arr_label = np.append(arr_label, str(a))
print(arr_label)

