import speech_recognition as sr

r = sr.Recognizer()

def escuchar():
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language='es-ES')
            print(f"Lo que tu dijiste: {texto}")
        except:
            print("Lo siento no entendi lo que dijiste, ¿puedes repetir por favor?")


if __name__ == '__main__':
    while True:
        escuchar()
