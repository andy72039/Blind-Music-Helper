import gtts as g

def tts(phrase, lan='it'):
    tts = g.gTTS(text=phrase, slow=True, lang=lan)
    tts.save(phrase + '.mp3')

while True:
    phrase = input()
    if phrase == 'q':
        break
    else:
        tts(phrase=phrase)
