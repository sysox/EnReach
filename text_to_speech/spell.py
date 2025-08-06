from gtts import gTTS
from playsound import playsound

def text_to_speech(text, lang='en', slow=False, filename='data/tmp.mp3'):
    """
    Convert text to speech and save it as an mp3 file.

    :param text: The text to convert to speech.
    :param lang: The language for the speech (default is English).
    :param slow: If True, the speech will be slower (default is False).
    :param filename: The name of the file to save the speech (default is 'data/tmp.mp3').
    """
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(filename)
    playsound(filename)

if __name__ == "__main__":
    text = "Spotreba granátov je taká vysoká, že nie je čas na dodržiavanie noriem – munície je potom dosť, ale lieta si, kam sa jej zachce."
    text_to_speech(text, lang='sk', slow=False, filename='data/tmp.mp3')

