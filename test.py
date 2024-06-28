from PIL import Image
import os


def resize(im,new_width):
    width,hight=im.size
    ratio=hight/width
    new_height =int (ratio*new_width)
    resized_image =im.resize((new_width,new_height))
    return resized_image


# Define the directory path
directory = "C:\\Users\\Administrator\\Desktop\\images"  

# Check if the directory exists
if not os.path.exists(directory):
    raise FileNotFoundError(f"The directory {directory} does not exist.")

files = os.listdir(directory)
# extensions = ['jpg', 'jpeg', 'png', 'gif', ]
extensions = ['jpg' ]

for file in files:
    ext = file.split(".")[-1].lower()
    if ext in extensions:
        im = Image.open(os.path.join(directory, file))
        im_resized = resize(im, 500)
        filepath = os.path.join(directory, f"/out/{os.path.splitext(file)[0]}.out.jpeg")
        im_resized.save(filepath)


example_image_path = os.path.join(directory, "image1.jpeg")
if os.path.exists(example_image_path):
    im = Image.open(example_image_path)
    im_resized = resize(im, 300)
    # im_resized.show()
    im_resized.save(filepath)
else:
    print(f"The file {example_image_path} does not exist. Skipping...")