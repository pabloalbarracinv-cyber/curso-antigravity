from PIL import Image

# Load the user uploaded image
img_path = r'C:\Users\1331\.gemini\antigravity\brain\f64ebb47-1ae0-45f9-9643-1cb5aff25720\.user_uploaded\media_1789602697301.jpg'
img = Image.open(img_path)

# Get dimensions
width, height = img.size

# The image is a full hero section. Let's crop the right 60% of the image.
# We will keep the top and bottom as is.
left = int(width * 0.35)
top = 0
right = width
bottom = height

cropped_img = img.crop((left, top, right, bottom))
cropped_img.save(r'C:\Users\1331\Documents\CURSO_ANTIGRAVITY\assets\hero_art.jpg', quality=95)
print(f'Cropped and saved to assets/hero_art.jpg. Original size: {width}x{height}, Cropped size: {cropped_img.size}')
