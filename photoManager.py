import os
import shutil
from datetime import datetime
import exifread
import exiftool

def organize_photos_by_date(source_folder):
    # 创建一个目标文件夹
    target_folder = os.path.join(source_folder, "OrganizedPhotos")
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    exclude_folders = ["OrganizedPhotos"]

    # 遍历源文件夹下的所有文件和子文件夹
    for root, dirs, files in os.walk(source_folder):
        dirs[:] = [d for d in dirs if d not in exclude_folders]
        for file in files:
            # 忽略以 "._" 开头的文件
            if file.startswith("._"):
                continue
            file_path = os.path.join(root, file)
            file_name, file_extension = os.path.splitext(file)
            current_path = os.path.join(root, file)

            # 检查文件类型是照片或视频
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mov', '.heic')):
                # 读取照片的拍摄日期
                shooting_time = get_date_taken(file_path)
                print(f"shooting_time: {shooting_time}")
                # if not shooting_time:
                #     shooting_time = get_image_modified_time(file_path)

                if shooting_time:
                    # 构建目标文件夹路径
                    target_subfolder = os.path.join(target_folder, shooting_time.strftime('%Y-%m'))

                    # 创建目标文件夹（如果不存在）
                    if not os.path.exists(target_subfolder):
                        os.makedirs(target_subfolder)

                    # 移动照片到目标文件夹
                    shutil.move(file_path, os.path.join(target_subfolder, file))

                    aae_file_path = os.path.join(root, file_name + ".AAE")
                    xmp_file_path = os.path.join(root, file_name + ".XMP")
                    # 处理相同文件名的xmp文件
                    if os.path.exists(xmp_file_path):
                        shutil.move(xmp_file_path, os.path.join(target_subfolder, file_name + ".xmp"))

                    if os.path.exists(aae_file_path):
                        shutil.move(aae_file_path, os.path.join(target_subfolder, file_name + ".aae"))

    print("照片整理完成！")

def get_date_taken(file_path):
    try:
        # 使用exifread获取照片的拍摄日期
        with open(file_path, 'rb') as file:
            tags = exifread.process_file(file)
            if 'EXIF DateTimeOriginal' in tags:
                date_taken_str = str(tags['EXIF DateTimeOriginal'])
                return datetime.strptime(date_taken_str, '%Y:%m:%d %H:%M:%S')
        return None
    except Exception as e:
        print(f"Error while getting date taken for {file_path}: {e}")
        return None

def get_image_modified_time(file_path):
    try:
        # 获取文件修改时间
        modified_timestamp = os.path.getmtime(file_path)
        modified_datetime = datetime.fromtimestamp(modified_timestamp)

        return modified_datetime
    except Exception as e:
        print(f"Error while getting modified time for {file_path}: {e}")
        return None

def delete_files_starting_with_underscore(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件名是否以 "._" 开头
        if filename.startswith("._"):
            file_path = os.path.join(folder_path, filename)
            # 删除文件
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

if __name__ == "__main__":
    source_folder_path = "/Volumes/Untitled/testphoto/"
    delete_files_starting_with_underscore(source_folder_path)
    organize_photos_by_date(source_folder_path)
