def find_match(target, delta, arr_lst, set_cnt=1):
    if target/(min(arr_lst)+max(arr_lst))*2 < 5:
        # 答案的list
        lst_ans = []

        # 將 input arr_num 換成 [label, num] 形式
        # 固定的組串數
        lst_fx = []
        for arr in arr_lst:
            lst_fx.append([str(arr), arr])
            # 如果輸入的條件剛好滿足在範圍內，就直接丟進答案 lst_ans 內
            print(arr)
            if target - delta <= arr < target:
                lst_ans.append([str(arr), arr])
            print(lst_ans)

        # 開始計算
        # 起始數據從原本加起
        lst_in = lst_fx
        cnt = 0

        # if target/max(arr_num)

        # 當 input 還有值時，繼續計算
        while lst_in:
            lst_out = []

            # 走過所有input值
            for lab_in, num_in in lst_in:
                # 走過所有要加的值
                for lab_fx, num_fx in lst_fx:

                    # 標籤紀錄 "a+b+...."
                    lab = lab_in + "+" + lab_fx

                    # 計算加總值
                    num = num_in + num_fx
                    cnt += 1
                    print(cnt, lab, num, set_cnt)

                    # 判斷加總沒有超過 target
                    if num <= target:

                        # 如果加總接近目標，丟進 ans
                        if num >= target - delta:
                            lst_ans.append([lab, num, set_cnt])
                            print(lst_ans)
                        # 如果沒有超過 target 丟到 out 等等丟回 input 再算
                        lst_out.append([lab, num])
            lst_in = lst_out
        return sorted(lst_ans, key=lambda x: x[1], reverse=True)
    else:
        return find_match(target/2, delta, arr_lst, set_cnt*2)

