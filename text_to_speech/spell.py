from gtts import gTTS
import pyttsx3

# from playsound import playsound

def text_to_speech(english_text):
    engine = pyttsx3.init()
    engine.say(english_text)
    engine.runAndWait()
    engine.stop()

def text_to_mp3(text, lang='en', slow=False, filename='data/tmp.mp3'):
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(filename)



if __name__ == "__main__":
    slovak_text = "Spotreba granátov je taká vysoká, že nie je čas na dodržiavanie noriem – munície je potom dosť, ale lieta si, kam sa jej zachce."
    english_translation = "Grenade consumption is so high that there is no time to comply with standards – there is then enough ammunition, but it flies wherever it wants."

    text_to_mp3(slovak_text, lang='sk', slow=False, filename='data/tmp.mp3')
    text_to_mp3(english_translation, lang='en', slow=False, filename='data/tmp.mp3')
    text_to_speech(english_translation)

