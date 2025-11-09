L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 正确的列表生成式示例：

# 1. 生成数字的平方
squares = [x**2 for x in range(1, 11)]
print("数字的平方:", squares)

# 2. 生成字符串组合
# 如果你想要生成 "11455141919810" 中每个数字与 1-99 的组合
combinations = [i + str(a) for i in "11455141919810" for a in range(1, 100)]
print("字符串组合示例:", combinations[:10])  # 只显示前10个
print("=" * 50)
# 3. 过滤偶数
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("1-20的偶数:", even_numbers)

# 4. 转换大小写
names_upper = [name.upper() for name in L]
print("名字大写:", names_upper)

# 切片操作示例
print("L[1:4]:", L[1:4])

# 解释 f"{str(range(1, 100))}" 的含义
print("\n--- 解释 f'{str(range(1, 100))}' ---")
range_obj = range(1, 100)
print("range(1, 100) 本身:", range_obj)

str_range = str(range_obj)
print("str(range(1, 100)):", str_range)

f_string_result = f"{str_range}"
print("f'{str(range(1, 100))}':", f_string_result)

print("迭代 f'{str(range(1, 100))}' 的结果:")
for char in f_string_result:
    print(f"  '{char}'", end=" ")

# 扁平化嵌套列表的详细解释
print("\n\n--- 扁平化嵌套列表 ---")
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print("原始嵌套列表:", nested_list)

# 逐步解释扁平化过程
print("\n扁平化过程:")
for i, sublist in enumerate(nested_list):
    print(f"  第{i+1}个子列表: {sublist}")
    for j, item in enumerate(sublist):
        print(f"    从子列表{i+1}中取出第{j+1}个元素: {item}")

# 最终结果
flattened = [item for sublist in nested_list for item in sublist]
print(f"\n扁平化结果: {flattened}")

# 等价于传统的for循环写法：
print("\n--- 传统for循环写法 ---")
flattened_traditional = []
for sublist in nested_list:
    for item in sublist:
        flattened_traditional.append(item)
print("传统写法结果:", flattened_traditional)
