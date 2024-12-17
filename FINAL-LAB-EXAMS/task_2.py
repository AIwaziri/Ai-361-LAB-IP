from skimage import io, img_as_float, img_as_ubyte
from skimage.filters import gaussian
import numpy as np


def apply_blur(region):
    """Applying the Gaussian blur to the selected  region."""
    # Handle multi-channel image by applying Gaussian blur to each channel individually
    if region.ndim == 3:  # Multi-channel (e.g., RGB)
        blurred_region = np.zeros_like(region)
        for i in range(region.shape[2]):  # Iterating over channels
            blurred_region[:, :, i] = gaussian(region[:, :, i], sigma=2)
        return blurred_region
    else:  # Single-channel (grayscale)
        return gaussian(region, sigma=2)


def apply_sharpen(region):
    """Applying sharpening kernel to the selected region."""
    # Sharpening kernel
    sharpening_kernel = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])
    from scipy.ndimage import convolve
    sharpened_region = np.zeros_like(region)
    for i in range(region.shape[2]):  # Applying on each channel
        sharpened_region[:, :, i] = convolve(region[:, :, i], sharpening_kernel)
    return np.clip(sharpened_region, 0, 1)


def blend_regions(original, enhanced, transparency):
    """Blending the enhanced region with the original using transparency."""
    return (transparency * enhanced) + ((1 - transparency) * original)


def report(coords, enhancement, transparency):
    """Printing user inputs and processing steps."""
    print("\n--- Report ---")
    print(f"Region Coordinates: Top-left ({coords[0]}, {coords[1]}), Width: {coords[2]}, Height: {coords[3]}")
    print(f"Enhancement Type: {enhancement}")
    print(f"Transparency Level: {transparency}")
    print("Steps Performed:")
    print("1. Extracted the user-defined region.")
    print(f"2. Applied '{enhancement}' enhancement.")
    print("3. Blended the processed region back into the original image with transparency.")
    print("4. Saved the processed image as 'task2_output.png'.")


def main():
    # Step 1: Input Parameters
    image_path = input("Enter the image path (e.g., image2.png): ")
    x = int(input("Enter top-left x coordinate: "))
    y = int(input("Enter top-left y coordinate: "))
    width = int(input("Enter width of the region: "))
    height = int(input("Enter height of the region: "))
    enhancement = input("Enter enhancement type (Blur/Sharpen): ").strip().lower()
    transparency = float(input("Enter transparency level (e.g., 0.5): "))

    # Step 2: Loading the Image
    try:
        image = io.imread(image_path)
    except FileNotFoundError:
        print("Error: Image not found. Check the file path.")
        return

    # Ensuring that the  image is in float format for processing
    image = img_as_float(image)

    # Step 3: Extracting the Region
    region = image[y:y + height, x:x + width].copy()

    # Step 4: Applying Enhancement
    if enhancement == "blur":
        processed_region = apply_blur(region)
    elif enhancement == "sharpen":
        processed_region = apply_sharpen(region)
    else:
        print("Error: Invalid enhancement type. Choose 'Blur' or 'Sharpen'.")
        return

    # Step 5: Blending the Processed Region with the Original Image
    blended_region = blend_regions(region, processed_region, transparency)
    image[y:y + height, x:x + width] = blended_region

    # Step 6: Saving the Processed Image
    output_path = "task2_output.png"
    io.imsave(output_path, img_as_ubyte(image))
    print(f"Processed image saved as '{output_path}'.")

    # Step 7: Printing the Report
    report((x, y, width, height), enhancement.capitalize(), transparency)


if __name__ == "__main__":
    main()
