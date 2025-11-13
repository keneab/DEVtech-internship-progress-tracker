import os
import shutil

# Path to the folder you want to organize
folder_path = input("Enter the path of the folder you want to organize: ")

# Define folder categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Others": []
}

# Create subfolders if they don't exist
for folder_name in file_types.keys():
    folder = os.path.join(folder_path, folder_name)
    if not os.path.exists(folder):
        os.mkdir(folder)

# Go through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    moved = False
    for folder_name, extensions in file_types.items():
        for ext in extensions:
            if filename.lower().endswith(ext):
                shutil.move(file_path, os.path.join(folder_path, folder_name, filename))
                print(f"Moved: {filename} → {folder_name}")
                moved = True
                break
        if moved:
            break

    # If file type not found, move to "Others"
    if not moved:
        shutil.move(file_path, os.path.join(folder_path, "Others", filename))
        print(f"Moved: {filename} → Others")

print("\n✅ Files organized successfully!")
