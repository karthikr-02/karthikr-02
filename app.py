

import os

def find_missing_images(directory, prefix, extension, start, end):
    """
    Finds missing images in an image sequence.

    Parameters:
    directory (str): The directory containing the images.
    prefix (str): The prefix of the image filenames (e.g., "image_").
    extension (str): The extension of the image files (e.g., ".png").
    start (int): The starting number of the sequence.
    end (int): The ending number of the sequence.

    Returns:
    list: A list of missing image filenames.
    """
    # Generate the expected filenames
    expected_files = [
        "{}{:04d}{}".format(prefix, i, extension) for i in range(start, end + 1)
    ]

    # List all files in the directory
    actual_files = set(os.listdir(directory))

    # Find the missing files
    missing_files = [
        file for file in expected_files if file not in actual_files
    ]

    return missing_files

# Usage
directory = r'C:\Users\karth\Downloads\hcw_mmtest_wide\MM_Test_Wide'

prefix = "hcw_mmtest_wide."
extension = ".png"
start, end = 0, 214  # Range of the sequence

missing_images = find_missing_images(directory, prefix, extension, start, end)
if missing_images:
    print("Missing images:")
    print("\n".join(missing_images))
else:
    print("No missing images.")
