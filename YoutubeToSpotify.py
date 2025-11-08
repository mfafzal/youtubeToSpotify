from yt_dlp import *
from pydub import *
from ffmpeg import *
import shutil
import os

def Converstion():
    '''
    Purpose: This function will prompt you for the url, download the audio of the video, and then put it into the proper folder.
    '''
    url = input("Please enter the url of the youtube video you want to send: ")
    name = input("Please enter the name of the song: ")
    fileName= name+".mp3"
    os.system(f'yt-dlp --extract-audio --audio-format mp3 --output "{fileName}" "{url}"')
    cwd = os.getcwd()
    currentPath = cwd+"\\"+fileName
    destination = "C:\\Users\\Fahad\\Documents\\music"  #Change this to the path of the folder you have designated spotify to pull music from
    shutil.move(currentPath, destination)

def Email():
    '''
    this function is to email yourself the mp3 file so that you can download it on your phone and be able to play the song on your phone also
    '''


Converstion()