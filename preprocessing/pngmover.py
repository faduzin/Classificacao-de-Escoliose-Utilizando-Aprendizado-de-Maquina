import os

main_folder_path = r'E:\Baropodometer_forces'
output_dir = r'E:\all images'

for root, dirs, files in os.walk(main_folder_path, topdown=False):
    for filename in files:
        image_path = os.path.join(root, filename)
        if filename.endswith('.png'):
            output_path = f"{output_dir}\{filename}"
            os.rename(image_path, output_path)