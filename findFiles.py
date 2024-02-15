import os

def get_dot_files(directory):
    dot_files = []

    # 递归遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith('.'):
                # 构建完整的文件路径并添加到列表中
                dot_files.append(os.path.join(root, file))

    return dot_files

if __name__ == "__main__":

    target_directory = "/Volumes/Untitled/photo"

    # 获取包含子目录的以.开头的文件名
    dot_files = get_dot_files(target_directory)

    # 打印结果
    print("Files starting with . :")
    for file in dot_files:
        print(file)