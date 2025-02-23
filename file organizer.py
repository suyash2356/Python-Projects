import os
import shutil

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css", ".php", ".rb"],
    "Others": []  # Catch-all category for unknown file types
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    
    # Create category folders if they don’t exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Move files into their respective folders
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, category, file))
                    moved = True
                    break
            
            # If no category matched, move to 'Others'
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", file))
    
    print("Files have been organized successfully.")

if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ")
    organize_files(target_directory)
