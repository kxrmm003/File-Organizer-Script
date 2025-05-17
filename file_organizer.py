# 📂 File Organizer Script
# Made by a beginner to learn automation using Python's os module

import os
import shutil

# Dictionary to map file extensions to folder names
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Others': []
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder path does not exist!")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file_name)
            moved = False

            for category, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    move_file(file_path, os.path.join(folder_path, category))
                    moved = True
                    break
                    
            if not moved:
                move_file(file_path, os.path.join(folder_path, 'Others'))

    print("✅ Files organized successfully!")

def move_file(src_path, dest_folder):
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    shutil.move(src_path, dest_folder)

# --------- Main Program ---------
if __name__ == "__main__":
    print("📁 File Organizer Script")
    user_folder = input("Enter the full path of the folder to organize: ")
    organize_files(user_folder)
