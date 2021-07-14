from gtts import gTTS
# pip install gTTs
from playsound import playsound

# pip install playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text=input("Input your text here : "),
          lang=language, slow=False)
sp.save(audio)
playsound(audio)
