from gtts import gTTS
from pygame import mixer
import os
import time
#Necesarias librerías gtts, pygame


def switchTextToVoice(nombreAudio, texto):
    s = gTTS(texto, lang='es', tld='com.mx')
    ruta = os.getcwd() + '\\audios\\' + nombreAudio + '.mp3'
    s.save(ruta)


# Prueba
# switchTextToVoice("alvaro2","Hipopotamonstroesquipedalofobia")


def playPhrase(nombreAudio):
    ruta = './audios/' + nombreAudio + '.mp3'
    mixer.init()
    mixer.music.load(ruta)
    mixer.music.play()
    bandera = True
    while bandera:
        bandera = mixer.music.get_busy()


#Prueba
# playPhrase("alvaro")


def playSong(nombreAudio):
    ruta = './audios/' + nombreAudio + '.mp3'
    mixer.init()
    mixer.music.load(ruta)
    mixer.music.play()
    input("Presiona ENTER para parar la canción...")
    mixer.music.stop()

# playSong("nothing")