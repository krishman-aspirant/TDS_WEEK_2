# from PIL import Image
# import os

# # Open the image
# img = Image.open("input_image.png")

# # Convert to a mode that is efficient for PNG/WebP
# # (For icons or simple images, use 'P' (palette) mode if applicable)
# img = img.convert("P", palette=Image.ADAPTIVE)

# # Save as optimized PNG
# img.save("compressed_image.png", optimize=True)

# # Alternatively, save as WebP in lossless mode
# img.save("compressed_image.webp", lossless=True, optimize=True)

# # Check the file size
# size = os.path.getsize("compressed_image.webp")
# print(f"Compressed file size: {size} bytes")
# ---------------------------------------------------------------------------------

# from PIL import Image
# import os


from PIL import Image

img = Image.open("input_image.png")

img.save("output.png", optimize=True, lossless=True)


img.save("output.webp",format="WEBP")