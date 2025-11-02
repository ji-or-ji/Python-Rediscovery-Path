def move(n : int = 1 , a : str = "A", b : str = "B", c : str = "C") :
    """
    汉诺塔递归解法
    n: 盘子数量
    a: 起始柱子
    b: 辅助柱子  
    c: 目标柱子
    """
    if n == 1 :
        print(f"{a} --> {c}")
        return 1
    else :
        # 将n-1个盘子从a移动到b，借助c
        count1 = move(n-1, a, c, b)
        # 将最大的盘子从a移动到c
        print(f"{a} --> {c}")
        # 将n-1个盘子从b移动到c，借助a
        count2 = move(n-1, b, a, c)
        return count1 + 1 + count2

# 测试3个盘子的汉诺塔
print("3个盘子的汉诺塔解法：")
total_steps = move(64, 'A', 'B', 'C')
