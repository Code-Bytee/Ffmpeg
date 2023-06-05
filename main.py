import os

import requests

url = 'https://cdn77-vid-mp4.xvideos-cdn.com/UQx9wQUinuxzckBikF6jvA==,1685958131/videos/mp4/f/2/f/xvideos.com_f2f8d4e50c7c02b19587ae8b0e56d647.mp4?ui=MTg1LjEwMS4yMC4xMTMtL3ZpZGVvNzY1MjQ3NjUveW91bmdfcmVkaGVhZF9j&download=1'

os.system("curl --output tmp.mp4 "+url)

os.system("ffmpeg -y -i 'tmp.mp4' -c:v libx265 -q:v 5 -c:a aac -ab 128k -ar 44100 'final.mp4'")

os.system("ffmpeg -i final.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
