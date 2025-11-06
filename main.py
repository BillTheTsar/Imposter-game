from PIL import Image
import numpy as np


def subtract_images(p1_path, p2_path, mode="clip"):
    """
    Subtracts image2 from image1 and shows the result.

    mode:
      - "clip": clip negative values to 0
      - "abs": take absolute value of the difference
    """
    # Load images
    img1 = Image.open(p1_path).convert("RGB")
    img2 = Image.open(p2_path).convert("RGB")

    # Ensure same size
    if img1.size != img2.size:
        raise ValueError("Images must have the same resolution")

    # Convert to NumPy arrays
    arr1 = np.array(img1, dtype=np.int16)  # use larger dtype to avoid overflow
    arr2 = np.array(img2, dtype=np.int16)

    # Subtract
    diff = arr1 - arr2

    # Handle negative values
    if mode == "clip":
        diff = np.clip(diff, 0, 255)
    elif mode == "abs":
        diff = np.abs(diff)
    else:
        raise ValueError("mode must be 'clip' or 'abs'")

    # Convert back to uint8 image
    diff_img = Image.fromarray(diff.astype(np.uint8))

    diff_img.show()  # Opens in default viewer
    return diff_img

# Example usage
subtract_images("E:/AI/Badminton Landing Project/Playing images all angles/3_frames/00120.jpg",
                "E:/AI/Badminton Landing Project/Playing images all angles/3_frames/00119.jpg", mode="abs")
