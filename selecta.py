import time
import sys
import os
import random
from selenium import webdriver
from folder_util import create_folder
from folder_util import cool_dude
from folder_util import move_music


playlist = []
start_url = sys.argv[1]

playlist.append(start_url)

def get_related_tracks(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    driver = webdriver.Chrome('/Users/tom/pythonprojects/chromedriver', options=chrome_options)
    driver.get(url)
    time.sleep(3)

    related_trax = []

    related_trax_elements = driver.find_elements_by_class_name('soundTitle__titleContainer')[1:4]

    for _ in related_trax_elements:
        track_url = _.find_elements_by_class_name('sc-link-dark')[0].get_attribute('href')
        related_trax.append(track_url)

    driver.close()

    return related_trax

def append_if_not_in_playlist(playlist, trax):
    
    while True:
        random_track = random.choice(trax)
        if random_track not in playlist:
            playlist.append(random_track)
            break
    

def event_loop():

    current_path, playlist_folder = create_folder()

    cool_dude()
    print('-' * 75) 
    print('Wait a sec, putting my lil headphones on...') 
    print('-' * 75) 

    spinning = True

    os.system('scdl -l ' + start_url)
    move_music(current_path, playlist_folder)

    cool_dude()
    print('-' * 75) 
    print('Wait a sec, putting my lil headphones on...') 
    print('-' * 75) 


    track_no = 0

    trax = get_related_tracks(start_url)
    time.sleep(5)

    playlist.append(random.choice(trax))

    while spinning == True:

        track_no += 1

        cued_track = playlist[track_no]
  
        more_trax = get_related_tracks(cued_track)
        append_if_not_in_playlist(playlist, more_trax)

        cool_dude()
        print('-' * 75) 
        name = input('OK mr DJ, do you want another track? y/n \n')
        print('-' * 75) 

        if name.lower() == 'y':
            cool_dude()
            print('-' * 75) 
            print('OKKKKK, Let\'s spinnnnn some tacks, baby!!!!')
            print('-' * 75) 
            os.system('scdl -l ' + playlist[track_no])
            move_music(current_path, playlist_folder)

        else:
            cool_dude()
            print('-' * 75) 
            print('ONE MORE CHOOOOON! \nONE MORE CHOOOOOOON! \nONE MORE CHOOOOOOOON!')
            print('-' * 75) 
            spinning = False

            
if __name__ == "__main__":

    event_loop()






