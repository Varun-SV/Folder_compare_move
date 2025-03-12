import os
import shutil

def move_missing_files(src, dest):
    """
    Move files not present in dest to dest from src.

    Args:
        src (str): Path to the source folder.
        dest (str): Path to the destination folder.
    """

    # Get the list of files in src and its subdirectories
    files_in_src = []
    for root, dirs, files in os.walk(src):
        for file in files:
            files_in_src.append(file)

    # Get the list of files in dest and its subdirectories
    files_in_dest = []
    for root, dirs, files in os.walk(dest):
        for file in files:
            files_in_dest.append(file)

    # Create the "Missed files" folder in dest if it doesn't exist
    missed_files_folder = os.path.join(dest, "Missed files")
    if not os.path.exists(missed_files_folder):
        os.makedirs(missed_files_folder)

    # Iterate over the files in src and its subdirectories
    for root, dirs, files in os.walk(src):
        for file in files:
            # Check if the file is not present in dest and its subdirectories
            if file not in files_in_dest:
            # Construct the full path to the file in src
                file_path_in_src = os.path.join(root, file)

                # Get the relative path from src to the current directory
                rel_path = os.path.relpath(root, src)

                # Construct the full path to the file in the "Missed files" folder
                if rel_path == ".":
                    file_path_in_dest = os.path.join(missed_files_folder, file)
                else:
                    file_path_in_dest = os.path.join(missed_files_folder, rel_path, file)

                # Create the subdirectory in the "Missed files" folder if it doesn't exist
                dest_dir = os.path.dirname(file_path_in_dest)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                # Move the file from src to the "Missed files" folder
                shutil.move(file_path_in_src, file_path_in_dest)
                print(f"Moved {file} from {root} to {dest_dir}")

# Example usage:
src = r"src_fldr"
dest = r"dest_fldr"
move_missing_files(src, dest)