import pandas as pd

list_num = [264, 286, 308, 330,  276, 299, 322, 345,  288, 312, 336, 360]

threshold = 1000
delta = 0.003

arr_label = []
for i in range(len(list_num)):
    arr_label.append(str(list_num[i]))

arr = [arr_label, list_num]

global aprch_data
aprch_data = []

def add_arr(arr_in, arr_fx, threshold, delta):
    global aprch_data
    arr_out_lb = []
    arr_out_num = []
    for i in range(len(arr_in[0])):
        for j in range(len(arr_fx[0])):
            data_label = arr_in[0][i] + "+" + arr_fx[0][j]
            data_value = arr_in[1][i] + arr_fx[1][j]
            arr_out_lb.append(data_label)
            arr_out_num.append(data_value)
            if (threshold - data_value) <= threshold*delta and data_value <= threshold:
                aprch_data.append([data_label, data_value])
    return [arr_out_lb, arr_out_num]

arr_out = arr
cnt = 0
while min(arr_out[1]) <= threshold:
    print(cnt+1)
    arr_out = add_arr(arr_out, arr, threshold, delta)
    #print(arr_out)
    cnt += 1

#print(aprch_data)
df = pd.DataFrame(aprch_data, columns=["Label", "Value"])
#print(len(df))
print(df.sort_values('Value', ascending=False))
print(len(df))