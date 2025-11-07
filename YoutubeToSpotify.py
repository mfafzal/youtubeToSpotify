from yt_dlp import *
from pydub import *
from ffmpeg import *
import os

def Converstion():
    url = input("Please enter the url of the youtube video you want to send: ")
    name = input("Please enter the name of the song: ")
    fileName= name+".mp3"
    os.system(f'yt-dlp --extract-audio --audio-format mp3 --output "{fileName}" "{url}"')
    
'''
    # Step 2: load the audio in Python
    audio = AudioSegment.from_file("output.mp3", format="mp3")

    https://www.youtube.com/watch?v=Qr_QLv1TPcY
'''

Converstion()