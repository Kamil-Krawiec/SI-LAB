from PIL import Image
import glob

# Specify the directory containing the PNG images
image_dir = './Charts/Models'

# Get a list of PNG files in the directory
image_files = sorted(glob.glob(f'{image_dir}/*.png'))

# Create a list to hold the image frames
frames = []

# Iterate over the image files and open each one
for image_file in image_files:
    image = Image.open(image_file)
    frames.append(image)

# Save the frames as a GIF animation
gif_path = 'Gifs/Modeling_animation_cross_mean_without_ba_si.gif'
frames[0].save(gif_path, format='GIF', append_images=frames[1:], save_all=True, duration=1000, loop=0)
