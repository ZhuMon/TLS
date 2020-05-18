import os
import docx
#import mp3play

#def playmusic(path):
#    clip = mp3play.load(path)
#    clip.play()
    
def main():
    lyrics = []
    mp3s = []
    dirs = []
    kinds = []

    # get kinds
    for f in os.listdir('./mp3/'):
        if os.path.isdir(f):
            kinds.append(f)

    print(f'輸入想要編輯的種類代號')
    for i,k in zip(range(len(kinds)),kinds):
        print(f'{i}. {k}')
    
    input_kind = input()

    # get lyrics and songs
    for f in os.listdir('./mp3/'+f'{kinds[input_kind]}'):
        file_extend = os.path.splitext(f)[-1]
        if file_extend in ['.mp3']:
            mp3s.append(f)
        elif file_extend == ['.txt', '.doc', '.docx']:
            lyrics.append(f)

    print(f'輸入想要編輯的歌曲代號')
    for i,s in zip(range(len(songs)), kinds):
        print(f'{i}. {s}')
    

    
if __name__ == '__main__':
    main()
