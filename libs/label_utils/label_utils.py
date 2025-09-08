from PIL import Image, ImageDraw, ImageFont

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


