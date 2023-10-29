#!/usr/bin/env python3
import os

from PIL import Image

path = os.path.dirname(os.path.realpath(__file__))

def generate_smallvariants(resource):
    global path
    wallpapers_path = os.path.join(path, resource)
    clean(wallpapers_path)
    wallpapers = os.listdir(wallpapers_path)

    for wallpaper in wallpapers:
        # Append _small.jpg to the wallpaper
        wallpaper_small = os.path.splitext(wallpaper)[0] + "_small.jpg"
        wallpaper_small_path = os.path.join(wallpapers_path, wallpaper_small)

        # Save the wallpaper with 480x480px size to wallpaper_small_path
        with Image.open(os.path.join(wallpapers_path, wallpaper)) as img:
            img_small = img.crop((300, 960,780, 1440))
            img_small.save(wallpaper_small_path, "JPEG")

def clean(wallpapers_path):
    wallpapers = os.listdir(wallpapers_path)

    for wallpaper in wallpapers:
        # Get rid of existing small variants
        if wallpaper.endswith("_small.jpg"):
            os.remove(os.path.join(wallpapers_path, wallpaper))

generate_smallvariants("res/drawable-nodpi")
