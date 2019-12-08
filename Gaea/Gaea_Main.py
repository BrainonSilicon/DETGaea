#import Pi stuff 
import time 
from adafruit_crickit import crikit 
import pygame #for playing audio
from adafruit_seesaw.neopixel import NeoPixel

import picamera     #camera library
import pygame as pg #audio library
import os           #communicate with os/command line

### AUDIO
RATE = 44100
CHUNK = int(RATE / 10)  # 100ms
import Gaea_Audio

#### NEOPIXELS
num_pixels = 8 #TODO change this  
pixels = NeoPixel(crickit.seesaw, 20, num_pixels) 

ss = crickit.seesaw

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0,0,0)

### MOTORS 
servos = (crickit.servo_1, crickit.servo_2, crickit.servo_3)
motor = crickit.dc_motor_1

pygame.init()
pygame.mixer.init()

def main():
    print ("running main")
    pixels.fill(OFF)
    servos.angle = 0
    Gaea_Audio.Eve_open_hatch()
    pixels.fill(GREEN)
    time.sleep(5)
    pixels.fill(WHITE)
    time.sleep(0.1)
    Gaea_Audio.Eve_closed_hatch()
    time.sleep(5)
    pixels.fill(GREEN)
    servos[0].angle = 180
    servos[0].angle = 10
    servos[0].angle = 180
    servos[0].angle = 18
    servos[0].angle = 180
    servos[0].angle = 18
    servos[0].angle = 180
    servos[0].angle = 18
    servos[1].angle = 90 #seed dispersed
    servos[0].angle = 180
    servos[0].angle = 18
    servos[0].angle = 180
    servos[0].angle = 18
    pixels.fill(BLUE)
    time.sleep(2)
    ####WATER SPOUT CODE
    Gaea_Audio.Eve_sings()
    time.sleep(5)
    pixels.fill(RED)
    time.sleep(0.5)
    pixels.fill(OFF)
    
if __name__ == '__main__':
    main()
    
    

    
    
    
    
     