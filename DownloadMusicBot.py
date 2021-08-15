import telebot
import os
import youtube_dl
bot = telebot.TeleBot('1822190412:AAFIRqRWy34m0ImdDyVsnrBG2baDDbBhKts')

def download_mp3(video_url): 
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = 'C:/Users/Rostyck/Desktop/m/'+f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    return filename


def send_audio(message,link):
    filename=download_mp3(link)
    file=open(filename,'rb')
    bot.send_audio(message.chat.id,file,timeout=60)
    print(filename)
    os.remove(filename)
    


@bot.message_handler(content_types=['text'])
def start_command(message):
    link=message.text
    if 'https://www.youtube.com/watch' in link  or 'https://youtu.be' in link:
        send_audio(message,link)
    else:
        bot.send_message(message.chat.id,'Ой, це не посилання з ютубу(')

print('Success')
bot.polling()
