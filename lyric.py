import os
#import mp3play

#def playmusic(path):
#    clip = mp3play.load(path)
#    clip.play()
    
def main():
    lyrics = []
    mp3s = []
    dirs = []
    for f in os.listdir('./'):
        #if os.path.isdir(f):
        #    dirs.append(f)
        file_extend = os.path.splitext(f)[-1]
        if file_extend == '.mp3':
            mp3s.append(f)
        elif file_extend == '.txt':
            lyrics.append(f)

    print(mp3s)
    print(lyrics)
if __name__ == '__main__':
    main()
