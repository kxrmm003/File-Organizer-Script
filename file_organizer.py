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
    'Others': []  # For unrecognized files
}

def organize_files(folder_path):
    """
    Organizes files in the given folder into subfolders based on file extensions.
    """
    if not os.path.exists(folder_path):
        print("❌ Folder path does not exist!")
        return

    # Loop through each file in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            # Get file extension
            _, ext = os.path.splitext(file_name)
            moved = False

            # Check which category the file belongs to
            for category, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    move_file(file_path, os.path.join(folder_path, category))
                    moved = True
                    break

            # If extension not found, move to 'Others'
            if not moved:
                move_file(file_path, os.path.join(folder_path, 'Others'))

    print("✅ Files organized successfully!")

def move_file(src_path, dest_folder):
    """
    Moves a file to the destination folder. Creates folder if it doesn't exist.
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # Create folder if not exists
    shutil.move(src_path, dest_folder)

# --------- Main Program ---------
if __name__ == "__main__":
    print("📁 File Organizer Script")
    user_folder = input("Enter the full path of the folder to organize: ")
    organize_files(user_folder)
