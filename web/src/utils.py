import os
import time


def delete_old_files(upload_folder_location):
    """Deletes files in the upload folder that are older than a specified number of days."""

    upload_folder = upload_folder_location
    days_to_keep = 30

    for file in os.listdir(upload_folder):
        file_path = os.path.join(upload_folder, file)
        if time.time() - os.stat(file_path).mtime > days_to_keep * 24 * 3600:
            os.remove(file_path)
