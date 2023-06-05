import os
import requests

url = 'https://vdownload-33.sb-cd.com/1/0/10448931-1080p.mp4?secure=Knb7OMx4w6tcZXwOCNqtGw,1685971528&m=33&d=5&_tid=10448931&name=Dani_Daniels_Seduces_Cameraman_in_Hotel_Fuckfest-pussyspace.com.mp4'

with open('tmp.mp4','wb') as f:
  f.write(requests.get(url).content)
os.system("curl --output tmp.mp4 "+url)
os.system("ffmpeg -i tmp.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
os.system("ffmpeg -y -i './vid/clip.mp4' -c:v libx265 -q:v 5 -c:a aac -a b 128k -ar 44100 './vid/final.mp4'")

#os.system("ffmpeg -y -i 'tmp.mp4' -c:v libx265 -q:v 5 -c:a aac -ab 128k -ar 44100 'final.mp4'")
#os.system("ffmpeg -i final.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
