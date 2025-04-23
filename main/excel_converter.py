import os
import pandas as pd
from datetime import datetime
import uuid
import shutil

def convert_2d_to_1d(input_file_path):
    # 读取原始Excel文件
    df = pd.read_excel(input_file_path)
    
    # 获取用户输入
    item_col = input("请输入第一列转化后的列标题（不输入则默认'项目'）：") or "项目"
    year_col = input("请输入第二列转化后的列标题（不输入则默认'年份'）：") or "年份"
    value_col = input("请输入第三列转化后的列标题（不输入则默认'金额'）：") or "金额"
    
    # 转换二维表到一维表
    melted_df = df.melt(
        id_vars=[df.columns[0]],  # 第一列作为项目列
        var_name=year_col,        # 列标题转为年份
        value_name=value_col      # 值转为金额
    )
    
    # 重新排序列顺序
    melted_df = melted_df[[df.columns[0], year_col, value_col]]
    
    # 创建输出目录结构
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(parent_dir, "output", f"{timestamp}_{unique_id}")
    os.makedirs(output_dir, exist_ok=True)
    
    # 复制原始文件到输出目录
    original_copy_path = os.path.join(output_dir, os.path.basename(input_file_path))
    shutil.copy2(input_file_path, original_copy_path)
    
    # 保存转换后的文件
    base_name, ext = os.path.splitext(input_file_path)
    converted_file_path = os.path.join(output_dir, f"{os.path.basename(base_name)}_converted{ext}")
    melted_df.to_excel(converted_file_path, index=False)
    
    print(f"转换完成！文件已保存到：{converted_file_path}")
    return converted_file_path

if __name__ == "__main__":
    # 检查output目录是否存在
    if not os.path.exists("output"):
        os.makedirs("output")
    
    input_path = input("请输入要转换的Excel文件路径或包含Excel文件的文件夹路径（支持xlsx格式）：")
    
    if os.path.isfile(input_path):
        # 如果输入的是单个文件
        if input_path.lower().endswith('.xlsx'):
            convert_2d_to_1d(input_path)
        else:
            print("错误：仅支持Excel文件（.xlsx格式）！")
    elif os.path.isdir(input_path):
        # 如果输入的是目录
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.lower().endswith('.xlsx'):
                    file_path = os.path.join(root, file)
                    convert_2d_to_1d(file_path)
    else:
        print("错误：路径不存在！")
