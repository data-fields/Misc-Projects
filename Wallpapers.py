import ctypes
import random
import time

while True:
    paper = open("wallpapers.txt").read().splitlines()
    wallpaper = (random.choice(paper))
    print(wallpaper)
    ctypes.windll.user32.SystemParametersInfoW(20,
                                           0,
                                           wallpaper,
                                           0)
    time.sleep(30)