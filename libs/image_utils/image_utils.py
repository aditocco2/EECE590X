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

def svg2png(input_filename, output_filename):
    """
    Uses inkscape as a backend, requires it in PATH :/
    """
    subprocess.run(["inkscape", 
                    '--export-type=png',
                    f"--export-filename={output_filename}",
                    input_filename])
    os.remove(input_filename)
