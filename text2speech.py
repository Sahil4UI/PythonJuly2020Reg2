from gtts import gTTS
import vlc
language='en'
data="avi is a good boy"

audio=gTTS(text=data,lang=language)
audio.save("data.mp3")
media=vlc.MediaPlayer("data.mp3")
media.play()
