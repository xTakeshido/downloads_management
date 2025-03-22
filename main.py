import os
import shutil
from PIL import Image

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.img_dir = os.path.join(directory, "img")
        self.exe_dir = os.path.join(directory, "executable")
        
        # Create target directories if they don't exist
        os.makedirs(self.img_dir, exist_ok=True)
        os.makedirs(self.exe_dir, exist_ok=True)

    def organize_files(self):
        """Move files to appropriate folders"""
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            
            if os.path.isfile(file_path):
                # Move images
                if self._is_valid_image(file_path):
                    self._move_file(file_path, self.img_dir)
                # Move executables
                elif filename.lower().endswith('.exe'):
                    self._move_file(file_path, self.exe_dir)

    def _is_valid_image(self, file_path):
        """Verify if file is actually an image"""
        try:
            with Image.open(file_path) as img:
                img.verify()
                return True
        except (IOError, SyntaxError, Image.UnidentifiedImageError):
            return False

    def _move_file(self, src_path, dest_dir):
        """Move a file to destination directory"""
        try:
            shutil.move(src_path, dest_dir)
            print(f"Moved {os.path.basename(src_path)} to {dest_dir}")
        except Exception as e:
            print(f"Error moving {os.path.basename(src_path)}: {str(e)}")

# Usage
if __name__ == "__main__":
    download_dir = "your_download_directory"
    organizer = FileOrganizer(download_dir)
    organizer.organize_files()