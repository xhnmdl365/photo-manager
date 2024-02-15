import os
import csv

def find_differences(folder_a, folder_b, output_csv):
    files_a = set(filename.lower() for filename in os.listdir(folder_a) if not filename.startswith('._'))
    files_b = set(filename.lower() for filename in os.listdir(folder_b) if not filename.startswith('._'))

    only_in_a = files_a - files_b
    only_in_b = files_b - files_a

    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['file_name', 'folder']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for filename in only_in_a:
            writer.writerow({'file_name': filename, 'folder': 'A'})

        for filename in only_in_b:
            writer.writerow({'file_name': filename, 'folder': 'B'})

# 输入文件夹路径和输出CSV文件路径
folder_a = '/Volumes/Qing/iphone photos and videos/'
folder_b = '/Volumes/Untitled/photo/'
output_csv = 'differences.csv'

find_differences(folder_a, folder_b, output_csv)
