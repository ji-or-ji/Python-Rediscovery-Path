def findMinAndMax(L) :
    # 保证列表中有数字
    if len(L) == 0 :
        return None , None
    else :
        max_int = L[0]
        min_int = L[0]
        # 同时计算最大值和最小值
        for i in L :
            if i >= max_int :
                max_int = i
            if i < min_int :
                min_int = i
    
    return (min_int, max_int)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
