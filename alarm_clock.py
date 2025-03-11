import time
import datetime
import pygame

def alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound = "alarm-clock-short-6402.mp3"
    alarm_running = True
    
    while alarm_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("Beep! Beep! Beep!")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            alarm_running = False
        
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    alarm(alarm_time)
