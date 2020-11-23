import os
import calendar
import sys
import glob
import shutil
from datetime import datetime
from pathlib import Path

def create_folder():

    nice_date = datetime.today().strftime('%Y%m%d-%H%M')

    current_path = str(Path(__file__).parent.absolute())

    try:
        playlist_path =  current_path + "/playlists/" + nice_date
        os.makedirs(playlist_path, exist_ok=True)
        print('-' * 75) 
        print('Yoooooo, I put ur new tunes in here:\n' + playlist_path)
        print('-' * 75) 

    except FileExistsError:
        print('specific client directory exists')
        playlist_path = current_path + "/playlists/" + nice_date + '.1'
        os.makedirs(playlist_path, exist_ok=True)
        print('-' * 75) 
        print('Yoooooo, I put ur new tunes in here:\n' + playlist_path)
        print('-' * 75) 
    
    return current_path, playlist_path


def move_music(src, dst):
    for f in glob.glob(os.path.join(src, '*.mp3')):
        shutil.move(f, dst)

    for f in glob.glob(os.path.join(src, '*.wav')):
        shutil.move(f, dst)

def cool_dude():

    dude = []
    os.system('clear')
    with open('cooldj.txt', "r", encoding='utf8') as f:
        dude.append(f.readlines())
    print("".join(dude[0]))

       
