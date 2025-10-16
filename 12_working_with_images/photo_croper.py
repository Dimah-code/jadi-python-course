import os

from PIL import Image


def get_path():
    return input("Enter photo path: ")


def get_box(img):
    print(f"Image size: {img.size}")

    print("Crop data: ")
    left = int(input("Enter left pixel: "))
    top = int(input("Enter top pixel: "))
    right = int(input("Enter right pixel: "))
    bottom = int(input("Enter bottom pixel: "))

    box = (left, top, right, bottom)
    fixed = img.crop(box)
    print(f"Photo cropped! Details: {box}")

    fixed.show()
    to_save(fixed)


def to_save(photo):
    save = input("Do you want to save this photo? (Y/N): ")

    if save.lower() == "y":
        folder = input("Enter a path (folder) to save: ").strip()
        photo_name = input(
            "Enter photo name (with extension, e.g., cropped.jpg): "
        ).strip()

        fp = os.path.join(folder, photo_name)

        try:
            photo.save(fp)
            print(f"Photo saved in {fp}")
        except Exception as e:
            print(f"Error saving photo: {e}")

        return True
    else:
        print("Photo not saved.")
        return False


if __name__ == "__main__":
    path = get_path()
    try:
        img = Image.open(path)
        get_box(img)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")
