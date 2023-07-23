import csv

# 读取原始CSV文件
with open('fyx_chinamoney.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# 将数据拆分为多个数组
batch_size = 80
batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

# 打印输出每个数组并保存为新的CSV文件
for i, batch in enumerate(batches):
    print(f'Batch {i + 1}:')
    for row in batch:
        print(row)
    # print()
    # 将数据保存为新的CSV文件
    with open(f'output_batch{i + 1}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(batch)

    print()
