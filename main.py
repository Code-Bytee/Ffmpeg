import os
import requests

url = 'https://vdownload-42.sb-cd.com/1/3/13187491-1080p.mp4?secure=N8IEJKwXcrBZH2kH2f4Wng,1685967500&m=42&d=1&_tid=13187491&name=She_reminds_me_of_Dani_Daniels-pussyspace.com.mp4'

os.system("curl --output tmp.mp4 "+url)
os.system("ffmpeg -i tmp.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
os.system("ffmpeg -y -i './vid/clip.mp4' -c:v libx265 -q:v 5 -c:a aac -a b 128k -ar 44100 './vid/final.mp4'")

#os.system("ffmpeg -y -i 'tmp.mp4' -c:v libx265 -q:v 5 -c:a aac -ab 128k -ar 44100 'final.mp4'")
#os.system("ffmpeg -i final.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
