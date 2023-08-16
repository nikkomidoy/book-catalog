import math
import os.path

from django.core.exceptions import ValidationError


def get_cover_image_upload_path(instance, filename):
    return os.path.join("book_image", f"upload-{instance.id}")


def convert_size(size_bytes):
    """Convert a file size integer in bytes to a human-readable string"""
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def valid_image_format(image, acceptable_formats):
    from PIL import Image
    image = Image.open(image)
    return True if image.format in acceptable_formats else False


def valid_jpeg(value):
    if not valid_image_format(value, "JPEG"):

        raise ValidationError("Image must be a valid JPEG file.", params={'value':value})

def valid_png(value):
    if not valid_image_format(value, "PNG"):
        raise ValidationError("Image must be a valid PNG file.", params={'value':value})


def valid_jpeg_or_png(value):
    try:
        valid_jpeg(value)
    except ValidationError:
        valid_png(value)
