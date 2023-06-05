import os
import requests

url = 'https://pt00202.cdntrex.com/remote_control.php?time=1685972610&cv=157fbef506bbd5de6e6fa5f407421296&lr=0&cv2=bf0a0c01e19d6273f6ec924b198ea012&file=%2F1171000%2F1171751%2F1171751_1080p.mp4&cv3=693e15b43e131045e0ebfb940709ed60&cv4=359be8ad4abbe03e1019712efcfa0449'

with open('tmp.mp4','wb') as f:
  f.write(requests.get(url).content)
#os.system("curl --output tmp.mp4 "+url)
#os.system("ffmpeg -i tmp.mp4 -ss 1:30 -t 30 clp.mp4")
os.system("ffmpeg -y -i 'tmp.mp4' -c:v libx265 'final.mp4'")
os.system("mv final.mp4 ./vid/")

#os.system("ffmpeg -y -i 'tmp.mp4' -c:v libx265 -q:v 5 -c:a aac -ab 128k -ar 44100 'final.mp4'")
#os.system("ffmpeg -i final.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
