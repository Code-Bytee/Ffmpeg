import os
import requests


url = 'https://pt01001.cdntrex.com/remote_control.php?time=1685951554&cv=5238fee3ead285ee0e0e59b458c44a71&lr=0&cv2=64a100c1bb0d5919fcdcad4626756bc1&file=%2F2277000%2F2277506%2F2277506_1080p.mp4&cv3=693e15b43e131045e0ebfb940709ed60&cv4=ded06edc116baa4fd6762c9d75e720bc'


os.system("curl --output tmp.mp4 "+url)
os.system("ffmpeg -i tmp.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
os.system("ffmpeg -y -i './vid/clip.mp4' -c:v libx265 -q:v 5 -c:a aac -a b 128k -ar 44100 './vid/final.mp4'")

#os.system("ffmpeg -y -i 'tmp.mp4' -c:v libx265 -q:v 5 -c:a aac -ab 128k -ar 44100 'final.mp4'")
#os.system("ffmpeg -i final.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
