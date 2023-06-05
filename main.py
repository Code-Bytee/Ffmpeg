import os
import requests

url = 'https://srv.badasserver3.com/download?data=xyJzMz3ZmdBUJo5spb262dgGJC3EbDaDbC%2FmLZl3xWukgDSjGPHNhr5cX3Kt%2FTgpBPHUDfqvx34ez92cpXq0in4KSu%2Fh0uTfBYqjY0f%2FMnupfqE1Xoy%2FeCO4d71xzjo0SxdDKopTarqZOrGZ3gqN19jsTs5HgKMg3buhjJMEstzYeQLyiSEBIJk4QukStFlBUl6fEKrrqnjVrzUA2YBPEsf4s4xdyPlu3XA1ZZNtTdVJg%2FTgNzKoxqEqKBlD5kZ%2FiFzskY%2FgKvgOut7x3hZaW7ZC8zyvJmTo80ZeKOVIbVdYvXxvohC7rCyq%2FDycu3PKskbeAqhl6ZYJYQFZ%2BQH8OPhwr70QdnCLCDO5n%2Ftkjyd7Tfm8dzXI200KOk8ysyvuaug8l27UC%2FwkCuaeEQEimysT%2FDrjwzWaBqoiCP%2FAJ6uDkvQn%2FEt6fmp%2BOkfW%2BxBNQo%2FVobW%2FCF4VES6IZcL6Gw%3D%3D'                                                                 
os.system("curl --output tmp.mp4 "+url)
os.system("ffmpeg -i tmp.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
os.system("ffmpeg -y -i './vid/clip.mp4' -c:v libx265 -q:v 5 -c:a aac -a b 128k -ar 44100 './vid/final.mp4'")

#os.system("ffmpeg -y -i 'tmp.mp4' -c:v libx265 -q:v 5 -c:a aac -ab 128k -ar 44100 'final.mp4'")
#os.system("ffmpeg -i final.mp4 -ss 1:30 -t 30 ./vid/clip.mp4")
