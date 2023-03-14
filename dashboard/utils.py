from PIL import Image
import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def resize_image(image, width, height):
    img = Image.open(image)
    img = img.resize((width, height), Image.ANTIALIAS)
    output = BytesIO()
    img.save(output, format='JPEG', quality=100)
    output.seek(0)
    return InMemoryUploadedFile(output, 'ImageField', f'{image.name.split(".")[0]}_resized.jpg', 'image/jpeg', output.getbuffer().nbytes, None)