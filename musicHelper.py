import csv
import music21 as m
import gtts as g
from pydub import AudioSegment

musicTerms = []

def parseMusicTerms():
    with open('music_terms.csv', newline='', encoding='utf8') as csvfile, open('temp.txt', 'w', encoding='utf8') as f:
        rows = csv.DictReader(csvfile)
    
        for row in rows:
            musicTerms.append(row)
        f.write(musicTerms[100]['ID'] + musicTerms[100]['Chinese'])
    # print('finish')

def readMusicXML(song):
    c = m.converter.parse(song + '.mxl')
    c.write('midi', song + '.mid')
    c.write('musicxml', song + '.musicxml')

def tts(words, lan):
    tts = g.gTTS('Andantino', lang='it')
    # tts.save('test.mp3')

def mixSound():
    sound1 = AudioSegment.from_mp3("input.mp3")
    sound2 = AudioSegment.from_mp3("test.mp3")

    # mix sound2 with sound1, starting at 5000ms into sound1)
    output = sound1.overlay(sound2, position=500)

    # save the result
    output.export("mixed_sounds.mp3", format="mp3")

if __name__=='__main__':
    # song = 'reve.musicxml'
    song = 'Una_furtiva_lagrima'
    readMusicXML(song)

    # parseMusicTerms()
    