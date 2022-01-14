"""
pytcha is a tool for generating different styles of captcha images for Flask Projects
or other python web applications
"""
import string

from PIL import Image, ImageDraw, ImageFont
import random


class Generate:

    def __init__(self):
        get_number = None
        size = None

    " get a captcha with just number "

    @staticmethod
    def captcha_numbers(size):
        get_number = str(random.randrange(1000, 99999, size))
        img = Image.new('RGB', (90, 30), color=(73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10, 10), get_number, fill=(255, 255, 0))
        img.save('captcha.png')
        print(get_number)
        return get_number

    " get a 6 character captcha with letters, lower and upper case + numbers "

    @staticmethod
    def captcha_combo(chars=string.ascii_uppercase + string.digits):
        result_str = ''.join((random.choice(chars) for i in range(6)))
        img = Image.new('RGB', (95, 40), color=(73, 109, 137))
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("FreeMono.ttf", 16)
        d.text((10, 10), result_str, font=fnt, fill=(255, 255, 0))
        img.save('captcha.png')
        print(str(result_str))


if __name__ == "__main__":
    get = Generate()
    get.captcha_combo()
