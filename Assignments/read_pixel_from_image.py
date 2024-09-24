from PIL import Image

# Load the image
img = Image.open('image.png')  # Replace with your image file

# Get the dimensions of the image
width, height = img.size
print(f"Image size: {width} x {height}")

# Read a specific pixel value (x, y)
x, y = 50, 50  # Replace with your coordinates
pixel_value = img.getpixel((x, y))

print(f"Pixel value at ({x}, {y}): {pixel_value}")

# Optionally, loop through all pixels
for y in range(height):
    for x in range(width):
        pixel = img.getpixel((x, y))
        # Do something with the pixel (for example, print it)
        print(f"Pixel value at ({x}, {y}): {pixel}")