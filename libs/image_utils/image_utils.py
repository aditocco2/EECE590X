from PIL import Image, ImageDraw, ImageFont
import os
import subprocess

def apply_labels(input_filename, output_filename, labels, coords, font_size=25, color="black"):

    """
    Function to more easily put labels on an image in mass. Uses PIL
    Arguments:
    input_filename
    output_filename
    labels: list of strings to write
    coords: list of tuples of (X, Y) coordinates, where top left is (0, 0)
    font_size: default 25
    color: default "black"
    """

    pic = Image.open(input_filename)
    drawer = ImageDraw.Draw(pic)
    font = ImageFont.truetype("calibri.ttf", font_size)
    image_copy_name = output_filename

    for label, coord in zip(labels, coords):
        # Draw centered
        drawer.text(coord, label, anchor="mm", font=font, fill=color)
    
    pic.save(output_filename)

def paste_images(input_filename, output_filename, images, coords, scale = 1):
    """
    Function to more easily paste smaller images on a bigger one in mass. Uses PIL
    Arguments:
    input_filename
    output_filename
    images: list of filenames of smaller images (can also just use 1 string)
    coords: list of tuples of (X, Y) coordinates, where top left is (0, 0). These
    will be the MIDDLE coordinates of where the small images go
    scale (int): Scale to resize the small image, default 1
    """

    # If a string is passed in, just duplicate it into a list
    if isinstance(images, str):
        images = [images for _ in range(len(coords))]

    bg = Image.open(input_filename)

    for image, coord in zip(images, coords):
        small = Image.open(image)

        # Scale up/down if needed
        if scale != 1:
            scale_w = int(scale * small.width)
            scale_h = int(scale * small.height)
            small = small.resize((scale_w, scale_h), Image.Resampling.NEAREST)

        # Derive top left coords from middle coords and small image size
        left_x = coord[0] - (small.width // 2)
        top_y = coord[1] - (small.height // 2)
        new_coord = (left_x, top_y)

        # Paste with transparency
        small = Image.alpha_composite(Image.new("RGBA", small.size), small.convert('RGBA'))
        bg.paste(small, new_coord, small)

    bg.save(output_filename)

def svg2png(input_filename, output_filename):
    """
    Uses inkscape as a backend, requires it in PATH :/
    """

    print(f"Converting {input_filename} to {output_filename}...", end=" ")

    subprocess.run(["inkscape", 
                    '--export-type=png',
                    f"--export-filename={output_filename}",
                    input_filename])
    os.remove(input_filename)
    
    print("Done")
