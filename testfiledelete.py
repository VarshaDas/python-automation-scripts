import os
import time

def delete_videos_with_prefix(folder_path, prefix):
    for filename in os.listdir(folder_path):
        if filename.startswith(prefix) and filename.endswith('.ica'):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f"Deleted: {filename}")

if __name__ == "__main__":
    folder_path = "/path/to/your/folder"  # Replace with the actual folder path
    video_prefix = "video_"  # Replace with your desired video prefix

    # Interval for daily execution in seconds (24 hours)
    interval_seconds = 24 * 60 * 60

    while True:
        delete_videos_with_prefix("", "WE")
        print("Waiting for the next execution...")
        time.sleep(interval_seconds)
