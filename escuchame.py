#pip install SpeechRecognition
import speech_recognition as sr

def escuchar():
    r = sr.Recognizer()
    print("Escuchando ...")
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='es-ES')
        except:
            print("No escuché 😅")
            text = input('Escríbelo: ')
        finally:
            return text

#Cancion favorita
def filtrarPalabrasClave(frase, lista):
    bandera = False
    for palabra in lista:
        if type(palabra) is tuple:
            banderaTupla = True
            for sub in palabra:
                banderaTupla = banderaTupla and (sub in frase)
            if banderaTupla:
                bandera = banderaTupla
                break
        else:
            bandera = palabra in frase
            if bandera:
                break
        
    return bandera

