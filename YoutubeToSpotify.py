from yt_dlp import *
from pydub import *
from ffmpeg import *
import shutil
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url = input("Please enter the url of the youtube video you want to send: ")
name = input("Please enter the name of the song: ")
fileName= name+".mp3"

def Converstion():
    '''
    Purpose: This function will prompt you for the url, download the audio of the video, and then put it into the proper folder.
    Parameters: None
    Returns: The path to the audio file just downloaded.
    '''
    os.system(f'yt-dlp --extract-audio --audio-format mp3 --output "{fileName}" "{url}"')
    cwd = os.getcwd()
    currentPath = cwd+"\\"+fileName
    destination = "C:\\Users\\<YourUsername>\\Documents\\music"  #Change this to the path of the folder you have designated spotify to pull music from
    shutil.move(currentPath, destination)
    return destination
   
def send_email(subject, body, sender, name, password, path):
    '''
    Purpose: This will send an email with the audio file attached to yourself so you can download it on your phone. If not needed delete bottom line
    Parameters: content of the subject line of email, content of the body of the email, sender email, name of the song, gmail app password, path to pull audio file from
    Returns: Nothing
    '''
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = sender  #recipient name here

    path = path+"\\"+name
    # Attach the body of the email
    msg.attach(MIMEText(body))

    with open(path, "rb") as attachment:
    # Add the attachment to the message
        part = MIMEBase("audio", "mpeg")  # Explicitly state this is a mp3 file
        part.set_payload(attachment.read())  # Read the file content
    encoders.encode_base64(part)  # Encode the attachment in base64
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {name}",
    )

    msg.attach(part)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, sender, msg.as_string())
    print("Message sent!")


destination = Converstion()

sender = "DummyEmail@gmail.com"
appPassword = "Insert gmail app password here"
send_email("New local music added to spotify", "This song was added to your spotify local music", sender, fileName, appPassword, destination)
