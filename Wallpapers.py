import ctypes
import random
import time

while True:
    image = open("wallpapers.txt").read().splitlines()
    wallpaper = (random.choice(image))
    ctypes.windll.user32.SystemParametersInfoW(20,
                                           0,
                                           wallpaper,
                                           0)
    time.sleep(30)
    
