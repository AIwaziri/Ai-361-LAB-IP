# Task 1: Dynamic Color Modification

from skimage import io, img_as_float, img_as_ubyte
import numpy as np

def adjust_color(img, red_adjust, green_adjust, blue_adjust):
    # Ensuring the image is a float type for calculations
    img = img_as_float(img)

    # Adding adjustments to R, G, and B channels
    img[:, :, 0] = np.clip(img[:, :, 0] + (blue_adjust / 255.0), 0, 1)  # Blue
    img[:, :, 1] = np.clip(img[:, :, 1] + (green_adjust / 255.0), 0, 1)  # Green
    img[:, :, 2] = np.clip(img[:, :, 2] + (red_adjust / 255.0), 0, 1)  # Red

    return img

def invert_colors(img):
    """Inverting the colors of an image."""
    return 1.0 - img  # Inversion for float images

def apply_brightness(img, scale):
    """Scaling the brightness of the image."""
    return np.clip(img * scale, 0, 1)

def report(red_adjust, green_adjust, blue_adjust, invert_colors_option, brightness_scale):
    """Printing user inputs and processing steps."""
    print("\n--- Reports ---")
    print(f"Color Channel Adjustments: R:{red_adjust}, G:{green_adjust}, B:{blue_adjust}")
    print(f"Invert Colors: {'Yes' if invert_colors_option else 'No'}")
    print(f"Brightness Scaling Factor: {brightness_scale}")
    print("Steps Performed:")
    print("1. Adjusted RGB channel intensities.")
    if invert_colors_option:
        print("2. Inverted image colors.")
    print("3. Applied brightness scaling.")
    print("4. Saved the modified image as 'task1_output.png'.")

def main():
    # Step 1: Input Parameters
    img_path = input("Enter the image path (e.g., image1.png): ")
    red_adjust = int(input("Enter red channel adjustment (e.g., +50): "))
    green_adjust = int(input("Enter green channel adjustment (e.g., -30): "))
    blue_adjust = int(input("Enter blue channel adjustment (e.g., 0): "))
    invert_colors_option = input("Invert colors? (Yes/No): ").strip().lower() == "yes"
    brightness_scale = float(input("Enter brightness scaling factor (e.g., 1.0 to 2.0): "))

    # Step 2: Loading the Image
    try:
        img = io.imread(img_path)
    except FileNotFoundError:
        print("Error: Image not found. Check the file path.")
        return

    # Step 3: Converting to Float for Processing
    img = img_as_float(img)

    # Step 4: Processing
    # 4a. Adjusting Color Channels
    mod_img = adjust_color(img, red_adjust, green_adjust, blue_adjust)

    # 4b. Inverting Colors (if selected)
    if invert_colors_option:
        mod_img = invert_colors(mod_img)

    # 4c. Applying Brightness Scaling
    mod_img = apply_brightness(mod_img, brightness_scale)

    # Step 5: Saving the Modified Image
    output_img_path = "task1_output.png"
    io.imsave(output_img_path, img_as_ubyte(mod_img))
    print(f"Modified image saved as '{output_img_path}'.")

    # Step 6: Printing the Report
    report(red_adjust, green_adjust, blue_adjust, invert_colors_option, brightness_scale)

if __name__ == "__main__":
    main()