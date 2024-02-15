import exifread
import os
import imageio
from datetime import datetime
import subprocess
import exiftool


def get_date_taken_mov(file_path):
    try:
        # 使用imageio获取MOV视频的拍摄日期
        with imageio.get_reader(file_path) as reader:
            meta_data = reader.get_meta_data()

            # 尝试获取拍摄日期信息
            if 'exif' in meta_data:
                exif_data = meta_data['exif']
                if 'DateTimeOriginal' in exif_data:
                    date_taken_str = str(exif_data['DateTimeOriginal'])
                    return datetime.strptime(date_taken_str, '%Y:%m:%d %H:%M:%S')
        
        return None
    except Exception as e:
        print(f"Error while getting date taken for {file_path}: {e}")
        return None

def get_date_taken(file_path):
    f = open(file_path, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)
    print(tags)
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print("Key: %s, value %s" % (tag, tags[tag]))
    # try:
    #     # 使用exifread获取照片的拍摄日期
    #     with open(file_path, 'rb') as file:
    #         tags = exifread.process_file(file)
    #         if 'EXIF DateTimeOriginal' in tags:
    #             date_taken_str = str(tags['EXIF DateTimeOriginal'])
    #             return datetime.strptime(date_taken_str, '%Y:%m:%d %H:%M:%S')
    #     return None
    # except Exception as e:
    #     print(f"Error while getting date taken for {file_path}: {e}")
    #     return None

def get_date_taken_heic(file_path):
    try:
        # 创建 ExifTool 实例
        with exiftool.ExifToolHelper() as et:
            # 使用 ExifTool 获取 HEIC 文件的拍摄时间
            metadata = et.get_metadata(file_path)
            for d in metadata:
                for k, v in d.items():
                    print(f"Dict: {k} = {v}")
            if date_taken_str:
                return datetime.strptime(date_taken_str, '%Y:%m:%d %H:%M:%S')
            else:
                return None
    except Exception as e:
        print(f"Error while getting date taken for {file_path}: {e}")
        return None
if __name__ == "__main__":
    # file_path = '/Volumes/Untitled/photo/IMG_9808.MOV'
    file_path = '/Volumes/Untitled/testphoto/IMG_3943.PNG'
    # file_path = '/Volumes/Untitled/photo/IMG_0230.HEIC'
    # if file file_extension is mov then call get_date_taken_mov
    # if file_path.lower().endswith(('.mov')):
    #     print(get_date_taken_mov(file_path))
    # elif file_path.lower().endswith(('.heic')):
    print(get_date_taken(file_path))
    # else:
    #     print(get_date_taken(file_path))