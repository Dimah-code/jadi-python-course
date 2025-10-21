# Image Cropping Exercise — Python PIL

### Goal:

Learn how to work with images in Python using the **Pillow** library.
This exercise will teach you to:

* Open images from a given path
* Get image size and user input for cropping
* Crop an image using coordinates
* Preview the cropped image
* Optionally save the cropped image to disk

### Requirements

* Python 3.x
* Pillow library (`pip install pillow`)
* Basic understanding of functions, user input, and file paths

### Exercise Instructions

1. **Get an image path from the user**
   Use `input()` to ask for the file path.

2. **Open the image**

   ```python
   img = Image.open(path)
   ```

3. **Display image size**

   ```python
   print(img.size)
   ```

4. **Ask the user for crop coordinates**

   * `left`, `top`, `right`, `bottom`
     Make sure they are integers and within image dimensions.

5. **Crop the image**

   ```python
   cropped_img = img.crop((left, top, right, bottom))
   ```

6. **Show the cropped image**

   ```python
   cropped_img.show()
   ```

7. **Optionally save the image**

   * Ask the user if they want to save (`Y/N`)
   * Get folder path and filename from the user
   * Save using:

     ```python
     cropped_img.save(os.path.join(folder, filename))
     ```

8. **Handle errors gracefully**

   * File not found
   * Invalid input
   * Any unexpected exceptions


### Example Run

```sh
Enter photo path: example.jpg
Image size: (1920, 1080)
Crop data: 
Enter left pixel: 100
Enter top pixel: 100
Enter right pixel: 800
Enter bottom pixel: 600
Photo cropped! Details: (100, 100, 800, 600)
Do you want to save this photo? (Y/N): Y
Enter a path (folder) to save: ./cropped
Enter photo name (with extension, e.g., cropped.jpg): my_crop.jpg
Photo saved in ./cropped/my_crop.jpg
```


### Learning Points

* How to **open and manipulate images** with Pillow (`Image.open`, `.crop()`, `.show()`, `.save()`)
* How to **work with file paths** using the `os` module
* How to **get and validate user input**
* How to **handle exceptions** in Python for better error messages

