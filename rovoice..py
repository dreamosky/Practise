from gtts import gTTS
tts = gTTS(text = 'hello, I love you')
tts.save("rovoice.mp3")
from pygame import mixer
mixer.init()
mixer.music.load('rovoice.mp3')
mixer.music.play()
import tempfile
def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text='sentence')
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()
speak("i love you so much")