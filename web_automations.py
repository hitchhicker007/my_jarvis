import time
import pygame
import playsound

def music():
    # pygame.mixer.init()
    # pygame.mixer.music.load("song.mp3")
    # pygame.mixer.music.play()
    playsound.playsound('song.mp3',True)

def current_time():
    date_time = time.strftime("%I:%M %p")
    return str(date_time)

def current_date():
    return str(time.strftime("%b %d %Y"))

def stop_music():
    pygame.mixer.music.stop()

def decrease_volume():
    temp = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(temp-0.2)

def increase_volume():
    temp = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(temp+0.2)