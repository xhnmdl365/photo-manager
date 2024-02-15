import os
import shutil

def move_and_clean_directory(src_dir, dest_dir):
    # 确保目标目录存在
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍历源目录中的所有文件和子目录
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            print(f"Moving {file} to {dest_dir}...")
            # 构建源文件路径和目标文件路径
            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, file)
            print(os.path.exists(src_path), os.path.exists(dest_path))
            if os.path.dirname(src_path) == src_dir:
                print(f"File {file} is already in the top level, skipping...")
            else:
                if os.path.exists(src_path):
                    shutil.move(src_path, dest_path)

    # 删除源目录及其子目录中的空文件夹
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

if __name__ == "__main__":
    source_directory = "/Volumes/Untitled/photo"
    destination_directory = "/Volumes/Untitled/photo"

    move_and_clean_directory(source_directory, destination_directory)
    print("Files moved and empty directories removed successfully.")
