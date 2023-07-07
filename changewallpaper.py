import os
import random
import ctypes

# Path to the folder containing the images
image_folder = "F:\图库\B 美术库\壁纸"

def set_wallpaper(image_path):
    # Change the desktop wallpaper using Windows API
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def select_random_image(folder_path):# Get a list of all image files in the folder
    image_files = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.bmp')) and file != "special.png"]
    if not image_files: #random list is fault
        print("No image files found in the folder.")
        return None
    # Select a random image from the list
    random_image = random.choice(image_files)
    # Return the full path to the selected image
    return os.path.join(folder_path, random_image)

# Select a random image from the folder
random_image_path = select_random_image(image_folder)
print(random_image_path)
if random_image_path:
    # Set the selected image as the desktop wallpaper
    set_wallpaper(random_image_path)