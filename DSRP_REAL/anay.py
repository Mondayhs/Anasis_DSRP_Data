import pandas as pd

# 读取第一个文件（从头读取）
file1 = "Data\RADFET Voltage-data-2025-01-20 08_04_16.csv"
df1 = pd.read_csv(file1)

# 读取第二个和第三个文件，从第二行开始（跳过第一行）
file2 = "Data\RADFET Voltage-data-2025-01-20 08_04_21.csv"
file3 = "Data\RADFET Voltage-data-2025-01-20 08_04_26.csv"

df2 = pd.read_csv(file2, skiprows=1)  # 跳过第一行
df3 = pd.read_csv(file3, skiprows=1)  # 跳过第一行

# 合并三个 DataFrame
merged_df = pd.concat([df1, df2, df3], ignore_index=True)

# 保存合并后的文件
output_file = "merged_file.csv"
merged_df.to_csv(output_file, index=False)

print(f"合并完成，保存为 {output_file}")
