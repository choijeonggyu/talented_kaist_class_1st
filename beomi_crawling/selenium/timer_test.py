#뽀모도로 기법을 적용 25분일하고 5분쉬고


import datetime
import pygame
import time

pygame.init()

audio_volume = 1.0
audio_interval = 1

sound = pygame.mixer.Sound('C:\Windows\media\Alarm05.wav')
print('{0}'.format(sound.get_volume()))
sound.set_volume(audio_volume)
sound.play()
print('sound.play(Alarm05.wav)')
time.sleep(audio_interval)

oldHour = 60

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    if now.minute == 0:
        if now.hour != oldHour:
            oldHour = now.hour
            playIndex = now.hour % 12
            sound = pygame.mixer.Sound('C:\Windows\media\Alarm06.wav')
            sound.set_volume(audio_volume)
            sound.play()
            print('sound.play(Alarm06.wav)')
            time.sleep(audio_interval)

            if (playIndex) == 0:
                sound = pygame.mixer.Sound('C:\Windows\media\Alarm07.wav')
            else:
                sound = pygame.mixer.Sound('C:\Windows\media\Alarm08.wav'.format(playIndex))

            sound.set_volume(audio_volume)
            sound.play()
            print('sound.play(Alarm07~8.wav)')
