"""
pytcha is a tool for generating different styles of captcha images for Flask Projects
or other python web applications
"""
import string
import random

import rstr
from PIL import Image, ImageDraw, ImageFont


class Generate:

    def __init__(self):
        pass

    " get a captcha with just number (set Minimum Size and Max size)"

    @staticmethod
    def captcha_numbers(min_size, max_size):
        numbers = string.digits
        random_string = rstr.rstr(numbers, min_size, max_size)
        img = Image.new('RGB', (90, 30), color=(73, 109, 137))
        d_img = ImageDraw.Draw(img)
        d_img.text((10, 10), random_string, fill=(255, 255, 0))
        img.save('captcha.png')
        print(random_string)
        return random_string

    # Only Lower and Uppercase Letters (set min/max chars)
    @staticmethod
    def captcha_letters(min_size, max_size):
        letters = string.ascii_uppercase
        lower_letters = string.ascii_lowercase
        random_string = rstr.rstr(lower_letters + letters, min_size, max_size)
        # random_string = ''.join((random.choice(chars) for i in range(6)))
        img = Image.new('RGB', (95, 40), color=(73, 109, 137))
        d_img = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("FreeMono.ttf", 16)
        d_img.text((10, 10), random_string, font=fnt, fill=(255, 255, 0))
        img.save('captcha.png')
        return random_string

    # lower/ uppercase letters + numbers (set min/max chars)
    @staticmethod
    def captcha_mix(min_size, max_size):
        letters = string.ascii_uppercase
        lower_letters = string.ascii_lowercase
        numbers = string.digits
        # not included but can be added on line 51 for special characters
        special_char = string.punctuation
        octdigits = string.octdigits
        random_string = rstr.rstr(lower_letters + letters + numbers + octdigits, min_size, max_size)
        img = Image.new('RGB', (95, 40), color=(73, 109, 137))
        d_img = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("FreeMono.ttf", 16)
        d_img.text((10, 10), random_string, font=fnt, fill=(255, 255, 0))
        img.save('captcha.png')
        print(random_string)
        return random_string

