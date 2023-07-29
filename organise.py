import os
import shutil

def organize_downloads_folder(folder_path):
    # Get the list of files in the Downloads folder
    files = os.listdir(folder_path)

    # Create a dictionary to map file extensions to folder names
    extension_to_folder = {
        ".txt": "TextFiles",
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".png": "Images",
        ".mp3": "Music",
        ".mp4": "Videos",
        # Add more extensions and corresponding folder names as needed
    }

    for filename in files:
        file_ext = os.path.splitext(filename)[1]
        if file_ext in extension_to_folder:
            # Create the destination folder if it doesn't exist
            dest_folder = os.path.join(folder_path, extension_to_folder[file_ext])
            os.makedirs(dest_folder, exist_ok=True)

            # Move the file to the destination folder
            src_path = os.path.join(folder_path, filename)
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved '{filename}' to '{dest_folder}'")

if __name__ == "__main__":
    # Replace with the path to your Downloads folder
    downloads_folder = "/Users/vd056735/Downloads"

    organize_downloads_folder(downloads_folder)
